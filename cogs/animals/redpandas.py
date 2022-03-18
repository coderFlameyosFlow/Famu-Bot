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

class RedPandasCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(description="Random red pandas from the internet (cute)!")
    async def redpandas(self, interaction):
        async with interaction.channel.typing():
            async def get_meme():
                async with aiohttp.ClientSession() as session:
                    async with session.get("https://www.reddit.com/r/redpandas/new.json") as r:
                        res = await r.json()

                return res['data']['children'][random.randint(0, 25)]['data']['url']

            async def button_callback(interaction):
                meme = await get_meme()
                emb = interaction.message.embeds[0].set_image(url=meme)
                emb.set_footer(text=f"🤩: {random.randint(0, 75000)} 😢: {random.randint(0, 35000)}")
                await interaction.response.edit_message(embed=emb)

            async def delete_callback(interaction):
                await interaction.message.delete()

            button1 = Button(
                label="Next Red Panda",
                style=nextcord.ButtonStyle.green,
            )
            button2 = Button(
                label="🗑️",
                style=nextcord.ButtonStyle.gray,
            ) 

            button1.callback = button_callback
            button2.callback = delete_callback
            
            view=View()  
            view.add_item(button1)
            view.add_item(button2)

            embed = nextcord.Embed(title="How cute!!")
            embed.set_image(url=await get_meme())
        
            embed.set_footer(text=f"🤩: {random.randint(0, 55000)} 😢: {random.randint(0, 35000)}")
            await interaction.send(embed=embed, view=view)

def setup(client):
    client.add_cog(RedPandasCommand(client))