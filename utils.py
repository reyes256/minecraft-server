import os
import random
import string
import subprocess


def generate_id(n: int = 64) -> str:
    """
    Generates a random alphanumeric string of length n.

    Parameters:
    - n (int): The length of the string to generate. Default is 64.

    Returns:
    - str: The generated alphanumeric string.
    """
    characters = string.ascii_letters + string.digits
    alphanumeric_id = "".join(random.choice(characters) for _ in range(n))
    return alphanumeric_id


def create_server_directory(container_name: str):
    """
    Create a directory for the server data

    Parameters:
    - container_name (str): The name of the container.

    Returns:
    - None
    """
    server_directory_path = f"/opt/minecraft/{container_name}"

    if not os.path.exists(server_directory_path):
        os.makedirs(server_directory_path)

    return server_directory_path


def run_shell_command(args):
    """
    Run command on current platform

    Parameters:
    - commands (str or list): The list of commands to execute.

    Raises:
    - subprocess.CalledProcessError: If the command execution fails.

    Returns:
    - CompletedProcess: The result of the command execution.
    """
    if isinstance(args, str):
        args = [args]

    try:
        process = subprocess.Popen(
            args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        for line in process.stdout:
            if not line.startswith(">"):
                print(line, end="")
        for line in process.stderr:
            if not line.startswith(">"):
                print(line, end="")

        return process.wait()
    except subprocess.CalledProcessError as e:
        print(f"Error executing shell command: {e}")
        raise


def run_rcon_command(args):
    """
    Sends command to Minecraft Server cli using rcon

    Parameters:
    - commands (str or list): The list of commands to execute.

    Returns:
    - None
    """
    if isinstance(args, str):
        args = [args]

    prefix_command = ["docker", "exec", "mc", "rcon-cli"]
    full_command = prefix_command + args

    try:
        subprocess.run(
            full_command,
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"Error executing shell command: {e}")
