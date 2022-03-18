import nextcord
from nextcord import (
    Interaction,
    slash_command
)
from nextcord.ext import commands
import datetime

class PollCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(name="poll", description="Make a Poll!")
    async def poll(
        self,
        interaction: Interaction, 
        topic = nextcord.SlashOption(
            name="topic",
            description="What is the topic of this poll?",
            required=True,
        ), 
        choice1 = nextcord.SlashOption(
            name="choice1",
            description="First Choice.",
            required=True 
        ), 
        choice2 = nextcord.SlashOption(
            name="choice2",
            description="Second Choice.",
            required=True,
        ),
        c3 = nextcord.SlashOption(
            name="choice3",
            description="Third Choice.",
            required=False,
        ),
        c4 = nextcord.SlashOption(
            name="choice4",
            description="Fourth Choice.",
            required=False,
        ),
        c5 = nextcord.SlashOption(
            name="choice5",
            description="Fifth Choice.",
            required=False,
        ),
        c6 = nextcord.SlashOption(
            name="choice6",
            description="Sixth Choice.",
            required=False,
        ),
        c7 = nextcord.SlashOption(
            name="choice7",
            description="Seventh Choice.",
            required=False,
        ),
        c8 = nextcord.SlashOption(
            name="choice8",
            description="Eighth Choice.",
            required=False,
        ),
        c9 = nextcord.SlashOption(
            name="choice9",
            description="Ninth Choice.",
            required=False,
        ),
        c10 = nextcord.SlashOption(
            name="choice10",
            description="Tenth Choice.",
            required=False,
        ),
    ):
        async with interaction.channel.typing():
            choices = [choice1, choice2, c3, c4, c5, c6, c7, c8, c9, c10]
            choice_reactions = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]

            embed = nextcord.Embed(
                title=topic,
                description="",
                color=nextcord.Color.green(),
                timestamp=datetime.datetime.utcnow()
            )
            embed.set_author(name="Requested by " + interaction.user.name, icon_url=interaction.user.avatar.url)
            options = [c for c in choices if c is not None]
            optionreaction = [cr for cr in choice_reactions if options is not None]

            for i in range(0, len(options)):
                embed.description += f'{optionreaction[i]} {options[i]}\n'

            await interaction.send(embed=embed)

            embed_msg = (await interaction.original_message())

            for i in range(0, len(options)):
                await embed_msg.add_reaction(optionreaction[i])

        return

def setup(client):
    client.add_cog(PollCommand(client))