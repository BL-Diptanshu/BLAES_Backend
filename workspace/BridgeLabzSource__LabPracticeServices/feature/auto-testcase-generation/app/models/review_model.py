import uuid
from sqlalchemy import Column, CHAR, Text, Integer, DateTime, ForeignKey, func, String, UniqueConstraint, Float
from sqlalchemy.orm import relationship
from app.config.database import Base
class Review(Base):
    __tablename__ = "reviews"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    answer_id = Column(
        String(36),
        ForeignKey("answers.id", ondelete="SET NULL"),
        nullable=True
    )


    question_id = Column(String(36), nullable=False)
    user_id = Column(String(36), nullable=False)

    reviewer = Column(String(100))

    correctness_feedback = Column(Text, nullable=True)
    improvement_suggestions = Column(Text, nullable=True)

    score_correctness = Column(Integer, nullable=True)
    score_code_quality = Column(Integer, nullable=True)
    score_efficiency = Column(Integer, nullable=True)
    score_overall = Column(Float, nullable=True)

    created_at = Column(DateTime, server_default=func.now())

    answer = relationship("Answer", back_populates="reviews")

    __table_args__ = (
        UniqueConstraint(
            'user_id',
            'answer_id',
            'question_id',
            name='uq_user_answer_question'
        ),
    )
