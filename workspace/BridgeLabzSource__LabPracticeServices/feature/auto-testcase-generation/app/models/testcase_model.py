from sqlalchemy import Column, String, Text, ForeignKey, JSON, Integer, Index
from sqlalchemy.orm import relationship
from app.config.database import Base
import uuid

class TestCase(Base):
    __tablename__ = "test_cases"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    question_id = Column(
        String(36),
        ForeignKey("questions.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )
    input_json = Column(JSON, nullable=False)
    expected_output_json = Column(JSON, nullable=False)
    reasoning = Column(Text, nullable=True)
    difficulty_level = Column(String(50), nullable=True)
    case_number = Column(Integer, nullable=True)

    question = relationship("Question", back_populates="test_cases")


Index("ix_test_cases_question_id", TestCase.question_id)

from app.models.ques_model import Question
