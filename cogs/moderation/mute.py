import nextcord
from nextcord import (
    Interaction,
    slash_command,
)
from nextcord.ext import commands
from nextcord.errors import Forbidden

import humanfriendly
import datetime

class MuteCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(name="mute", description="Mute someone!")
    async def mute(
        self,
        interaction: Interaction, 
        time = nextcord.SlashOption(
            name="time",
            description="How long do you want them muted?",
            required=True
        ), 

        member: nextcord.Member = nextcord.SlashOption(
            name="member",
            description="Who is the member?",
            required=True
        ), 

        reason: str = nextcord.SlashOption(
            name="reason",
            description="What is the reason?",
            required=False
        )
    ):
        async with interaction.channel.typing():
            if not (interaction.user.guild_permissions.moderate_members):
                await interaction.response.send_message("You can't use this as you don't have `timeout members`.", ephemeral=True)
                pass

            else:
                try:
                    if member == interaction.user:
                        await interaction.send("You can\'t mute yourself!")
                        return
    
                    duration = humanfriendly.parse_timespan(time)
                    await member.timeout(timeout=nextcord.utils.utcnow() + datetime.timedelta(seconds=duration), reason=reason)
                    embed = nextcord.Embed(
                        title=f"Muted {member.name}!",
                        description=f"Information about the muted user. ID: {member.id}",
                        color=0xe40707
                    )
                    embed.add_field(
                        name="**Muted by:**", 
                        value=f"Username: {interaction.user.mention} ID: {interaction.user.id}",inline=False
                    )
                    embed.add_field(
                        name="**Muted from**", 
                        value=f"{interaction.guild}", 
                        inline=False
                    )
                    embed.add_field(
                        name="**Muted for:**", 
                        value=f"{reason}", 
                        inline=False
                    )
                    embed.add_field(
                        name="**Time:**", 
                        value=f"{time}", 
                        inline=False
                    )
    
                    await interaction.send(embed=embed)
                    embed = nextcord.Embed(
                        title=f"You were muted!",
                        description=f"Information about you. ID: {member.id}",
                        color=0xe40707
                    )
                    embed.add_field(
                        name="**Muted by:**", 
                        value=f"Username: {interaction.user.mention} ID: {interaction.user.id}",inline=False
                    )
                    embed.add_field(
                        name="**Muted from**", 
                        value=f"{interaction.guild}", 
                        inline=False
                    )
                    embed.add_field(
                        name="**Muted for:**", 
                        value=f"{reason}", 
                        inline=False
                    )
                    embed.add_field(
                        name="**Time:**", 
                        value=f"{time}", 
                        inline=False
                    )
                    await member.send(embed=embed)

                except Forbidden:
                    embed = nextcord.Embed(
                        title="Error:",
                        description="I didn't have enough permissions, could be because: ``` 1: This was performed in a direct message \n2: I didn't have the permission Moderate Members/Timeout Members \n3: The user's top role is higher than my top role \n4: An action has been performed on the server owner \n```",
                        color=nextcord.Color.red()
                    )
                    await interaction.send(embed=embed)
                    return

    @slash_command(name="unmute", description="Unmute members!")
    async def unmute(
        self,
        interaction: Interaction, 
        member: nextcord.Member = nextcord.SlashOption(
            name="member",
            description="Who do you want to unmute?",
            required=True
        ),

        reason = nextcord.SlashOption(
            name="reason",
            description="What is the reason?",
            required=False
        )
    ):
        async with interaction.channel.typing():
            if not (interaction.user.guild_permissions.moderate_members):
                await interaction.response.send_message("You can't use this as you don't have `timeout members`.", ephemeral=True)
                pass

            else:

                await member.edit(timeout=None, reason=reason)
                embed = nextcord.Embed(
                    title=f"Unmuted {member.name}!", 
                    color=0xe40707
                )
                await interaction.send(embed=embed)
                embed2 = nextcord.Embed(
                    title=f"You were Unmuted!", 
                    color=0xe40707
                )
                await member.send(embed=embed2)

def setup(client):
    client.add_cog(MuteCommand(client))
