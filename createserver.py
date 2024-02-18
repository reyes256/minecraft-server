import random
import string
import subprocess


def generate_id(n=64):
    characters = string.ascii_letters + string.digits
    alphanumeric_id = "".join(random.choice(characters) for _ in range(n))
    return alphanumeric_id


def run_shell_command(commands):
    """
    Run command on current platform

    Parameters:
    - commands (str or list): The list of commands to execute.

    Returns:
    - None
    """
    if isinstance(commands, str):
        commands = [commands]

    try:
        subprocess.run(
            commands,
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"Error executing shell command: {e}")
    pass


cmd = [
    "docker",
    "run",
    "-d",
    "-it",
    "-p",
    "25565:25565",
    "--rm",
    "-e",
    "EULA=TRUE",
    "-e",
    "VERSION=1.20.2",
    "--name",
    f"mc-{generate_id(6)}",
    "itzg/minecraft-server",
]

run_shell_command(cmd)
