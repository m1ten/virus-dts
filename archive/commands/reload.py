import discord
from discord.ext import commands

class Reload(commands.Cog, ):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, extension='miscellaneous'):
        try:
            self.bot.reload_extension(f'commands.{extension}')
            await ctx.send(f'Successfully reloaded ``{extension}``!')
        except:
            await ctx.send(f':x: | Error reloading ``{extension}``!')

def setup(bot):
    bot.add_cog(Reload(bot))