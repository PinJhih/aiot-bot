import discord

TOKEN = "YOUR_DISCORD_BOT_TOKEN"

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
        await message.channel.send(f"你好, {message.author.mention}! 你標記了我。")


client.run(TOKEN)
