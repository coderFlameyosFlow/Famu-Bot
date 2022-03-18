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

class PuppysCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(description="Random puppys from the internet!")
    async def puppy(self, interaction):
        async with interaction.channel.typing():
            async def get_puppys():
                async with aiohttp.ClientSession() as cs:
                    async with cs.get("https://www.reddit.com/r/dogpictures/new.json") as r:
                        res = await r.json()

                return res['data']['children'][random.randint(0, 25)]['data']['url']

            async def btncallback(interaction):
                pup = await get_puppys()
                emb = interaction.message.embeds[0].set_image(url=pup)
                emb.set_footer(text=f"🤩: {random.randint(1, 10001)} 😢: {random.randint(0, 1000)}")
                await interaction.response.edit_message(embed=emb)

            async def delcallback(interaction):
                await interaction.message.delete()

            btn1 = Button(
                label="Next Puppy",
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

            embed = nextcord.Embed(
                title="I got a cute one for you!"
            )
            embed.set_image(url=await get_puppys())
            embed.set_footer(text= f"🤩: {random.randint(1, 10000)} 😢: {random.randint(1, 1000)}")

            await interaction.response.send_message(embed=embed, view=view)

def setup(client):
    client.add_cog(PuppysCommand(client))