import nextcord
from nextcord import (
    slash_command,
    Interaction
)
from nextcord.ext import commands

import datetime

class ServerInfoCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(description="Information about your server!")
    async def serverinfo(
        self,
        interaction: Interaction, 
    ):
        async with interaction.channel.typing():
            roles = [role for role in interaction.guild.roles]
            bots = [m for m in interaction.guild.bots]
            embed = nextcord.Embed(
                title=f"Info about {interaction.guild.name}", 
                description=f"These are information about your server!",
                color=nextcord.Color.random(),
                timestamp=datetime.datetime.utcnow()
            )
            embed.add_field(
                name="Server Name:",
                value="```\n" + interaction.guild.name + "#" + interaction.guild.owner.discriminator +  "\n```",
                inline=False
            )
            embed.add_field(
                name="Owner:",
                value="```\n" + interaction.guild.owner.name + "#" + interaction.guild.owner.discriminator +  "\n```",
                inline=False
            )
            embed.add_field(
                name="ID:",
                value="```\n" + str(interaction.guild.id) + "\n```",
                inline=False
            )
            embed.add_field(
                name="Members:",
                value="```\n" + str(interaction.guild.member_count) + "\n```",
                inline=False
            )
            embed.add_field(
                name="Bots:",
                value="```\n" + str(len(bots)) + "\n```",
                inline=False
            )
            embed.add_field(
                name="Region:",
                value="```\n" + str(interaction.guild.region) + "\n```",
                inline=False
            )
            embed.add_field(
                name="Created On:",
                value="```\n" + str(interaction.guild.created_at.strftime("%A %B %-d, %Y, %-I:%M %p %Z")) + "\n```",
                inline=False
            )
            embed.add_field(
                name="Text Channels:",
                value="```\n" + str(len(interaction.guild.text_channels)) + "\n```",
                inline=False
            )
            embed.add_field(
                name="Voice Channels:",
                value="```\n" + str(len(interaction.guild.voice_channels)) + "\n```",
                inline=False
            )
            embed.add_field(
                name="Total Channels:",
                value="```\n" + str(len(interaction.guild.voice_channels) + len(interaction.guild.text_channels)) + "\n```",
                inline=False
            )
            embed.add_field(
                name=f"Roles: [{len(roles)}]",
                value="```\n" +  " \n ".join([role.name for role in roles]) + "\n```",
                inline=False
            )
            await interaction.send(embed=embed, ephemeral=True)

def setup(client):
    client.add_cog(ServerInfoCommand(client))