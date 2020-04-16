import yaml
import discord
from discord.ext import commands

with open("config.yml", "r") as f:
    try:
        config = yaml.safe_load(f)
    except yaml.YAMLError as exc:
        print(exc)

client = commands.Bot(command_prefix = config.get("prefix"))

@client.event
async def on_ready():
    print("The bot is ready")


@client.command()
async def testbot(ctx):
    await ctx.send("the bot is online.")


client.run(config.get("token"))
