import nextcord
from nextcord import (
    slash_command,
    Interaction
)
from nextcord.ext import commands

import os

import motor
import motor.motor_asyncio

cluster = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://FlameyosFlow:reZPy4ZKz5YqumS@discord.fm5pk.mongodb.net/discord?retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE")
db = cluster.discord
collection = db.bank
items = db.items

mainshop = [
    {
        "buyname": ["bodyguard", "bg", "Bodyguard", "BODYGUARD", "BG", "bODYGUARD"],
        "name": "<:Thief:952151438157570078> Bodyguard",
        "price": 35000,
        "description": f"If you get robbed, This bodyguard can SAVE you AND your valuables, you can buy up to 5 bodyguards"
    }, 
    {
        "buyname": ["laptop", "Laptop", "lap", "Lap", "LAPTOP", "lAPTOP", "LAP", "lAB"],
        "name": "<:laptop:952184538556145695> Laptop",
        "price": 25000,
        "description": f"You would need this to start a compan, an online company leads to an EVEN BIGGER company!",
    }, 
    {
        "buyname": ["antivirus", "Antivirus", "AntiVirus", "anti-virus", "Anti-Virus", "ANTIVIRUS", "ANTI-VIRUS", "aNTIVIRUS", "aNTI-VIRUS"],
        "name": "<:AVG:952151491773345832> Anti-Virus",
        "price": 15000,
        "description": "Scared of your company being hacked? even losing all of your company progress? well this anti-virus will block it! (**most** likely)",
    }, 
    {
        "name": "Ferrari", 
        "price": 99999,
        "description": "Sports Car",
    }, 
]

class BuyCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(description="Buy an item from the Shop! (/shop)")
    async def buy(
        self, 
        interaction: Interaction,
        item: str = nextcord.SlashOption(
            description="What would you like to buy from (/shop)?",
            required=True
        ),
        amount: int = nextcord.SlashOption(
            description="How much of that item?",
            required=False,
            default=1,
        )
    ):
        bodyguardaa = ["bodyguard", "bg", "Bodyguard", "BODYGUARD", "BG", "bODYGUARD"]
        laptopaa = ["laptop", "Laptop", "lap", "Lap", "LAPTOP", "lAPTOP", "LAP", "lAB"]
        antivirusaa = ["antivirus", "Antivirus", "AntiVirus", "anti-virus", "Anti-Virus", "ANTIVIRUS", "ANTI-VIRUS", "aNTIVIRUS", "aNTI-VIRUS"]
        async def buy_item(item, amount=1):
            member = interaction.user
            findbank = await collection.find_one({"_id": member.id})
            if not findbank:
                await collection.insert_one({"_id": member.id, "wallet": 0})
                
            finditems = await items.find_one({"_id": member.id})
            if not finditems:
                await items.insert_one({"_id": member.id, "bodyguard": False, "antivirus": False, "laptop": False})

            wallet = findbank["wallet"]
            bodyguard = finditems["bodyguard"]
            antivirus = finditems["antivirus"]
            laptop = finditems["laptop"]
            if item in bodyguardaa:
                bodyguard_price = 35000
                if wallet < bodyguard_price:
                    await interaction.send("You don't have enough money.")
                    return
                if bodyguard == 5:
                    await interaction.send("You already have max bodyguards.")
                    return
                if amount > 5:
                    await interaction.send("You can't buy more bodyguards than 5 (for now).")
                    return

                await collection.update_one({"_id": member.id}, {"$set": {"wallet": wallet - bodyguard_price}})
                await items.update_one({"_id": member.id}, {"$set": {"bodyguard": bodyguard + 1}})
                await interaction.send("Successfully bought a bodyguard <:Thief:952151438157570078>!")
                
            if item in laptopaa:
                laptop_price = 25000
                if wallet < laptop_price:
                    await interaction.send("You don't have enough money.")
                    return
                if laptop == 1:
                    await interaction.send("You already have a laptop.")
                    return
                if amount > 1:
                    await interaction.send("You can't buy more laptops than 1 (for now).")
                    return

                await collection.update_one({"_id": member.id}, {"$set": {"wallet": wallet - laptop_price}})
                await items.update_one({"_id": member.id}, {"$set": {"laptop": laptop + amount}})
                await interaction.send("Successfully bought a laptop <:laptop:952184538556145695>!")

            if item in antivirusaa:
                bodyguards = 0
                antivirus_price = 15000
                if wallet < antivirus_price:
                    await interaction.send("You don't have enough money.")
                    return
                if antivirus == 1:
                    await interaction.send("You already have an antivirus!")
                    return
                if amount > 1:
                    await interaction.send("You can't buy more antiviruses than 1 (for now).")
                    return

                await collection.update_one({"_id": member.id}, {"$set": {"wallet": wallet - antivirus_price}})
                await items.update_one({"_id": member.id}, {"$set": {"antivirus": bodyguards + amount}})
                await interaction.send("Successfully bought an antivirus <:AVG:952151491773345832>!")
                
        await buy_item(item, amount)

def setup(client):
    client.add_cog(BuyCommand(client))
