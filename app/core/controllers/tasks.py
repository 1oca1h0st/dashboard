from celery import Celery

jobs = Celery(
    broker="redis://127.0.0.1:6379/0",
    backend="redis://127.0.0.1:6379/1"
)


def get_celery_task_status(task_id: str):
    return jobs.AsyncResult(task_id).status


def get_celery_task_result(task_id: str):
    return jobs.AsyncResult(task_id).result
