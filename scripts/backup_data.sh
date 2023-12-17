#!/bin/bash

cd /opt/minecraft-server/data/ && \
docker compose down && \
echo "Minecraft Server is down"

if [ ! -d "/opt/minecraft-server-backups" ]; then
  sudo mkdir /opt/minecraft-server-backups
fi

zip -v
if [ $? -ne 0 ]; then
  sudo apt install zip -y
fi

cd /opt/minecraft-server/data/ && \
sudo zip -r /opt/minecraft-server-backups/backup-$(date +%Y-%m-%d-%H-%M-%S).zip . 

cd /opt/minecraft-server/ && \
docker compose up -d && \
echo "Minecraft Server is up"