import nextcord
from nextcord import (
    slash_command,
    Interaction
)
from nextcord.errors import Forbidden
from nextcord.ext import commands

import datetime

class AFKCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(
        name="afk", 
        description="Make everyone know your away from keyboard!"
    )
    async def afk(
        self,
        interaction: Interaction, 
        reason = nextcord.SlashOption(
            name="reason",
            description="What is the reason?",
            required=False
        )
    ):
        async with interaction.channel.typing():
            try:
                await interaction.user.edit(nick=f"[AFK] {interaction.user.name}", reason=reason)
            except Forbidden:
                await interaction.send("I didn't have permissions to nick you, tell the server owner to give me more permissions!")
                return

            em = nextcord.Embed(
                title=f"{interaction.user} has went AFK!", 
                description="Just type anything or /unafk", 
                timestamp=datetime.datetime.utcnow(), 
                color=nextcord.Color.random()
            )
            em.add_field(name="Reason:", value=f"{reason}")
            await interaction.response.send_message(embed=em)

            def check(m):
                return m.author == interaction.user

            raw_msg = await self.client.wait_for("message", check=check, timeout=None)
            msg = raw_msg.content

            if msg:
                em1 = nextcord.Embed(
                    title=f"{interaction.user.name}#{interaction.user.discriminator} has UNAFKED!", 
                    description=f"Welcome back {interaction.user.mention}", timestamp=datetime.datetime.utcnow(), 
                    color=nextcord.Color.random()
                )
                await interaction.send(embed=em1)

        @slash_command(
            name="unafk", 
            description="Make everyone know your not away from keyboard anymore!"
        )
        async def unafk(interaction: Interaction):
            async with interaction.channel.typing():
                try:
                    if "[AFK]" in interaction.user.display_name:
                        await interaction.user.edit(nick=interaction.user.name)
                    else:
                        await interaction.send("You're not even afk.")
                        return

                except Forbidden:
                    await interaction.send("I don't have permissions to nickname you.")
                return

                em = nextcord.Embed(
                    title=f"{interaction.user} has UNAFKED!", 
                    description=f"Welcome back {interaction.user.mention}", timestamp=datetime.datetime.utcnow(), 
                    color=nextcord.Color.random()
                )
                await interaction.send(embed=em)

def setup(client):
    client.add_cog(AFKCommand(client))