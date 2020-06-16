import discord
from discord.ext import commands

class Cogs(commands.Cog,):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def load(self, ctx, extension='miscellaneous'):
        try: 
            self.bot.load_extension(f'cogs.{extension}')
            await ctx.send(f'Successfully loaded ``{extension}``!')
        except:
            await ctx.send(f'Error loading ``{extension}``!')

    @commands.command()
    async def unload(self, ctx, extension='miscellaneous'):
        try: 
            self.bot.unload_extension(f'cogs.{extension}')
            await ctx.send(f'Successfully unloaded ``{extension}``!')
        except:
            await ctx.send(f'Error unloading ``{extension}``!')

    @commands.command()
    async def reload(self, ctx, extension='miscellaneous'):
        try: 
            self.bot.reload_extension(f'cogs.{extension}')
            await ctx.send(f'Successfully reloaded ``{extension}``!')
        except:
            await ctx.send(f'Error reloading ``{extension}``!')

def setup(bot):
    bot.add_cog(Cogs(bot))