import nextcord
from nextcord.ext import (
    commands,
    tasks,
)

import os
import logging
import datetime

import asyncio

import cooldowns
from cooldowns import CallableOnCooldown

logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.WARNING)
logging.basicConfig(level=logging.CRITICAL)
logging.basicConfig(level=logging.ERROR)
logging.basicConfig(level=logging.DEBUG)

client = commands.Bot(
    command_prefix="?", 
    intents=nextcord.Intents.all(), 
    help_command=None,
    owner_id=852485677777682432
)

@client.event
async def on_application_command_error(interaction: nextcord.Interaction, error):
    error = getattr(error, "original", error)

    if isinstance(error, CallableOnCooldown):
        embed = nextcord.Embed(
            title="You're being cooldowned!",
            description=f"Try issuing this command again in {error.retry_after} seconds!",
            color=nextcord.Color.red(),
            timestamp=datetime.datetime.now()
        )
        await interaction.send(embed=embed)

    else:
        raise error
        
@client.event
async def on_ready():
    await client.wait_until_ready()
    
    await client.change_presence(activity=nextcord.Game(name=f"Prefix - Slash Commands | in ABOUT {len(client.guilds)} servers"), status=nextcord.Status.dnd)
    print('We are logged in as {0.user} by FlameyosFlow#8894!'.format(client))
    
    change_presence.start()
    
@client.event
async def on_connect():
    client.add_all_application_commands() 
    await client.sync_application_commands()
    print("Connecting to discord...")

for folder in os.listdir("./cogs"):
    for filename in os.listdir(f"./cogs/{folder}"):
        if filename.endswith(".py"):
            client.load_extension(f"cogs.{folder}.{filename[:-3]}")

for filename in os.listdir(f"./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

@tasks.loop(minutes=10.0)
async def change_presence():
    await client.change_presence(
        activity=nextcord.Game(
            name=f"Prefix - Slash Commands | in ABOUT {len(client.guilds)} servers"
        ), 
        status=nextcord.Status.dnd
    )

client.run("OTAxMDk3NTIzNzAyMjg4Mzg1.YXK6dw.6mf58Yyh4jc5oOHA9ibjIvNwKm0")
