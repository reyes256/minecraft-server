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

    start_server_cmd = [
        "docker",
        "compose",
        "-f",
        "/opt/minecraft-server/docker-compose.yml",
        "up",
        "-d",
    ]

    follow_logs_cmd = [
        "docker",
        "logs",
        "mc",
        "-f",
    ]

    run_shell_command(start_server_cmd)
    run_shell_command(follow_logs_cmd)


@server.command()
def stop():
    click.echo("Stopping Minecraft Server...")
    run_rcon_command("stop")


@server.command()
def build():
    click.echo("Building Minecraft Server Container...")
    run_shell_command(
        [
            "docker",
            "compose",
            "-f",
            "/opt/minecraft-server/docker-compose.yml",
            "up",
            "-d",
            "--build",
        ]
    )


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
    run_shell_command(
        [
            "docker",
            "logs",
            "mc",
            "-f",
        ]
    )


@server.command()
def shell():
    click.echo("Connecting Minecraft Server Shell...")
    run_shell_command(
        [
            "docker",
            "exec",
            "-i",
            "mc",
            "rcon-cli",
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
