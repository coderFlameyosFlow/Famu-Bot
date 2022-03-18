import nextcord
from nextcord import (
    Interaction,
    slash_command,
)
from nextcord.ext import commands
from nextcord.errors import Forbidden

class KickCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(name="kick", description="Kick someone!")
    async def kick(
        self,
        interaction: Interaction, 
        member: nextcord.Member = nextcord.SlashOption(
            name="member",
            description="Who do you want to kick?",
            required=True
        ),

        reason = nextcord.SlashOption(
            name="reason",
            description="What is the reason of kicking this member?",
            required=False
        ),
    ):
        async with interaction.channel.typing():
            if not (interaction.user.guild_permissions.kick_members):
                await interaction.response.send_message("You can't use this.", ephemeral=True)
                pass
                
            else:
                try:
                    if member == interaction.user:
    
                        await interaction.send("You can't kick yourself!")
                        return
                    else:
                        await member.kick(reason=reason)
                        embed2 = nextcord.Embed(
                            title=f"Kicked {member.name}!", 
                            description="Information about the kicked user.", 
                            color=nextcord. Color.red()
                        )
                        embed2.add_field(
                            name="**Kicked by:**", 
                            value=f"{interaction.user.mention}", 
                            inline=False
                        )
                        embed2.add_field(
                            name="**Kicked from**", 
                            value=f"{interaction.guild}", 
                            inline=False
                        )
                        embed2.add_field(
                            name="**Kicked for:**", 
                            value=f"{reason}", 
                            inline=False
                        )
                        await interaction.send(embed=embed2)
                        em = nextcord.Embed(
                            title="You were kicked!", 
                            description="Information about you.", 
                            color=nextcord.Color.red()
                        )
                        em.add_field(
                            name="**Kicked by:**", 
                            value=f"{interaction.user.mention}", 
                            inline=False
                        )
                        em.add_field(
                            name="**Kicked from:**", 
                            value=f"{interaction.guild}", 
                            inline=False
                        )
                        em.add_field(
                            name="**Kicked for:**", 
                            value=f"{reason}", 
                            inline=False    
                        )
                        await member.send(embed=em)

                except Forbidden:
                    embed = nextcord.Embed(
                        title="Error:",
                        description="I didn't have enough permissions, could be because: ``` 1: This was performed in a direct message \n2: I didn't have the permission Kick Members \n3: The user's top role is higher than my top role \n4: An action has been performed on the server owner \n```",
                        color=nextcord.Color.red()
                    )
                    await interaction.send(embed=embed)
                    return

def setup(client):
    client.add_cog(KickCommand(client))