from app.config.logger import AppLogger
from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from pydantic import ValidationError
from app.schemas.common_schema import ErrorResponse
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.models.ans_model import Answer
from app.schemas.ans_schema import AnswerInput
from app.utils.s3_utils import upload_to_s3
from app.crud.ans_crud import store_answer_records
from app.utils.code_utils import review_code_with_gemini
from app.crud.review_crud import store_reviews_with_answer_mapping
from app.utils.user_activity_utils import log_user_activity
import boto3
import os
import io
from dotenv import load_dotenv

load_dotenv()

logger = AppLogger.get_logger()

review_router = APIRouter(prefix="/submit-test", tags=["Test Submission API'S"])

@review_router.post("/generate-review/")
async def create_answer(payload: AnswerInput, db: Session = Depends(get_db)):
    review_results = None
    try:
        payload_dict = payload.model_dump()
        file_url = upload_to_s3(payload_dict)

        logger.info("Storing Answer url in DB...")
        stored_ans = store_answer_records(file_url, db)
        logger.info(f"Answers stored in DB")

        if type(stored_ans) == dict and stored_ans.get("status") == 409:
            raise HTTPException(
            status_code=409,
            detail={
                "user_message": stored_ans.get("message"),
                "payload": stored_ans.get("payload", {})
                }
            )


        platform_track_resp = log_user_activity(payload, db)
        logger.info(f"platform_track_resp --> {platform_track_resp}")

        try:
            logger.info("Running code review with code analyser agent...")
            review_results = await review_code_with_gemini(db, payload.prompt, payload.content, "Java")
            logger.info(f"Code Analysing finished with Review results: {review_results}")
        except ValueError as e:
            logger.warning(f"Code review failed: {e}")
            review_results = None

        if payload.answer_type == "CODE":
            store_reviews_with_answer_mapping(db, review_results.get("individual_reviews", []), stored_ans)
        # elif payload.answer_type == "TEXT":
        #     store_theory_review_to_db(db, new_answer.id, review_results)
        # else:
            # logger.warning(f"Unknown answer type: {payload.answer_type}")

        return {
            "message": "Answer stored and review generated successfully",
            "payload": {
                "user_id": payload.user_id,
                "file_url": stored_ans,
                "review_generated": review_results,
                "platform_track_resp":platform_track_resp
                },
            "status": 201
        }

    except SQLAlchemyError as db_err:
        db.rollback()
        return ErrorResponse(message = "Database error occurred",
                             detail = str(db_err),
                             status = 500)
        
    except ValueError as val_err:
        return ErrorResponse(message = "Invalid input",
                             detail = str(val_err),
                             status = 400)

    except ValidationError as pyd_err:
        return JSONResponse(
            status_code=422,
            content={
                "message": "Validation failed",
                "errors": pyd_err.errors(),
                "status": 422
            }
        )
    except HTTPException:
        raise

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "message": "Unexpected error occurred",
                "detail": str(e),
                "status": 500
            }
        )