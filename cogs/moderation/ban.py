import nextcord
from nextcord import (
    Interaction,
    slash_command,
)
from nextcord.errors import Forbidden
from nextcord.ext import commands

class BanCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(name="ban", description="Ban someone!")
    async def ban(
        self,
        interaction: Interaction, 
        member: nextcord.Member = nextcord.SlashOption(
            description="Who is the person?"
        ),
        reason = nextcord.SlashOption(
            description="What is the person?"
            )
    ):
        async with interaction.channel.typing():
            if not (interaction.user.guild_permissions.ban_members):
                await interaction.response.send_message("You can't use this.", ephemeral=True)
                pass

            else:

                if member == interaction.user:

                    await interaction.send("You can't ban yourself!")
                    return
                else:
                    try:
                        await member.ban(reason=reason)
                        embed2 = nextcord.Embed(
                            title=f"Banned {member.name}!", 
                            description="Information about the banned user.", color=nextcord.Color.red()
                        )
                        embed2.add_field(
                            name="**Banned by:**", 
                            value=f"{interaction.user.mention}", 
                            inline=False
                        )
                        embed2.add_field(
                            name="**Banned from**", 
                            value=f"{interaction.guild}", 
                            inline=False
                        )
                        embed2.add_field(
                            name="**Banned for:**", 
                            value=f"{reason}", 
                            inline=False
                        )
                        await interaction.send(embed=embed2)
                        em = nextcord.Embed(
                            title="You were Banned!", 
                            description="Information about you.", 
                            color=nextcord.Color.red()
                        )
                        em.add_field(
                            name="**Banned by:**", 
                            value=f"{interaction.user.mention}", 
                            inline=False
                        )
                        em.add_field(
                            name="**Banned from:**", 
                            value=f"{interaction.guild}", 
                            inline=False
                        )
                        em.add_field(
                            name="**Banned for:**", 
                            value=f"{reason}", 
                            inline=False
                        )
                        await member.send(embed=em)
                    except Forbidden:
                        embed = nextcord.Embed(
                            title="Error:",
                            description="I didn't have enough permissions, could be because: ``` 1: This was performed in a direct message \n2: I didn't have the permission Ban Members \n3: The user's top role is higher than my top role \n4: An action has been performed on the server owner \n```",
                            color=nextcord.Color.red()
                        )
                        await interaction.send(embed=embed)
                        return

def setup(client):
    client.add_cog(BanCommand(client))