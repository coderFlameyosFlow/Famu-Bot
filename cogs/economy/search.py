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

cluster = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://FlameyosFlow:reZPy4ZKz5YqumS@discord.fm5pk.mongodb.net/discord?retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE")
db = cluster.discord
collection = db.bank

class SearchCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(name="search", description="Search for coins all around the world!")
    async def search(
        self,
        interaction: Interaction, *, 
        where: str = nextcord.SlashOption(
            name="area",
            description="Where do you wanna search for money?",
            required=True
        )
    ):
        async with interaction.channel.typing():
            member = interaction.user
            findbank = await collection.find_one({"_id": member.id})
            if not findbank:
                await collection.insert_one({"_id": member.id, "wallet": 0})

            wallet = findbank["wallet"]
            f = random.randint(1, 101)
            earnings = random.randint(1, 1001)
            jackpot = random.randint(21000, 30001)
            jackpot_e = wallet + jackpot
            earnings_e = wallet + earnings

            if where == "park":
                if f > 50:
                    e = nextcord.Embed(
                        title="Hooray!",
                        description="You searched the park and found a wallet with ${:,}!".format(earnings),
                        color=nextcord.Color.random(),
                        timestamp=datetime.datetime.utcnow()
                    )

                    await interaction.response.send_message(embed=e)
                    await collection.update_one({"_id": member.id}, {"$set": {"wallet": earnings_e}})

                elif f == 50:
                    e = nextcord.Embed(
                        title="HOLY-",
                        description="You searched the park and found a wallet with ${:,}!".format(jackpot),
                        color=nextcord.Color.random(),
                        timestamp=datetime.datetime.utcnow()
                    )

                    await interaction.response.send_message(embed=e)
                    await collection.update_one({"_id": member.id}, {"$set": {"wallet": jackpot_e}})

                else:

                    e = nextcord.Embed(
                        title="ooh-",
                        description=f"You searched the park and found nothing.",
                        color=nextcord.Color.random(),
                        timestamp=datetime.datetime.utcnow()
                    )

                await interaction.response.send_message(embed=e)
                return

            elif where == "closet":
                if f > 50:
                    e = nextcord.Embed(
                        title="Hooray!",
                        description="You searched your closet and found ${:,}!".format(earnings),
                        color=nextcord.Color.random(),
                        timestamp=datetime.datetime.utcnow()
                    )

                    await interaction.response.send_message(embed=e)
                    return
                    await collection.update_one({"_id": member.id}, {"$set": {"wallet": earnings_e}})

                elif f == 50:
                    e = nextcord.Embed(
                        title="HOLY-",
                        description="You searched your closet and found ${:,}!".format(jackpot),
                        color=nextcord.Color.random(),
                        timestamp=datetime.datetime.utcnow()
                    )

                    await interaction.response.send_message(embed=e)
                    return
                    await collection.update_one({"_id": member.id}, {"$set": {"wallet": jackpot_e}})

                else:

                    e = nextcord.Embed(
                        title="ooh-",
                        description=f"You searched your closet and found nothing but clothes.",
                        color=nextcord.Color.random(),
                        timestamp=datetime.datetime.utcnow()
                    )

                    await interaction.response.send_message(embed=e)
                    return

            elif where == "bed":
                if f > 50:
                    e = nextcord.Embed(
                        title="Hooray!",
                        description="You searched under your bed and found ${:,}!".format(earnings),
                        color=nextcord.Color.random(),
                        timestamp=datetime.datetime.utcnow()
                    )

                    await interaction.response.send_message(embed=e)
                    return
                    await collection.update_one({"_id": member.id}, {"$set": {"wallet": earnings_e}})

                elif f == 50:
                    e = nextcord.Embed(
                        title="HOLY-",
                        description="You searched under your bed and found ${:,}!".format(jackpot),
                        color=nextcord.Color.random(),
                        timestamp=datetime.datetime.utcnow()
                    )

                    await interaction.response.send_message(embed=e)
                    return
                    await collection.update_one({"_id": member.id}, {"$set": {"wallet": jackpot_e}})

                else:

                    e = nextcord.Embed(
                        title="ooh-",
                        description=f"You searched under your bed and found a monster :joy:, just kidding but you found nothing.",
                        color=nextcord.Color.random(),
                        timestamp=datetime.datetime.utcnow()
                    )

                    await interaction.response.send_message(embed=e)
                    return

            elif where == "company":
                if f > 50:
                    e = nextcord.Embed(
                        title="Hooray!",
                        description="You searched your company and found a wallet with ${:,}!".format(earnings),
                        color=nextcord.Color.random(),
                        timestamp=datetime.datetime.utcnow()
                    )

                    await interaction.response.send_message(embed=e)
                    return
                    await collection.update_one({"_id": member.id}, {"$set": {"wallet": earnings_e}})

                elif f == 50:
                    e = nextcord.Embed(
                        title="HOLY-",
                        description="You searched your company and found a wallet with ${:,}!".format(jackpot),
                        color=nextcord.Color.random(),
                        timestamp=datetime.datetime.utcnow()
                    )

                    await interaction.response.send_message(embed=e)
                    return
                    await collection.update_one({"_id": member.id}, {"$set": {"wallet": jackpot_e}})

                else:
                    e = nextcord.Embed(
                        title="oop-",
                        description=f"You searched your company and found nothing!",
                        color=nextcord.Color.random(),
                        timestamp=datetime.datetime.utcnow()
                    )

                    await interaction.response.send_message(embed=e)
                    return

            elif where == "paypal":
                if f > 50:
                    e = nextcord.Embed(
                        title="Hooray!",
                        description="You searched your paypal and found ${:,}!".format(earnings),
                        color=nextcord.Color.random(),
                        timestamp=datetime.datetime.utcnow()
                    )

                    await interaction.response.send_message(embed=e)
                    return
                    await collection.update_one({"_id": member.id}, {"$set": {"wallet": earnings_e}})

                elif f == 50:
                    e = nextcord.Embed(
                        title="HOLY-",
                        description="You searched your paypal that you literally never even use and found {:,}!".format(jackpot),
                        color=nextcord.Color.random(),
                        timestamp=datetime.datetime.utcnow()
                    )

                    await interaction.response.send_message(embed=e)
                    return
                    await collection.update_one({"_id": member.id}, {"$set": {"wallet": jackpot_e}})

                else:

                    e = nextcord.Embed(
                        title="ooh-",
                        description=f"You searched your paypal that you never use and found nothing.",
                        color=nextcord.Color.random(),
                        timestamp=datetime.datetime.utcnow()
                    )

                    await interaction.response.send_message(embed=e)
                    return

            elif where == "car":
                if f > 50:
                    e = nextcord.Embed(
                        title="Hooray!",
                        description="You searched your car and found a wallet with ${:,}!".format(earnings),
                        color=nextcord.Color.random(),
                        timestamp=datetime.datetime.utcnow()
                    )

                    await interaction.response.send_message(embed=e)
                    return
                    await collection.update_one({"_id": member.id}, {"$set": {"wallet": earnings_e}})

                elif f == 50:
                    e = nextcord.Embed(
                        title="HOLY-",
                        description="You searched your car and found a wallet with ${:,}!".format(jackpot),
                        color=nextcord.Color.random(),
                        timestamp=datetime.datetime.utcnow()
                    )

                    await interaction.response.send_message(embed=e)
                    return
                    await collection.update_one({"_id": member.id}, {"$set": {"wallet": jackpot_e}})

                elif f < 50:

                    e = nextcord.Embed(
                        title="ooh-",
                        description=f"You searched in the middle of the street and found nothing",
                        color=nextcord.Color.random(),
                        timestamp=datetime.datetime.utcnow()
                    )

                    await interaction.response.send_message(embed=e)
                    return

            elif where == "dumpster":
                if f > 50:
                    e = nextcord.Embed(
                        title="Hooray!",
                        description="You searched a dumpster and found a wallet with ${:,}!".format(earnings),
                        color=nextcord.Color.random(),
                        timestamp=datetime.datetime.utcnow()
                    )

                    await interaction.response.send_message(embed=e)
                    return
                    await collection.update_one({"_id": member.id}, {"$set": {"wallet": earnings_e}})

                elif f == 50:
                    e = nextcord.Embed(
                        title="HOLY-",
                        description="You searched a dumpster and found a wallet with ${:,}!".format(jackpot),
                        color=nextcord.Color.random(),
                        timestamp=datetime.datetime.utcnow()
                    )

                    await interaction.response.send_message(embed=e)
                    return
                    await collection.update_one({"_id": member.id}, {"$set": {"wallet": jackpot_e}})

                else:

                    e = nextcord.Embed(
                        title="ooh-",
                        description=f"You searched a dumpster and found nothing, you kinda stink tho, lol.",
                        color=nextcord.Color.random(),
                        timestamp=datetime.datetime.utcnow()
                    )

                    await interaction.response.send_message(embed=e)
                    return

            else:
                await interaction.response.send_message("Try /search `park`, `street`, `car`, `dumpster`, `company`, `paypal`")

def setup(client):
    client.add_cog(SearchCommand(client))
