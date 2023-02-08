import discord
import asyncio
from discord.ext import tasks, commands
from get_balance import *

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

    @commands.command(name="eth")
    async def Eth_info(self, ctx):
        
        """A simple command which showcases the use of embeds.
        Have a play around and visit the Visualizer."""

        info = eth_info()

        embed = discord.Embed(color=0x4e11c0)
        embed.set_author(name='CryptoNews',url='https://github.com/BBgamesTV/ETH-Info',icon_url='https://cdn.discordapp.com/avatars/741610011536654409/3b042d2a45230cfa891816f914d24d37.png?size=1024')
        embed.add_field(name="Valeur", value=f"""```ml
1 {info[1]} = {info[4]} € 
```""")
        embed.add_field(name="Performance 24H", value=f"""```ml
{info[5]} %
```""",inline=True)
        embed.add_field(name="Rang", value=f"""```ml
{info[1]} est #{info[3]} dans le classement des capitalisation boursière relative
```""",inline=False)
        embed.set_thumbnail(url=info[2])
        embed.set_footer(text='Par Petit Prince#3575', icon_url=info[2])

        await ctx.send(content=f'**{info[0]}**', embed=embed)

    @commands.command(name="balance")
    async def balance_info(self, ctx, adress):
        
        """A simple command which showcases the use of embeds.
        Have a play around and visit the Visualizer."""

        info = balance_eth(adress)

        embed = discord.Embed(title='Example Embed',description='Showcasing the use of Embeds...\nSee the visualizer for more info.',colour=0x4e11c0)
        embed.set_author(name='CryptoNews',url='https://github.com/BBgamesTV/ETH-Info',icon_url='https://cdn.discordapp.com/avatars/741610011536654409/3b042d2a45230cfa891816f914d24d37.png?size=1024')
        embed.add_field(name="Valeur", value=f"""```ml
1 {info} = {info} € 
```""")
        embed.add_field(name="Performance 24H", value=f"""```ml
{info} %
```""",inline=True)
        embed.add_field(name="Rang", value=f"""```ml
{info} est #{info} dans le classement des capitalisation boursière relative
```""",inline=False)
        embed.set_thumbnail(url=info)
        embed.set_footer(text='Par Petit Prince#3575', icon_url=info)

        await ctx.send(content=f'**{info}**', embed=embed)

class Auto_Embed_Info(commands.Cog):
    def __init__(self, bot):
        self.index = 0
        self.bot = bot
        self.embed_info.start()

    def cog_unload(self):
        self.embed_info.cancel()

    @tasks.loop(seconds=60.0)
    async def embed_info(self):
        print(self.index)
        self.index += 1
        channel = bot.get_channel(1071188822676738059)
        info = eth_info()
        embed = discord.Embed(color=0x4e11c0)
        embed.set_author(name='CryptoNews',url='https://github.com/BBgamesTV/ETH-Info',icon_url='https://cdn.discordapp.com/avatars/741610011536654409/3b042d2a45230cfa891816f914d24d37.png?size=1024')
        embed.add_field(name="Valeur", value=f"""```ml
1 {info[1]} = {info[4]} € 
```""")
        embed.add_field(name="Performance 24H", value=f"""```ml
{info[5]} %
```""",inline=True)
        embed.add_field(name="Rang", value=f"""```ml
{info[1]} est #{info[3]} dans le classement des capitalisation boursière relative
```""",inline=False)
        embed.set_thumbnail(url=info[2])
        embed.set_footer(text='Par Petit Prince#3575', icon_url=info[2])
        await channel.send(content=self.index,embed=embed)

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
    botactivity = discord.Activity(type=discord.ActivityType.competing,name="Sécuriser la blockchain🍀", large_image_url='https://www.kindpng.com/picc/m/290-2907032_court-quest-court-clipart-hd-png-download.png')
    await bot.change_presence(activity=botactivity, status=discord.Status.do_not_disturb)
    


async def main():
    async with bot:
        await bot.add_cog(Moderation(bot))
        await bot.add_cog(Crypto(bot))
        await bot.add_cog(Auto_Embed_Info(bot))
        await bot.start("NzQxNjEwMDExNTM2NjU0NDA5.GxAYO7.rF3MwBkXKmCqBp0gCIbFaePVdcSWwFUDn8S2BQ")

asyncio.run(main())