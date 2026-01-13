from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.config.database import get_db
from app.models.testcase_model import TestCase
from app.schemas.testcase_schema import TestCaseResponse, TestCaseResponseItem, RunCodeRequest
from typing import List
from app.config.logger import AppLogger
import os
import json
import shutil
import tempfile
import subprocess

logger = AppLogger.get_logger()

testcase_router = APIRouter(prefix="/test-cases", tags=["Test Cases"])


@testcase_router.get("/{question_id}", response_model=TestCaseResponse)
def get_test_cases(question_id: str, db: Session = Depends(get_db)):
    try:
        """
        Get all test cases for a specific question ID.
        """
        test_cases = (
            db.query(TestCase)
            .filter(TestCase.question_id == question_id)
            .all()
        )    

        if not test_cases:
            return{
            "message":"No test cases found",
            "payload":[],
            "status":201
            }
        
        payload_items = [
            TestCaseResponseItem.model_validate(tc) for tc in test_cases
        ]
        return{
            "message":"Test cases found",
            "payload":payload_items,
            "status":201
            }
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Database Error: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Unexpected Error: {str(e)}"
        )


@testcase_router.post("/run-code")
def run_code(payload: RunCodeRequest, db: Session = Depends(get_db)):
    test_cases = (
        db.query(TestCase)
        .filter(TestCase.question_id == payload.question_id)
        .order_by(TestCase.case_number)
        .all()
    )

    if not test_cases:
        return {"status": "error", "message": "No test cases found"}

    results = []

    for tc in test_cases:
        tmp_dir = tempfile.mkdtemp()
        formatted_input = "" # We'll store the raw input string here

        try:
            # 1. Prepare and Write input
            if isinstance(tc.input_json, dict):
                formatted_input = " ".join(map(str, tc.input_json.values()))
            elif isinstance(tc.input_json, list):
                formatted_input = " ".join(map(str, tc.input_json))
            else:
                formatted_input = str(tc.input_json)

            with open(os.path.join(tmp_dir, "input.txt"), "w") as f:
                f.write(formatted_input)

            # 2. Run Docker
            result = subprocess.run(
                [
                    "docker", "run", "--rm",
                    "--network=none",
                    "--memory=256m",
                    "--cpus=0.5",
                    "-e", f"CODE={payload.code}",
                    "-v", f"{tmp_dir}:/runner",
                    "java-executor"
                ],
                capture_output=True,
                text=True,
                timeout=5
            )

            # Handle case where Docker fails completely (Empty stdout)
            if not result.stdout.strip():
                results.append({
                    "case_number": tc.case_number,
                    "status": "system_error",
                    "input": formatted_input,
                    "error": result.stderr or "No output from container"
                })
                continue

            response = json.loads(result.stdout)

            # 3. Handle compile/runtime errors from inside the container
            if response["status"] != "success":
                results.append({
                    "case_number": tc.case_number,
                    "status": response["status"],
                    "input": formatted_input,
                    "error": response.get("error")
                })
                continue

            # 4. Compare output
            user_output = response["output"].strip()
            expected_output = str(tc.expected_output_json).strip()
            passed = user_output == expected_output

            results.append({
                "case_number": tc.case_number,
                "input": formatted_input,
                "passed": passed,
                "expected": expected_output,
                "actual": user_output,
                "status": "success"
            })

        except Exception as e:
            results.append({
                "case_number": tc.case_number,
                "status": "server_error",
                "error": str(e)
            })

        finally:
            shutil.rmtree(tmp_dir)

    # 5. Final response
    return {
        "status": "completed",
        "total": len(results),
        "passed": sum(1 for r in results if r.get("passed", False)),
        "results": results
    }