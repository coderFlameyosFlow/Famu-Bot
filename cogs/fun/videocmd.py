import nextcord
from nextcord import (
    slash_command,
    Interaction
)
from nextcord.ext import commands

import random

bullylink = [
    "https://media2.giphy.com/media/4zR888BBbyfiE/giphy.gif?cid=ecf05e47jpv8hofgict82ecd33u657m70h60l2hp4ooi5b3e&rid=giphy.gif&ct=g",
    "https://media0.giphy.com/media/xT5LMtZ06eAXSmftYs/200.gif?cid=ecf05e4713p77gk37gch6881lmfevdtrakkkf812qnooavcq&rid=200.gif&ct=g",
    "https://media2.giphy.com/media/j5QmKNxMNEy24wrr5R/200w.gif?cid=ecf05e4713p77gk37gch6881lmfevdtrakkkf812qnooavcq&rid=200w.gif&ct=g",
    "https://media2.giphy.com/media/vW6r05KjlTxRrvRjGo/100.gif?cid=ecf05e4713p77gk37gch6881lmfevdtrakkkf812qnooavcq&rid=100.gif&ct=g",
    "https://media2.giphy.com/media/j5QmKNxMNEy24wrr5R/200w.gif?cid=ecf05e4713p77gk37gch6881lmfevdtrakkkf812qnooavcq&rid=200w.gif&ct=g",
]

yeetlink = [
    "https://media1.giphy.com/media/j3p5J3EJvAJyJWXyZG/200w.gif?cid=ecf05e47wswqw7c55bqmi3v2wg9n2bmoonryzttm27qa4hts&rid=200w.gif&ct=v",
    "https://media0.giphy.com/media/xCyjMEYF9H2ZcLqf7t/200w.gif?cid=ecf05e47o1o380lro3vi7evf8cahipozzmsayfzaucow7ntz&rid=200w.gif&ct=g",
    "https://media4.giphy.com/media/4EEIsDmNJCiNcvAERe/200w.gif?cid=ecf05e47o1o380lro3vi7evf8cahipozzmsayfzaucow7ntz&rid=200w.gif&ct=g",
    "https://media4.giphy.com/media/NThOsGBwbZi8qaEear/200w.gif?cid=ecf05e472rq89p2gks5vbcy0ne0vok4ug8zp38cylq4pnsd5&rid=200w.gif&ct=g",
    "https://media4.giphy.com/media/5PhDdJQd2yG1MvHzJ6/giphy.gif?cid=ecf05e47b6g62pr0saw4hpkbsc4rz4mbibhc0cneora13jto&rid=giphy.gif&ct=g",
]

kisslink = [
    "https://media1.giphy.com/media/4a6hs4izxxEpCR4nvA/200w.gif?cid=ecf05e477wjoasz9z41xq1kjd8m09ck0g1i5959no0obkqvl&rid=200w.gif&ct=v",
    "https://media0.giphy.com/media/3o72F3zlbWvP4kJp4c/200.gif?cid=ecf05e47ixnjozuwj65chepdus8yujt2tp6ddlu8ndfclb61&rid=200.gif&ct=g",
    "https://media4.giphy.com/media/26tjZKoo8gwbugbsc/200.gif?cid=ecf05e47s6h3682l25uemrbezlzee47zqztki9w9rsq583tm&rid=200.gif&ct=g",
    "https://media4.giphy.com/media/3o7TKqhF898sKm6opy/200w.gif?cid=ecf05e47s6h3682l25uemrbezlzee47zqztki9w9rsq583tm&rid=200w.gif&ct=g",
    "https://media2.giphy.com/media/l2Jhok92mZ2PZHjDG/giphy.gif?cid=ecf05e47z92betjirr7mtzp3d0s8pkr8x5hx7nntly9jst3g&rid=giphy.gif&ct=g",
]

