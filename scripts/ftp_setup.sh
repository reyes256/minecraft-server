#!/bin/bash

sudo apt install vsftpd -y
sudo cp /etc/vsftpd.conf /etc/vsftpd.conf.backup
sudo sed -i 's/#write_enable=YES/write_enable=YES/' /etc/vsftpd.conf
sudo service vsftpd restart
sudo chmod a+w -R /opt/minecraft-server/data