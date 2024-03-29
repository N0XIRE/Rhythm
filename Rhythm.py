# Works with Python 3.6+
# THIS IS THE LIVE VERSION
import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
import json

with open('config.json', 'r') as f:
    config = json.load(f)

TOKEN = config['token']
client = commands.Bot(command_prefix="-")
startup_extensions = [""]
client.remove_command('help')

async def on_ready():
    pass

@client.event
async def on_ready():
    # sets Playing message on discord
    await client.change_presence(activity=Game(name="-help"))
    # prints succesful launch in console
    print('---\nLogged in as\nUser: ' + client.user.name + '\nID: ' + str(client.user.id) + '\n---')

# load commands
@client.command()
async def load(ctx, string):
    string = 'cogs.' + string
    try:
        client.load_extension(string)
        print('Loaded extension \"{}\"'.format(string))
        await ctx.message.channel.send('Loaded extension \"{}\"'.format(string))
    except Exception as e:
        exc = '{}: {}'.format(type(e).__name__, e)
        print('Failed to load extension \"{}\"\n{}'.format(string, exc))
        await ctx.message.channel.send('Failed to load extension \"{}\"'.format(string))

# unload commands
@client.command()
async def unload(ctx, string):
    string = 'cogs.' + string
    try:
        client.unload_extension(string)
        print('Unloaded extension \"{}\"'.format(string))
        await ctx.message.channel.send('Unloaded extension \"{}\"'.format(string))
    except Exception as e:
        exc = '{}: {}'.format(type(e).__name__, e)
        print('Failed to unload extension \"{}\"\n{}'.format(string, exc))

# reload commands
@client.command()
async def reload(ctx, string):
    string = 'cogs.' + string
    try:
        client.unload_extension(string)
        print('Unloaded extension \"{}\"'.format(string))
    except Exception as e:
        exc = '{}: {}'.format(type(e).__name__, e)
        print('Failed to unload extension \"{}\"\n{}'.format(string, exc))
    try:
        client.load_extension(string)
        print('Loaded extension \"{}\"'.format(string))
        await ctx.message.channel.send('Reloaded extension \"{}\"'.format(string))
    except Exception as e:
        exc = '{}: {}'.format(type(e).__name__, e)
        print('Failed to load extension \"{}\"\n{}'.format(string, exc))
        await ctx.message.channel.send('Failed to load extension \"{}\"'.format(string))

# IMPORT EXTENSIONS/COGS
if __name__ == "__main__":
    print('\n')
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
            print('Loaded extension \"{}\"'.format(extension))
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension \"{}\"\n{}'.format(extension, exc))
# DONE IMPORT EXTENSIONS/COGS

client.run(TOKEN)
