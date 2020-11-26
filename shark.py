from discord.ext import commands
import discord
import os
import json

# predetermined functions
def clear():
    if os.name == "nt": 
        _ = os.system("cls") 
    else: 
        _ = os.system("clear")
def file(path_to_file, permission='r', data=None, indent=4):

    if permission == 'r':
        return json.load(open(path_to_file, 'r'))

    elif permission == 'w':
        return json.dump(data, open(path_to_file, 'w'), indent=indent)

clear()
print("\nShark.py Discord Bot by miten!\n")

# variables
bot_data = {
    "name": None,
    "token": None,
    "owner_id": None,
    "status": None,
    "activity": None
}
bot_file = "./data/bot.json"

server = {}

user = {}

# initialize setup


def config():
    global bot_data
    global bot_file

    try:
        bot_data = file(bot_file)
    except FileNotFoundError:
        pass

    if bot_data["name"] is None:
        bot_data["name"] = input("Enter Bot Name: ")

    if bot_data["token"] is None:
        bot_data["token"] = input("Enter Bot Token: ")

    if bot_data["owner_id"] is None:
        bot_data['owner_id'] = int(input("Enter Owner ID: "))

    if bot_data["status"] is None:
        bot_data["status"] = input("Enter Bot Status [online, idle, dnd]: ")

    if bot_data["activity"] is None:
        bot_data["activity"] = input("Enter Bot Activity (Playing...): ")

    print("Edit ./data/bot.json to change bot information.")

    file(bot_file, 'w', bot_data)

    return bot_data


async def get_prefix(bot, ctx):

    try:
        server = file("./data/" + str(ctx.guild.id) +
                      "/" + str(ctx.guild.name) + ".json")
        return server["prefix"]
    except:
        pass
    try:
        user = file("./data/" + str(ctx.user.id) +
                    "/" + str(ctx.user.name) + ".json")
        return user["prefix"]
    except:
        pass

    return '!'

bot = commands.Bot(command_prefix=get_prefix)


@bot.event
async def on_ready():
    global bot_data

    await bot.change_presence(status=bot_data["status"],
                              activity=discord.Game(bot_data["activity"]))

    bot.owner_id = bot_data["owner_id"]

    try:
        owner = await bot.fetch_user(bot.owner_id)
        await owner.send(f"{bot_data['name']} is {bot_data['status']}.")
    except:
        pass

    print(f"{bot_data['name']} is {bot_data['status']}.")

    return

if __name__ == "__main__":
    bot_data = config()

    for command_files in os.listdir('commands'):
        if command_files.endswith('.py') and not command_files.startswith('_'):
            bot.load_extension(f'commands.{command_files[:-3]}')

    bot.run(bot_data["token"])
