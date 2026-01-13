from pydantic import BaseModel, Field
from typing import Optional, Any
from enum import Enum
from decimal import Decimal

class QuestionType(str, Enum):
    ASSIGNMENT = "ASSIGNMENT"
    ASSISTED   = "ASSISTED"
    SELF       = "SELF"
    TEST       = "TEST"

class AnswerType(str, Enum):
    MCQ          = "MCQ"
    MULTI_SELECT = "MULTI_SELECT"
    NUMERIC      = "NUMERIC"
    TEXT         = "TEXT"
    CODE         = "CODE"
    MATCHING     = "MATCHING"

class Difficulty(str, Enum):
    EASY   = "EASY"
    MEDIUM = "MEDIUM"
    HARD   = "HARD"


class QuestionCreate(BaseModel):
    programme_id: str
    module_id: str
    topic_id: str
    subtopic_id: str
    question_type: QuestionType
    answer_type: AnswerType
    difficulty: Difficulty = Difficulty.MEDIUM
    stem_md: str
    solution_md: Optional[str] = None
    score_weight: Decimal = Decimal("1.00")
    metadata_json: Optional[Any] = None


class QuestionResponse(QuestionCreate):
    id: str
    version: int
    is_current: bool

    model_config = {
        "from_attributes": True
    }


class QuestionFiltered(BaseModel):
    id: str
    question_type: str
    answer_type: str
    stem_md: str
    solution_md: Optional[str]
    score_weight: float

    model_config = {
        "from_attributes": True
    }
