import nextcord
from nextcord import (
    Interaction,
    slash_command
)
from nextcord.errors import Forbidden
from nextcord.ext import commands
import asyncio

class ClearCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(name="clear", description="Clear messages!")
    async def clear(
        self,
        interaction: Interaction, 
        amount: int = nextcord.SlashOption(
            name="amount",
            description="How many messages do you want to delete?",
            required=True
        ),
    ):
        async with interaction.channel.typing():
            if not (interaction.user.guild_permissions.manage_messages):
                await interaction.response.send_message("You can't use this as you don't have `manage messages` perission.", ephemeral=True)
                return

            else:

                try:
                    amount = amount + 1
                    if amount > 101:
                        await interaction.response.send_message("{} needs to be under 101 at least.".format(amount - 1), ephemeral=True)
                        return

                    if amount <= 0:
                        await interaction.response.send_message("{} needs to be above 0 at least.".format(amount - 1), ephemeral=True)
                        return

                    await interaction.channel.purge(limit=amount)
                    em = nextcord.Embed(
                        title=f"{amount} message(s) has been deleted", 
                        description="Use /clear <amount> to use this command again!", color=nextcord.Color.green()
                    )
                    await interaction.send(embed=em)
                    await asyncio.sleep(5)
                    await (await interaction.original_message()).delete()
                    return

                except Forbidden:
                    embed = nextcord.Embed(
                        title="Error:",
                        description="I didn't have enough permissions, could be because: ``` 1: This was performed in a direct message \n2: I didn't have the permission Manage Members \n3: The user's top role is higher than my top role \n4: An action has been performed on the server owner \n```",
                        color=nextcord.Color.red()
                    )
                    await interaction.send(embed=embed)
                    return

def setup(client):
    client.add_cog(ClearCommand(client))