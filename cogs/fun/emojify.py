import nextcord
from nextcord import (
    slash_command,
    Interaction
)
from nextcord.ext import commands

class EmojifyCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(
        name="emojify", 
        description="Turn numbers and letters into emojis",
    )
    async def emojify(
        self,
        interaction: Interaction, *, 
        message = nextcord.SlashOption(
            name="message",
            description="What is your message?",
            required=True
        )
    ):
        async with interaction.channel.typing():
            emojis = []
            message = message.lower()
            for s in message:
                if s.isdecimal():
                    num2emo = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
                    emojis.append(f':{num2emo.get(s)}:')
                elif s.isalpha():
                    emojis.append(f':regional_indicator_{s}:')
                else:
                    emojis.append(s)

            await interaction.send(' '.join(emojis))

def setup(client):
    client.add_cog(EmojifyCommand(client))