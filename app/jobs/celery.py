from celery import Celery
import time

jobs = Celery("tasks", broker="redis://127.0.0.1:6379/0", backend="redis://127.0.0.1:6379/1")


@jobs.task()
def add(x, y):
    time.sleep(30)
    return x + y
