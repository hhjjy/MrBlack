#!/bin/bash

# 導航到腳本所在的目錄
cd "$(dirname "$0")"

# 導航到項目根目錄
cd ..

# 讀 .env 
source .dev.env 

# 安裝 ngork 
curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc \
	| sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null \
	&& echo "deb https://ngrok-agent.s3.amazonaws.com buster main" \
	| sudo tee /etc/apt/sources.list.d/ngrok.list \
	&& sudo apt update \
	&& sudo apt install ngrok
# 設定 ngork 
ngrok config add-authtoken $NGROK_AUTHTOKEN

