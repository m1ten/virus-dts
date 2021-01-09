from discord.ext import commands
import discord, os, json

# Variables 

data = {
    "name": None,
    "token": None,
    "owner_id": None,
    "status": None,
    "activity": None
}
path = "./data/bot.json"
server = {}
user = {}

# Defined Functions

def clear():
    if os.name == "nt": 
        _ = os.system("cls") 
    else: 
        _ = os.system("clear")

def file(path_to_file, permission='r', data="ALL PREVIOUS DATA WILL BE ERASED", indent=4):

    if permission == 'r':
        return json.load(open(path_to_file, 'r'))

    elif permission == 'w':
        return json.dump(data, open(path_to_file, 'w'), indent=indent)

    else: return

def config(data, path_to_file):

    try:
        data = file(path_to_file)
    except FileNotFoundError:
        pass

    for i in data:
        if data[i] == None:
            data[i] = input(f"Enter {i}: ")
            print(f"{i} = {data[i]}")

    print("Edit ./data/bot.json to change bot information.")

    file(path_to_file, 'w', data)

    return data

async def get_prefix(bot, ctx):
    if ctx.guild.id:
        server = file("./data/" + str(ctx.guild.id) +
                      "/" + str(ctx.guild.name) + ".json")
        return server["prefix"]
    elif ctx.user.id:
        user = file("./data/" + str(ctx.user.id) +
                    "/" + str(ctx.user.name) + ".json")
        return user["prefix"]
    else: return '!'

bot = commands.Bot(command_prefix=get_prefix)

if __name__ == "__main__":
    data = config(data, path)