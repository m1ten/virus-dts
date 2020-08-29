import discord
import os
import json
from discord.ext import commands

# variables
bot = {
    "name": "shark",
    "token": None,
    "owner_id": None
}
guild = {}
user = {}


# initialize setup
def _bot_():
    global bot

    # load data from bot.json
    read_bot = open('./data/bot.json', 'r')
    bot = json.load(read_bot)
    read_bot.close()

    # open bot.json with write permission
    write_bot = open('./data/bot.json', 'w')

    # if there is no token, input token
    if bot['token'] is None:
        data['token'] = input('Enter Bot Token: ')

    # if there is no owner_id, input owner_id
    if bot['owner_id'] is None:
        data['owner_id'] = int(input('Enter Owner ID: '))

    # dump data to bot.json
    json.dump(bot, write_bot, indent=4)
    write_bot.close()

    return bot

def json_load(file):
    return json.load(open(file, 'r'))

def json_dump(variable, file, indent=4):
    return json.dump(variable, open(file, 'w'), indent=indent)



# get prefix from data
async def get_prefix(bot, ctx):
    guild = json_load('./data/guild.json')
    user = json_load('./data/user.json')

    try: return guild[str(ctx.guild.id)]["prefix"]
    
    try: return user[str(ctx.guild.id)]["prefix"]

    return "!"

# define bot, assign prefix
client = commands.Bot(command_prefix=get_prefix)


@bot.event
async def on_ready(client):
    # set status and activity of bot
    await client.change_presence(status=discord.Status.idle,
                              activity=discord.Game('! | m1ten.me/sharkdev'))

    shark = json_load('./data/bot.json')
    client.owner_id = shark['owner_id']

    try: await client.get_user(bot.owner_id).send('Shark is online.')

    print(f'{bot.name} is online.')

    return

if __name__ == '__main__':
    _bot_()

    for command_files in os.listdir('commands'):
        if command_files.endswith('.py') and not command_files.startswith('_'):
            client.load_extension(f'commands.{command_files[:-3]}')

client.run(bot['token'])
