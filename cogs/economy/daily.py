import nextcord
from nextcord import (
    Interaction,
    slash_command
)
from nextcord.ext import commands

import os
import datetime

import motor
import motor.motor_asyncio

import cooldowns

cluster = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://FlameyosFlow:reZPy4ZKz5YqumS@discord.fm5pk.mongodb.net/discord?retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE")
db = cluster.discord
collection = db.bank

class DailyCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(name="daily", description="Get daily money!")
    @cooldowns.cooldown(1, 86400, bucket=cooldowns.SlashBucket.author)
    async def daily(self, interaction: Interaction):
        async with interaction.channel.typing():
            member = interaction.user
            findbank = await collection.find_one({"_id": member.id})
            if not findbank:
                await collection.insert_one({"_id": member.id, "wallet": 0})

            wallet = findbank["wallet"]
            uw = wallet + 10000

            await collection.update_one({"_id": member.id}, {"$set": {"wallet": uw}})
            embed = nextcord.Embed(
                title="Success!", 
                description=f"You have recieved $10,000 from /daily, see you next day!",
                color=nextcord.Color.green(),
                timestamp=datetime.datetime.utcnow(),
            )
            await interaction.send(embed=embed)

def setup(client):
    client.add_cog(DailyCommand(client))
