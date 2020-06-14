from functions import save, load

prefix = load('prefix')
bot = commands.Bot(prefix)

@bot.command()
async def ping(msg):
    await msg.send('pong')