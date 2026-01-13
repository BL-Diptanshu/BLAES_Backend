from pydantic import BaseModel, Field

class ErrorResponse(BaseModel):
    """
    Schema representing a standardized error response body for a 500 status code.
    """
    message: str = Field(..., description="A high-level description of the error.")
    detail: str = Field(..., description="The detailed, possibly technical, error information (e.g., the exception message).")
    status: int = Field(..., description="The HTTP status code.")

    class Config:
        json_schema_extra = {
            "example": {
                "message": "Database error occurred",
                "detail": "psycopg2.errors.UndefinedTable: relation 'questions' does not exist",
                "status": 500
            }
        }