import discord
from discord.ext import commands
import json


class Help(commands.Cog, ):

    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command('help')

    @commands.command(pass_context=True)
    async def help(self, ctx):
        author = ctx.message.author

        embed = discord.Embed()

        embed.set_author(name='Help')
        embed.add_field(name='ping', value='Pong!', inline=False)

        await author.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
