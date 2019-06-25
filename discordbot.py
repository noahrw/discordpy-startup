from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def vnn(ctx):
    await ctx.send('やめときな……')

@bot.command()
async def cobra(ctx):
    await ctx.send('ｼﾞｬｰｰｰｰｰｰｰｰｰｰｰｰｯ!!')

bot.run(token)
