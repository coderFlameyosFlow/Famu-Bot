import nextcord
from nextcord import (
    Interaction,
    slash_command
)
from nextcord.ext import commands

import datetime
import os
import random

import motor
import motor.motor_asyncio

import cooldowns

cluster = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://FlameyosFlow:reZPy4ZKz5YqumS@discord.fm5pk.mongodb.net/discord?retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE")
db = cluster.discord
collection = db.bank

class CasinoCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(name="slots", description="Slot some money!")
    @cooldowns.cooldown(1, 60, bucket=cooldowns.SlashBucket.author)
    async def slots(
        self,
        interaction: Interaction, 
        amount = nextcord.SlashOption(
            name="amount",
            description="How much do you want to bet?",
            required=True
        )
    ):
        async with interaction.channel.typing():
            user = interaction.user
            findbank = await collection.find_one({"_id": user.id})
            if not findbank:
                await collection.insert_one({"_id": user.id, "wallet": 0})

            wallet = findbank["wallet"]
            if amount == ["all", "All"]:
                if int(wallet) < 500000:
                    amount = int(wallet)
                elif int(amount) <= 0:
                    await interaction.send(f"You have too little money (your balance is {int(wallet):,}), minimum amount is $100.")
                elif int(amount) < 100:
                    await interaction.send(f"You have little money (your balance is ${int(wallet):,}), minimum amount is $100.")
                else:
                    await interaction.send("You have too much money, maximum amount is $500,000.")
                return

            amount = int(amount)

            if amount > int(wallet):
                await interaction.send('You do not have sufficient balance')
                return

            if amount < 0:
                await interaction.send('Amount must be positive!')
                return

            final = []
            a1 = random.choice(['♦️','♣️','♠️'])
            a2 = random.choice(['♦️','♣️','♠️'])
            a3 = random.choice(['♦️','♣️','♠️'])

            final.append(a1)
            final.append(a2)
            final.append(a3)

            if final[0] == final[1] or final[1] == final[2] or final[0] == final[2]:
                uw = wallet + amount
                await collection.update_one({"_id": interaction.user.id}, {"$set": {"wallet": uw}})
                embed = nextcord.Embed(
                    description=f"| {a1} | {a2} | {a3} | \nYou WON!",
                    color=nextcord.Color.green(),
                ).set_footer(
                    text=f"You got ${amount:,}!", 
                    icon_url=interaction.user.avatar.url,
                )
                await interaction.send(embed=embed)
            else:
                uw = wallet - amount
                await collection.update_one({"_id": interaction.user.id}, {"$set": {"wallet": uw}})
                embed = nextcord.Embed(
                    description=f"| {a1} | {a2} | {a3} | \nYou LOST!",
                    color=nextcord.Color.red(),
                ).set_footer(
                    text=f"You lost ${amount:,}!", 
                    icon_url=interaction.user.avatar.url
                )
                await interaction.send(embed=embed)

def setup(client):
    client.add_cog(CasinoCommand(client))
