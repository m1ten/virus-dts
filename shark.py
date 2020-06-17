import discord
import os
import json
from discord.ext import commands

data = {}
data['token'] = None
data['prefix'] = None
data['owner_id'] = None


try:
    rf = open('data.json', 'r')
    data = json.load(rf)
    rf.close()
except:
    pass


if data['token'] == None:
    wf = open('./data.json', 'w')
    data['token'] = input('Enter token: ')
    json.dump(data, wf, indent=4)
    wf.close()
else:
    pass


async def get_prefix(bot, ctx):
    try:
        return data['prefix'][str(ctx.guild.id)]
    except:
        return '!'


bot = commands.Bot(command_prefix=get_prefix)


if data['owner_id'] == None:
    wf = open('./data.json', 'w')
    data['owner_id'] = input('Enter owner_id: ')
    bot.owner_id = data['owner_id']
    json.dump(data, wf, indent=4)
    wf.close()
else:
    pass


@bot.event
async def on_ready():
    print('Shark is online.')
    return


if __name__ == '__main__':
    for file in os.listdir('cogs'):
        if file.endswith('.py') and not file.startswith('_'):
            bot.load_extension(f'cogs.{file[:-3]}')


bot.run(data['token'])
