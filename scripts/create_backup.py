import os
import shutil
import sys
from datetime import datetime, timedelta
from getpass import getuser

sys.path.append(f"/home/{getuser()}/minecraft-server/")
from utils import run_shell_command


def delete_old_backups(directory: str, days_threshold: int = 7):
    now = datetime.now()
    threshold = now - timedelta(days=days_threshold)

    for filename in os.listdir(directory):
        if filename.endswith(".zip"):
            file_path = os.path.join(directory, filename)
            modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))

            if modified_time < threshold:
                os.remove(file_path)
                print(f"Deleted {filename}")


def copy_folders(src_folder, dest_folder, folders_to_copy):
    for folder in folders_to_copy:
        shutil.copytree(
            os.path.join(src_folder, folder), os.path.join(dest_folder, folder)
        )


def create_backup(server):

    if not os.path.exists(f"/opt/minecraft/{server}"):
        print(f"Server directory {server} not found.")
        sys.exit(1)

    print(f"Stopping server: {server}")
    run_shell_command(
        [
            "docker",
            "stop",
            server,
        ]
    )

    server_data_src_path = f"/opt/minecraft/{server}/data/"
    server_data_tmp_path = f"/tmp/{server}_backup/"

    backup_base_path = f"/opt/minecraft/{server}/backups"
    backup_full_path = f"{backup_base_path}/{server}_backup_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}"

    if not os.path.exists(backup_base_path):
        os.makedirs(backup_base_path)

    copy_folders(
        server_data_src_path,
        server_data_tmp_path,
        ["world", "world_nether", "world_the_end"],
    )

    shutil.make_archive(backup_full_path, "zip", server_data_tmp_path)
    shutil.rmtree(server_data_tmp_path)

    print(f"Deleting old backups for {server}")
    delete_old_backups(backup_base_path, days_threshold=7)

    print(f"Starting Server: {server}")
    run_shell_command(
        [
            "docker",
            "start",
            server,
        ]
    )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 create_backup.py <SERVER_NAME>")
        sys.exit(1)

    server = sys.argv[1]
    create_backup(server)
