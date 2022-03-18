import nextcord
from nextcord import (
    Interaction,
    slash_command,
)
from nextcord.ext import commands

class WarnCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(name="warn", description="Warn someone!")
    async def warn(
        self,
        interaction: Interaction, 
        member: nextcord.Member = nextcord.SlashOption(
            description="Who is the person?"
        ), 
        reason = nextcord.SlashOption(
            description="What is the reason?"
        )
    ):
        async with interaction.channel.typing():
            if not (interaction.user.guild_permissions.moderate_members):
                await interaction.send("You don't have permissions for `timeout members`")
                pass

            else:
                embed2 = nextcord.Embed(
                    title=f"Warned {member.name}",
                    description="Information about the Warned user.",
                    color=0xe40707
                )
                embed2.add_field(
                    name="**Warned by:**",
                    value=f"{interaction.user.mention}",
                    inline=False
                )
                embed2.add_field(
                    name="**Warned from**",
                    value=f"{interaction.guild}",
                    inline=False
                )

                embed2.add_field(
                    name="**Warned for:**",
                    value=f"{reason}",
                    inline=False
                )
                await interaction.send(embed=embed2)

                embed3 = nextcord.Embed(
                    title=f"Warned {member.name}!",       
                    color=0xe40707
                )
                embed3.add_field(
                    name="**Warned by:**",
                    value=f"{interaction.user.mention}",
                    inline=False
                )
                embed3.add_field(
                    name="**Warned from**",
                    value=f"{interaction.guild}",
                    inline=False
                )
                embed3.add_field(
                    name="**Warned for:**",
                    value=f"{reason}",
                    inline=False
                )
                await member.send(embed=embed3)

def setup(client):
    client.add_cog(WarnCommand(client))