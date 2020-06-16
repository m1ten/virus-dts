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


def get_prefix(bot, ctx):
    try:
        with open('./data/prefix.json', 'r') as f:
            prefixes = json.load(f)
        return prefixes[str(ctx.guild.id)]
    except:
        return '!'


bot = commands.Bot(command_prefix = get_prefix)

try: 
    with open('./data/owner_id.json', 'r') as f:
        owner_id = json.load(f)
        bot.owner_id = owner_id
except: bot.owner_id = None

if bot.owner_id == None:
    with open('./data/owner_id.json', 'w') as f:
        owner_id = int(input('Enter owner_id: '))
        json.dump(owner_id, f, indent=4)
        bot.owner_id = owner_id

@bot.event
async def on_ready():
    try:
        owner = bot.get_user(bot.owner_id)
        await owner.send('Shark is online.')
    except:
        pass
    print('Shark is online.')
    return


if __name__ == '__main__':
    for file in os.listdir('cogs'):
        if file.endswith('.py') and not file.startswith('_'):
            bot.load_extension(f'cogs.{file[:-3]}')
    

bot.run(get_token())