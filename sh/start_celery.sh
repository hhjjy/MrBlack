#!/bin/bash
# 腳本位於 ~/MrBlack/sh/start_celery.sh

# 導航到腳本所在的目錄
cd "$(dirname "$0")"

# 導航到項目根目錄
cd ..

mkdir -p log

# 終止現有的 Celery worker 和 beat 進程
echo "終止現有的 Celery 進程..."
pkill -f 'celery -A MrBlack worker'
pkill -f 'celery -A MrBlack beat'

# 稍等一段時間讓進程完全停止
sleep 5

echo "啟動新的 Celery 進程..."
# 啟動 Celery worker
nohup celery -A MrBlack worker -l info --logfile=log/worker.log > log/worker.nohup.out 2>&1 &

# 啟動 Celery beat
nohup celery -A MrBlack beat -l info --logfile=log/beat.log > log/beat.nohup.out 2>&1 &

echo "Celery worker 和 beat 已啟動。"
