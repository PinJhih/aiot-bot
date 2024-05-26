import os
import requests
from io import BytesIO

import discord
from PIL import Image
from dotenv import load_dotenv


import gemini
from logger import logger

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
    if not client.user.mentioned_in(message):
        return

    logger.info(
        f"""From: {message.author} in {message.channel}
    {message.content}\n"""
    )

    attachment = message.attachments[0] if message.attachments else None
    if attachment and attachment.content_type.startswith("image"):
        res = requests.get(attachment.url)
        image_data = BytesIO(res.content)
        image = Image.open(image_data)

        logger.info("Send image to Gemini")
        response = gemini.send_image(message.content, image)
    else:
        logger.info("Send message to Gemini")
        response = gemini.send_message(message.content)
    await message.channel.send(f"{response}")


client.run(TOKEN)
