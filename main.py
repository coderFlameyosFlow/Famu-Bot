import nextcord
from nextcord.ext import (
    commands,
    tasks,
)

from keep_alive import keep_alive

import os
import logging

import yarsaw
import asyncio
from gtts import gTTS

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

@client.event
async def on_ready():
    await client.change_presence(
        activity=nextcord.Game(
            name=f"Prefix - Slash Commands | in ABOUT {len(client.guilds)} servers"
        ), 
        status=nextcord.Status.dnd
    )
    print('We are logged in as {0.user} by FlameyosFlow#8894!'.format(client))
    change_presence.start()

@client.slash_command(description="Talk with the bot!")
async def talk(interaction):
    if (interaction.user.voice):
        vc = await interaction.user.voice.channel.connect()
        talking = True
        await interaction.send("You are now talking to me, to leave this, issue /leave or say goodbye famurai")
        while talking:
            try:
                def check(m):
                    return m.author == interaction.user and m.channel == interaction.channel
                raw_msg = await client.wait_for("message", check=check, timeout=60.0)
                msg = raw_msg.content
            except asyncio.TimeoutError:
                talking = False
                await interaction.guild.voice_client.disconnect()
                await interaction.send("You timed out, issue the command again")

            if msg == "goodbye famurai":
                talking = False
                await interaction.send("Goodbye {0.user}, I had a great time talking to you!".format(interaction))
                await interaction.guild.voice_client.disconnect()
            else:
                raw_response = await bot.get_ai_response(
                    msg, 
                    bot_name="Famu but people call me Famurai", 
                    bot_master="FlameyosFlow", 
                    bot_location="Qatar", 
                    bot_favorite_color="Black", 
                    bot_birth_place="Egypt", 
                    bot_company="Fire Samurai inc.",
                    bot_build='Public',
                    bot_email='...I have no email.',
                    bot_age='1',
                    bot_birth_date='18th December, 2021',
                    bot_birth_year='2021',
                    bot_favorite_book='Harry Potter',
                    bot_favorite_band='Balenciaga',
                    bot_favorite_artist='Eminem',
                    bot_favorite_actress='Selena Gomez',
                    bot_favorite_actor='Tom Holland',
                )
                response = raw_response.AIResponse
                output = gTTS(text=response, lang='en', slow=False)
                output.save("output.mp3")
                vc.play(nextcord.FFmpegPCMAudio("output.mp3"))

                await interaction.send(str(response))

@client.slash_command(description="Stop chatting with Famurai")
async def leave(interaction):
    talking = True
    while talking is True:
        talking = False
    else:
        try:
            await interaction.guild.voice_client.disconnect()
        except:
            pass
        await interaction.send("I'm not even talking to you.")
        return

    print(talking)
    if (interaction.user.voice or client.user.voice):
        await interaction.guild.voice_client.disconnect()
        await interaction.send("I have left the voice channel!")

    else:
        await interaction.send("Okay, Thanks for talking with me :D")

"""
@client.slash_command(description="Talk with the bot!")
async def talk(interaction):
        async with interaction.channel.typing():
            if (interaction.user.voice):
                vc = interaction.user.voice.channel
                vca = await vc.connect()
                talking = True
                await interaction.send("You are now talking to me, to end this interaction type: goodbye famurai!")

                while talking:

                    try:
                        def check(m):
                            return m.author == interaction.user

                        msg_raw = await client.wait_for("message", check=check, timeout=60.0)
                        msg = msg_raw.content
                    except asyncio.TimeoutError:
                        talking = False
                        await interaction.send("You timed out, rerun the command.")
                        return

                    raw_response = await bot.get_ai_response(
                        msg, 
                        bot_name="Famu but people call me Famurai", 
                        bot_master="FlameyosFlow", 
                        bot_location="Qatar", 
                        bot_favorite_color="Black", 
                        bot_birth_place="Egypt", 
                        bot_company="Fire Samurai inc.",
                        bot_build='Public',
                        bot_email='...I have no email.',
                        bot_age='1',
                        bot_birth_date='18th December, 2021',
                        bot_birth_year='2021',
                        bot_favorite_book='Harry Potter',
                        bot_favorite_band='Balenciaga',
                        bot_favorite_artist='Eminem',
                        bot_favorite_actress='Selena Gomez',
                        bot_favorite_actor='Tom Holland',
                    )

                    response = raw_response.AIResponse
                    output = gTTS(text=response, lang="en", slow=False)
                    output.save("output.mp3")

                    if msg == "goodbye famurai":
                        talking = False
                        await interaction.send("Okay, I will stop talking to you, nice seeing you {}".format(interaction.user.mention))
                        await interaction.guild.voice_client.disconnect()

                    else:
                        vca.play(nextcord.FFmpegPCMAudio("output.mp3"))
                        await interaction.send(response)

            else:
                await interaction.send("You're not in a voice channel, do you want to continue without voice? respond in `yes` or `no`")
                try:
                    def check(m):
                        return m.author == interaction.user
                        
                    raw_msg = await client.wait_for("message", check=check, timeout=60.0)
                    msg = raw_msg.content
                except asyncio.TimeoutError:
                    await interaction.send("You timed out, rerun the command.")
                    pass

                if msg == "yes":
                    talking = True
                    await interaction.send("You are now talking to me, to end this interaction: type goodbye famurai!")

                    while talking:

                        try:
                            def check(m):
                                return m.author == interaction.user and m.channel == interaction.channel

                            msg_raw = await client.wait_for("message", check=check, timeout=60.0)
                            msg = msg_raw.content
                        except asyncio.TimeoutError:
                            await interaction.send("You timed out, rerun the command.")
                            pass

                        if msg == "goodbye famurai":
                            talking = False
                            await interaction.send("Okay, I will stop talking to you, nice seeing you {}".format(interaction.user.mention))

                        else:
                            raw_response = await bot.get_ai_response(
                                msg, 
                                bot_name="Famu but people call me Famurai", 
                                bot_master="FlameyosFlow", 
                                bot_location="Qatar", 
                                bot_favorite_color="Black", 
                                bot_birth_place="Egypt", 
                                bot_company="Fire Samurai inc.",
                                bot_build='Public',
                                bot_email='...I have no email.',
                                bot_age='1',
                                bot_birth_date='18th December, 2021',
                                bot_birth_year='2021',
                                bot_favorite_book='Harry Potter',
                                bot_favorite_band='Balenciaga',
                                bot_favorite_artist='Eminem',
                                bot_favorite_actress='Selena Gomez',
                                bot_favorite_actor='Tom Holland',
                            )
                            response = raw_response.AIResponse

                            await interaction.send(response)

                elif msg == "no":
                    await interaction.response.send_message("Okay, I guess I will take that as a no.")

@client.slash_command(description="Stop chatting with Famurai")
async def leave(interaction):
        async with interaction.channel.typing():
            talking = True
            while talking is True:
                talking = False
            else:
                await interaction.send("I'm not even talking to you.")

            print(talking)
            if (interaction.user.voice):
                await interaction.guild.voice_client.disconnect()
                await interaction.send("I have left your voice channel!")

            else:
                await interaction.send("Okay, Thanks for talking with me :D")
"""

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
