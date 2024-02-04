#!.venv/bin/python
import subprocess

import click


@click.group()
def mcli():
    pass


@mcli.group()
def server():
    pass


@server.command()
def start():
    click.echo("Starting Minecraft Server...")
    run_shell_command(
        [
            "docker",
            "compose",
            "-f",
            "/opt/minecraft-server/docker-compose.yml",
            "up",
            "-d",
        ]
    )


@server.command()
def stop():
    click.echo("Stopping Minecraft Server...")
    run_rcon_command("stop")


@server.command()
def restart():
    click.echo("Restarting Minecraft Server...")
    run_shell_command(
        [
            "docker",
            "restart",
            "mc",
        ]
    )


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


if __name__ == "__main__":
    mcli()
