import discord
import random
from discord.ext import commands


class MiscCogs(commands.Cog, name='Miscellaneous Commands'):
  '''These are miscellaneous commands.'''

  def __init__(self, bot):
    self.bot = bot
  



  @commands.command()
  async def ping (self, ctx):
    await ctx.send ("Thank you, now go away")
    # Just a simple command to test that the bot works


  
  @commands.command()
  async def help(self, ctx):
        embed = discord.Embed(title=f'<:help:935724279453073429> Commands that currently work', description="and even then, they work like shit",)
        embed.add_field(name="ping", value=f'<:ping:935724878735237190> More or less a test to see if the bot will respond')
        embed.add_field(name="rd", value=f'<:ques:935724223886942208> Random responses. Its very nice.', inline=False)
        embed.add_field(name="gif", value=f'<:g_:936080191757881353> Random gif response', inline=False)
        embed.add_field(name="game", value=f'<:game:943327288496357427> Games for your enjoyment', inline=False)
        await ctx.send (embed=embed)

  @commands.command()
  async def rd(self, ctx,):
        responses = ['fuck you',
                     'There is no reason why you should use this command',
                     'stfu, and go away',
                     'If you stop using this command, I will give you a treat',
                     'Leave me alone, I have a lot of work to do.',
                     'Is their something better you could be doing?',
                     'This does not benifit you, go away',
                     '<:stop:935727578004733982>',
                     '||bitch||']
        await ctx.send(f'{ctx.author.mention} \n{random.choice(responses)}')

  @commands.command()
  async def gif(self, ctx):
        responses = ['https://tenor.com/view/anime-hug-sweet-love-gif-14246498',
                     'https://tenor.com/view/girl-anime-kiss-anime-i-love-you-girl-kiss-gif-14375355',
                     'https://tenor.com/view/anime-kiss-love-sweet-gif-5095865',
                     'https://tenor.com/view/anime-acchi-kocchi-anime-couple-neko-anime-rain-gif-16085531',
                     'https://tenor.com/view/hug-anime-clingy-gif-7552075']
        await ctx.send(f'{ctx.author.mention} \n{random.choice(responses)}')
  
  @commands.command()
  async def woah(self, ctx):
        responses = ['https://cdn.donmai.us/original/e0/21/e02163927540bb64eba55303515a0cf6.gif',
                     'https://cdn.donmai.us/original/7c/01/7c01c09f34d52a86aa01ee663b5e1b7d.mp4',
                     'https://cdn.donmai.us/original/01/d6/01d69929301fdc08dacefc7a7fe748b7.gif',
                     'https://cdn.donmai.us/original/40/7a/407aaac820a8b461912f636f364c53de.gif',
                     'https://cdn.donmai.us/original/30/7f/307fa8860c094d1a9927f6da6e398bc3.mp4']
        await ctx.send(f'{ctx.author.mention} \n{random.choice(responses)}')

  



  

# needed per cog
def setup(bot):  bot.add_cog(MiscCogs(bot))