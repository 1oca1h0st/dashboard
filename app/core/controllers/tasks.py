from celery import Celery

jobs = Celery(
    broker="redis://127.0.0.1:6379/0",
    backend="redis://127.0.0.1:6379/1"
)
