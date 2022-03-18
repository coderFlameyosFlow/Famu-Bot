import nextcord
from nextcord import (
    Interaction,
    slash_command,
)
from nextcord.ext import commands

class PingCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(name="ping", description="Famurai latency!")
    async def ping(self, interaction: Interaction):
        async with interaction.channel.typing():
            if round(self.client.latency * 1000) <= 50:
                embed = nextcord.Embed(
                    title="PONG!",
                    description=f"The ping is **{round(self.client.latency * 1000)}** milliseconds!",
                    color=nextcord.Color.green()
                )

            elif round(self.client.latency * 1000) <= 100:
                embed = nextcord.Embed(
                    title="PONG!",
                    description=f"The ping is **{round(self.client.latency * 1000)}** milliseconds!",
                    color=nextcord.Color.green()
                )

            elif round(self.client.latency * 1000) <= 200:
                embed = nextcord.Embed(
                    title="PONG!",
                    description=f"The ping is **{round(self.client.latency * 1000)}** milliseconds!",
                    color=nextcord.Color.yellow()
                )

            else:
                embed = nextcord.Embed(
                    title="PONG!",
                    description=f"The ping is **{round(self.client.latency * 1000)}** milliseconds!",
                    color=nextcord.Color.red()
                )

            await interaction.response.send_message(embed=embed)

def setup(client):
    client.add_cog(PingCommand(client))