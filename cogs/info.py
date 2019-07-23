import discord
import asyncio
import json
import time
from discord.ext import commands
from discord.ext.commands import Bot

startTime = time.time()

with open('help.json', 'r') as f:
    help = json.load(f)


class info(commands.Cog):
    def __init__(self, client):
        self.client = client

    # help command
    @commands.command(aliases=['commands'])
    async def help(self, ctx, string=None):
        embed = discord.Embed(title="**Help: **", description="Command arguments are shown with `<int/string>` and are required.", color=0x589BFF)

        for category in help:
            categoryFormat = category.capitalize()
            embed.add_field(name=f"\u200b\n{categoryFormat}", value="_ _", inline=False)
            for command in help[category]:
                cmd = command['cmd']
                usage = command['usage']
                desc = command['desc']
                embed.add_field(name=f"`-{usage}` - {desc}", value="_ _", inline=False)

        message = await ctx.message.channel.send(embed=embed)

    # info command
    @commands.command(aliases=['information'])
    async def info(self, ctx):
        await ctx.message.delete()

        secs = (time.time() - startTime)
        days = secs//86400
        hours = (secs - days * 86400)//3600
        minutes = int(secs - days * 86400 - hours * 3600)//60
        seconds = int(secs - days * 86400 - hours * 3600 - minutes * 60)

        days = int(days)
        hours = int(hours)
        minutes = int(minutes)

        embed = discord.Embed(title="_ _", description="A piano bot.", color=0x589BFF)
        embed.set_author(name="Rhythm | Bot Information")
        embed.add_field(name="Uptime", value="{}d {}h {}m {}s".format(days, hours, minutes, seconds), inline=True)
        embed.add_field(name="Links", value="_ _")
        embed.set_footer(text="Made by N0XIRE#0001 & Sp3n#0054 | Python 3.6.6 & Discord.py", icon_url="")
        message = await ctx.message.channel.send(embed=embed)


def setup(client):
    client.add_cog(info(client))
