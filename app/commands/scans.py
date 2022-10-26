from core.controllers.tasks import jobs
from core.db.mongo import mongo


async def get_nmap_scan_status():
    tasks = mongo["assets"].find({"status": "created"})
    print(tasks)
    for task in tasks:
        job = jobs.AsyncResult(task.task_id)
        if job.status == "SUCCESS":
            result = job.get()
            await mongo["assets"].update_one(
                {
                    "task_id": task.task_id
                },
                {
                    "$set": {
                        "details": result
                    }
                }
            )
    print("aaa")
