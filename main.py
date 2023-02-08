import discord
import asyncio
from discord.ext import tasks, commands
from get_balance import *

from datetime import datetime



class Moderation(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.command()
    async def ping(self,ctx):
        """Pong! + la latence du bot en ms"""
        await ctx.send('Pong!🏓 ' +str(format(round(bot.latency*100, 3))+' ms'))


    @commands.command(aliases= ['purge','delete'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self,ctx, amount :int = -1):
        """Nettoyes les messages d'un salon '<clear' | '<clear 5' """
        if amount == -1:
            await bot.change_presence(activity=discord.Streaming(name=(f'🧹je fais le ménage'), url='https://www.twitch.tv/bbgamestv'))
            await ctx.channel.purge(limit=100)
        else:
            await ctx.channel.purge(limit=amount+1)

class Crypto(commands.Cog):

    def __init__(self,bot):
        self.bot=bot

    @commands.command(name="balance")
    async def balance_info(self, ctx, adress):
        
        """Recupére les ETH d'une wallet ETH UNIQUEMENT"""
        
        info = balance_eth(adress)
        eth_price = eth_info()
        
        embed = discord.Embed(title=f"{adress}",description=f"""```
1 ETH = {eth_price[4]} €
```""",color=0x4e11c0)
        embed.set_author(name='CryptoBalance',url='https://github.com/BBgamesTV/ETH-Info',icon_url='https://cdn.discordapp.com/avatars/741610011536654409/3b042d2a45230cfa891816f914d24d37.png?size=1024')
        embed.add_field(name=f"Valeur en ETH", value=f"""```ml
{info} 
```""")
        if type(info) != str:
            embed.add_field(name=f"Valeur en EUR €", value=f"""```ml
{round(info*eth_price[4],3)} €  
```""")
        embed.set_footer(text=f'Par Petit Prince#3575')
        
        await ctx.send(content=None,embed=embed)    

class Auto_Embed_Info(commands.Cog):
    def __init__(self, bot):
        self.index = 0
        self.bot = bot
        self.embed_info.start()

    def cog_unload(self):
        self.embed_info.cancel()

    @tasks.loop(seconds=90.0)
    async def embed_info(self):
        date = datetime.now()
        dt_string = date.strftime("%d/%m/%Y %H:%M:%S")

        self.index += 1
        channel = bot.get_channel(1071188822676738059)
        info = eth_info()
        embed = discord.Embed(title=f"{info[1]} {info[0]}",color=0x4e11c0)
        embed.set_author(name='CryptoNews',url='https://github.com/BBgamesTV/ETH-Info',icon_url='https://cdn.discordapp.com/avatars/741610011536654409/3b042d2a45230cfa891816f914d24d37.png?size=1024')
        embed.add_field(name=f"Valeur de {info[0]}", value=f"""```ml
1 {info[1]} = {info[4]} € 
```""")
        embed.add_field(name="Performance 24H", value=f"""```ml
{info[5]} %
```""",inline=True)

        embed.add_field(name="Difference 24H", value=f"""```ml
Difference24h : {round(info[4]*(info[6]/100),2)}€\n1 {info[1]} valait {round(info[4]-round(info[4]*(info[6]/100),2),2)}€ h-24
```""",inline=False)

        embed.add_field(name="Rang", value=f"""```ml
{info[1]} est #{info[3]} dans le classement des capitalisation boursière
```""",inline=False)
        embed.set_thumbnail(url=info[2])
        embed.set_footer(text=f'Par Petit Prince#3575 | 📊{self.index} | {dt_string}', icon_url=info[2])
        await channel.send(content=None,embed=embed)
        print("📊 ",self.index," ",{info[0]}, {info[1]}," ",dt_string)

    @embed_info.before_loop
    async def before_embed_info(self):
        print('waiting...')
        await self.bot.wait_until_ready()



intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix=("<"),
    description='EthBot pour vous servir 👾',
    intents=intents,
)


@bot.event
async def on_ready():
    print(f'🍃 --> {bot.user} (ID: {bot.user.id})')
    print('---------')
    botactivity = discord.Activity(type=discord.ActivityType.watching,name="la blockchain🍀", large_image_url='https://www.kindpng.com/picc/m/290-2907032_court-quest-court-clipart-hd-png-download.png')
    await bot.change_presence(activity=botactivity, status=discord.Status.do_not_disturb)
    


async def main():
    async with bot:
        await bot.add_cog(Moderation(bot))
        await bot.add_cog(Crypto(bot))
        await bot.add_cog(Auto_Embed_Info(bot))
        await bot.start("NzQxNjEwMDExNTM2NjU0NDA5.GxAYO7.rF3MwBkXKmCqBp0gCIbFaePVdcSWwFUDn8S2BQ")

asyncio.run(main())