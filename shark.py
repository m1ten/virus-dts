import discord
import os
import json
from discord.ext import commands

data = {'token': None, 'prefix': {}, 'owner_id': None}

try:
    rf = open('data.json', 'r')
    data = json.load(rf)
    rf.close()
except:
    pass


if data['token'] is None:
    wf = open('./data.json', 'w')
    data['token'] = input('Enter token: ')
    json.dump(data, wf, indent=4)
    wf.close()
else:
    pass

if data['owner_id'] is None:
    wf = open('./data.json', 'w')
    data['owner_id'] = int(input('Enter owner_id: '))
    bot.owner_id = data['owner_id']
    json.dump(data, wf, indent=4)
    wf.close()
else:
    pass


async def get_prefix(bot, ctx):
    prefix_file = open('data.json', 'r')
    data = json.load(prefix_file)
    prefix_file.close
    
    try:
        return data['prefix'][str(ctx.guild.id)]
    except:
        return '!'


bot = commands.Bot(command_prefix=get_prefix)


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle,
                              activity=discord.Game('!help | m1t3n.tk'))

    rf = open('./data.json', 'r')
    data = json.load(rf)
    bot.owner_id = data['owner_id']
    owner = bot.get_user(bot.owner_id)
    try:
        await owner.send('Shark is online.')
    except: 
        pass
    print('Shark is online.')
    return

if __name__ == '__main__':
    for file in os.listdir('cogs'):
        if file.endswith('.py') and not file.startswith('_'):
            bot.load_extension(f'cogs.{file[:-3]}')


bot.run(data['token'])

