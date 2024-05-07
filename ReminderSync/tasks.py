import csv
import requests
from celery import shared_task
from .models import Reminder
from datetime import datetime
from celery.utils.log import get_task_logger
from celery import shared_task
from datetime import timedelta
from celery.task import periodic_task


logger = get_task_logger(__name__)

@periodic_task(run_every=timedelta(seconds=10))
def update_database_periodically():
    update_database.delay()

logger = get_task_logger(__name__)

@shared_task
def update_database():
    logger.info("開始更新資料庫")
    print("開始更新資料庫")  # 簡單的輸出來確認這個函數是否被調用

    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSMbMMFOQY6bJb1buR4RsYHi1WHX2CxPqy1X0z34S3eRDrfiNC-KC49C6e3fbj1NtA8V082u3duuaDL/pub?output=csv"
    response = requests.get(url)
    if response.status_code == 200:
        print("hey")
        response.raise_for_status() 
        csv_data = response.text.splitlines()
        
        for row in csv.reader(csv_data):
            timestamp, assignee, target, task, deadline, completed_date, repeat, completed = row
            
            deadline = datetime.strptime(deadline, "%Y/%m/%d")
            completed_date = datetime.strptime(completed_date, "%Y/%m/%d") if completed_date else None
            
            Reminder.objects.create(
                timestamp=timestamp,
                assignee=assignee,
                target=target,
                task=task,
                deadline=deadline,
                completed_date=completed_date,
                repeat=repeat,
                completed=completed
            )
    # ...
    print("資料庫更新完成")  # 簡單的輸出來確認這個函數是否被調用
    logger.info("資料庫更新完成")
    