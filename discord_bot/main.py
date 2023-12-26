import subprocess
import settings
import discord
from discord.ext import commands

def run():
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='!', intents=intents)
    
    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user} (ID: {bot.user.id})')
        print('------')

    @bot.command(aliases=['p'])
    async def ping(ctx):
        await ctx.send('Pong!')
        
    @bot.command()
    async def say(ctx, *messages):
        await ctx.send("Mensaje enviado: " + " ".join(messages))
        
    @bot.command()
    async def op(ctx, player="none"):
        if player == "none":
            return
        
        command = ["docker", "exec", "mc", "mc-send-to-console", "op", player]
        command2 = ["docker", "compose", "-f","/opt/minecraft-server/docker-compose.yml", "up", "-d"]

        try:
            result = subprocess.run(command2, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            print("Command Output:")
            print(result.stdout)

            if result.stderr:
                print("Command Error:")
                print(result.stderr)

            await ctx.send(f"Fakin {player} ya es OP")
        except subprocess.CalledProcessError as e:
            # Handle exceptions for non-zero exit codes
            print(f"Error executing command: {e}")
            await ctx.send(f"Error ejecutando el comando: {e}")
        except Exception as e:
            # Handle other exceptions
            print(f"An unexpected error occurred: {e}")
            await ctx.send(f"Error inesperado: {e}")

            
        
    bot.run(settings.DISCORD_API_TOKEN)

if __name__ == "__main__":
    run()