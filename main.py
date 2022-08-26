import nextcord
from nextcord.ext import (
    commands,
    tasks,
)

import os
import logging
import datetime

import yarsaw
import asyncio
from gtts import gTTS

import cooldowns
from cooldowns import CallableOnCooldown

bot = yarsaw.Client("ybSHEatbivek", "0fc8104d3bmsh9fcc7b9c2a86b3fp14c1ebjsn3b44d7af5e86")

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

@bot.event
async def on_application_command_error(interaction: nextcord.Interaction, error):
    error = getattr(error, "original", error)

    if isinstance(error, CallableOnCooldown):
        embed = nextcord.Embed(
            title="You're being cooldowned!",
            description=f"Try again in {error.retry_after}.",
            color=nextcord.Color.red(),
            datetime=datetime.datetime.now()
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

@client.slash_command(description="Talk with the bot!")
async def talk(interaction):
        talking = True
        await interaction.send("You are now talking to me, to leave this, say goodbye famurai")
        while talking:
            try:
                def check(m):
                    return m.author == interaction.user and m.channel == interaction.channel
                raw_msg = await client.wait_for("message", check=check, timeout=60.0)
                msg = raw_msg.content
            except asyncio.TimeoutError:
                talking = False
                await interaction.send("You timed out, issue the command again")

            if msg == "goodbye famurai":
                talking = False
                await interaction.send("Goodbye {0.user}, I had a great time talking to you!".format(interaction))
            else:
                raw_response = await bot.get_ai_response(
                    msg, 
                    bot_name="Famu but people call me Famurai", 
                    bot_master="FlameyosFlow", 
                    bot_location="Egypt", 
                    bot_favorite_color="Black", 
                    bot_birth_place="Qatar", 
                    bot_company="Famurai inc.",
                    bot_build='Public',
                    bot_email='I have no email.',
                    bot_age='2',
                    bot_birth_date='18th December, 2021',
                    bot_birth_year='2021',
                    bot_favorite_book='Harry Potter',
                    bot_favorite_band='Imagine Dragons',
                    bot_favorite_artist='Eminem',
                    bot_favorite_actress='Selena Gomez',
                    bot_favorite_actor='Tom Holland',
                )
                response = raw_response.AIResponse

                await interaction.send(str(response))

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
