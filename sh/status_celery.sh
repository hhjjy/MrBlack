#!/bin/bash
# 腳本位於 ~/MrBlack/sh/status_celery.sh

# 定義顏色
GREEN='\033[0;32m'
NC='\033[0m' # 無顏色

echo -e "${GREEN}Checking Celery workers and beat status...${NC}"

# 使用 grep --color=always 強制顯示顏色
ps aux | grep --color=always 'celery -A MrBlack worker'
ps aux | grep --color=always 'celery -A MrBlack beat'
