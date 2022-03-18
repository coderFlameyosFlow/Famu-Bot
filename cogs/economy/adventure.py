import nextcord
from nextcord import (
    Interaction, 
    slash_command
)
from nextcord.ext import commands

import random
import datetime
import os

import motor
import motor.motor_asyncio

cluster = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("mongodb"))
db = cluster.discord
crates = db.crates

class AdventureCrateCommands(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(name="adventure", description="Stop it, Go Travel.")
    async def adventure(
        self,
        interaction: Interaction, 
        direction = nextcord.SlashOption(
            name="direction",
            choices={"Left", "Right", "Middle"},
            description="Which direction do you wanna go?",
        )
    ):
        async with interaction.channel.typing():
            member = interaction.user
            f = random.randint(1, 101)
            findcrates = await crates.find_one({"_id": member.id})
            if not findcrates:
                await crates.insert_one({"_id": member.id, "crates": 0})

            num_crates = findcrates["crates"]

            user = interaction.user

            if direction == "Left":
                if f >= 78:
                    e = nextcord.Embed(
                        title=f"you went {direction}",
                        description=f"you got 3 crates :eyes:",
                        color=nextcord.Color.green(),
                        timestamp=datetime.datetime.utcnow()
                    )
                    e.set_footer(text="why is that not me nerd")
                    e.set_author(name=user.name, icon_url=user.avatar.url)
                    await interaction.response.send_message(embed=e)
                    crates_updated = num_crates + 3
                    await crates.update_one({"_id": user.id}, {"$set": {"crates": crates_updated}})

                elif f >= 60:
                    e = nextcord.Embed(
                        title=f"you went {direction}",
                        description=f"you got 2 crates :eyes:",
                        color=nextcord.Color.green(),
                        timestamp=datetime.datetime.utcnow()
                    )
                    e.set_footer(text="why is that not me nerd")
                    e.set_author(name=user.name, icon_url=user.avatar.url)
                    await interaction.response.send_message(embed=e)
                    crates_updated = num_crates + 2
                    await crates.update_one({"_id": user.id}, {"$set": {"crates": crates_updated}})

                elif f >= 50:
                    e = nextcord.Embed(
                        title=f"you went {direction}",
                        description=f"you got 1 crate :eyes:",
                        color=nextcord.Color.green(),
                        timestamp=datetime.datetime.utcnow()
                    )
                    e.set_footer(text="why is that not me nerd")
                    e.set_author(name=user.name, icon_url=user.avatar.url)
                    await interaction.response.send_message(embed=e)
                    crates_updated = num_crates + 1
                    await crates.update_one({"_id": user.id}, {"$set": {"crates": crates_updated}})

                else:
                    e = nextcord.Embed(
                        title=f"you went {direction}",
                        description=f"you got no crates :eyes:",
                        color=nextcord.Color.green(),
                        timestamp=datetime.datetime.utcnow()
                    )
                    e.set_footer(text="good thing I'm not you ;)")
                    e.set_author(name=user.name, icon_url=user.avatar.url)
                    await interaction.response.send_message(embed=e)
                    return

            elif direction == "Right":
                if f >= 78:
                    e = nextcord.Embed(
                        title=f"you went {direction}",
                        description=f"you got 3 crates :eyes:",
                        color=nextcord.Color.green(),
                        timestamp=datetime.datetime.utcnow()
                    )
                    e.set_footer(text="why is that not me nerd")
                    e.set_author(name=user.name, icon_url=user.avatar.url)
                    await interaction.response.send_message(embed=e)
                    crates_updated = num_crates + 3
                    await crates.update_one({"_id": user.id}, {"$set": {"crates": crates_updated}})

                elif f >= 60:
                    e = nextcord.Embed(
                        title=f"you went {direction}",
                        description=f"you got 2 crates :eyes:",
                        color=nextcord.Color.green(),
                        timestamp=datetime.datetime.utcnow()
                    )
                    e.set_footer(text="why is that not me nerd")
                    e.set_author(name=user.name, icon_url=user.avatar.url)
                    await interaction.response.send_message(embed=e)
                    crates_updated = num_crates + 2
                    await crates.update_one({"_id": user.id}, {"$set": {"crates": crates_updated}})

                elif f >= 50:
                    e = nextcord.Embed(
                        title=f"you went {direction}",
                        description=f"you got no crates :eyes:",
                        color=nextcord.Color.green(),
                        timestamp=datetime.datetime.utcnow()
                    )
                    e.set_footer(text="why is that not me nerd")
                    e.set_author(name=user.name, icon_url=user.avatar.url)
                    await interaction.response.send_message(embed=e)
                    crates_updated = num_crates + 1
                    await crates.update_one({"_id": user.id}, {"$set": {"crates": crates_updated}})

                else:
                    e = nextcord.Embed(
                        title=f"you went {direction}",
                        description=f"you got 3 crates :eyes:",
                        color=nextcord.Color.green(),
                        timestamp=datetime.datetime.utcnow()
                    )
                    e.set_footer(text="good thing I'm not you ;)")
                    e.set_author(name=user.name, icon_url=user.avatar.url)
                    await interaction.response.send_message(embed=e)
                    return

            elif direction == "Middle":
                if f >= 78:
                    e = nextcord.Embed(
                        title=f"you went {direction}",
                        description=f"you got 3 crates :eyes:",
                        color=nextcord.Color.green(),
                        timestamp=datetime.datetime.utcnow()
                    )
                    e.set_footer(text="why is that not me nerd")
                    e.set_author(name=user.name, icon_url=user.avatar.url)
                    await interaction.response.send_message(embed=e)
                    crates_updated = num_crates + 3
                    await crates.update_one({"_id": user.id}, {"$set": {"crates": crates_updated}})

                elif f >= 60:
                    e = nextcord.Embed(
                        title=f"you went {direction}",
                        description=f"you got 2 crates :eyes:",
                        color=nextcord.Color.green(),
                        timestamp=datetime.datetime.utcnow()
                    )
                    e.set_footer(text="why is that not me nerd")
                    e.set_author(name=user.name, icon_url=user.avatar.url)
                    await interaction.response.send_message(embed=e)
                    crates_updated = num_crates + 2
                    await crates.update_one({"_id": user.id}, {"$set": {"crates": crates_updated}})

                elif f >= 50:
                    e = nextcord.Embed(
                        title=f"you went {direction}",
                        description=f"you got 1 crate :eyes:",
                        color=nextcord.Color.green(),
                        timestamp=datetime.datetime.utcnow()
                    )
                    e.set_footer(text="why is that not me nerd")
                    e.set_author(name=user.name, icon_url=user.avatar.url)
                    await interaction.response.send_message(embed=e)
                    crates_updated = num_crates + 1
                    await crates.update_one({"_id": user.id}, {"$set": {"crates": crates_updated}})

                else:
                    e = nextcord.Embed(
                        title=f"you went {direction}",
                        description=f"you got no crates :eyes:",
                        color=nextcord.Color.green(),
                        timestamp=datetime.datetime.utcnow()
                    )
                    e.set_footer(text="good thing I'm not you ;)")
                    e.set_author(name=user.name, icon_url=user.avatar.url)
                    await interaction.response.send_message(embed=e)
            return

def setup(client):
    client.add_cog(AdventureCrateCommands(client))