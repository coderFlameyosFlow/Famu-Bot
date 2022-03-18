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

cluster = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("mongodb"))
db = cluster.discord
collection = db.bank
companyaa = db.company

class WorkCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(name="work", description="Work and get Money!")
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

            loss = random.randint(1000, 5000)
            a = random.randint(1, 101)

            if a > 75:
                embed = nextcord.Embed(
                    title="oh shi-",
                    description=f"You got absolutely nothing from working, actually you owe us ${loss:,}.",
                    color=nextcord.Color.random(),
                    timestamp=datetime.datetime.utcnow()
                )

                await interaction.followup.send(embed=embed)
                updated_coins = wallet - loss
                await collection.update_one({"_id": user.id}, {"$set": {"wallet": updated_coins}})

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