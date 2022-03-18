import nextcord
from nextcord.ext import commands
from nextcord import (
    Interaction,
    slash_command
)
import random
import datetime

class _8BallCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(name="8ball", description="You have called the 8ball to predict the future for you.")
    async def _8ball(
        self,
        interaction: Interaction,
        question: str = nextcord.SlashOption(
            name="question",
            description="What question do you wanna ask the bot?",
            required=True 
        )
    ):
        async with interaction.channel.typing():
            possibilities = [
                "Yes.",
                "Ofcourse!",
                "Maybe.",
                "Infact, you're right!",
                "Facts!",
                "I don't know, I'm just an 8ball",
                "Use another 8ball I'm not worth it :(",
                "Probably not.",
                "Ofcourse not!",
                "No."
                "Never",
                "Suck it up #$&@%, Never Ever Ever Never Ever!"
            ]

            responses = random.choice(possibilities)
            if (
                question.startswith("should")
                or question.startswith("did") 
                or question.startswith("were") 
                or question.startswith("may") 
                or question.startswith("could") 
                or question.startswith("would") 
                or question.startswith("can") 
                or question.startswith("is") 
                or question.startswith("are") 
                or question.startswith("will") 
                or question.startswith("what") 
                or question.startswith("do") 
                or question.startswith("does") 
                or question.startswith("am") 
                or question.startswith("Should") 
                or question.startswith("May") 
                or question.startswith("Could") 
                or question.startswith("Would") 
                or question.startswith("Can") 
                or question.startswith("Is") 
                or question.startswith("Are") 
                or question.startswith("Will") 
                or question.startswith("What") 
                or question.startswith("Do") 
                or question.startswith("Does") 
                or question.startswith("Am") 
                or question.startswith("Did") 
                or question.startswith("Were")
            ):
                if question.endswith("?"):

                    e = nextcord.Embed(
                        title="The 8ball has spoken", 
                        color=nextcord.Color.random(), 
                        timestamp=datetime.datetime.utcnow()
                    )
                    e.add_field(name="Question:", value=f"{question}")
                    e.add_field(name="🎱 Answer:", value=f"🎱 {responses}", inline=False)

                else:

                    e = nextcord.Embed(title="The 8ball has spoken", color = nextcord.Color.random(), timestamp=datetime.datetime.utcnow())
                    e.add_field(name="Question:", value=f"{question}?")
                    e.add_field(name="Answer:", value=f"{responses}", inline=False)

                await interaction.response.send_message(embed=e)
                return
            
            else:

                await interaction.response.send_message("That could not have been a question, start with: \n`do`, `is`, `are`, `did`, `were`, `could`, `will`, `can`, `would`, `what`, `may`, `should`, `does` or `am`")

def setup(client):
    client.add_cog(_8BallCommand(client))