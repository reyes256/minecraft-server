#!/bin/bash

sudo apt update && \
sudo apt install zip unzip -y

#-------
# Clone server repo
cd /opt && \
sudo git clone https://github.com/reyes256/minecraft-server.git && \
git config --global --add safe.directory /opt/minecraft-server
sudo chmod -R a+w /opt/minecraft-server/
sudo chmod +x /opt/minecraft-server/scripts/*.sh 
sudo cp /opt/minecraft-server/.env.example /opt/minecraft-server/.env

#--------------------------
#       Set local time
sudo timedatectl set-timezone America/Phoenix

#--------------------------
#       Set Cronjob for world backups
existing_crontab=$(crontab -l 2>/dev/null)
new_cron_job="0 3 * * * /opt/minecraft-server/scripts/backup_data.sh"

updated_crontab="${existing_crontab}\n${new_cron_job}"

sudo chmod +x /opt/minecraft-server/scripts/backup_data.sh
echo -e "$updated_crontab" | crontab -
echo "Cron job appended successfully."

#--------------------------
#       Install docker
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg -y
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y

sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker