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

class AwwCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(description="Random cute animals from the internet!")
    async def aww(self, interaction):
        async with interaction.channel.typing():
            async def get_birbs():
                async with aiohttp.ClientSession() as cs:
                    async with cs.get("https://www.reddit.com/r/aww/new.json") as r:
                        res = await r.json()

                return res['data']['children'][random.randint(0, 25)]['data']['url']

            async def btncallback(interaction):
                birbs = await get_birbs()
                emb = interaction.message.embeds[0].set_image(url=birbs)
                emb.set_footer(text=f"🤩: {random.randint(1, 10000)} 😢: {random.randint(1, 1000)}")
                await interaction.response.edit_message(embed=emb)

            async def delcallback(interaction):
                await interaction.message.delete()

            btn1 = Button(
                label="Next Cute Animal",
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

            embed = nextcord.Embed(title="These are SOOO CUTEEE") 
            embed.set_image(url=await get_birbs())
            embed.set_footer(text=f"🤩: {random.randint(1, 10000)} 😢: {random.randint(1, 1000)}")

            await interaction.send(embed=embed, view=view)

def setup(client):
    client.add_cog(AwwCommand(client))