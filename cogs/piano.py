import discord
import asyncio
import json
import math
import wave
import array
import struct
from discord.ext import commands
from discord.ext.commands import Bot

class piano(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def play(self, ctx, duration=1.0, freq=440, channel: discord.VoiceChannel = None):
        if not discord.opus.is_loaded():
            discord.opus.load_opus('opus')
        if not channel:
            try:
                channel = ctx.author.voice.channel
            except:
                print('User not in voice channel')

        vc = ctx.voice_client

        if vc:
            pass
        else:
            vc = await channel.connect()
        vc = ctx.voice_client

        # duration = 3 # seconds
        # freq = 640 # of cycles per second (Hz) (frequency of the sine waves)
        volume = 100 # percent
        data = array.array('h') # signed short integer (-32768 to 32767) data
        sampleRate = 48000 # of samples per second (standard)
        numChan = 1 # of channels (1: mono, 2: stereo)
        dataSize = 2 # 2 bytes because of using signed short integers => bit depth = 16
        numSamplesPerCyc = int(sampleRate / freq)
        numSamples = int(sampleRate * duration)
        for i in range(numSamples):
            sample = 32767 * float(volume) / 100
            sample *= math.sin(math.pi * 2 * (i % numSamplesPerCyc) / numSamplesPerCyc)
            data.append(int(sample))
        f = wave.open('test.wav', 'w')
        f.setparams((numChan, dataSize, sampleRate, numSamples, "NONE", "Uncompressed"))
        f.writeframes(data.tostring())
        f.close()

        vc.play(discord.FFmpegPCMAudio('test.wav'))
        await ctx.message.channel.send('Playing NOTE')

def setup(client):
    client.add_cog(piano(client))
