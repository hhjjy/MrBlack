from celery.utils.log import get_task_logger
from celery import shared_task
import requests
logger = get_task_logger(__name__)


@shared_task
def trigger_task_reminder():
    url = 'http://127.0.0.1:9000/api/reminder-analysis/task-reminder/'
    logger.info("檢測任務清單")
    print("檢測任務清單")  # 簡單的輸出來確認這個函數是否被調用
    response = requests.get(url)
    if response.status_code == 200:
        print("任務提醒已成功發送")
    else:
        print("發送任務提醒時發生錯誤")