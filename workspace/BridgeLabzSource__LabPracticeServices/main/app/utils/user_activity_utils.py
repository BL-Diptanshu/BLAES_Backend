from app.models.user_activity_model import UserActivity, UserTotalTime
from app.config.logger import AppLogger

logger = AppLogger.get_logger()

def log_user_activity(data: dict, db):
    """
    Log user activity using UNIX timestamps in milliseconds.
    Example payload:
    {
      "user_id": "user_123",
      "start_ts": 1731486000000,
      "end_ts": 1731488130000
    }
    """
    try:
        user_id = data.user_id
        start_ts = data.start_ts
        end_ts = data.end_ts

        if not all([user_id, start_ts, end_ts]):
            return {"status":"activity track not successfull as data is missing"}

        if not isinstance(start_ts, int) or not isinstance(end_ts, int):
            return {"status":"Timestamps must be integers (milliseconds)"}

        if end_ts < start_ts:
            return {"status":"end_ts cannot be before start_ts"}

        duration_seconds = (end_ts - start_ts) // 1000

        # Store session log
        session_entry = UserActivity(
            user_id=user_id,
            session_start=start_ts,
            session_end=end_ts,
            duration_seconds=duration_seconds,
        )
        db.add(session_entry)

        # Update total time
        total_entry = db.query(UserTotalTime).filter_by(user_id=user_id).first()
        if total_entry:
            total_entry.total_time_spent += duration_seconds
        else:
            total_entry = UserTotalTime(user_id=user_id, total_time_spent=duration_seconds)
            db.add(total_entry)

        db.commit()
        db.close()

        logger.info(f"Logged session for {user_id}: {duration_seconds} seconds")

        return {
            "status": "User session logged successfully.",
            "user_id": user_id,
            "duration_seconds_spent": duration_seconds
        }

    except Exception as e:
        logger.exception("Error logging user activity")
        return {"status":f"Error logging user activity: {e}"}