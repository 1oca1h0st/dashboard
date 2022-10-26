from datetime import datetime

from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from commands.scans import *


def func(name):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(now + f"Hello: {name}")


task = {
    "jobstores": {
        "default": MemoryJobStore()
    },
    "executors": {
        #"default": ThreadPoolExecutor(10)
    },
    "job_defaults": {
        # 是否合并执行
        "coalesce": False,
        "max_instance": 5
    }
}

scheduler = AsyncIOScheduler(**task)
scheduler.add_job(func, "interval", seconds=3, args=["commands"], id="test_job", replace_existing=True)
#scheduler.add_job(get_nmap_scan_status, "interval", seconds=3)
