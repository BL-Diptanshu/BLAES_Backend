from sqlalchemy.orm import Session
from app.models.ans_model import Answer
import uuid
from sqlalchemy.orm import Session
from app.models.ans_model import Answer
from app.schemas.ans_schema import AnswerCreate
from app.config.logger import AppLogger
from sqlalchemy.exc import IntegrityError
import pymysql

logger = AppLogger.get_logger()

def create_answer(db: Session, answer: AnswerCreate):
    db_answer = Answer(
        question_id=answer.question_id,
        what_worked_well=answer.analysis_output.what_worked_well,
        what_can_be_improved=answer.analysis_output.what_can_be_improved,
        correctness=answer.quality_feedback.correctness,
        readability=answer.quality_feedback.readability,
        maintainability=answer.quality_feedback.maintainability,
        design=answer.quality_feedback.design,
        scalability=answer.quality_feedback.scalability,
        correctness_score=answer.quality_scores.correctness,
        readability_score=answer.quality_scores.readability,
        maintainability_score=answer.quality_scores.maintainability,
        design_score=answer.quality_scores.design,
        scalability_score=answer.quality_scores.scalability,
        overall_score=answer.quality_scores.overall
    )
    db.add(db_answer)
    db.commit()
    db.refresh(db_answer)
    return db_answer


def store_answer_records(payload: list, db: Session):
    """
    Insert one DB row per uploaded file URL.

    payload format:
    [
        {"question_id": "...", "user_id": "...", "url": "..."},
        {"question_id": "...", "user_id": "...", "url": "..."},
        ...
    ]
    """

    saved_answers = []

    try:
        for item in payload:
            question_id = item.get("question_id")
            user_id = item.get("user_id")
            file_url = item.get("url")

            if not (question_id and user_id and file_url):
                logger.warning(f"Skipping incomplete answer entry: {item}")
                continue

            new_answer = Answer(
                id=str(uuid.uuid4()),
                question_id=question_id,
                user_id=user_id,
                file_url=file_url
            )

            db.add(new_answer)
            db.commit()
            db.refresh(new_answer)

            logger.info(f"Answer stored in DB: {new_answer.id}")
            saved_answers.append(new_answer)

        return saved_answers
    
    except IntegrityError as e:
        db.rollback()

        if isinstance(e.orig, pymysql.err.IntegrityError) and e.orig.args[0] == 1062:
            return {
                "message": "User has already submitted an answer for this question.",
                "payload":{
                    "user_id": new_answer.user_id,
                    "question_id": new_answer.question_id
                    },
                "status": 409
            }
    except Exception as e:
        db.rollback()
        logger.error(f"Error saving answer records: {e}")
        raise
