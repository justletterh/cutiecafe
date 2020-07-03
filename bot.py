import discord, jishaku
from discord.ext import commands
from time import sleep

hid=666317117154525185
did=676454199742955530
lid=701254727534510129
owners=[hid,did,lid]
status="— ୨୧ 𝐬𝐧𝐮𝐠𝐠𝐥𝐢𝐧’ 𝐭𝐡𝐞 𝐜𝐮𝐭𝐢𝐞 𝐩𝐢𝐞𝐬! ₓ˚. ୭ ˚○◦"
join="""\U00002601 . . . ⇢ ˗ˏˋ <@&689140834200846374> ࿐ྂ
 
**welcome sweetheart!! please verify to gain access to the rest of the server!** <:b_powheart:727644834265038918> <:b_teddy:727644836819107860> <:b_powheart:727644834265038918> 

<:b_wingies2:727644834806104124> **get some roles in** <a:b_arrow:727644833597882459> <#650563103699763240> 

<:b_wingies2:727644834806104124>  **make an intro in** <a:b_arrow:727644833597882459> <#650562789546655790> 

<:b_wingies2:727644834806104124> **read and react to the triggers and rules list** <a:b_arrow:727644833597882459> <#662158949239226388> + <#668220102482722821> 

<:b_wingies2:727644834806104124> **ping staff in** <a:b_arrow:727644833597882459> <#694558376029454386>

<a:b_butterflies:727644835023945778> — **and have loads of fun, $USER!**"""
leave= """<a:B4562AEA046F4DB6B1892479B9ADA72D:727644835023945778> — **oh no!! an angel named $USER left us :c god speed little angel. god speed.** <:5CD871E9E3E34685A9E579DA3BC0D982:727644834265038918>"""
welcomechan=650560380271067148
color=0xf8dfea
def isown(usr):
    if usr.id in owners:
        return True
    else:
        return False

bot = commands.Bot(command_prefix='~',owner_ids=owners)
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=status), status=discord.Status('online'))

@bot.event
async def on_member_join(member):
    with open('./app/join.gif', 'rb') as fp:
        await bot.get_channel(welcomechan).send(content=join.replace("$USER",member.mention),file=discord.File(fp,"join.gif"))
@bot.event
async def on_member_remove(member):
    with open('./app/leave.gif', 'rb') as fp:
        await bot.get_channel(welcomechan).send(content=leave.replace("$USER",f"@{member.name}#{member.discriminator}"),file=discord.File(fp,"leave.gif"))

@bot.event
async def on_message(message):
    if ("h " in message.content.lower() or "hh" in message.content.lower() or message.content.lower()=="h") and message.author.id==hid:
        await message.channel.send(content="h")
    await bot.process_commands(message)

@bot.command(name='join')
@commands.is_owner()
async def _join(ctx):
    with open('./app/join.gif', 'rb') as fp:
        await bot.get_channel(welcomechan).send(content=join.replace("$USER",ctx.author.mention),file=discord.File(fp,"join.gif"))
    await ctx.send(content="Done!")
@bot.command(name='leave')
@commands.is_owner()
async def _leave(ctx):
    with open('./app/leave.gif', 'rb') as fp:
       await bot.get_channel(welcomechan).send(content=leave.replace("$USER",f"@{ctx.author.name}#{ctx.author.discriminator}"),file=discord.File(fp,"leave.gif"))
    await ctx.send(content="Done!")
@bot.command(name='say')
@commands.is_owner()
async def _say(ctx, *, arg):
    await ctx.send(content=arg)
    await ctx.message.delete()
@bot.command()
@commands.is_owner()
async def tst(ctx):
	await ctx.send(content=join)
@bot.command(name='fetchmsg')
@commands.is_owner()
async def _msg(ctx, arg):
	arg=int(arg)
	m=await ctx.channel.fetch_message(arg)
	await ctx.send(content=f"\U00000060\U00000060\U00000060{m.content}\U00000060\U00000060\U00000060")

bot.load_extension('jishaku')
bot.load_extension("utils")
bot.load_extension("misc")
bot.load_extension("voice")
bot.run('BOT_TOKEN_HERE')