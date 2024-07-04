import discord
from discord.ext import commands
from token import token
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
@bot.command()
async def bilgi1(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, şimdi sana şakayla bilgi vericem,adam denize girdi çöp adama dönüştü')

@bot.command()
async def bilgi2(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, şimdi sana şakayla bilgi vericem,demir çağindan sonraki çağ plastik çağidir')   

bot.run(token)