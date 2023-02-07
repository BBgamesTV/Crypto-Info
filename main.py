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

    @commands.command(name="embeds")
    async def example_embed(self, ctx):
        """A simple command which showcases the use of embeds.
        Have a play around and visit the Visualizer."""

        embed = discord.Embed(title='Example Embed',
                              description='Showcasing the use of Embeds...\nSee the visualizer for more info.',
                              colour=0x98FB98)
        embed.set_author(name='MysterialPy',
                         url='https://gist.github.com/MysterialPy/public',
                         icon_url='http://i.imgur.com/ko5A30P.png')
        embed.set_image(url='https://cdn.discordapp.com/attachments/84319995256905728/252292324967710721/embed.png')

        embed.add_field(name='Embed Visualizer', value='[Click Here!](https://leovoel.github.io/embed-visualizer/)')
        embed.add_field(name='Command Invoker', value=ctx.author.mention)
        embed.set_footer(text='Made in Python with discord.py@rewrite', icon_url='http://i.imgur.com/5BFecvA.png')

        await ctx.send(content='**A simple Embed for discord.py@rewrite in cogs.**', embed=embed)




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