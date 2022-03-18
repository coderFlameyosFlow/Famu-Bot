import nextcord
from nextcord import (
    slash_command,
    Interaction
)
from nextcord.ext import commands

class AvatarCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(description="See someone's avatar!")
    async def avatar(
        self,
        interaction: Interaction,
        member: nextcord.Member = nextcord.SlashOption(
            name="member",
            description="Who are we taking avatar's picture?",
            required=False
        )
    ):
        await interaction.response.defer()
        member = member or interaction.user

        async with interaction.channel.typing():
            await interaction.followup.send(embed=nextcord.Embed(title=f"Here is {member.name}'s avatar!").set_image(url=member.display_avatar.url))
        return

def setup(client):
    client.add_cog(AvatarCommand(client))