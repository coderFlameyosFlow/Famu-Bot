import nextcord
from nextcord import (
    Interaction,
    slash_command,
)
from nextcord.ext import commands
from nextcord.errors import NotFound, Forbidden

import os

import motor
import motor.motor_asyncio
cluster = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://FlameyosFlow:reZPy4ZKz5YqumS@discord.fm5pk.mongodb.net/discord?retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE")
db = cluster.discord
collection = db.bank

class LeaderboardCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(name="lb", description="Leaderboard of people, ranked by money!")
    async def lb(self, interaction: Interaction):
        x: int = 10
        cursor = collection.find().sort([('_id', 1)])
        docs = await cursor.to_list(length=x)
        leader_board = {}
        total = []
        for entry in docs:
            total_amount = entry["wallet"]
            name = int(entry["_id"])
            leader_board[total_amount] = name
            total.append(total_amount)
            docs = await cursor.to_list(length=x)

        total = sorted(total, reverse=True)

        em = nextcord.Embed(
            title=f"Top {x} Richest People", 
            description="This is decided on the basis of raw money in the wallet.", 
            color=nextcord.Color.blurple()
        )
        index = 1
        for amt in total:
            id_ = leader_board[amt]
            if id_ is not None:
                try:
                    member = await interaction.guild.fetch_member(id_)
                except NotFound:
                    pass
                except Forbidden:
                    pass
                
                em.add_field(name=f"{index}. {name}", value=f"{amt}", inline=False)
                
                if index == x:
                    break
                else:
                    index += 1
                await interaction.send(embed=em)

def setup(client):
    client.add_cog(LeaderboardCommand(client))
