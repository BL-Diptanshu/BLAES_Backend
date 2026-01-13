from celery import Celery

celery = Celery(
    "celery_tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
    include=["app.tasks.testcase_tasks","app.tasks.java_runner"] 
)

celery.conf.update(
    task_track_started=True,
    result_expires=3600,
)

celery.autodiscover_tasks(["app.tasks"])
