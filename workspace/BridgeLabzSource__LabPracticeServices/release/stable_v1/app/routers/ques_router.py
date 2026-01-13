# app/routers/questions.py
from fastapi import APIRouter, Depends, Query, status, HTTPException
from fastapi.responses import JSONResponse
from decimal import Decimal
from sqlalchemy.orm import Session
from typing import List
from app.schemas import ques_schema
from app.crud import ques_crud
from app.config.database import get_db
from app.models.ques_model import Question

question_router = APIRouter(prefix="/questions", tags=["Questions"])

@question_router.post("/get_questions", response_model=ques_schema.QuestionListResponse)
def read_questions(filter_request: ques_schema.QuestionFilterRequest, db: Session = Depends(get_db)):
    query = db.query(Question)

    if filter_request.programme_id:
        query = query.filter(Question.programme_id == filter_request.programme_id)

    if filter_request.module_id:
        query = query.filter(Question.module_id == filter_request.module_id)

    if filter_request.topic_id:
        query = query.filter(Question.topic_id == filter_request.topic_id)

    if filter_request.subtopic_id:
        query = query.filter(Question.subtopic_id == filter_request.subtopic_id)

    if filter_request.question_type:
        query = query.filter(Question.question_type == filter_request.question_type)

    if filter_request.answer_type:
        query = query.filter(Question.answer_type == filter_request.answer_type)

    if filter_request.difficulty:
        query = query.filter(Question.difficulty == filter_request.difficulty)

    total_count = query.count()

    questions = query.limit(filter_request.limit).all()

    return ques_schema.QuestionListResponse(
        message="Questions fetched successfully",
        payload=[ques_schema.QuestionItem.model_validate(q) for q in questions],
        total=total_count,
        limit=filter_request.limit,
        status=200
    )

