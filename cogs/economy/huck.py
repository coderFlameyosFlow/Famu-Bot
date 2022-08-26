import nextcord
from nextcord import (
    slash_command,
    Interaction
)
from nextcord.ext import commands

import os
import random

import motor
import motor.motor_asyncio
cluster = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://FlameyosFlow:reZPy4ZKz5YqumS@discord.fm5pk.mongodb.net/discord?retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE")
db = cluster.discord
collection = db.bank
company = db.company

class HackCompanyCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(name="hack", description="hi")
    @cooldowns.cooldown(1, 350, bucket=cooldowns.SlashBucket.author)
    async def huck(self, interaction: Interaction):
        pass

    @huck.subcommand(name="company", description="Hack someone's company!")
    @cooldowns.cooldown(1, 350, bucket=cooldowns.SlashBucket.author)
    async def coompany(
        self, 
        interaction: Interaction,
        member: nextcord.Member = nextcord.SlashOption(
            description="Who's company are we hacking?"
        )
    ):
        user = interaction.user
        findbank = await collection.find_one({"_id": user.id})
        if not findbank:
            await collection.insert_one({"_id": user.id, "wallet": 0})
            await interaction.send(f"You don't have enough money ($1,500+ required)")
            
        findmembercompany = await collection.find_one({"_id": member.id})
        if not findmembercompany:
            await interaction.send(f"{member.mention} doesn't have a company...")
        else:
            wallet = findbank["wallet"]
            worth = findmembercompany["worth"]
            if wallet < 1500:
                await interaction.send(f"You don't have enough money ($1,500+ required)")
    
            if worth < 1500:
                await interaction.send(f"Not worth it. (company needs $1,500+ required)")
            else:
                pass
                
def setup(client):
    client.add_cog(HackCompanyCommand(client))
