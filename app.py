import discord
from discord.ext import commands
from functions import save, load

try:
    prefix = load('prefix')
except:
    prefix = command_prefix='!'
    save(prefix, 'prefix')

bot = commands.Bot(prefix)

@bot.command()
async def ping(msg):
    await msg.send('pong')

@bot.command()
async def calc(msg, a, calc, b):
    if calc == '+':
        await msg.send(float(a) + float(b))
    elif calc == '-':
        await msg.send(float(a) - float(b))
    elif calc == '**' or '^':
        await msg.send(float(a) ** float(b))
    elif calc == '*':
        await msg.send(float(a) * float(b))
    elif calc == '/':
        await msg.send(float(a) / float(b))
    else:
            await msg.send('error')

try:
    token = load('token')
except:
    token = input('Enter Token: ')
    save(token, 'token')

print('Shark is online.')

bot.run(token)