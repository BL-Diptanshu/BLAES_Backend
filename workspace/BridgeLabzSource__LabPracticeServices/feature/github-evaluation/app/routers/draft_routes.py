# from fastapi import APIRouter, HTTPException, status
# from datetime import datetime
# import duckdb

# from app.utils.duckdb_client import get_duckdb_conn
# from app.schemas.draft_schema import DraftInput, DraftResponse

# draft_router = APIRouter(prefix='/draft', tags=["Draft API'S"])

# @draft_router.post("/save-draft", response_model=DraftResponse)
# def save_draft(draft: DraftInput):
#     conn = get_duckdb_conn()
#     now_iso = datetime.utcnow().isoformat(sep=" ", timespec="seconds")

#     try:
#         # Start manual transaction
#         conn.execute("BEGIN TRANSACTION;")

#         conn.execute(
#             "DELETE FROM drafts WHERE user_id = ? AND question_id = ?;",
#             (draft.user_id, draft.question_id)
#         )

#         conn.execute(
#             "INSERT INTO drafts (user_id, question_id, draft_text, updated_at) VALUES (?, ?, ?, ?);",
#             (draft.user_id, draft.question_id, draft.draft_text or "", now_iso)
#         )

#         conn.execute("COMMIT;")

#         return DraftResponse(
#             user_id=draft.user_id,
#             question_id=draft.question_id,
#             draft_text=draft.draft_text or "",
#             updated_at=now_iso
#         )

#     except Exception as e:
#         conn.execute("ROLLBACK;")
#         raise HTTPException(
#             status_code=500,
#             detail=f"Unexpected error saving draft: {e}"
#         )

# @draft_router.get("/get-draft", response_model=DraftResponse)
# def get_draft(user_id: str, question_id: str):
#     conn = get_duckdb_conn()

#     try:
#         row = conn.execute(
#             "SELECT draft_text, updated_at FROM drafts WHERE user_id = ? AND question_id = ?;",
#             (user_id, question_id)
#         ).fetchone()

#         if not row:
#             raise HTTPException(
#                 status_code=status.HTTP_404_NOT_FOUND,
#                 detail="Draft not found"
#             )

#         draft_text, updated_at = row
#         updated_at_str = (
#             updated_at.isoformat(sep=" ", timespec="seconds")
#             if hasattr(updated_at, "isoformat") else str(updated_at)
#         )

#         return DraftResponse(
#             user_id=user_id,
#             question_id=question_id,
#             draft_text=draft_text or "",
#             updated_at=updated_at_str
#         )

#     except duckdb.Error as db_err:
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail=f"DuckDB error fetching draft: {db_err}"
#         )
#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail=f"Unexpected error fetching draft: {e}"
#         )

from app.config.logger import AppLogger
from datetime import datetime
from fastapi import APIRouter
from app.schemas.draft_schema import DraftInput, DraftResponse
import redis

logger = AppLogger.get_logger()

redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)

draft_router = APIRouter(prefix='/draft', tags=["Draft API'S"])

@draft_router.post("/save-draft")
def save_draft(draft: DraftInput):
    try:
        redis_key = f"draft:{draft.user_id}:{draft.question_id}"

        redis_client.hset(redis_key, mapping={
            "draft_text": draft.draft_text,
            "last_updated": int(datetime.utcnow().timestamp())
        })

        redis_client.expire(redis_key, 1 * 24 * 3600)

        return {
            "message": "Draft saved successfully",
            "status": 200
        }

    except Exception as e:
        logger.exception("Error saving draft")
        return {
            "message": "Unexpected error saving draft",
            "detail": str(e),
            "status": 500
        }

@draft_router.get("/get-draft")
def get_draft(user_id: str, question_id: str):
    try:
        redis_key = f"draft:{user_id}:{question_id}"

        data = redis_client.hgetall(redis_key)

        if not data:
            return {
                "message": "No draft found",
                "payload":{
                    "draft": "public class Main {\\n    public static void main(String[] args) {\\n           }\\n}",
                    "last_updated": None
                    },
                "status": 404
            }

        return {
            "message": "Draft fetched successfully",
            "payload":{
                "draft": data.get("draft_text", ""),
                "last_updated": data.get("last_updated")
                },
            "status": 200
        }

    except Exception as e:
        logger.exception("Error fetching draft")
        return {
            "message": "Unexpected error fetching draft",
            "detail": str(e),
            "status": 500
        }