#!/bin/bash
# 腳本位於 ~/MrBlack/sh/start_celery.sh

# 導航到腳本所在的目錄
cd "$(dirname "$0")"

# 導航到項目根目錄
cd ..

# 啟動 Celery worker
celery -A MrBlack worker -l info -D

# 啟動 Celery beat
celery -A MrBlack beat -l info -D
