from sqlalchemy.orm import Session
from app.models.ques_model import Question
from app.schemas.ques_schema import QuestionCreate
from typing import List
import uuid

# def get_questions_by_ans_type(
#     db: Session, answer_type: str, skip: int = 0, limit: int = 10
# ) -> List[Question]:
#     return (
#         db.query(
#             Question.id,
#             Question.question_type,
#             Question.answer_type,
#             Question.stem_md,
#             Question.solution_md,
#             Question.score_weight,
#         )
#         .filter(Question.answer_type == answer_type)
#         .offset(skip)
#         .limit(limit)
#         .all()
#     )

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
