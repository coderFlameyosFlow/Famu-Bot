import nextcord
from nextcord import (
    slash_command,
    Interaction
)
from nextcord.ext import commands

class InfoCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(name="info", description="Info about someone!")
    async def info(
        self,
        interaction: Interaction, 
        member: nextcord.Member = nextcord.SlashOption(
            name="member",
            description="Who do you want to check information on?",
            required=False
        )
    ):
        async with interaction.channel.typing():
            member = member or interaction.user

            roles = [role for role in member.roles]

            isBot = member.bot
            if isBot == True:
                isBot = "BOT"
            else:
                isBot = "Member"

            embed = nextcord.Embed(
                title=f"Information on {member}.", 
                color=member.color,
            )
            embed.set_author(
                name=member.name, 
                icon_url=member.avatar.url
            )
            embed.set_footer(
                text=f"Requested by: {interaction.user}", icon_url=interaction.user.avatar.url
            )
            embed.add_field(
                name="ID:", 
                value=member.id, 
                inline=True
            )
            embed.add_field(
                name="Member Nickname:", 
                value=member.nick, 
                inline=True
            )
            if member.status is nextcord.Status.online:
                status = "Online"

            if member.status is nextcord.Status.dnd or member.status is nextcord.Status.do_not_disturb:
                status = "Do Not Disturb"

            if member.status is nextcord.Status.idle:
                status = "Idle"

            if member.status is nextcord.Status.offline:
                status = "Offline"

            else:
                member.status = f"{str(member.status)}"

            if member.activity is not None:
                activity = f"{str(member.activity.type).title()}: {member.activity.name}"
            else:
                activity = "No Activity Provided"

            embed.add_field(
                name="Current Status:",
                value=status,
                inline=True
            )
            embed.add_field(
                name="Current Activity:",
                value=activity,
                inline=True
            )
            embed.add_field(
                name="Account created at:",
                value=member.created_at.strftime("%A %B %-d, %Y, %-I:%M %p %Z"),
                inline=True
            )
            embed.add_field(
                name="Server joined at:",
                value=member.joined_at.strftime("%A %B %-d, %Y, %-I:%M %p %Z"),
                inline=True
            )
            embed.add_field(
                name=f"Roles [{len(roles)}]", 
                value=" **|** ".join([role.mention for role in roles]),
                inline=True
            )
            embed.add_field(
                name="Major Role:", 
                value=member.top_role, 
                inline=True
            )
            embed.add_field(
                name="Type:", 
                value=isBot, 
                inline=True
            )
            await interaction.response.send_message(embed=embed)
            return

def setup(client):
    client.add_cog(InfoCommand(client))