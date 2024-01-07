#!/bin/bash

cd /opt/minecraft-server/data/ && \
docker compose down && \
echo "Minecraft Server is down"

BACKUP_DIR="/opt/minecraft-server-backups"
[ ! -d "${BACKUP_DIR}" ] && sudo mkdir ${BACKUP_DIR}

zip -v
[ $? -ne 0 ] && sudo apt install zip -y

cd /opt/minecraft-server/data/ && \
sudo zip -r ${BACKUP_DIR}/backup-$(date +%Y-%m-%d-%H-%M-%S).zip . 

find "$BACKUP_DIR" -name "backup-*" -mtime +3 -exec bash -c 'echo "Borrando: {}" && sudo rm -f "{}" ' \; # Delete backups older than 3 days

cd /opt/minecraft-server/ && \
docker compose up -d && \
echo "Minecraft Server is up"