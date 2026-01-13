from pydantic import BaseModel, Field, field_validator
from typing import Optional, Any, List
from enum import Enum
from decimal import Decimal

class QuestionType(str, Enum):
    ASSIGNMENT = "ASSIGNMENT"
    LAB        = "LAB"
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

# ------------------------------
# LIST QUESTIONS OUTPUT SCHEMA
# ------------------------------
class QuestionItem(BaseModel):
    id: str
    programme_id: str
    module_id: str
    topic_id: str
    subtopic_id: str
    question_type: QuestionType
    answer_type: AnswerType
    difficulty: Difficulty
    stem_md: str
    solution_md: Optional[str]
    score_weight: float

    model_config = {"from_attributes": True}

class QuestionItemDiff(BaseModel):
    id: str
    answer_type: AnswerType
    difficulty: Difficulty
    stem_md: str
    solution_md: Optional[str]
    score_weight: float

    model_config = {"from_attributes": True}

# ------------------------------
# QUESTION COUNT REQUESTED
# ------------------------------
class QuestionCountRequested(BaseModel):
    easy: int
    medium: int
    hard: int


# ------------------------------
# FILTER REQUEST SCHEMA
# ------------------------------
class QuestionFilterRequest(BaseModel):
    programme_id: Optional[str] = None
    module_id: Optional[str] = None
    submodule_id: Optional[str] = None
    question_type: Optional[QuestionType] = None
    answer_type: Optional[AnswerType] = None
    question_count_req: QuestionCountRequested

    @field_validator("programme_id", "module_id", "question_type", mode="before")
    def empty_to_none(cls, v):
        if v == "" or v is None:
            return None
        return v


# ------------------------------
# FINAL RESPONSE SCHEMA
# ------------------------------
class QuestionListResponse(BaseModel):
    message: str
    payload: List[QuestionItemDiff]
    total: int
    status: int