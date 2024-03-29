.PHONY: server-start server-stop server-shell backup-create backup-restore

server-start:
	@echo Starting Minecraft Server...
	@sudo docker compose up -d
	@sudo docker logs mc -f

server-stop:
	@echo Stopping Minecraft Server...
	@sudo docker compose down

server-shell:
	@echo Connecting To Server Shell...
	@sudo docker exec -i mc rcon-cli

backup-create:
	@echo Creating world map backup... 
	@sudo bash ./scripts/backup_create.sh

backup-restore: # make backup-restore NAME=backup-2024-01-28-11-52-43.zip
	@echo Restoring world map to a previous backup... [$(NAME)]
	@sudo bash ./scripts/backup_restore.sh $(NAME)