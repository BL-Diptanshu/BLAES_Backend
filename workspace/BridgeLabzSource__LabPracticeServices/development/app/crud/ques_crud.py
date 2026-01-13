from sqlalchemy.orm import Session
from app.models.ques_model import Question
from app.schemas.ques_schema import QuestionCreate,QuestionFilterRequest, Difficulty
from typing import List
import uuid

def get_questions_by_ans_type(db: Session, q_id: str) -> List[Question]:
    return (
        db.query(
            Question.id,
            Question.question_type,
            Question.answer_type,
            Question.stem_md,
            Question.solution_md,
            Question.score_weight,
        )
        .filter(Question.id == q_id)
        .limit(1)
        .all()
    )


def create_question(db: Session, question_data: QuestionCreate):
    new_question = Question(
        id=str(uuid.uuid4()),
        programme_id=question_data.programme_id,
        module_id=question_data.module_id,
        topic_id=question_data.topic_id,
        subtopic_id=question_data.subtopic_id,
        question_type=question_data.question_type,
        answer_type=question_data.answer_type,
        difficulty=question_data.difficulty,
        stem_md=question_data.stem_md,
        solution_md=question_data.solution_md,
        score_weight=question_data.score_weight,
        metadata_json=question_data.metadata_json,
    )
    db.add(new_question)
    db.commit()
    db.refresh(new_question)
    return new_question


def get_questions_as_per_difficulty_count(db: Session, data:QuestionFilterRequest):
    results = []
    query = db.query(Question.id, Question.answer_type, Question.difficulty, Question.stem_md, Question.solution_md, Question.score_weight)

    if data.programme_id:
        query = query.filter(Question.programme_id == data.programme_id)

    if data.module_id:
        query = query.filter(Question.module_id == data.module_id)

    if data.submodule_id:
        query = query.filter(Question.submodule_id == data.submodule_id)

    if data.question_type:
        query = query.filter(Question.question_type == data.question_type)

    if data.answer_type:
        query = query.filter(Question.answer_type == data.answer_type)

    if data.question_count_req:
        easy_req = data.question_count_req.easy
        med_req = data.question_count_req.medium
        hard_req = data.question_count_req.hard

        if easy_req > 0:
            easy_q = (
                query.filter(Question.difficulty == Difficulty.EASY)
                .limit(easy_req)
                .all()
            )
            results.extend(easy_q)

        if med_req > 0:
            med_q = (
                query.filter(Question.difficulty == Difficulty.MEDIUM)
                .limit(med_req)
                .all()
            )
            results.extend(med_q)

        if hard_req > 0:
            hard_q = (
                query.filter(Question.difficulty == Difficulty.HARD)
                .limit(hard_req)
                .all()
            )
            results.extend(hard_q)
    return results