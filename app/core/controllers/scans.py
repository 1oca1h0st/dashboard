from core.controllers.tasks import jobs


def sub_domain_brute(domain: str):
    task_id = jobs.send_task("workers.workers.sub_domain_brute", [domain])
    return task_id


def nmap_scan(ip: str, ports: str):
    scope = ip.split(",")
    task = jobs.send_task("workers.workers.nmap_scan", [scope, ports])
    return task
