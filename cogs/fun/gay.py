import nextcord
from nextcord import (
    slash_command,
    Interaction
)
from nextcord.ext import commands

import random

class GayCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(name="gay", description="Test people's gayness!")
    async def gay(
        self,
        interaction: Interaction,
        member: nextcord.Member = nextcord.SlashOption(
            name="member",
            description="Who do you want to test gayness on?",
            required=False
        )
    ):
        async with interaction.channel.typing():
            if member == None:
                member = interaction.user
            
            k = random.randint(1, 101)

            if k > 50:
                em = nextcord.Embed(
                    title=f"{member}'s Gay Result", 
                    description=f"{member.mention}'s Gay Result is {k}! \nYou are in 🏳️‍🌈!",
                    color = nextcord.Color.red()
                )
                await interaction.send(embed=em)
            else:
            
                em = nextcord.Embed(
                    title=f"{member}'s Gay Result", 
                    description=f"{member.mention}'s Gay Result is {k}! \nCONGRATULATIONS on not being Gay! :tada:",
                    color=nextcord.Color.green()
                )
                await interaction.send(embed=em)

def setup(client):
    client.add_cog(GayCommand(client))