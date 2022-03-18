import nextcord
from nextcord import (
    slash_command,
    Interaction
)
from nextcord.ext import commands

import datetime
import random
import os

import motor
import motor.motor_asyncio

cluster = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("mongodb"))
db = cluster.discord
collection = db.bank

class RobCommand(commands.Cog):
    def __init__(self, client:commands.Bot):
        self.client = client

    @slash_command(
        name="rob", 
        description="Rob some innocent people!"
    )
    async def rob(
        self,
        interaction: Interaction, 
        member: nextcord.Member = nextcord.SlashOption(
            name="member", 
            description="Who is the unlucky person?", 
            required=True)
    ):
        async with interaction.channel.typing():
            fmb = await collection.find_one({"_id": member.id})
            fb = await collection.find_one({"_id": interaction.user.id})
            if not fmb:
                await collection.insert_one({"_id": interaction.user.id, "wallet": 0})

            mwallet = fmb["wallet"]
            wallet = fb["wallet"]

            if member == interaction.user:
                em = nextcord.Embed(
                    title="Error:",
                    description="You can't rob yourself!",
                    color=nextcord.Color.red(),
                    timestamp=datetime.datetime.utcnow() 
                )
                await interaction.send(embed=em)
                pass

            elif int(fmb["wallet"]) < 1500:
                em = nextcord.Embed(
                    title="Error:",
                    description="Not worth the risk man.",
                    color=nextcord.Color.red(),
                    timestamp=datetime.datetime.utcnow()
                )

                await interaction.send(embed=em)
                pass

            elif int(fb["wallet"]) < 1500:
                em = nextcord.Embed(
                    title="Error:",
                    description="You don't have enough money (you need $1,500).",
                    color=nextcord.Color.red(),
                    timestamp=datetime.datetime.utcnow()
                )

                await interaction.send(embed=em)
                pass

            else:
                chance = [False, True, True, False, False, True, False, False, True, False, True, True]

                chances = random.choice(chance)
                earnings = random.randrange(int(0.65*int(mwallet)))
                loss = random.randrange(int(0.35*int(wallet)))

                if chances == True:
                    earningsa = wallet + earnings
                    lossa = mwallet - earnings
                    await collection.update_one({"_id": interaction.user.id}, {"$set": {"wallet": earningsa}})
                    await collection.update_one({"_id": member.id}, {"$set": {"bank": lossa}})
                    em = nextcord.Embed(
                        title="Successful Robbery!",
                        description="You robbed {} and got ${:,}!".format(member.mention, earnings),
                        color = nextcord.Color.green(),
                        timestamp=datetime.datetime.utcnow()
                    )
                    em.set_author(name=interaction.user.display_name, icon_url=interaction.user.avatar.url)
                    em.set_footer(text="He's so unlucky.", icon_url=member.avatar.url)

                    await interaction.send(embed=em)

                    em = nextcord.Embed(
                        title="You got robbed!",
                        description="You got robbed by {} and he got ${:,}!".format(member.mention, earnings),
                        color = nextcord.Color.red(),
                        timestamp=datetime.datetime.utcnow()
                    )

                    em.set_author(name=interaction.user.display_name, icon_url=interaction.user.avatar.url)
                    em.set_footer(text="You're so unlucky.", icon_url=member.avatar.url)

                    await member.send(embed=em)

                else:
                    earningsa = mwallet + loss
                    lossa = wallet - loss
                    await collection.update_one({"_id": interaction.user.id}, {"$set": {"wallet": lossa}})
                    await collection.update_one({"_id": member.id}, {"$set": {"bank": earningsa}})
                    em = nextcord.Embed(
                        title="Unuccessful Robbery!",
                        description="You **tried to** rob {} and lost ${:,}!".format(member.mention, loss),
                        color = nextcord.Color.red(),
                        timestamp=datetime.datetime.utcnow()
                    )
                    em.set_author(name=interaction.user.display_name, icon_url=interaction.user.avatar.url)
                    em.set_footer(text="He's so lucky.", icon_url=member.avatar.url)

                    await interaction.send(embed=em)

                    em = nextcord.Embed(
                        title="You got robbed!",
                        description="You got robbed by {} but thats okay, \nHe failed and he had to pay ${:,} for his consequences!".format(interaction.user.mention, loss),
                        color = nextcord.Color.green(),
                        timestamp=datetime.datetime.utcnow()
                    )

                    em.set_author(name=interaction.user.display_name, icon_url=interaction.user.avatar.url)
                    em.set_footer(text="You're so lucky.", icon_url=member.avatar.url)

                    await member.send(embed=em)

def setup(client):
    client.add_cog(RobCommand(client))