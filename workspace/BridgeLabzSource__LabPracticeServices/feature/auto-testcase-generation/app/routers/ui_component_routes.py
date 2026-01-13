from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from app.config.database import get_db
from sqlalchemy.orm import Session
from app.models.ques_model import QuestionType, AnswerType, Difficulty
from app.crud.common_quereis import get_ques_count_levelwise_for_dropdown
from app.schemas.common_schema import ErrorResponse

ui_component_router = APIRouter(prefix="/components", tags=["Ui Component API'S"])

@ui_component_router.get("/mentor-page-dropdown-data")
def get_question_metadata(db: Session = Depends(get_db)):
    try:
        programme_data = get_ques_count_levelwise_for_dropdown(db)
        return {
            "message": "Fetched Content for UI",
            "payload": {
                "programmes": programme_data,
                "question_types": [qt.value for qt in QuestionType],
                "answer_types": [at.value for at in AnswerType],
                "difficulty_levels": [d.value for d in Difficulty]
            },
            "status": 200,
        }

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
