import nextcord
from nextcord import (
    slash_command
)
from nextcord.ui import (
    Button, 
    View
)
from nextcord.ext import commands
import random
import aiohttp

class KittysCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(description="Random kittys from the internet")
    async def kittys(self, interaction):
        async with interaction.channel.typing():
            async def get_kittys():
                async with aiohttp.ClientSession() as cs:
                    async with cs.get("https://www.reddit.com/r/catpictures/new.json") as r:
                        res = await r.json()

                return res['data']['children'][random.randint(1, 25)]['data']['url']

            async def btncallback(interaction):
                cat = await get_kittys()
                emb = interaction.message.embeds[0].set_image(url=cat)
                emb.set_footer(text=f"🤩: {random.randint(1, 10000)} 😢: {random.randint(1, 1000)}")
                await interaction.response.edit_message(embed=emb)

            async def delcallback(interaction):
                await interaction.message.delete()

            btn1 = Button(
                label="Next Kittys",
                style=nextcord.ButtonStyle.green,
            )

            btn2 = Button(
                style=nextcord.ButtonStyle.gray,
                emoji="🗑️"
            )

            btn1.callback = btncallback
            btn2.callback = delcallback

            view=View()
            view.add_item(btn1)
            view.add_item(btn2)

            embed = nextcord.Embed(title="I got one of the cutiest one:")
            embed.set_image(url=await get_kittys())
            embed.set_footer(text=f"🤩: {random.randint(1, 10000)} 😢: {random.randint(1, 1000)}")
            
            await interaction.response.send_message(embed=embed, view=view)

def setup(client):
    client.add_cog(KittysCommand(client))