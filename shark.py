import discord
import os
import json
from discord.ext import commands

# data variable
data = {
    "bot": {
        "token": None,
        "owner_id": None
    },
    "guild": {},
    "user": {}
}


# initialize setup
def _data_():
    global data

    # load data from data.json
    read_data = open('./data.json', 'r')
    data = json.load(read_data)
    read_data.close()

    # open data.json with write permission
    write_data = open('./data.json', 'w')

    # if there is no token, input token
    if data['token'] is None:
        data['token'] = input('Enter Bot Token: ')

    # if there is no owner_id, input owner_id
    if data['owner_id'] is None:
        data['owner_id'] = int(input('Enter Owner ID: '))

    # dump data to data.json
    json.dump(data, write_data, indent=4)
    write_data.close()

    return data


# get prefix from data
async def get_prefix(bot, ctx):
    data = _data_()

    try:
        return data[str(ctx.guild.id)]["prefix"]
    except:
        return '!'  # if no prefix assigned or dm

# define bot, assign prefix
bot = commands.Bot(command_prefix=get_prefix)


@bot.event
async def on_ready():
    # set status and activity of bot
    await bot.change_presence(status=discord.Status.idle,
                              activity=discord.Game('! | m1ten.me/shark'))

    data = _data_()
    bot.owner_id = data['owner_id']

    try:
        await bot.get_user(bot.owner_id).send('Shark is online.')
    except:
        pass

    print('Shark is online.')

    return

if __name__ == '__main__':
    _data_()

    for cog_files in os.listdir('commands'):
        if cog_files.endswith('.py') and not cog_files.startswith('_'):
            bot.load_extension(f'commands.{cog_files[:-3]}')

bot.run(data['token'])