shootlink = [
    "https://media4.giphy.com/media/9umH7yTO8gLYY/200.gif?cid=ecf05e47oukjlbyuwatzf0ex7te6gklxa5hk898q03ne1v6u&rid=200.gif&ct=g",
    "https://media3.giphy.com/media/cS9lGF8gIBdQs/200.gif?cid=ecf05e47oukjlbyuwatzf0ex7te6gklxa5hk898q03ne1v6u&rid=200.gif&ct=g",
    "https://media2.giphy.com/media/Bm6jGUsWDBrHy/200.gif?cid=ecf05e47oukjlbyuwatzf0ex7te6gklxa5hk898q03ne1v6u&rid=200.gif&ct=g",
    "https://media0.giphy.com/media/l4nlWhecm3qN6cYtO9/200w.gif?cid=ecf05e47k1cams6bspui695cpimnr5hjaay66yibx00xmp55&rid=200w.gif&ct=g",
    "https://media2.giphy.com/media/wTZLkZNqI6QYz5cjjG/200w.gif?cid=ecf05e47elj4bczmdlq0ay049ine3vw3kpticwnso5mp81w3&rid=200w.gif&ct=g",
]

stablink = [
    "https://media4.giphy.com/media/3o6gE2MlZupcFIEMP6/200w.gif?cid=ecf05e479afjj0bar8pfcdga9kkvbt0bqk1w4lq7qe3y3j9l&rid=200w.gif&ct=g",
    "https://media3.giphy.com/media/RGecJFMSrMTZz4satb/200.gif?cid=ecf05e479v2f59xzdsy0e8jzymfpnbf2njkr389dg3zbt4vb&rid=200.gif&ct=g",
    "https://media4.giphy.com/media/3orif0HPtMKPs8su6Q/200.gif?cid=ecf05e474z9z804ymcmcivg9nxyt6ocrnaibjvotmgfpolel&rid=200.gif&ct=g",
    "https://media2.giphy.com/media/3o6ozCytqK9iZYgoVO/200w.gif?cid=ecf05e474z9z804ymcmcivg9nxyt6ocrnaibjvotmgfpolel&rid=200w.gif&ct=g",
    "https://media2.giphy.com/media/26grAXwZFhA8kyT60/200w.gif?cid=ecf05e4789n95kh60bvyf6dc0fovfocgu4bzufugv2uqmfnd&rid=200w.gif&ct=g",
]

slaplink = [
    "https://media2.giphy.com/media/Ql5voX2wAVUYw/giphy.gif?cid=ecf05e47hrghq60mnybqyjd8apk4d94nadpr0drm9aqw3thv&rid=giphy.gif&ct=g",
    "https://media1.giphy.com/media/Qvwc79OfQOa4g/200.gif?cid=ecf05e47hrghq60mnybqyjd8apk4d94nadpr0drm9aqw3thv&rid=200.gif&ct=g",
    "https://media2.giphy.com/media/s5zXKfeXaa6ZO/giphy.gif?cid=ecf05e47hrghq60mnybqyjd8apk4d94nadpr0drm9aqw3thv&rid=giphy.gif&ct=g",
    "https://media4.giphy.com/media/3XlEk2RxPS1m8/200.gif?cid=ecf05e47hrghq60mnybqyjd8apk4d94nadpr0drm9aqw3thv&rid=200.gif&ct=g",
    "https://media4.giphy.com/media/uG3lKkAuh53wc/giphy.gif?cid=ecf05e47bra41jymi3e9k5c57msc20dt2p6le7cg51ac9va1&rid=giphy.gif&ct=g",
]

huglink = [
    "https://media3.giphy.com/media/26wkBtoUrZwYnFLWg/200w.gif?cid=ecf05e47m1ivohv3jn16s7oqttpd6f336uc07lyxo3txzkk7&rid=200w.gif&ct=g",
    "https://media1.giphy.com/media/kggfTFCnrAFJSf8JL8/100.gif?cid=ecf05e47m1ivohv3jn16s7oqttpd6f336uc07lyxo3txzkk7&rid=100.gif&ct=g",
    "https://media2.giphy.com/media/bvFS4rALdNDag/giphy.gif?cid=ecf05e47m1ivohv3jn16s7oqttpd6f336uc07lyxo3txzkk7&rid=giphy.gif&ct=g",
    "https://media3.giphy.com/media/EvYHHSntaIl5m/giphy.gif?cid=ecf05e4717ahvmvv2sk76ayh7g6ge9wgearxeikx8crrrc4t&rid=giphy.gif&ct=g",
    "https://media1.giphy.com/media/llmZp6fCVb4ju/giphy.gif?cid=ecf05e47yllvta0wslwqux53gmkrsfgn8ieg5om7fpwllgyx&rid=giphy.gif&ct=g",
]

