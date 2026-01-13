from fastapi import APIRouter, Query
from pydantic import BaseModel
from typing import Any, Dict
from app.templates.prompts import CODE_ANALYSER_PROMPT, REVIEW_PROMPT_THEORY
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from app.schemas.common_schema import ErrorResponse

prompt_router = APIRouter(prefix="/prompts", tags=["Default Prompt  API'S"])

class PromptResponse(BaseModel):
    message: str
    payload: Dict[str, Any]
    status: int


@prompt_router.get("/default-prompt", response_model=PromptResponse)
def get_default_prompt(answer_type: str = Query(..., description="Type of question (e.g. 'code' or 'theory')")):
    try:
        """
        Return the default system prompt currently configured in the agent
        """
        if answer_type.upper() == "CODE":
            return {
                "message": "Successfully fetched default code check prompt",
                "payload": {"default_code_check_prompt":CODE_ANALYSER_PROMPT},
                "status": 200
                }
        else:
            return {
                "message": "Successfully fetched default code check prompt",
                "payload": {"default_theory_check_prompt":REVIEW_PROMPT_THEORY},
                "status": 200
                }
        
    except ValueError as val_err:
        return ErrorResponse(message = "Invalid input",
                             detail = str(val_err),
                             status = 400)

    except ValidationError as pyd_err:
        return JSONResponse(
            status_code=422,
            content={
                "message": "Validation failed",
                "errors": pyd_err.errors(),
                "status": 422
            }
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "message": "Unexpected error occurred",
                "detail": str(e),
                "status": 500
            }
        )

