import nextcord
from nextcord import (
    Interaction,
    slash_command
)
from nextcord.ext import commands

class NickCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(description="Nickname someone!")
    async def nick(
        self, 
        interaction: Interaction,
        member: nextcord.Member = nextcord.SlashOption(
            description="Who are we nicknaming?",
            required=True,
        ),
        name: str = nextcord.SlashOption(
            description="What is the name? If this is not set then the member's name will reset.",
            required=False,
        ),
    ):
        if not (interaction.user.guild_permissions.manage_nicknames):
            await interaction.send("You don't have the permission `Manage Nicknames`")
            return

        try:
            if name is not None:
                await member.edit(nick=name)
                embed = nextcord.Embed(
                    title="Success:",
                    description=f"{member.mention}'s nickname has been changed to {name}",
                    color=nextcord.Color.green()
                )
                await interaction.send(embed=embed)
                return
                
            else:
                await member.edit(nick=member.name)
                embed = nextcord.Embed(
                    title="Success:",
                    description=f"{member.mention}'s nickname has been changed to their original name",
                    color=nextcord.Color.green()
                )
                await interaction.send(embed=embed)
                return
            
        except nextcord.errors.Forbidden:
            embed = nextcord.Embed(
                title="Error:",
                description="I didn't have enough permissions, could be because: ``` 1: This was performed in a direct message \n2: I didn't have the permission Manage Nicknames \n3: The user's top role is higher than my top role \n4: An action has been performed on the server owner \n```",
                color=nextcord.Color.red()
            )
            await interaction.send(embed=embed)
        return
        
def setup(client):
    client.add_cog(NickCommand(client))