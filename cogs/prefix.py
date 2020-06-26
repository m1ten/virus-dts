import discord
from discord.ext import commands
import json


class Prefix(commands.Cog, ):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        rf = open('././data.json', 'r')
        data = json.load(rf)
        rf.close()

        wf = open('././data.json', 'w')
        data['prefix'][str(guild.id)] = '!'
        print(data)
        json.dump(data, wf, indent=4)
        wf.close()

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        rf = open('././data.json', 'r')
        data = json.load(rf)
        rf.close()

        wf = open('././data.json', 'w')
        data['prefix'].pop(str(guild.id))
        json.dump(data, wf, indent=4)
        wf.close()

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def prefix(self, ctx, new_prefix=None):
        rf = open('././data.json', 'r')
        data = json.load(rf)
        rf.close()

        if new_prefix is None:
           return await ctx.send(f"Current prefix for this guild is ``{data['prefix'][str(ctx.guild.id)]}``.")

        wf = open('././data.json', 'w')
        data['prefix'][str(ctx.guild.id)] = new_prefix
        json.dump(data, wf, indent=4)

        await ctx.send(f'Prefix changed to ``{new_prefix}``')


def setup(bot):
    bot.add_cog(Prefix(bot))
