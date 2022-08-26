import nextcord
from nextcord import (
    Interaction,
    slash_command,
    ChannelType,
)
from nextcord.abc import GuildChannel
from nextcord.ext import (
  commands,
  application_checks,
)

class LockdownCommands(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
       
    @slash_command(description="Lock a server/channel!")
    @application_checks.has_guild_permissions(manage_channels=True)
    @application_checks.bot_has_guild_permissions(manage_channels=True)
    @application_checks.guild_only()
    async def lock(
        self,
        interaction: Interaction,
        setting: str = nextcord.SlashOption(
            description="What is the setting? if you selected --server then option \'channel\' will be useless.",
            choices=[
                "--server",
                "--channel",
            ],
            required=True,
        ),
        channel: GuildChannel = nextcord.SlashOption(
            description="What is the channel? If this is not set then the locked down channel will be this current channel.",
            channel_types=[ChannelType.text, ChannelType.public_thread, ChannelType.private_thread],
            required=False,
        ),
    ):
        if setting == "--server":
            embed = nextcord.Embed(
                title="Success:",
                description="Locked down the WHOLE server.",
                color=nextcord.Color.green()
            )
            await interaction.send(embed=embed)
            for channel in interaction.guild.channels:
                await channel.set_permissions(interaction.guild.default_role, reason=f"{interaction.user} locked {interaction.guild.name}", send_messages=False)
            return

        elif setting == "--channel":
            if not channel:
                channel = interaction.message.channel
            embed = nextcord.Embed(
                title="Success:",
                description="Locked down the channel",
                color=nextcord.Color.green()
            )
            await interaction.send(embed=embed)
            await channel.set_permissions(interaction.guild.default_role, reason=f"{interaction.user} locked {channel.name}", send_messages=False)
            return
      
    @slash_command(description="Unlock a server/channel!")
    @application_checks.has_guild_permissions(manage_channels=True)
    @application_checks.bot_has_guild_permissions(manage_channels=True)
    @application_checks.guild_only()
    async def unlock(
        self,
        interaction: Interaction,
        setting: str = nextcord.SlashOption(
            description="What is the setting? if you selected --server then option \'channel\' will be useless.",
            choices=[
                "--server",
                "--channel",
            ],
            required=True,
        ),
        channel: GuildChannel = nextcord.SlashOption(
            description="What is the channel? If this is not set then the locked down channel will be this current channel.",
            required=False,
        ),
    ):
        if setting == "--server":
            for channel in interaction.guild.channels:
                await channel.set_permissions(interaction.guild.default_role, reason=f"{interaction.user} locked {interaction.guild.name}", send_messages=True)
                embed = nextcord.Embed(
                title="Success:",
                description="Unlocked the WHOLE server.",
                color=nextcord.Color.green()
            )
            await interaction.send(embed=embed)
            return
          
        elif setting == "--channel":
            if not channel:
                channel = interaction.message.channel
            await channel.set_permissions(interaction.guild.default_role, reason=f"{interaction.user} locked {channel.name}", send_messages=True)
            embed = nextcord.Embed(
                title="Success:",
                description="Unlocked the channel",
                color=nextcord.Color.green()
            )
            await interaction.send(embed=embed)
            return
        return
    
    @lock.error
    async def lock_error(interaction: Interaction, error):
        if isinstance(error, application_checks.MissingGuildPermissions):
            await interaction.send("You don't have enough permissions to manage channels.")
        if isinstance(error, application_checks.BotMissingGuildPermissions):
            await interaction.send("I don't have enough permissions to manage channels, please contact the owner of the server if this is a mistake.")
            
    @unlock.error
    async def unlock_error(interaction: Interaction, error):
        if isinstance(error, application_checks.MissingGuildPermissions):
            await interaction.send("You don't have enough permissions to manage channels.")
        if isinstance(error, application_checks.BotMissingGuildPermissions):
            await interaction.send("I don't have enough permissions to manage channels, please contact the owner of the server if this is a mistake.")
        
def setup(client):
    client.add_cog(LockdownCommands(client))
