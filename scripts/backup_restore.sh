#!/bin/bash

BACKUP_NAME=$1

if [ -z "$BACKUP_NAME" ]; then
    echo "The name of the backup zip is required."
    exit 0
fi

cd /opt/minecraft-server/ && \
sudo docker compose down && \
echo "Minecraft Server is down"

OLD_WORLD_FOLDER=/opt/minecraft-server/data/old_world_$(date +%Y-%m-%d-%H-%M-%S)
mkdir $OLD_WORLD_FOLDER
mv /opt/minecraft-server/data/world $OLD_WORLD_FOLDER
mv /opt/minecraft-server/data/world_nether $OLD_WORLD_FOLDER
mv /opt/minecraft-server/data/world_the_end $OLD_WORLD_FOLDER

cp /opt/world-backups/${BACKUP_NAME} /opt/minecraft-server/data/backup.zip

cd /opt/minecraft-server/data/
unzip ./backup.zip && \
sudo chmod -R a+w ./world*

sudo rm -f ./backup.zip

cd /opt/minecraft-server/ && \
sudo docker compose up -d && \
echo "Minecraft Server is up"