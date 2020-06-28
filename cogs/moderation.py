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
        try:
            await member.send(f':x: | You have been kicked from ``{ctx.guild}`` with the reason, ``{reason}``.')
            await member.kick(reason=reason)
        except discord.Forbidden:
            await member.kick(reason=reason)
        await ctx.send(f':white_check_mark: | Successfully kicked {member.mention} with the reason, ``{reason}``.', delete_after=5)


    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await ctx.message.delete()
        try:
            await member.send(f':x: | You have been banned from ``{ctx.guild}`` with the reason, ``{reason}``.')
            await member.ban(reason=reason)
        except discord.Forbidden:
            await member.ban(reason=reason)
        await ctx.send(f':white_check_mark: | Successfully banned {member.mention} with the reason, ``{reason}``.', delete_after=5)


    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        
        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f':white_check_mark: | Successfully unbanned {user.mention}.', delete_after=5)
                return
    
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


    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.CommandInvokeError):
            if isinstance(error.original, discord.Forbidden):
                await ctx.send(':x: | Unable to ban member.', delete_after=5)
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(':x: | You are missing ``ban_members`` permission.', delete_after=5)
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send(':x: | I am missing ``ban_members`` permission.', delete_after=5)


def setup(bot):
    bot.add_cog(Moderation(bot))
