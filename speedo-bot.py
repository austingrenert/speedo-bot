import os;
import sys;
import csv;
import discord;
from discord.ext import commands;
from dotenv import load_dotenv;

# load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# get discord client
client = discord.Client()

@client.event
async def on_ready():
    print(f"Client {client.user} has connected to Discord!")

# run discord bot
client.run(TOKEN)

