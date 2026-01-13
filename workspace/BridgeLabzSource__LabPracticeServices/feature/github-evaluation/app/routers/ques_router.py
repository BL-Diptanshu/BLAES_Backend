from fastapi import APIRouter, Depends, Query
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

