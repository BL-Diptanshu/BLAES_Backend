from app.config.logger import AppLogger
from fastapi import APIRouter, Depends, HTTPException
from pydantic import ValidationError
from fastapi.responses import JSONResponse
from decimal import Decimal
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import List
from app.schemas import ques_schema
from app.crud.ques_crud import get_questions_as_per_difficulty_count
from app.config.database import get_db
from app.models.ques_model import Question,Difficulty
from app.schemas.common_schema import ErrorResponse
from app.crud.ques_crud import create_question
from app.tasks.testcase_tasks import generate_test_cases_task

logger = AppLogger.get_logger()

question_router = APIRouter(prefix="/questions", tags=["Question API'S"])

@question_router.post("/get_questions", response_model=ques_schema.QuestionListResponse)
def read_questions(filter_request: ques_schema.QuestionFilterRequest, db: Session = Depends(get_db)):
    try:
       
        results = get_questions_as_per_difficulty_count(db, filter_request)

        total_count = len(results)

        return ques_schema.QuestionListResponse(
                message="Questions fetched successfully (difficulty-wise)",
                payload=[ques_schema.QuestionItemDiff.model_validate(q) for q in results],
                total=total_count,
                status=200
            )
    
    except SQLAlchemyError as db_err:
        db.rollback()
        return ErrorResponse(message = "Database error occurred",
                             detail = str(db_err),
                             status = 500)
        
    except ValueError as val_err:
        return ErrorResponse(message = "Invalid input",
                             detail = str(db_err),
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

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "message": "Unexpected error occurred",
                "detail": str(e),
                "status": 500
            }
        )
    

@question_router.post("/add", status_code=201)
def add_question(payload: ques_schema.QuestionCreate, db: Session = Depends(get_db)):
    try:
        new_question = create_question(db, payload)
        logger.info(f"Triggered test case generation task for {new_question.id}")
        generate_test_cases_task.delay(
            question_id=new_question.id,
            question_text=new_question.stem_md,
            language="Java"
        )

        
        return {
            "message": "Question created successfully & test case generation started",
            "payload": {
                "question_id": new_question.id
            },
            "status": 201
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