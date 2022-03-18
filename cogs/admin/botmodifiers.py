import nextcord
from nextcord.ext import commands

import os

class AdminCommands(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Admin Commands Loaded!")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.NotOwner):
            return
        
        if isinstance(error, commands.CommandNotFound):
            return

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx):
        for folder in os.listdir("./cogs"):
            for filename in os.listdir(f"./cogs/{folder}"):
                if filename.endswith(".py"):
                    self.client.reload_extension(f"cogs.{folder}.{filename[:-3]}")
                    
        await ctx.author.send("Reloaded All Extensions")

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx):
        for folder in os.listdir("./cogs"):
            for filename in os.listdir(f"./cogs/{folder}"):
                if filename.endswith(".py"):
                    self.client.load_extension(f"cogs.{folder}.{filename[:-3]}")

        await ctx.author.send("loaded All Extensions")

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx):
        for folder in os.listdir("./cogs"):
            for filename in os.listdir(f"./cogs/{folder}"):
                if filename.endswith(".py"):
                    self.client.unload_extension(f"cogs.{folder}.{filename[:-3]}")

        await ctx.author.send("Unloaded All Extensions")
        
    @commands.command()
    @commands.is_owner()
    async def reloadext(self, ctx, extension):
        self.client.reload_extension(str(extension))
                    
        await ctx.author.send("Reloaded Extension")

    @commands.command()
    @commands.is_owner()
    async def loadext(self, ctx, extension):
        self.client.load_extension(str(extension))

        await ctx.author.send("Loaded Extension")

    @commands.command()
    @commands.is_owner()
    async def unloadext(self, ctx, extension):
        self.client.unload_extension(str(extension))

        await ctx.author.send("Unloaded Extension")

def setup(client):
    client.add_cog(AdminCommands(client))