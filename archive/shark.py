import discord
import os
import json
from discord.ext import commands

# variables
client = {
    "name": None,
    "token": None,
    "owner_id": None
}
guild = {}
user = {}


# initialize setup
def _client_():
    global client

    try:
        # load data from client.json
        read_client = open('./data/client.json', 'r')
        client = json.load(read_client)
        read_client.close()
    except: pass

    # open client.json with write permission
    write_client = open('./data/client.json', 'w')

    # if there is no name, input name
    if client['name'] is None:
        client['name'] = input('Enter Bot Name: ')

    # if there is no token, input token
    if client['token'] is None:
        client['token'] = input('Enter Bot Token: ')

    # if there is no owner_id, input owner_id
    if client['owner_id'] is None:
        client['owner_id'] = int(input('Enter Owner ID: '))

    # dump data to client.json
    json.dump(client, write_client, indent=4)
    write_client.close()

    return client

def json_load(file):
    return json.load(open(file, 'r'))

def json_dump(variable, file, indent=4):
    return json.dump(variable, open(file, 'w'), indent=indent)



# get prefix from data
async def get_prefix(bot, ctx):

    try: 
        guild = json_load('./data/guild.json')
        return guild[str(ctx.guild.id)]["prefix"]
    except: pass
    try: 
        user = json_load('./data/user.json')
        return user[str(ctx.guild.id)]["prefix"]
    except: pass

    return "!"

# define bot, assign prefix
bot = commands.Bot(command_prefix=get_prefix)


@bot.event
async def on_ready():
    # set status and activity of bot
    await bot.change_presence(status=discord.Status.idle,
                              activity=discord.Game('! | m1ten.me/sharkdev'))

    client = json_load('./data/client.json')
    bot.owner_id = client['owner_id']

    try: 
        await bot.get_user(bot.owner_id).send(client['name'] + ' is online.')
    except: pass

    print(client['name'] + ' is online.')

    return

if __name__ == '__main__':
    _client_()

    for command_files in os.listdir('commands'):
        if command_files.endswith('.py') and not command_files.startswith('_'):
            bot.load_extension(f'commands.{command_files[:-3]}')

bot.run(client['token'])