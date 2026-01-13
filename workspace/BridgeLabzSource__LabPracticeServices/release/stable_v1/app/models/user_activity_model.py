from sqlalchemy import Column, String, BigInteger, Integer, DateTime
from app.config.database import Base
from datetime import datetime
import uuid

class UserActivity(Base):
    __tablename__ = "user_activity"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(64), nullable=False, index=True)
    session_start = Column(BigInteger, nullable=False)
    session_end = Column(BigInteger, nullable=False)
    duration_seconds = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class UserTotalTime(Base):
    __tablename__ = "user_total_time"

    user_id = Column(String(64), primary_key=True)
    total_time_spent = Column(Integer, default=0)