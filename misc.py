import discord, random
from discord.ext import commands

color=0xf8dfea

def isown(usr):
    hid=666317117154525185
    did=676454199742955530
    lid=701254727534510129
    owners=[hid,did,lid]
    if usr.id in owners:
        return True
    else:
        return False
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
    ignore=["is","the","of","and","as","but","for","if","or","so","than","that","when","it","no","a","on"]
    count=0
    for i in s:
        if (i[0].isalpha() and not any("|"+word in f"|{i.lower()}" for word in ignore)) or (i[0].isalpha() and (count==0 or count==len(s)-1)):
            o.append(f"{i[0].upper()}{i[1:len(i)]}")
        else:
            o.append(i)
        count=count+1
    return " ".join(o)
def owoify(owo):
    substitution = {'r': 'w', 'l': 'w', 'R': 'W', 'L': 'W', 'no': 'nu', 'has': 'haz', 'have': 'haz', 'you': 'uu', 'the': 'da', 'The': 'Da'}
    prefix = ['<3 ', 'H-hewwo?? ', 'HIIII! ', 'Haiiii! ', 'Huohhhh. ', 'OWO ', 'OwO ', 'UwU ', 'H-h-hi ']
    suffix = [' :3', ' UwU', ' ʕʘ‿ʘʔ', ' >_>', ' ^_^', '..', ' Huoh.', ' ^-^', ' ;_;', ' xD', ' x3', ' :D', ' :P', ' ;3', ' XDDD', ', fwendo', ' ㅇㅅㅇ', ' (人◕ω◕)', ' （＾ｖ＾）', ' Sigh.', ' ._.', ' >_<xD xD xD', ':D :D :D']
    for word, initial in substitution.items():
        owo = owo.replace(word.lower(), initial)
    output = random.choice(prefix) + owo + random.choice(suffix)
    return output
class A(list):
    def find(self, s):
        count=0
        for i in self:
            if i==s:
                return count
            else:
                count=count+1
class M(str):
    def explode(self):
        o=[]
        for char in self:
            o.append(char)
        return o
def ceasar(s, step=1):
    s=M(s).explode()
    alph=A(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
    o=[]
    for i in s:
        if i.isalpha():
            if i.isupper():
                i=alph.find(i.lower())+step
                if i>25:
                    i=i-26
                o.append(alph[i].upper())
            else:
                i=alph.find(i)+step
                if i>25:
                    i=i-26
                o.append(alph[i])
        else:
            o.append(i)
    return "".join(o)

class misc(commands.Cog):
    @commands.command(name="owo")
    async def _owo(self, ctx, *, arg):
        await ctx.send(content=f">>> {owoify(arg)}")

    @commands.command(name="owosay")
    @commands.is_owner()
    async def _owosay(self, ctx, *, arg):
        await ctx.send(content=f"{owoify(arg)}")
        await ctx.message.delete()

    @commands.command(name="ceasar")
    async def _ceasar(self, ctx, *, arg):
        if arg.split()[0].replace("-","").isnumeric():
            step=int(arg.split()[0])
            s=arg[len(str(step))+1:len(arg)]
            await ctx.send(content=ceasar(s,step))
        else:
            await ctx.send(content=ceasar(arg))

def setup(bot):
    bot.add_cog(misc())