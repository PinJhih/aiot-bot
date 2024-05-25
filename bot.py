import os

import discord
from dotenv import load_dotenv

import gemini

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Logged in as {client.user.name} (ID: {client.user.id})")
    print("-" * 32)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user.mentioned_in(message):
        response = gemini.send_message(message.content)
        await message.channel.send(f"{response}")


client.run(TOKEN)
