import nextcord
from nextcord import (
    Interaction,
    slash_command
)
from nextcord.ext import commands

import random
import datetime
import os

import motor
import motor.motor_asyncio

import cooldowns

cluster = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://FlameyosFlow:reZPy4ZKz5YqumS@discord.fm5pk.mongodb.net/discord?retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE")
db = cluster.discord
collection = db.bank
companyaa = db.company

class WorkCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(name="work", description="Work and get Money!")
    @cooldowns.cooldown(1, 90, bucket=cooldowns.SlashBucket.author)
    async def work(self, interaction: Interaction):
        await interaction.response.defer()
        async with interaction.channel.typing():
            user = interaction.user
            findbank = await collection.find_one({"_id": user.id})
            if not findbank:
                await collection.insert_one({"_id": user.id, "wallet": 0})
                return

            findcompany = await companyaa.find_one({"_id": user.id})
            if not findcompany:
                await interaction.followup.send("You currently don't have a company! You can create one by `/company`.")

            wallet = findbank["wallet"]
            level = findcompany["level"]
            worthaa = findcompany["worth"]

            if level == 1:
                worth = random.randrange(float(100))
                earnings = random.randrange(1000, 10001)
            if level == 2:
                worth = random.randrange(float(250))
                earnings = random.randrange(1000, 15001)
            if level == 3:
                worth = random.randrange(float(350))
                earnings = random.randrange(5000, 25001)

            a = random.randint(1, 101)

            if a >= 85:
                embed = nextcord.Embed(
                    title="oh shi-",
                    description=f"Suddenly you had 12 hours to make a huge project, you stayed up overnight and ran late with no coffee, you accidentally dropped your huge project and poured your cup of coffee on it.",
                    color=nextcord.Color.random(),
                    timestamp=datetime.datetime.utcnow()
                )

            else:
                embed2 = nextcord.Embed(
                    title="Successful work", 
                    description=f"You have made a total of `${earnings}` after a long day of work!", color=nextcord.Color.green(),
                    timestamp=datetime.datetime.utcnow()
                )
                await interaction.followup.send(embed=embed2)
                updated_coins = wallet + earnings
                updated_worth = worthaa + round(worth)
                await collection.update_one({"_id": user.id}, {"$set": {"wallet": updated_coins}})
                await companyaa.update_one({"_id": user.id}, {"$set": {"worth": updated_worth}})

def setup(client):
    client.add_cog(WorkCommand(client))
