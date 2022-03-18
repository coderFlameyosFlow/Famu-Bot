import nextcord
from nextcord import (
    Interaction,
    slash_command
)
from nextcord.ext import commands

class GreentextCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(description="Greentext your text!")
    async def greentext(
        self,
        interaction: Interaction,
        text: str = nextcord.SlashOption(
            name="text",
            description="What would you like to greentext?",
            required=True
        )
    ):
        async with interaction.channel.typing():
            await interaction.send(
                f"""
                ```
                {text}
                ```
                """
            )
            return

def setup(client):
    client.add_cog(GreentextCommand(client))