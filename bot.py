"""Client for discord bot."""

import os

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

bot = commands.Bot(command_prefix="./")


@bot.command(name="ping")
async def ping(ctx):
    await ctx.channel.send("pong")


@bot.command()
async def parrot(ctx, *, arg):
    await ctx.send(arg)


class Guild:
    def chat_server():
        """Return the single server instance from environment settings."""
        return discord.utils.find(lambda g: g.name == GUILD, bot.guilds)


@bot.event
async def on_ready():
    """Run bot bot."""
    guild = Guild.chat_server()
    print(f"{bot.user} is connected to the following guild:\n" f"{guild.name}")


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f"Hi {member.name}, welcome to {GUILD}!")


@bot.add_listener
async def on_message(message):
    if message.author == bot.user:
        return

    greetings_message = "Ciao"

    if "ciao" in message.content.lower():
        await message.channel.send(
            f"{greetings_message} <@!{message.author.id}> ! :wave:"
        )


if __name__ == "__main__":
    bot.run(TOKEN)
