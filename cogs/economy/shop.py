import nextcord
from nextcord import (
    Interaction,
    slash_command
)
from nextcord.ext import commands
coins = "<a:coins:952154182851383416>"
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
        "name": "Anti-Virus",
        "price": 15000,
        "description": "Scared of your company being hacked? even losing all of your company progress? well this anti-virus will block it! (**most** likely)",
    }, 
    {
        "name": "Ferrari", 
        "price": 99999,
        "description": "Sports Car",
    }, 
]

class ShopCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(name="shop", description="Look at the Shop!")
    async def shop(self, interaction: Interaction):

        async with interaction.channel.typing():
            em = nextcord.Embed(title="Shop", color=nextcord.Color.blue())

            for item in mainshop:
                name = item["name"]
                price = item["price"]
                desc = item["description"]
                em.add_field(
                    name=f"{name}", 
                    value=f"${price:,}{coins} | {desc}", 
                    inline=False
                )

            await interaction.send(embed=em)

def setup(client):
    client.add_cog(ShopCommand(client))