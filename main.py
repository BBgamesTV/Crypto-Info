import discord
import asyncio
from discord.ext import commands
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

    @commands.command()
    async def eth(self,ctx):
        """donnes les informations principales sur l'ETH"""
        embed=discord.Embed(title="Sample Embed", url="https://realdrewdata.medium.com/", description="This is an embed that will show how to build an embed and the different components", color=0x109319)
        embed.set_author(name="RealDrewData", url="https://twitter.com/RealDrewData", icon_url="https://pbs.twimg.com/profile_images/1327036716226646017/ZuaMDdtm_400x400.jpg")
        embed.set_thumbnail(url="https://i.imgur.com/axLm3p6.jpeg")
        embed.add_field(name="Field 1 Title", value="This is the value for field 1. This is NOT an inline field.", inline=False)
        embed.add_field(name="Field 2 Title", value="It is inline with Field 3", inline=True)
        embed.add_field(name="Field 3 Title", value="It is inline with Field 2", inline=True)
        embed.set_footer(text="This is the footer. It contains text at the bottom of the embed")
        ctx.author.display_name
        ctx.author.avatar_url
        await ctx.send(content=None,embed=embed)




intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix=("<"),
    description='Space Worker pour vous servir 👾',
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
        await bot.start("NzQxNjEwMDExNTM2NjU0NDA5.GxAYO7.rF3MwBkXKmCqBp0gCIbFaePVdcSWwFUDn8S2BQ")

asyncio.run(main())