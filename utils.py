import discord, time, jishaku, io, aiohttp, json
from discord.ext import commands
from cairosvg import svg2png

helpjson=json.loads(r'{"hex":{"syntax":"~hex {hex color}","description":"searches a hex color","permission":"everybody"},"char":{"syntax":"~char {character}","description":"searches a unicode character","permission":"everybody"},"help":{"syntax":"~help {command name}","description":"gives info on a command, if no command is given, it displays all commands","permission":"everybody"},"say":{"syntax":"~say {message}","description":"says a message then deletes the original message","permission":"bot owners"},"join":{"syntax":"~join","description":"tests join message","permission":"bot owners"},"leave":{"syntax":"~leave","description":"tests leave message","permission":"bot owners"},"whois":{"syntax":"~whois {user}","description":"displays info on a specified user","permission":"everyone"},"connectchan":{"syntax":"~connectchan {voice channel}","description":"connects to a specific voice channel","permission":"owners only"},"connect":{"syntax":"~connect","description":"connects to your current voice channel","permission":"everyone"},"disconnect":{"syntax":"~disconnect","description":"disconnects from current voice channel","permission":"everyone"},"owo":{"syntax":"~owo {message}","description":"owoifies a message","permission":"everyone"},"owosay":{"syntax":"~owosay {message}","description":"owofies message then deletes the original message","permission":"bot owners"},"ceasar":{"syntax":"~ceasar [step] {message}","description":"runs the message through the ceasar cipher with the given step, if no step is given, it defaults to 1","permission":"everyone"}}')
color=0xf8dfea

def ishex(s):
    try:
        int(s, 16)
        return True
    except ValueError:
        return False
def ename(d):
    if d['name']['exact_match_name']:
        return f"this color is {d['name']['value']}"
    else:
        return f"the closest named color is {d['name']['value']}({d['name']['closest_named_hex']}) with a distance of {d['name']['distance']}"
def percnt(n):
    if n==None:
        n=0
    if isinstance(n, str):
        n=eval(n)
    elif isinstance(n, (float, int)):
        pass
    else:
        n=eval(str(n))
    if n<1:
        n=str(round(n*100))
        return f"{n[0:2]}%"
    else:
        return "100%"
def invertHex(hexNumber):
    inverse = hex(abs(int(hexNumber, 16) - 255))[2:] 
    if len(inverse) == 1: 
        inverse = '0'+inverse
    return inverse
def colorInvert(hexCode):
    inverse = "" 
    if len(hexCode) == 6: 
        R = hexCode[:2]
        G = hexCode[2:4]
        B = hexCode[4:]
    else:
        return hexCode 
    inverse = inverse + invertHex(R)
    inverse = inverse + invertHex(G)
    inverse = inverse + invertHex(B)
    return inverse
def cap(s):
    s=s.lower()
    s=s.split(" ")
    o=[]
    for i in s:
        if i[0].isalpha():
            o.append(f"{i[0].upper()}{i[1:len(i)]}")
        else:
            o.append(i)
    return " ".join(o)
def tcap(s):
    s=s.lower()
    s=s.split(" ")
    o=[]
    ignore=["is","the","of","and","as","but","for","if","or","so","than","that","when","it","no","a","on","to"]
    count=0
    for i in s:
        if (i[0].isalpha() and not any("|"+word in f"|{i.lower()}" for word in ignore)) or (i[0].isalpha() and (count==0 or count==len(s)-1)):
            o.append(f"{i[0].upper()}{i[1:len(i)]}")
        else:
            o.append(i)
        count=count+1
    return " ".join(o)
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

