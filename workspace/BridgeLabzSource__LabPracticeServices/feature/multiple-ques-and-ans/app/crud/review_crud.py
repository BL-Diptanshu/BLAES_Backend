from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from app.models.review_model import Review
from app.config.logger import AppLogger

logger = AppLogger.get_logger()

def store_reviews_with_answer_mapping(
    db,
    individual_reviews: list,
    answer_records: list,
    
):
    """
    Stores multiple reviews by mapping each review.question_id
    to the corresponding answer_id & user_id from answer_records.
    """
    logger.info(f"\n\n individual_reviews --> {individual_reviews}")
    logger.info(f"\n\n answer_records --> {answer_records}")

    stored = []
    failed = []

    answer_map = {
        ans.question_id: {
            "answer_id": ans.id,
            "user_id": ans.user_id
        }
        for ans in answer_records
    }

    try:
        for review in individual_reviews:

            qid = review.get("question_id")

            # Skip if no matching answer record exists
            if qid not in answer_map:
                failed.append({
                    "question_id": qid,
                    "reason": "No matching answer record"
                })
                continue

            mapped_answer_id = answer_map[qid]["answer_id"]
            mapped_user_id = answer_map[qid]["user_id"]

            try:
                r = Review(
                    answer_id=mapped_answer_id,
                    user_id=mapped_user_id,
                    question_id=qid,

                    reviewer="Gemini-AI",

                    correctness_feedback=review.get("correctness_feedback"),
                    improvement_suggestions=review.get("improvement_suggestions"),

                    # Scores
                    score_correctness=review["scores"].get("correctness_score"),
                    score_code_quality=review["scores"].get("code_quality_score"),
                    score_efficiency=review["scores"].get("efficiency_score"),
                    score_overall=review["scores"].get("overall_score"),
                )

                db.add(r)
                db.commit()
                db.refresh(r)

                stored.append({
                    "review_id": r.id,
                    "answer_id": mapped_answer_id,
                    "question_id": qid
                })

            except IntegrityError:
                db.rollback()
                failed.append({
                    "question_id": qid,
                    "reason": "Duplicate review (same user_id + answer_id)"
                })

            except Exception as inner:
                db.rollback()
                failed.append({
                    "question_id": qid,
                    "reason": str(inner)
                })

        return {
            "message": "Review storing completed",
            "stored": stored,
            "failed": failed,
            "status": 201
        }

    except SQLAlchemyError as db_err:
        db.rollback()
        return {
            "message": "Database error occurred",
            "detail": str(db_err),
            "status": 500
        }

    except Exception as e:
        db.rollback()
        return {
            "message": "Unexpected error",
            "detail": str(e),
            "status": 500
        }