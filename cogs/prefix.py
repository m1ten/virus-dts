import discord
from discord.ext import commands
import json

class Prefix(commands.Cog,):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with open('././data/prefix.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(guild.id)] = '!'

        with open('././data/prefix.json', 'w') as f:
            json.dump(prefixes, f, indent=4)


    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        with open('././data/prefix.json', 'r') as f:
            prefixes = json.load(f)

        prefixes.pop(str(guild.id))

        with open('././data/prefix.json', 'w') as f:
            json.dump(prefixes, f, indent=4)


    @commands.command()
    async def prefix(self, ctx, new_prefix):
        with open('././data/prefix.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = new_prefix

        with open('././data/prefix.json', 'w') as f:
            json.dump(prefixes, f, indent=4)
    
        await ctx.send(f'Prefix changed to ``{new_prefix}``')


def setup(bot):
    bot.add_cog(Prefix(bot))