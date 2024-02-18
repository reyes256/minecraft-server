import click

from utils import run_rcon_command, run_shell_command


@click.group()
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
