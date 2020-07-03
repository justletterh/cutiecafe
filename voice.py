import discord
from discord.ext import commands

hid=666317117154525185
did=676454199742955530
lid=701254727534510129
owners=[hid,did,lid]
def isown(usr):
    if usr.id in owners:
        return True
    else:
        return False

class voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.is_owner()
    async def connectchan(self, ctx, *, channel: discord.VoiceChannel=None):
        if channel==None:
            await ctx.send(content="Please specify a voice channel for me to join :(")
        if ctx.voice_client is not None:
            await ctx.voice_client.disconnect()
        await channel.connect()
        await ctx.send(content="Done!!!")

    @commands.command()
    async def connect(self, ctx):
        if ctx.author.voice != None:
            channel=ctx.author.voice.channel
        else:
            await ctx.send(content="You aren't in a voice channel :(")
            return
        if ctx.voice_client is not None:
            await ctx.voice_client.disconnect()
        await channel.connect()
        await ctx.send(content="Done!!!")

    @commands.command()
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()
        await ctx.send(content="Done!!!")

def setup(bot):
    bot.add_cog(voice(bot))