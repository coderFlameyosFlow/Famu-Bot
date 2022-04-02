import nextcord
from nextcord import (
    Interaction,
    slash_command,
    ChannelType,
)
from nextcord.abc import GuildChannel
from nextcord.ext import commands
from nextcord.errors import Forbidden

import datetime
import humanfriendly

class SlowdownCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(description="Slowdown a channel with this command!")
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
            channel_types=[ChannelType.text, ChannelType.public_thread, ChannelType.private_thread]
            required=False
        ), 
    ):
        if not (interaction.user.guild_permissions.manage_channels):
            await inter.send("You need `Manage Channels` permissions")
            return

          try:
              time = humanfriendly.parse_timespan(duration)
              if not channel:
                  channel = interaction.channel

              if time > 21600:
                  await interaction.send("You can't exceed 21600 seconds/6 hours of slowmode. \n(maximum the discord API could handle)")
                  return

              await channel.edit(slowmode_delay=time, reason=f"{interaction.user} used slowmode on {channel.name}")
               await interaction.send(f"You slowmoded ({channel.name}) successfully!")

          except Forbidden:
              embed = nextcord.Embed(
                  title="Error:",
                  description="I didn't have enough permissions, could be because: ``` 1: I didn't have the permission Manage Channels or Manage Messages \n2: Some stuff failed (please join the support server) \n```",
                  color=nextcord.Color.red()
              )
              await interaction.send(embed=embed)
              return

def setup(client):
    client.add_cog(SlowdownCommand(client))
