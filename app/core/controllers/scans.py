from core.controllers.tasks import jobs


def sub_domain_brute(domain: str):
    task_id = jobs.send_task("workers.workers.sub_domain_brute", [domain])
    return task_id
