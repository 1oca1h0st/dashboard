import datetime

from fastapi.encoders import jsonable_encoder

from core.controllers.tasks import jobs
from core.db.mongo import mongo


def sub_domain_brute(domain: str):
    task = jobs.send_task("workers.workers.sub_domain_brute", [domain])
    return task


async def nmap_scan(ip: str, ports: str):
    task = jobs.send_task("workers.workers.nmap_scan", [ip.split(","), ports])
    # 保存任务数据
    data = jsonable_encoder({
        "task_id": task.id,
        "name": f'{ip} - {ports} 的扫描任务',
        "status": "created",
        "created_time": datetime.datetime.now(),
        "updated_time": datetime.datetime.now(),
    })
    await mongo["assets"].insert_one(data)
    return task.id