class utils(commands.Cog):
    @commands.command(name="hex")
    async def h(self,ctx,*,arg):
        orig=arg
        if arg.startswith("#"):
            arg=arg[1:len(arg)]
        if len(arg)==3 and ishex(arg):
            arg=f"{arg[0]*2}{arg[1]*2}{arg[2]*2}"
        size=150
        if ishex(arg) and len(arg)==6:
            async with aiohttp.ClientSession() as session:
                picurl=f"http://www.singlecolorimage.com/get/{arg}/{size}x{size}"
                async with session.get(picurl) as resp:
                    if resp.status != 200:
                        return await ctx.send('Could not download file...')
                    pic=io.BytesIO(await resp.read())
                async with session.get(f"http://thecolorapi.com/id?hex={arg}&format=json") as resp:
                    if resp.status != 200:
                        return await ctx.send(f'Could not download file... {arg}')
                    dat=json.loads(await resp.read())
            e=discord.Embed(url=picurl,title=f"#{arg}",description=f"you gave me:\n*{orig}*",color=eval(f"0x{arg}"))
            e.set_image(url=picurl)
            e.set_thumbnail(url=f'attachment://{arg}.png')
            e.add_field(name='Name',value=ename(dat))
            e.add_field(name='RGB',value=f"red: {dat['rgb']['r']} ({percnt(dat['rgb']['fraction']['r'])})\ngreen: {dat['rgb']['g']} ({percnt(dat['rgb']['fraction']['g'])})\nblue: {dat['rgb']['b']} ({percnt(dat['rgb']['fraction']['b'])})")
            e.add_field(name='HSL',value=f"hue: {dat['hsl']['h']} ({percnt(dat['hsl']['fraction']['h'])})\nsaturation: {dat['hsl']['s']} ({percnt(dat['hsl']['fraction']['s'])})\nlightness: {dat['hsl']['l']} ({percnt(dat['hsl']['fraction']['l'])})")
            e.add_field(name='CMYK',value=f"cyan: {dat['cmyk']['c']} ({percnt(dat['cmyk']['fraction']['c'])})\nmagenta: {dat['cmyk']['m']} ({percnt(dat['cmyk']['fraction']['m'])})\nyellow: {dat['cmyk']['y']} ({percnt(dat['cmyk']['fraction']['y'])})\nblack: {dat['cmyk']['k']} ({percnt(dat['cmyk']['fraction']['k'])})")
            e.set_footer(text=f"inverted: #{colorInvert(arg)}",icon_url=f"http://www.singlecolorimage.com/get/{colorInvert(arg)}/50x50")
            await ctx.send(embed=e,file=discord.File(io.BytesIO(svg2png(url=f"http://www.thecolorapi.com/id?format=svg&hex={arg}")), f'{arg}.png'))
        else:
            await ctx.send(content="invalid __**hex**__ color")

    @commands.command(name="char")
    async def c(self,ctx,*,arg):
        m=await ctx.send(content="loading...")
        n=f"{ord(arg[0]):x}"
        async with aiohttp.ClientSession() as session:
            async with session.get(f"http://codepoints.net/api/v1/codepoint/{n}?property=na,cp") as resp:
                if resp.status != 200:
                    return await m.edit(content='Could not download file...')
                dat=json.loads(await resp.read())
        await m.edit(content=f">>> __**CHAR INFO**__\nname: `{dat['na']}`\ncodepoint: `{dat['cp']}`\npython escape: `\\U{n:>08}`\nHTML escape: `&#x{n}`\nsemi-universal escape: `\\x{n}`\nhttp://www.fileformat.info/info/unicode/char/{n}")

    @commands.command()
    async def help(self,ctx, arg=None):
        if arg==None:
            e=discord.Embed(title="Help Message",description=tcap("This Message Displays Info On All Of This Bot's Commands!"),color=color)
            for i in helpjson:
                e.add_field(name=i,value=f"{tcap(helpjson[str(i)]['description'])}\n`{helpjson[str(i)]['syntax']}`")
            e.set_thumbnail(url=ctx.bot.user.avatar_url)
            await ctx.send(embed=e)
        else:
            arg=arg.lower().replace("~","")
            if arg in helpjson:
                cm=helpjson[arg]
                e=discord.Embed(title=f"Help Message For {arg}",description=f"{tcap(cm['description'])}",color=color)
                for f in cm:
                    if f!='description' and f!='syntax':
                        e.add_field(name=cap(f),value=f"{cm[f]}")
                    elif f=='syntax':
                        e.add_field(name='How To Use',value=f"`{cm[f]}`")
                e.set_thumbnail(url=ctx.bot.user.avatar_url)
                await ctx.send(embed=e)
            else:
                await ctx.send(content="Command Not Found :(\nPlease do `~help` for a list of commands")

    @commands.command()
    async def whois(self,ctx, arg):
        arg=arg.replace("<@!","").replace(">","")
        usr=await ctx.bot.fetch_user(arg)
        e=discord.Embed(title="Member Info",description=f"@{usr.name}#{usr.discriminator} <{usr.id}>",color=color)
        e.set_thumbnail(url=usr.avatar_url)
        e.add_field(name="Created At",value=f"{date(str(usr.created_at))}")
        await ctx.send(embed=e)

def setup(bot):
    bot.add_cog(utils())