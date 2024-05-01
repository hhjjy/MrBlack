#!/bin/bash
# 腳本位於 ~/MrBlack/sh/stop_celery.sh

# 殺掉 Celery worker 進程
pkill -f 'celery -A MrBlack worker'

# 殺掉 Celery beat 進程
pkill -f 'celery -A MrBlack beat'
