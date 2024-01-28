.PHONY: backup-restore

backup-create:
	@echo Creating world map backup... 
	sudo bash ./scripts/backup_create.sh

backup-restore:
	@sudo bash ./scripts/backup_restore.sh $(ZIP_PATH)

test:
	@echo $(MSG)

# make backup-restore ZIP_PATH=/path/to/your/backup.zip