class VideoCommands(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @slash_command(
        name="bully", 
        description="Bully some kids, hehe ;D",
    )
    async def bully(
        self,
        interaction: Interaction, 
        member: nextcord.Member = nextcord.SlashOption(
            name="member",
            description="Who is the unlucky person?",
            required=True
        )
    ):
        async with interaction.channel.typing():
            embed = nextcord.Embed(title=f"You are bullying {member}!", description=f"You have bullied {member.mention} {interaction.user.mention}.", color = nextcord.Color.random())
            embed.set_image(url=random.choice(bullylink))
            await interaction.response.send_message(embed=embed)

    @slash_command(name="yeet", description="Yeet some kids, hehe ;D")
    async def yeet(
        self,
        interaction: Interaction, 
        member: nextcord.Member = nextcord.SlashOption(
            name="member",
            description="Who is the unlucky person?",
            required=True
        )
    ):
        async with interaction.channel.typing():
            embed = nextcord.Embed(title=f"You are yeeting {member}!", description=f"You have yeeted {member.mention} {interaction.user.mention}.", color = nextcord.Color.random())
            embed.set_image(url=random.choice(yeetlink))
            await interaction.response.send_message(embed=embed)

    @slash_command(name="kiss", description="Kiss someone.")
    async def kiss(
        self,
        interaction: Interaction, 
        member: nextcord.Member = nextcord.SlashOption(
            name="member",
            description="Who is the lucky person?",
            required=True
        )
    ):
        async with interaction.channel.typing():
            embed = nextcord.Embed(title=f"You are kissinging {member}!", description=f"You have kissed {member.mention} {interaction.user.mention}.", color = nextcord.Color.random())
            embed.set_image(url=random.choice(kisslink))
            await interaction.response.send_message(embed=embed)

    @slash_command(name="shoot", description="Shoot some kids, hehe ;D")
    async def shoot(
        self,
        interaction: Interaction, 
        member: nextcord.Member = nextcord.SlashOption(
            name="member",
            description="Who is the unlucky person?",
            required=True
        )
    ):
        async with interaction.channel.typing():
            embed = nextcord.Embed(title=f"You are shooting {member}!", description=f"You have shot {member.mention} {interaction.user.mention}.", color = nextcord.Color.random())
            embed.set_image(url=random.choice(shootlink))
            await interaction.response.send_message(embed=embed)

    @slash_command(name="stab", description="Stab some kids, hehe ;D")
    async def stab(
        self,
        interaction: Interaction, 
        member: nextcord.Member = nextcord.SlashOption(
            name="member",
            description="Who is the unlucky person?",
            required=True
        )
    ):
        async with interaction.channel.typing():
            embed = nextcord.Embed(title=f"You are stabing {member}!", description=f"You have stabbed {member.mention} {interaction.user.mention}.", color = nextcord.Color.random())
            embed.set_image(url=random.choice(stablink))
            await interaction.response.send_message(embed=embed)

    @slash_command(name="slap", description="Slap some kids, hehe ;D")
    async def slap(
        self,
        interaction: Interaction, 
        member: nextcord.Member = nextcord.SlashOption(
            name="member",
            description="Who is the unlucky person?",
            required=True
        )
    ):
        async with interaction.channel.typing():
            embed = nextcord.Embed(title=f"You are slapping {member}!", description=f"You have slapped {member.mention} {interaction.user.mention}.", color = nextcord.Color.random())
            embed.set_image(url=random.choice(slaplink))
            await interaction.response.send_message(embed=embed)

    @slash_command(name="hug", description="Hug some people.")
    async def hug(
        self,
        interaction: Interaction, 
        member: nextcord.Member = nextcord.SlashOption(
            name="member",
            description="Who is the unlucky person?",
            required=True
        )
    ):
        async with interaction.channel.typing():
            embed = nextcord.Embed(title=f"You are hugging {member}!", description=f"You have hugged {member.mention} {interaction.user.mention} :D.", color = nextcord.Color.random())
            embed.set_image(url=random.choice(huglink))
            await interaction.response.send_message(embed=embed)

def setup(client):
    client.add_cog(VideoCommands(client))