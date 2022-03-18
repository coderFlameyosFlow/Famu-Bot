import nextcord
from nextcord import (
    Interaction,
    slash_command
)
from nextcord.ext import commands
from nextcord.ui import (
    View,
    Button
)
from urllib.parse import quote_plus

class Google(View):
    def __init__(self, query: str):
        super().__init__()
        
        query = quote_plus(query)
        url = f"https://www.google.com/search?q={query}"

        self.add_item(Button(label='Results From Google', url=url))

class GoogleCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(description="Search on google directly using this command!")
    async def google(
        interaction: Interaction, 
        query: str = nextcord.SlashOption(
            name="search",
            description="What would you like to search on google?",
            required = True
        )
    ):
        view = Google(query)
        async with interaction.channel.typing():
            await interaction.send(f"Google Results for: `{query}`", view=view)

def setup(client):
    client.add_cog(GoogleCommand(client))