import nextcord
from nextcord import (
    Interaction,
    slash_command
)
from nextcord.ext import commands
from nextcord.errors import Forbidden

class CreateStuffCommands(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(name="cc", description="Create a category!")
    async def cc(
        self,
        interaction: Interaction, 
        name = nextcord.SlashOption(
            description="What is the name?"
        )
    ):
        if not (interaction.user.guild_permissions.manage_channels):
            await interaction.response.send_message("You can't use this.", ephemeral=True)
            pass

        else:
            async with interaction.channel.typing():
                try:
                    await interaction.guild.create_category(name)
                    await interaction.send(f"created category {name}")
                except Forbidden:
                        embed = nextcord.Embed(
                            title="Error:",
                            description="I didn't have enough permissions, could be because: ``` 1: This was performed in a direct message \n2: I didn't have the permission Manage Channels \n```",
                            color=nextcord.Color.red()
                        )
                        await interaction.send(embed=embed)
                        return

    @slash_command(name="ctc", description="Create a text channel!")
    async def ctc(
        self,
        interaction: Interaction, 
        name = nextcord.SlashOption(
            description="What is the name?"
        )
    ):
        if not (interaction.user.guild_permissions.manage_channels):
            await interaction.response.send_message("You can't use this.", ephemeral=True)
            pass

        else:
            async with interaction.channel.typing():
                try:
                    await interaction.guild.create_text_channel(name)
                    await interaction.send(f"created text channel {name}")
                except Forbidden:
                    embed = nextcord.Embed(
                        title="Error:",
                        description="I didn't have enough permissions, could be because: ``` 1: This was performed in a direct message \n2: I didn't have the permission Manage Channels \n```",
                        color=nextcord.Color.red()
                    )
                    await interaction.send(embed=embed)
                    return

    @slash_command(name="cvc", description="Create a voice channel!")
    async def cvc(
        self,
        interaction: Interaction, 
        name = nextcord.SlashOption(
            description="What is the name?"
        )
    ):
        if not (interaction.user.guild_permissions.manage_channels):
            await interaction.response.send_message("You can't use this.", ephemeral=True)
            pass

        else:
            async with interaction.channel.typing():
                try:
                    await interaction.guild.create_voice_channel(name)
                    await interaction.send(f"created voice channel {name}")
                except Forbidden:
                        embed = nextcord.Embed(
                            title="Error:",
                            description="I didn't have enough permissions, could be because: ``` 1: This was performed in a direct message \n2: I didn't have the permission Manage Channels \n```",
                            color=nextcord.Color.red()
                        )
                        await interaction.send(embed=embed)
                        return

    @slash_command(name="ar", description="Add a role to Someone!")
    async def ar(
        self,
        interaction: Interaction, 
        user: nextcord.Member = nextcord.SlashOption(
            description="Who is the person?"
        ), 
        role: nextcord.Role = nextcord.SlashOption(
            description="What is the role?"
        )
    ):
        if not (interaction.user.guild_permissions.manage_roles):
            await interaction.response.send_message("You can't use this.", ephemeral=True)
            pass

        else:
            async with interaction.channel.typing():
                try:
                    if role in user.roles:
                        await interaction.send(f"{user} already has this role called {role}.")
                        return
                    else:
                        await user.add_role(role)
                        await interaction.send(f"Added {role} to {user.mention}.")
                except Forbidden:
                    embed = nextcord.Embed(
                        title="Error:",
                        description="I didn't have enough permissions, could be because: ``` 1: This was performed in a direct message \n2: I didn't have the permission Manage Roles \n```",
                        color=nextcord.Color.red()
                    )
                    await interaction.send(embed=embed)
                    return

    @slash_command(name="rr", description="Remove a role from Someone!")
    async def rr(
        self,
        interaction: Interaction, 
        user: nextcord.Member = nextcord.SlashOption(
            description="Who is the person?"
        ), 
        role: nextcord.Role = nextcord.SlashOption(
            description="What is the role?"
        )
    ):
        if not (interaction.user.guild_permissions.manage_roles):
            await interaction.response.send_message("You can't use this.", ephemeral=True)
            pass

        else:
            async with interaction.channel.typing():
                try:
                    if role not in user.roles:
                        await interaction.send(f"{user} already doesn't have this role called {role}.")
                        return
                    else:
                        await user.remove_role(role)
                        await interaction.send(f"Removed {role} to {user.mention}.")
                except Forbidden:
                    embed = nextcord.Embed(
                        title="Error:",
                        description="I didn't have enough permissions, could be because: ``` 1: This was performed in a direct message \n2: I didn't have the permission Manage Roles\n```",
                        color=nextcord.Color.red()
                    )
                    await interaction.send(embed=embed)
                    return

def setup(client):
    client.add_cog(CreateStuffCommands(client))