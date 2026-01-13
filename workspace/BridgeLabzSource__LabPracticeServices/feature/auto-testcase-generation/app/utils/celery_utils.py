import os
import subprocess
import platform
import signal
import shutil
import psutil
from app.config.logger import AppLogger


# from celery import Celery

# celery = Celery(
#     "celery_tasks",
#     broker="redis://localhost:6379/0",
#     backend="redis://localhost:6379/0"
# )

# celery.conf.update(
#     task_track_started=True,
#     result_expires=3600,
# )

# celery.autodiscover_tasks(["app"])

logger = AppLogger.get_logger()
celery_process = None

def start_celery_worker():
    """
    Starts Celery in a new terminal window and keeps the process handle for later shutdown.
    Works on Windows + Linux.
    """
    global celery_process
    system = platform.system()
    celery_command = (
    "celery -A app.core.celery_app worker --loglevel=info --pool=solo"
    if system == "Windows"
    else "celery -A app.core.celery_app worker --loglevel=info"
    )

    try:
        if system == "Windows":
            logger.info("Starting Celery in new CMD window (Windows)...")
            celery_process = subprocess.Popen(
                ["cmd.exe", "/k", celery_command],
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )
            logger.info(f"Celery worker started in new terminal (PID={celery_process.pid})")

        elif system == "Linux":
            logger.info("Starting Celery in new terminal (Linux)...")

            if shutil.which("gnome-terminal"):
                celery_process = subprocess.Popen([
                    "gnome-terminal", "--", "bash", "-c",
                    f"{celery_command}; exec bash"
                ])
            elif shutil.which("xterm"):
                celery_process = subprocess.Popen([
                    "xterm", "-hold", "-e", celery_command
                ])
            else:
                celery_process = subprocess.Popen(
                    celery_command.split(),
                    preexec_fn=os.setsid
                )
                logger.warning("No GUI terminal found — running Celery in background.")

            logger.info(f"Celery worker started (PID={celery_process.pid})")

        else:
            logger.warning(f"Unsupported OS {system}, running in background.")
            celery_process = subprocess.Popen(
                celery_command.split(),
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

        return celery_process

    except Exception as e:
        logger.exception(f"Failed to start Celery worker: {e}")
        return None


def stop_celery_worker():
    """
    Stops the Celery worker and closes the terminal window.
    """
    global celery_process
    if not celery_process:
        logger.warning("No Celery worker process to stop.")
        return

    system = platform.system()
    pid = celery_process.pid
    logger.info(f"Attempting to stop Celery (PID={pid})...")

    try:
        if system == "Windows":
            try:
                # Kill the entire process tree (cmd.exe + celery)
                parent = psutil.Process(pid)
                for child in parent.children(recursive=True):
                    child.kill()
                parent.kill()
                logger.info("Celery terminal and worker closed on Windows.")
            except Exception as e:
                logger.error(f"Failed to kill process tree: {e}")
                os.system(f"taskkill /F /T /PID {pid}")

        elif system == "Linux":
            os.killpg(os.getpgid(pid), signal.SIGTERM)
            logger.info("Celery terminal and worker closed on Linux.")

        else:
            logger.warning(f"Unsupported OS {system} — killing directly.")
            celery_process.terminate()

    except Exception as e:
        logger.error(f"Error stopping Celery worker: {e}")