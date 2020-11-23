"""Client for discord bot."""

import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

client = discord.Client()


class Guild:
    def chat_server():
        """Return the single server instance from environment settings."""
        return discord.utils.find(lambda g: g.name == GUILD, client.guilds)


@client.event
async def on_ready():
    """Run bot client."""
    guild = Guild.chat_server()

    print(f"{client.user} is connected to the following guild:\n" f"{guild.name}")


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f"Hi {member.name}, welcome to {GUILD}!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    happy_birthday_message = "Auguri di Buon Compleanno"

    if "buon compleanno" in message.content.lower() and message.raw_mentions:
        await message.channel.send(
            f"{happy_birthday_message} <@!{message.raw_mentions[0]}> ! :cake: :champagne_glass:"
        )


if __name__ == "__main__":
    client.run(TOKEN)
