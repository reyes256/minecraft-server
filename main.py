import click

from commands.server import server


@click.group()
def mcli():
    pass


mcli.add_command(server)

if __name__ == "__main__":
    mcli()
