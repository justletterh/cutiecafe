import discord, jishaku
from discord.ext import commands
from discord.ext.commands import has_permissions
from time import sleep

hid=666317117154525185
did=676454199742955530
status="— ୨୧ 𝐬𝐧𝐮𝐠𝐠𝐥𝐢𝐧’ 𝐭𝐡𝐞 𝐜𝐮𝐭𝐢𝐞 𝐩𝐢𝐞𝐬! ₓ˚. ୭ ˚○◦"
join="""<@&689140834200846374>
───────────────────
˗ˏˋ $USER has arrived to the cafe!! ♡ˎˊ˗

· · ─────── ·𖥸· ─────── · ·

❝ tips on how to verify !

♡ ⋮꒱ <#650562789546655790> : make an intro !

 ♡ ⋮꒱  <#650563103699763240> : get your roles ! 

♡ ⋮꒱  <#668220102482722821> + <#662158949239226388> : react to the rules n triggers list ! 

 ━ when you're all done, ping @​ ♡. staffies in <#694558376029454386>  ! 
· · ─────── ·𖥸· ─────── · · 
:cloud:  ʚ have fun cutie, and welcome to the cafe~ ɞ"""
leave= """
° 𐐪𐑂 ♡ 𐐪𐑂 ₒ 𐐪𐑂 ♡ 𐐪𐑂 °
**˚‧º·(˚ ˃̣̣̥⌓˂̣̣̥ )‧º·˚ — o nuu! $USER just left the server! we wish you well, cutie pie!
 ( ˘ ³˘)♡**
° 𐐪𐑂 ♡ 𐐪𐑂 ₒ 𐐪𐑂 ♡ 𐐪𐑂 °
https://gph.is/1n6h5lm
"""
welcomechan=650560380271067148
color=0xf8dfea

def date(s):
    months={'01':"January",'02':"Febuary",'03':"March",'04':"April",'05':"May",'06':"June",'07':"July",'08':"August",'09':"September",'10':"October",'11':"November",'12':"December"}
    s=s[0:len(s)-7]
    d=s.split()[0]
    d=d.split("-")
    d=f"on {months[str(d[1])]} {d[2]} of {d[0]}"
    t=s.split()[1]
    t=t.split(":")
    t=f" at {t[0]}:{t[1]} and {t[2]} seconds"
    return d+t

bot = commands.Bot(command_prefix='~',owner_ids=[hid,did])
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=status), status=discord.Status('online'))

@bot.event
async def on_member_join(member):
    await bot.get_channel(welcomechan).send(content=join.replace("$USER",member.mention))
@bot.event
async def on_member_remove(member):
    await bot.get_channel(welcomechan).send(content=leave.replace("$USER",f"@{member.name}#{member.discriminator}"))

@bot.command(name='join')
@commands.is_owner()
async def _join(ctx):
    if ctx.author.id == hid:
        await bot.get_channel(welcomechan).send(content=join.replace("$USER",ctx.author.mention))
        await ctx.send(content="Done!")
@bot.command(name='leave')
@commands.is_owner()
async def _leave(ctx):
    if ctx.author.id == hid:
        await bot.get_channel(welcomechan).send(content=leave.replace("$USER",f"@{ctx.author.name}#{ctx.author.discriminator}"))
        await ctx.send(content="Done!")
@bot.command(name='say')
@commands.is_owner()
async def _say(ctx, *, arg):
    await ctx.send(content=arg)
    await ctx.message.delete()

@bot.command()
async def whois(ctx, arg):
    usr=await bot.fetch_user(arg)
    e=discord.Embed(title="Member Info",description=f"@{usr.name}#{usr.discriminator} <{usr.id}>",color=color)
    e.set_thumbnail(url=usr.avatar_url)
    e.add_field(name="Created At",value=f"{date(str(usr.created_at))}")
    await ctx.send(embed=e)


bot.load_extension('jishaku')
bot.run('TOKEN_HERE')
