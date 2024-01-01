import subprocess
import settings
import discord
from discord.ext import commands

def run_command(cmd):
    try:
        full_cmd = f"docker exec mc mc-send-to-console {cmd}"
        output = subprocess.check_output(full_cmd, shell=True, text=True)
        return output
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return e

def main():
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='!', intents=intents)
    
    @bot.event
    async def on_ready():
        print('------')
        print(f'Logged in as {bot.user} (ID: {bot.user.id})')
        print('------')

    @bot.command(aliases=['p'])
    async def ping(ctx):
        await ctx.send('Pong!')
        
    @bot.command()
    async def say(ctx, *messages):
        full_message = " ".join(messages)
        
        run_command(f"say {full_message}")
        await ctx.send("Mensaje enviado: " + " ".join(messages))
        
    @bot.command()
    async def op(ctx, player="none"):
        if player == "none":
            return
        
        run_command(f"op {player}")
        await ctx.send(f"{player} es ahora operador")
    
    @bot.command()
    async def deop(ctx, player="none"):
        if player == "none":
            return
        
        run_command(f"deop {player}")
        await ctx.send(f"{player} ya no es operador")
        
    bot.run(settings.DISCORD_API_TOKEN)

if __name__ == "__main__":
    main()