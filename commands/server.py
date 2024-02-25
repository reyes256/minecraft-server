import click

from utils import create_server_directory, generate_id, run_shell_command


@click.group()
def server():
    pass


@server.command()
@click.option("-p", "--port", default=25565)
@click.option("-v", "--version", default="LATEST")
@click.option("-t", "--type", "server_type", default="PAPER")
@click.option("-m", "--memory", default="1", help="Gigabytes to allocate to the server")
@click.option("-d", "--difficulty", default="hard", help="Game difficulty")
@click.option("-vd", "--view-distance", default="7", help="Game view distance")
@click.argument("name", default=f"mc_{generate_id(6)}")
def create(name, port, version, server_type, memory, difficulty, view_distance):
    click.echo("Creating Minecraft Server...")
    click.echo(f"\nName: {name}")
    click.echo(f"Port: {port}")
    click.echo(f"Version: {version}")
    click.echo(f"Type: {server_type}")
    click.echo(f"Memory: {memory}G")
    click.echo(f"Difficulty: {difficulty}")
    click.echo(f"View Distance: {view_distance}\n")

    server_directory_path = create_server_directory(name)

    create_server_cmd = [
        "docker",
        "run",
        "-d",
        "-it",
        "-p",
        f"{port}:25565",
        "-e",
        "EULA=TRUE",
        "-e",
        f"TYPE={server_type}",
        "-e",
        f"VERSION={version}",
        "-e",
        f"MEMORY={memory}G",
        "-e",
        f"MOTD={name}: Servercito pa los cuates",
        "-e",
        f"DIFFICULTY={difficulty}",
        "-e",
        f"VIEW_DISTANCE={view_distance}",
        "-e",
        "ICON=https://raw.githubusercontent.com/reyes256/minecraft-server/main/server-icon.png",
        "-v",
        f"{server_directory_path}/data:/data",
        "-v",
        f"{server_directory_path}/plugins:/plugins",
        "--name",
        name,
        "itzg/minecraft-server",
    ]

    run_shell_command(create_server_cmd)


@server.command()
@click.argument("name", default="mc")
def start(name):
    click.echo("Starting Minecraft Server...")

    start_server_cmd = [
        "docker",
        "start",
        name,
    ]

    follow_logs_cmd = [
        "docker",
        "logs",
        name,
        "-f",
    ]

    run_shell_command(start_server_cmd)
    run_shell_command(follow_logs_cmd)


@server.command()
@click.argument("name", default="mc")
def logs(name):
    click.echo("Following server logs...")

    follow_logs_cmd = [
        "docker",
        "logs",
        name,
        "-f",
    ]

    run_shell_command(follow_logs_cmd)


@server.command()
@click.option("--all", is_flag=True)
@click.argument("name", default="mc")
def stop(name, all):
    if name == "mc" and not all:
        click.echo("Server name is required...")
        return

    if all:
        click.echo("Stopping All Server...")
        click.echo(f"Containers: {containers_list}")

        cmd_output = run_shell_command(["docker", "ps", "-aq"])
        containers_list = cmd_output.stdout.strip().split("\n")

        for container in containers_list:
            stop_cmd = [
                "docker",
                "stop",
                container,
            ]
            run_shell_command(stop_cmd)
        return

    click.echo(f"Stopping {name}...")
    stop_cmd = [
        "docker",
        "stop",
        name,
    ]

    run_shell_command(stop_cmd)


# @server.command()
# @click.argument("name", default="mc")
# def shell(name):
#     click.echo("Connecting Minecraft Server Shell...")

#     run_shell_command(
#         [
#             "docker",
#             "exec",
#             "-i",
#             name,
#             "rcon-cli",
#         ]
#     )


# @server.command()
# def build():
#     click.echo("Building Minecraft Server Container...")
#     run_shell_command(
#         [
#             "docker",
#             "compose",
#             "-f",
#             "/opt/minecraft-server/docker-compose.yml",
#             "up",
#             "-d",
#             "--build",
#         ]
#     )


# @server.command()
# def restart():
#     click.echo("Restarting Minecraft Server...")
#     run_shell_command(
#         [
#             "docker",
#             "restart",
#             "mc",
#         ]
#     )
#     run_shell_command(
#         [
#             "docker",
#             "logs",
#             "mc",
#             "-f",
#         ]
#     )
