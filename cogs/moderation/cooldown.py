import nextcord
from nextcord import (
    Interaction,
    slash_command,
    ChannelType,
)
from nextcord.abc import GuildChannel
from nextcord.ext import commands
from nextcord.errors import Forbidden
from nextcord.ext import application_checks

import datetime
import humanfriendly

class SlowdownCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(description="Slowdown a channel with this command!")
    @application_checks.has_permissions(manage_channels=True)
    @application_checks.bot_has_permissions(manage_channels=True)
    async def slowmode(
        self,
        interaction: Interaction, 
        duration = nextcord.SlashOption(
            name="time",
            description="How long should the slowdown be? e.g: 1m or seconds! if not set, it resets this channel's slowmode.",
            required=False
        ), 
        channel: GuildChannel = nextcord.SlashOption(
            description="Where should the slowdown be? if not set, the slowmode will be in this channel.",
            channel_types=[ChannelType.text, ChannelType.public_thread, ChannelType.private_thread],
            required=False
        ), 
    ):
      time = humanfriendly.parse_timespan(duration)
      if not channel:
          channel = interaction.channel

      if time >= 21600:
          await interaction.send("You can't exceed 21600 seconds/6 hours of slowmode - Discord")
          return

      await channel.edit(slowmode_delay=time, reason=f"{interaction.user} used slowmode on {channel.name}")
       await interaction.send(f"You slowmoded ({channel.name}) successfully!")
    
    @slowmode.error
    async def slowmode_error(interaction: Interaction, error):
        if isinstance(error, application_checks.MissingPermissions):
            await interaction.send("You're missing manage channels permissions!")
            
        if isinstance(error, application_checks.BotMissingPermissions):
            await interaction.send("I'm missing manage channels permissions, please contact the owner of the server about this if this is a mistake!")

def setup(client):
    client.add_cog(SlowdownCommand(client))
