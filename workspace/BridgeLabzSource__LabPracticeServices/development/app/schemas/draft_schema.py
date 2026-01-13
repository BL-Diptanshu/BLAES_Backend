from pydantic import BaseModel, Field
from typing import Optional

class DraftInput(BaseModel):
    user_id: str = Field(..., description="User id")
    question_id: str = Field(..., description="Unique question identifier")
    draft_text: Optional[str] = Field("", description="User's saved draft text")

class DraftResponse(BaseModel):
    user_id: str
    question_id: str
    draft_text: str
    updated_at: Optional[str]
