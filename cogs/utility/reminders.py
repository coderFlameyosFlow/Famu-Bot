import nextcord
from nextcord import (
    slash_command,
    Interaction
)
from nextcord.ext import commands
import asyncio
import humanfriendly

class ReminderCommands(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(description="Set a reminder!")
    async def remindme(
        self,
        interaction: Interaction, 
        time = nextcord.SlashOption(
            name="time",
            description="How long is the timer? ex: 6h or 7d",
            required=True
        ), 

        message = nextcord.SlashOption(
            name="message",
            description="What is your reminder message?",
            required=True
        ),
        dms = nextcord.SlashOption(
            name="dms",
            description="Do you want this to go in your DMS?",
            required=True
        ),
    ):
            duration = humanfriendly.parse_timespan(time)
            await interaction.send(
                f"Set reminder for {interaction.user.mention} \n{message} \n||Set for {time}||"
            )

            await asyncio.sleep(duration)

            if not dms == True:
                await interaction.channel.send(
                    f"Reminder for {interaction.user.mention} \n{message}"
                )
            else:
                await interaction.user.send(
                    f"Reminder for {interaction.user.mention} \n{message}"
                )
def setup(client):
    client.add_cog(ReminderCommands(client))