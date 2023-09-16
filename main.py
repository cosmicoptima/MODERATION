from dotenv import load_dotenv
load_dotenv()
from os import getenv

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("yooooo")

client.run(getenv("DISCORD_BOT_TOKEN"))
