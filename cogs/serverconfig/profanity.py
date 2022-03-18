import nextcord
from nextcord import (
    Interaction, 
    slash_command,
)
from nextcord.ext import commands

import os

import motor
import motor.motor_asyncio

cluster = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://FlameyosFlow:reZPy4ZKz5YqumS@discord.fm5pk.mongodb.net/discord?retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE")
db = cluster.discord
collection = db.swears

class AutoProfanityCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(description="Add disabled swears to your guild!")
    async def addswears(
        self,
        interaction: Interaction, 
        swears: str = nextcord.SlashOption(
            description="What swears do you wanna add? To add multiple add ; like frick;freak",
            required=True
        ),
    ):
        swears = swears.split(" ")
        print(swears)
        findswears = await collection.find_one({"_id": interaction.guild.id})
        if not findswears:
            await collection.insert_one({"_id": interaction.guild.id, "swears": swears})
            await interaction.send(f"Your swears are now set! If you want to update this then you could issue this command again.")
        else:
            
            await collection.update_one(
                {"_id": interaction.guild.id}, 
                {"$set": {"swears": swears}}
            )

            await interaction.send(f"Your swears are now set! If you want to update this then you could issue this command again.")

    @slash_command(description="Remove disabled swears from your guild!")
    async def removeswears(
        self,
        interaction: Interaction, 
        swears: str = nextcord.SlashOption(
            description="What swears do you wanna remove? You can remove multiple!",
            required=True
        ),
    ):
        findswears = await collection.find_one({"_id": interaction.guild.id})
        if not findswears:
            await interaction.send("You don't have an anti-profanity setup set, do so by issuing /addswears")

    @slash_command(description="Current disabled swears on this guild!")
    async def swears(self, interaction: Interaction):
        pass
        
def setup(client):
    client.add_cog(AutoProfanityCommand(client))
