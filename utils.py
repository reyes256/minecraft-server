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


def run_shell_command(commands):
    """
    Run command on current platform

    Parameters:
    - commands (str or list): The list of commands to execute.

    Raises:
    - subprocess.CalledProcessError: If the command execution fails.

    Returns:
    - CompletedProcess: The result of the command execution.
    """
    if isinstance(commands, str):
        commands = [commands]

    try:
        result = subprocess.run(commands, check=True)
        return result
    except subprocess.CalledProcessError as e:
        print(f"Error executing shell command: {e}")
        raise


def run_rcon_command(commands):
    """
    Sends command to Minecraft Server cli using rcon

    Parameters:
    - commands (str or list): The list of commands to execute.

    Returns:
    - None
    """
    if isinstance(commands, str):
        commands = [commands]

    prefix_command = ["docker", "exec", "mc", "rcon-cli"]
    full_command = prefix_command + commands

    try:
        subprocess.run(
            full_command,
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"Error executing shell command: {e}")
