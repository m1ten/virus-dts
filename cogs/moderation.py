import discord
from discord.ext import commands
import time


class Moderation(commands.Cog, ):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def clear(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount)
        if amount == 1:
            await ctx.send(f'Successfully deleted ``{amount}`` message.')
        else:
            await ctx.send(f'Successfully deleted ``{amount}`` messages.')
        time.sleep(5)
        await ctx.channel.purge(limit=1)


def setup(bot):
    bot.add_cog(Moderation(bot))
