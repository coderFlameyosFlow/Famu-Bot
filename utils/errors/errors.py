import nextcord

class NotOwnerFlame(nextcord.errors.DiscordException):
    def __init__(self):
        super().__init__(
            "Unsuccessfully issued an only owner command"
            "The problem could be because the interaction.user"
            "was not the owner, which is FlameyosFlow#8894"
        )