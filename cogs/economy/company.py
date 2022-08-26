import nextcord
from nextcord import (
    Interaction,
    slash_command,
)
from nextcord.ui import (
    Button, 
    View
)
from nextcord.ext import commands

import datetime
import os
import asyncio

import motor
import motor.motor_asyncio

cluster = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://FlameyosFlow:reZPy4ZKz5YqumS@discord.fm5pk.mongodb.net/discord?retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE")
db = cluster.discord
collection = db.bank
companyaa = db.company

class CompanyCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(name="company", description="Company!")
    async def company(self, interaction: Interaction):
        pass

    @company.subcommand(name="upgrade", description="Upgrade your company!")
    async def company_upgrade(self, interaction):
        member = interaction.user
        findcompany = await companyaa.find_one({"_id": member.id})
        if not findcompany:
            await interaction.send("You currently don't have a company! You can create one by `/company create`.")

        findbank = await collection.find_one({"_id": member.id})
        if not findbank:
            await collection.insert_one({"_id": member.id, "wallet": 0})

        wallet = findbank["wallet"]

        level = findcompany["level"]

        while level < 3:
            async def btncallback(interaction):
                if level == 1:
                    if wallet >= 35000:
                        await collection.update_one({
                                "_id": member.id
                            },

                            {
                                "$set": {
                                    "wallet": wallet - 35000
                                }
                            })

                        await companyaa.update_one({
                                "_id": member.id
                            },

                            {
                                "$set": {
                                    "level": level + 1
                                }
                            })

                        await interaction.send("Your company level has been upgraded to level 2!", ephemeral=True)
                        pass

                    else:
                        await interaction.send("You don't even have enough money.", ephemeral=True)
                        pass

                if level == 2:
                    if wallet >= 100000:
                        await collection.update_one({
                                "_id": member.id
                            },

                            {
                                "$set": {
                                    "wallet": wallet - 100000
                                }
                            })

                        await companyaa.update_one({
                                "_id": member.id
                            },

                            {
                                "$set": {
                                    "level": level + 1
                                }
                            })


                        await interaction.send("Your company level has been upgraded to level 3!", ephemeral=True)
                        pass

                    else:
                        await interaction.send("You don't even have enough money.", ephemeral=True)
                        pass

            async def btn2callback(interaction):
                await interaction.send("You have declined this.", ephemeral=True)
                pass

            button = Button(
                label="Yes",
                style=nextcord.ButtonStyle.green
            )

            button2 = Button(
                label="No",
                style=nextcord.ButtonStyle.red
            )

            button.callback = btncallback
            button2.callback = btn2callback
            view=View()
            view.add_item(button)
            view.add_item(button2) 

            embed = nextcord.Embed(
                title=f"Would you like to upgrade your company to level {level + 1:,}?",
                description="It'll cost $35,000.",
                color=nextcord.Color.green(),
                timestamp=datetime.datetime.utcnow()
            ).set_thumbnail(url=interaction.user.avatar.url)
            await interaction.send(embed=embed, view=view)
            return

        else:
            await interaction.send("You hit the max level for your company, maybe stay tuned for more")

    @company.subcommand(name="info", description="Information about your company!")
    async def company_info(self, interaction):
        member = interaction.user
        findcompany = await companyaa.find_one({"_id": member.id})
        if not findcompany:
            await interaction.send("You don't have a company, create one with /company create.")

        worth = findcompany["worth"]
        level = findcompany["level"]
        name = findcompany["name"]
        embed = nextcord.Embed(
            title="{} information:".format(name),
            description="A list of information about your company",
            color=nextcord.Color.green(),
            timestamp=datetime.datetime.utcnow()
        )

        embed.add_field(
            name="Company Worth:",
            value=f"{round(worth)}",
        )

        embed.add_field(
            name="Company Level:",
            value=f"{int(level)}",
        )

        await interaction.send(embed=embed)

    @company.subcommand(name="create", description="Create a company!")
    async def company_create(self, interaction):
        async with interaction.channel.typing():
            member = interaction.user
            findcompany = await companyaa.find_one({"_id": member.id})
            if not findcompany:
                await interaction.send("What would you like to name your company? 1 minute to respond.")
                def check(m):
                    return m.author == interaction.user

                try:
                    raw_name = await self.client.wait_for("message", check=check, timeout=60.0)
                    name = raw_name.content
                except asyncio.TimeoutError:
                    await interaction.send("You ran out of time, rerun the command.")
                    pass
                
                embed = nextcord.Embed(
                    title=f"Company successfully created named {name}!", 
                    description="Try using `/work` or `/company` subcommands.", 
                    color=nextcord.Color.green(), 
                    timestamp=datetime.datetime.utcnow()
                )
                await interaction.send(embed=embed)

                await companyaa.insert_one({"_id": member.id, "name": str(name), "worth": 0, "level": 1})

            else:
                await interaction.send("You already have a company, no need for a new one!")

def setup(client):
    client.add_cog(CompanyCommand(client))
