from pydantic import BaseModel, Field
from typing import List
class CodeCheckRequest(BaseModel):
    content: str = Field(..., description="GitHub file URL")

class CodeEvaluationkRequest(BaseModel):
    content: str = Field(..., description="GitHub file URL")
    question_text: str = Field(..., description="Question Text")
    language:str = Field(..., description="Mention langauge used")

class CodeCheckPayload(BaseModel):
    question_text:str
    answer_text:str

class CodeCheckEvaluation(BaseModel):
    content:List[CodeCheckPayload] = Field(..., description="Can be one or more questions")
    language:str
    