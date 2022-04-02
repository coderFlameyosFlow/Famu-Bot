import nextcord
from nextcord import (
    Interaction,
    slash_command
)
from nextcord.abc import GuildChannel
from nextcord.errors import Forbidden
from nextcord.ext import (
  commands,
  application_checks,
)

class LockdownCommands(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
       
    @slash_command(description="Lock a server/channel!")
    async def lock(
        self,
        interaction: Interaction,
        setting: str = nextcord.SlashOption(
            description="What is the setting? if you selected --server then option \'channel\' will be useless.",
            choices=[
                "--server",
                "--channel",
            ]
            required=True,
        ),
        channel: GuildChannel = nextcord.SlashOption(
            description="What is the channel? If this is not set then the locked down channel will be this current channel.",
            required=False,
        ),
    ):
        if not (interaction.user.guild_permissions.manage_channels):
            await interaction.send("You don't have permissions \"Manage Channels\".")
            return
        try:
            if setting == "--server":
                for channel in interaction.guild.channels:
                    await channel.set_permissions(interaction.guild.default_role, reason=f"{interaction.user} locked {interaction.guild.name}", send_messages=False)
                    embed = nextcord.Embed(
                    title="Success:",
                    description="Locked down the WHOLE server.",
                    color=nextcord.Color.green()
                )
                await interaction.send(embed=embed)
                return
              
        except Forbidden:
            embed = nextcord.Embed(
                title="Error:",
                description="I didn't have enough permissions, could be because: ``` 1: This was performed in a direct message \n2: I didn't have the permission Manage Nicknames \n```",
                color=nextcord.Color.red()
            )
            await interaction.send(embed=embed)
            return
          
        try:
            if not channel:
                channel = interaction.message.channel
            await channel.set_permissions(interaction.guild.default_role, reason=f"{interaction.user} locked {channel.name}", send_messages=False)
            embed = nextcord.Embed(
                title="Success:",
                description="Locked down the channel",
                color=nextcord.Color.green()
            )
            await interaction.send(embed=embed)
            return
            
        except nextcord.errors.Forbidden:
            embed = nextcord.Embed(
                title="Error:",
                description="I didn't have enough permissions, could be because: ``` 1: This was performed in a direct message \n2: I didn't have the permission Manage Nicknames \n```",
                color=nextcord.Color.red()
            )
            await interaction.send(embed=embed)
            return
        return
      
    @slash_command(description="Unlock a server/channel!")
    async def unlock(
        self,
        interaction: Interaction,
        setting: str = nextcord.SlashOption(
            description="What is the setting? if you selected --server then option \'channel\' will be useless.",
            choices=[
                "--server",
                "--channel",
            ]
            required=True,
        ),
        channel: GuildChannel = nextcord.SlashOption(
            description="What is the channel? If this is not set then the locked down channel will be this current channel.",
            required=False,
        ),
    ):
        if not (interaction.user.guild_permissions.manage_channels):
            await interaction.send("You don't have permissions \"Manage Channels\".")
            return
        try:
            if setting == "--server":
                for channel in interaction.guild.channels:
                    await channel.set_permissions(interaction.guild.default_role, reason=f"{interaction.user} locked {interaction.guild.name}", send_messages=False)
                    embed = nextcord.Embed(
                    title="Success:",
                    description="Locked down the WHOLE server.",
                    color=nextcord.Color.green()
                )
                await interaction.send(embed=embed)
                return
              
        except Forbidden:
            embed = nextcord.Embed(
                title="Error:",
                description="I didn't have enough permissions, could be because: ``` 1: This was performed in a direct message \n2: I didn't have the permission Manage Nicknames \n```",
                color=nextcord.Color.red()
            )
            await interaction.send(embed=embed)
            return
          
        try:
            if not channel:
                channel = interaction.message.channel
            await channel.set_permissions(interaction.guild.default_role, reason=f"{interaction.user} locked {channel.name}", send_messages=False)
            embed = nextcord.Embed(
                title="Success:",
                description="Locked down the channel",
                color=nextcord.Color.green()
            )
            await interaction.send(embed=embed)
            return
            
        except nextcord.errors.Forbidden:
            embed = nextcord.Embed(
                title="Error:",
                description="I didn't have enough permissions, could be because: ``` 1: This was performed in a direct message \n2: I didn't have the permission Manage Nicknames \n```",
                color=nextcord.Color.red()
            )
            await interaction.send(embed=embed)
            return
        return
        
def setup(client):
    client.add_cog(LockdownCommands(client))
