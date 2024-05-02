#!/bin/bash
cd "$(dirname "$0")"
cd .. 
ngrok http http://localhost:9000 --log=stdout > log/ngrok.log &
sleep 3
cat log/ngrok.log