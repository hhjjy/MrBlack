from celery.utils.log import get_task_logger
from celery import shared_task

logger = get_task_logger(__name__)

@shared_task
def update_database():
    logger.info("開始更新資料庫")
    print("開始更新資料庫")  # 簡單的輸出來確認這個函數是否被調用

    # 你的更新邏輯
    # ...
    print("資料庫更新完成")  # 簡單的輸出來確認這個函數是否被調用
    logger.info("資料庫更新完成")
