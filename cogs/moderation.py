import discord
from discord.ext import commands


class Moderation(commands.Cog, ):

    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def say(self, ctx, *args, ):
        try:
            await ctx.message.delete()
        except:
            pass
        msg = ' '.join(args)
        await ctx.send(msg)


    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def clear(self, ctx, amount : int):
        await ctx.message.delete()
        await ctx.channel.purge(limit=amount)
        if amount == 1:
            await ctx.send(f':white_check_mark: | I successfully deleted ``{amount}`` message.', delete_after=5)
        else:
            await ctx.send(f':white_check_mark: | I successfully deleted ``{amount}`` messages.', delete_after=5)
            


    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await ctx.message.delete()
        await member.send(f':x: | You have been kicked from ``{ctx.guild}`` with the reason, ``{reason}``.')
        await member.kick(reason=reason)
        await ctx.send(f':white_check_mark: | Successfully kicked ``{member}`` with the reason, ``{reason}``.', delete_after=5)

    # errors

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(':x: | You are missing ``manage_messages`` permission.', delete_after=5)
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send(':x: | I am missing ``manage_messages`` permission.', delete_after=5)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(':x: | Missing required amount.', delete_after=5)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.CommandInvokeError):
            if isinstance(error.original, discord.Forbidden):
                await ctx.send(':x: | Unable to kick member.', delete_after=5)
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(':x: | You are missing ``kick_members`` permission.', delete_after=5)
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send(':x: | I am missing ``kick_members`` permission.', delete_after=5)


def setup(bot):
    bot.add_cog(Moderation(bot))
