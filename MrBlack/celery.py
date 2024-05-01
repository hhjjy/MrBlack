from __future__ import absolute_import, unicode_literals
import os
import logging
from celery import Celery
from celery.schedules import crontab, timedelta
from celery.signals import after_setup_task_logger
# 執行定期執行需要分別開兩個視窗執行下列兩個命令
# celery -A MrBlack worker -l info 被動執行
# celery -A MrBlack beat -l info 定時觸發 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MrBlack.settings')

app = Celery('MrBlack')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@after_setup_task_logger.connect
def setup_task_logger(logger, *args, **kwargs):
    handler = logging.FileHandler('celery.log')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    logger.propagate = False


# 任務調度設定 
app.conf.beat_schedule = {
    'update-database-every-5-minutes': {
        'task': 'ReminderSync.tasks.update_database',
        'schedule': timedelta(seconds=20),  # 根据需要调整时间间隔
    }
}
app.conf.broker_connection_retry_on_startup = True
