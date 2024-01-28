#!/bin/bash

cd /opt/minecraft-server/data/ && \
docker compose down && \
echo "Minecraft Server is down"

BACKUP_DIR="/opt/world-backups"
[ ! -d "${BACKUP_DIR}" ] && sudo mkdir ${BACKUP_DIR}

zip -v
[ $? -ne 0 ] && sudo apt install zip -y

cd /opt/minecraft-server/data/ && \
sudo zip -r ${BACKUP_DIR}/backup-$(date +%Y-%m-%d-%H-%M-%S).zip world world_nether world_the_end

find "$BACKUP_DIR" -name "backup-*" -mtime +7 -exec bash -c 'echo "Borrando: {}" && sudo rm -f "{}" ' \; # Delete backups older than a week

cd /opt/minecraft-server/ && \
docker compose up -d && \
echo "Minecraft Server is up"