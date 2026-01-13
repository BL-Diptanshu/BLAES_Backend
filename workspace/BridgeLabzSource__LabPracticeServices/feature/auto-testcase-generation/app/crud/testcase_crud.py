from sqlalchemy.orm import Session
from app.models.testcase_model import TestCase
from app.schemas.testcase_schema import TestCaseCreate
from app.config.logger import AppLogger

logger = AppLogger.get_logger()

def create_bulk_test_cases(db: Session, question_id: str, cases_data: list[TestCaseCreate]):
    """Efficient bulk insert for many test cases."""
    test_cases = [
        TestCase(question_id=question_id, **case.model_dump())
        for case in cases_data
    ]
    db.bulk_save_objects(test_cases)
    db.commit()
    logger.info(f"Inserted {len(test_cases)} test cases for question {question_id}")
    return test_cases
