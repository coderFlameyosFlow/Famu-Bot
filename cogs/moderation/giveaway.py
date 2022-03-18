import nextcord
from nextcord import (
    Interaction,
    slash_command
)
from nextcord.ext import commands
from nextcord.errors import Forbidden

import random
import asyncio
import datetime
import humanfriendly

class GiveawayCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(description="Create a giveaway with this command!")
    async def gstart(
        self,
        inter: Interaction, 
        duration = nextcord.SlashOption(
            name="time",
            description="How long should it last? ex: 7d or 12h",
            required=True
        ), 
        prize = nextcord.SlashOption(
            name="prize",
            description="What is the prize?",
            required=True
        )
    ):
        if not (inter.user.guild_permissions.manage_guild):
            await inter.send("You need `manage_guild` permissions")
            pass

        else:
            try:
                dur = humanfriendly.parse_timespan(duration)
    
                end = datetime.datetime.utcnow() + datetime.timedelta(seconds=dur)
    
                giveaway = nextcord.Embed(
                    title="Made by {}".format(inter.user),
                    description="Prize: {} \nTime: {}".format(prize, duration),
                    color = nextcord.Color.green(),
                    timestamp=datetime.datetime.utcnow()
                )
                giveaway.set_author(name=inter.user.name, icon_url=inter.user.avatar.url)
                giveaway.set_footer(text=f"Ends in {end} UTC")
                async with inter.channel.typing():
                    await inter.send(embed=giveaway)
    
                await (await inter.original_message()).add_reaction("🎉")
                await asyncio.sleep(dur)
                old_msg = await inter.original_message()
    
                new_msg = await inter.channel.fetch_message(old_msg.id)
                users = await new_msg.reactions[0].users().flatten()
                users.pop(users.index(self.client.user))
    
                winner = random.choice(users) if users is not None else users.append(self.client.user)
                await inter.send(f"Congratulations {winner.mention}, you just won the prize of {prize}")
            except Forbidden:
                embed = nextcord.Embed(
                    title="Error:",
                    description="I didn't have enough permissions, could be because: ``` 1: I didn't have the permission Add Reactions \n2: Some stuff failed (please join the support server) \n```",
                    color=nextcord.Color.red()
                )
                await inter.send(embed=embed)
                return

def setup(client):
    client.add_cog(GiveawayCommand(client))