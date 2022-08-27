import nextcord
from nextcord import (
    slash_command,
    Interaction,
)
from nextcord.ext import commands

import os

import motor
import motor.motor_asyncio

cluster = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://FlameyosFlow:reZPy4ZKz5YqumS@discord.fm5pk.mongodb.net/discord?retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE")
db = cluster.discord
collection = db.bank

class BalanceCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(name="bal", description="Check your balance!")
    async def balance(
        self,
        interaction: Interaction,
        member: nextcord.Member = nextcord.SlashOption(
            name="member",
            description="Who's balance are we checking?",
            required=False
        )
    ):
        await interaction.response.defer()
        member = member or interaction.user

        findbank = await collection.find_one({"_id": member.id})
        if not findbank:
            await collection.insert_one({"_id": member.id, "wallet": 0})

        wallet = findbank["wallet"]

        em = nextcord.Embed(
            description="__**Wallet Balance**__: \n{:,}".format(wallet),
            color=member.color
        ).set_author(
            name=str(member.name + "#" + member.discriminator), 
            icon_url=member.avatar.url
        )
        await interaction.followup.send(embed=em)

def setup(client):
    client.add_cog(BalanceCommand(client))
