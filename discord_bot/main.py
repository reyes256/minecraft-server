import subprocess
import settings
import discord
from discord.ext import commands

def run_command(command):
    try:
        output = subprocess.check_output(command, shell=True, text=True)
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
        
        cmd = f"docker exec mc mc-send-to-console say {full_message}"
        run_command(cmd)
        
        await ctx.send("Mensaje enviado: " + " ".join(messages))
        
    @bot.command()
    async def op(ctx, player="none"):
        if player == "none":
            return
        
        cmd = f"docker exec mc mc-send-to-console op {player}"
        run_command(cmd)
        
        await ctx.send(f"Fakin {player} ya es OP")
    
    @bot.command()
    async def deop(ctx, player="none"):
        if player == "none":
            return
        
        cmd = f"docker exec mc mc-send-to-console deop {player}"
        run_command(cmd)
        
        await ctx.send(f"Mamaste {player}, ya no eres OP")
        
    bot.run(settings.DISCORD_API_TOKEN)

if __name__ == "__main__":
    main()