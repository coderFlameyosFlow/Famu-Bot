import nextcord
from nextcord import (
    slash_command,
    Interaction,
)
from nextcord.ext import commands

import datetime
import random
import os

import motor
import motor.motor_asyncio

import cooldowns

cluster = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://FlameyosFlow:reZPy4ZKz5YqumS@discord.fm5pk.mongodb.net/discord?retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE")
db = cluster.discord
collection = db.bank

meanresponses = [
    "ew you got germs on me",
    "get away from me you stinky person",
    "can you please like get off my back",
    "I don't have any change, sorry poor buckaro",
    "you think I'm jeff bezos or something?",
    "can you like, go and get a job?",
    "I would not even give you the salary of a school janitor",
    "please, get awayyy",
    "look at you ew get a job",
    "you just ruined my wedding dress!!!!! you little-",
    "*runs away from homeless buckaro*",
    "get away bucko *spills coffee at you*",
    "you're lucky I'm not spitting at you",
    "*ignores*",
    "ughh you broke my phone I need to go to aPpLe",
    "YOU JUST RUINED MY TIKTOK HOW COULD YOU *spits at you*",
]

class BegCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(name="beg", description="Beg off the streets!")
    @cooldowns.cooldown(1, 25, bucket=cooldowns.SlashBucket.author)
    async def beg(self, interaction: Interaction):
        member = interaction.user
        findbank = await collection.find_one({"_id": member.id})
        if not findbank:
            await collection.insert_one({"_id": member.id, "wallet": 0, "bank": 0})

        wallet = findbank["wallet"]

        earnings = random.randrange(1, 1001)

        begchance = random.randint(1, 101)
                
        if begchance > 55:
            em = nextcord.Embed(
                title="oh uh-", 
                description=f"Some Person: {random.choice(meanresponses)}", 
                color=nextcord.Color.red(), 
                timestamp=datetime.datetime.utcnow()
            )
            em.set_footer(text="Maybe next time buddy.")
            await interaction.response.send_message(embed=em)

        elif begchance < 45:
            updated_money = wallet + earnings
            await collection.update_one({"_id": member.id}, {"$set": {"wallet": updated_money}})
            em = nextcord.Embed(
                title="les goo!", 
                description=f"Someone gave you ${earnings}, May god keep Them.", color=nextcord.Color.green(),
                timestamp=datetime.datetime.utcnow()
            )
            await interaction.response.send_message(embed=em)
        return

def setup(client):
    client.add_cog(BegCommand(client))
