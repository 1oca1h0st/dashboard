from loguru import logger
import os
import time

logs_dir = os.path.join(os.getcwd(), "logs")

if not os.path.exists(logs_dir):
    os.mkdir(logs_dir)

log = os.path.join(logs_dir, f'{time.strftime("%Y-%m-%d")}_log.log')
error_log = os.path.join(logs_dir, f'{time.strftime("%Y-%m-%d")}_error.log')

logger.add(log, rotation="00:00", backtrace=True, diagnose=False)
logger.add(error_log, rotation="00:00", backtrace=True, diagnose=True)
