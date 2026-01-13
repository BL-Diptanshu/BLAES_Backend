from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from pydantic import ValidationError
from app.schemas.common_schema import ErrorResponse
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.schemas.ans_schema import AnswerCreate
from app.crud.ans_crud import create_answer
from app.config.logger import AppLogger

logger = AppLogger.get_logger()
answer_router = APIRouter(prefix="/answers", tags=["Answer  API'S"])

@answer_router.post("/insert-answer", status_code=201)
def add_answer(answer: AnswerCreate, db: Session = Depends(get_db)):
    try:
        new_answer = create_answer(db, answer)
        logger.info(f"Answer inserted for question_id={answer.question_id}")
        return {
            "message": "Answer inserted successfully",
            "payload": {
                "answer_id": new_answer.id,
                "question_id": new_answer.question_id
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

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "message": "Unexpected error occurred",
                "detail": str(e),
                "status": 500
            }
        )
