from celery import Celery

from workers.assets.subfinder import SubFiner

jobs = Celery(
    "tasks",
    broker="redis://127.0.0.1:6379/0",
    backend="redis://127.0.0.1:6379/1"
)


@jobs.task()
def sub_domain_brute(domain: str):
    return SubFiner().scan(domain, "", 0)
