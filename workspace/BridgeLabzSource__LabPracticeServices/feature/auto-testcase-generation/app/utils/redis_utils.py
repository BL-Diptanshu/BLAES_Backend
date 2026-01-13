import os
import platform
import shutil
import subprocess
import time
import signal
import redis
from app.config.logger import AppLogger

logger = AppLogger.get_logger()

redis_process = None

# ---------------------------------------------------------------
# Environment detection
# ---------------------------------------------------------------

def is_production() -> bool:
    """
    Determines if running in production mode.
    """
    return os.getenv("ENV", "local").lower() in ["prod", "production"]


# ---------------------------------------------------------------
# Main Redis start logic
# ---------------------------------------------------------------

def start_redis_server():
    """
    Starts Redis locally only in local/dev environments.
    In production environments it will NOT attempt to start a server.
    """
    global redis_process

    if is_production():
        logger.info("Production mode detected — skipping local Redis startup.")
        return None

    logger.info("Local development mode — checking Redis installation...")

    system = platform.system()
    redis_exe = None

    try:
        # Detect redis executable
        if system == "Windows":
            redis_paths = [
                r"C:\Program Files\Memurai\memurai.exe",
                r"C:\Program Files\Redis\redis-server.exe",
            ]
            redis_exe = next((p for p in redis_paths if os.path.exists(p)), None)
        else:
            redis_exe = shutil.which("redis-server")

        if not redis_exe:
            logger.warning("Redis/Memurai executable not found — cannot auto-start.")
            return None

        if _is_redis_running():
            logger.info("Redis already running — skipping startup.")
            return None

        logger.info(f"Starting Redis locally: {redis_exe}")

        if system == "Windows":
            redis_process = subprocess.Popen(
                [redis_exe],
                creationflags=subprocess.CREATE_NEW_CONSOLE,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
        else:
            redis_process = subprocess.Popen(
                [redis_exe],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                preexec_fn=os.setsid
            )

        if _wait_for_redis_ready():
            logger.info("Redis is ready to accept connections.")
        else:
            logger.warning("Redis started but not responding yet.")

        return redis_process

    except Exception as e:
        logger.error(f"Failed to start Redis: {e}")
        return None


# ---------------------------------------------------------------
# Stop Redis (dev only)
# ---------------------------------------------------------------

def stop_redis_server():
    global redis_process

    if is_production():
        logger.info("Production mode — skipping Redis shutdown.")
        return

    logger.info("Stopping local Redis...")

    try:
        if shutil.which("redis-cli"):
            try:
                subprocess.run(["redis-cli", "shutdown"], check=True)
                logger.info("Redis stopped gracefully.")
                return
            except subprocess.CalledProcessError:
                logger.warning("Graceful shutdown failed — killing process...")

        if redis_process and redis_process.poll() is None:
            os.killpg(os.getpgid(redis_process.pid), signal.SIGTERM)
            logger.info("Local Redis killed via process group.")
    except Exception as e:
        logger.error(f"Failed to stop Redis: {e}")


# ---------------------------------------------------------------
# Helper utilities
# ---------------------------------------------------------------

def _is_redis_running(port=6379):
    try:
        client = redis.Redis(host="localhost", port=port)
        return client.ping()
    except Exception:
        return False


def _wait_for_redis_ready(host="localhost", port=6379, retries=10, delay=1):
    for attempt in range(1, retries + 1):
        try:
            client = redis.Redis(host=host, port=port)
            if client.ping():
                logger.info(f"Redis ready (attempt {attempt})")
                return True
        except Exception:
            time.sleep(delay)
    return False
