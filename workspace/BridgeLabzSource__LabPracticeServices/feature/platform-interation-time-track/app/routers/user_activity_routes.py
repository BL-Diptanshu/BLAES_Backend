from fastapi import APIRouter, HTTPException,status
from app.config.database import SessionLocal
from app.models.user_activity_model import UserTotalTime
from app.config.logger import AppLogger
from datetime import timedelta

user_pt_act_router = APIRouter(prefix="/platform-activity", tags=["User Activity"])
logger = AppLogger.get_logger()


@user_pt_act_router.get("/total/{user_id}")
def get_total_user_time(user_id: str):
    """
    Fetch total time spent by a user across all sessions.

    Example:
        GET /activity/total/user_123

    Response:
        {
            "user_id": "user_123",
            "total_time_seconds": 5400,
            "total_time_human": "1h 30m 0s",
            "last_updated": "2025-11-13T11:45:00"
        }
    """
    db = SessionLocal()
    try:
        total_entry = db.query(UserTotalTime).filter_by(user_id=user_id).first()

        if not total_entry:
            return  {
                "message":f"No activity found for user_id: {user_id}",
                "payload":{
                    "user_id": None,
                    "total_time_seconds": 0,
                    "total_time_human": "00:00:00",
                },
                "status":status.HTTP_404_NOT_FOUND
                }
    
        total_seconds = total_entry.total_time_spent or 0
        human_readable = str(timedelta(seconds=total_seconds))

        logger.info(f"User {user_id} total duration fetched → {human_readable}")

        return  {
                "message":f"Activity found for user_id: {user_id}",
                "payload":{
                    "user_id": user_id,
                    "total_time_seconds": total_seconds,
                    "total_time_human": human_readable,
                },
                "status":status.HTTP_200_OK
                }

    except HTTPException:
        raise
    except Exception as e:
        logger.exception(f"Error fetching total duration for user {user_id}: {e}")
        return  {
                "message":f"Error fetching total duration for user {user_id}: {e}",
                "payload":None,
                "status":status.HTTP_404_NOT_FOUND
                }
    finally:
        db.close()

