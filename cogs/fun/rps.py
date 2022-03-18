import nextcord
from nextcord import (
    slash_command,
    Interaction
)
from nextcord.ext import commands

import random

class RockPaperScissorsCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(name="rps", description="Rock Paper Scissors")
    async def rps(
        self,
        interaction: Interaction, 
        mode = nextcord.SlashOption(
            description="What mode? rock, paper, scissors?", 
            required=True
        )
    ):
        s = ["scissors","Scissors"]
        p = ["paper","Paper"]
        r = ["rock","Rock"]

        z = ["scissors","Scissors","paper","Paper","rock","Rock"]

        b = ["scissors","paper","rock"]
        b2 = random.choice(b)

        if mode not in z:
            await interaction.send("You can only do *scissors*, *paper* or *rock*!")
            return

        if b2 == "scissors":
            if mode in s:
                await interaction.send(f"My choice was scissors aswell, So It was a tie!")
            if mode in p:
                await interaction.send(f"My choice was scissors, so you lost! :rofl:")
            if mode in r:
                await interaction.send(f"My choice was scissors, so you won! :sob:")

        if b2 == "paper":
            if mode in s:
                await interaction.send(f"My choice was paper, so you won! :sob:")
            if mode in p:
                await interaction.send(f"My choice was paper aswell, So It was a tie!")
            if mode in r:
                await interaction.send(f"My choice was paper, so you lost! :rofl:")

        if b2 == "rock":
            if mode in s:
                await interaction.send(f"My choice was rock, so you lost! :rofl:")
            if mode in p:
                await interaction.send(f"My choice was rock! You won! :sob:")
            if mode in r:
                await interaction.send(f"My choice was rock aswell, So It was a tie!")

def setup(client):
    client.add_cog(RockPaperScissorsCommand(client))