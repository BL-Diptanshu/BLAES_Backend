# app/routers/questions.py
from fastapi import APIRouter, Depends, Query, status, HTTPException
from fastapi.responses import JSONResponse
from decimal import Decimal
from sqlalchemy.orm import Session
from typing import List
from app.schemas import ques_schema
from app.crud import ques_crud
from app.config.database import get_db

question_router = APIRouter(prefix="/questions", tags=["Questions"])


# @question_router.get("/get_questions", response_model=List[ques_schema.QuestionFiltered])
# def read_questions(
#     answer_type: str = Query(..., description="Filter by question type"),
#     skip: int = 0,
#     limit: int = 10,
#     db: Session = Depends(get_db)
# ):
#     try:
#         questions = ques_crud.get_questions_by_ans_type(
#             db, answer_type=answer_type, skip=skip, limit=limit
#         )

#         payload = [
#             {
#                 "id": q.id,
#                 "question_type": q.question_type,
#                 "answer_type": q.answer_type,
#                 "stem_md": q.stem_md,
#                 "solution_md": q.solution_md,
#                 "score_weight": float(q.score_weight) if isinstance(q.score_weight, Decimal) else q.score_weight
#             }
#             for q in questions
#         ]

#         return JSONResponse(
#             status_code=status.HTTP_200_OK,
#             content={
#                 "message": "Questions fetched successfully",
#                 "payload": payload,
#                 "status": status.HTTP_200_OK
#             }
#         )

#     except Exception as e:
#         return JSONResponse(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             content={
#                 "message": f"Error fetching questions: {str(e)}",
#                 "payload": [],
#                 "status": status.HTTP_500_INTERNAL_SERVER_ERROR
#             }
#         )

@question_router.get("/get_questions", response_model=List[ques_schema.QuestionFiltered])
def read_questions(
    q_id: str = Query(..., description="Filter by question id"),
    db: Session = Depends(get_db)
):
    try:
        questions = ques_crud.get_questions_by_ans_type(
            db, q_id=q_id
        )

        payload = [
            {
                "id": q.id,
                "question_type": q.question_type,
                "answer_type": q.answer_type,
                "stem_md": q.stem_md,
                "solution_md": q.solution_md,
                "score_weight": float(q.score_weight) if isinstance(q.score_weight, Decimal) else q.score_weight
            }
            for q in questions
        ]

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": "Questions fetched successfully",
                "payload": payload,
                "status": status.HTTP_200_OK
            }
        )

    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "message": f"Error fetching questions: {str(e)}",
                "payload": [],
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR
            }
        )


@question_router.post("/add-question")
def add_ques_with_test_cases(question:ques_schema.QuestionCreate, db:Session = Depends(get_db)):
    """
    Add a new question to the database.
    """
    try:
        question = ques_crud.create_question(db, question)
        return question
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

