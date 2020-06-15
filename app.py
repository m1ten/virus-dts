import discord
import os
import json
from discord.ext import commands

def get_token():
    try:
        with open('./data/token.json', 'r') as f:
            token = json.load(f)
    except ValueError:
        with open('./data/token.json', 'w') as f:
            token = input('Enter Token: ')
            json.dump(token, f, indent=4)

    return token


def get_prefix(bot, message):
    with open('./data/prefix.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

bot = commands.Bot(command_prefix = get_prefix)


@bot.event
async def on_guild_join(guild):
    with open('./data/prefix.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '!'

    with open('./data/prefix.json', 'w') as f:
         json.dump(prefixes, f, indent=4)


@bot.event 
async def on_guild_remove(guild):
    with open('./data/prefix.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('./data/prefix.json', 'w') as f:
         json.dump(prefixes, f, indent=4)


@bot.command()
async def prefix(ctx, new_prefix):
    with open('./data/prefix.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = new_prefix

    with open('./data/prefix.json', 'w') as f:
         json.dump(prefixes, f, indent=4)
    
    await ctx.send(f'Prefix changed to ``{new_prefix}``')


@bot.event
async def on_ready():
    print('Shark is online.')
    return


@bot.command()
async def load(ctx, extension='miscellaneous'):
    try: 
        bot.load_extension(f'cogs.{extension}')
        await ctx.send(f'Successfully loaded ``{extension}``!')
    except:
        await ctx.send(f'Error loading ``{extension}``!')

@bot.command()
async def unload(ctx, extension='miscellaneous'):
    try: 
        bot.unload_extension(f'cogs.{extension}')
        await ctx.send(f'Successfully unloaded ``{extension}``!')
    except:
        await ctx.send(f'Error unloading ``{extension}``!')

@bot.command()
async def reload(ctx, extension='miscellaneous'):
    try: 
        bot.reload_extension(f'cogs.{extension}')
        await ctx.send(f'Successfully reloaded ``{extension}``!')
    except:
        await ctx.send(f'Error reloading ``{extension}``!')


if __name__ == '__main__':
    for file in os.listdir('cogs'):
        if file.endswith('.py') and not file.startswith('_'):
            bot.load_extension(f'cogs.{file[:-3]}')

bot.run(get_token())