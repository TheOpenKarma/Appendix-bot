import discord
import random
from discord.ext import commands

class MiscCogs(commands.Cog, name='Miscellaneous Commands'):
  '''These are miscellaneous commands.'''

  def __init__(self, bot):
    self.bot = bot
  


  @commands.command()
  async def ping(self, ctx):
    await ctx.send(f'hey {ctx.author.mention} stop that')
    # Just a simple command to test that the bot works

  @commands.command(pass_context=True)
  async def peek(self, ctx):
    await ctx.send("Whatcha doinnn <:gawrgurapeek:928161107221315595>")

  @commands.command()
  async def test(self, ctx):
        embed = discord.Embed(title="Will this work?", description="maybe it will work")
        await ctx.send(embed=embed)

  
  @commands.command()
  async def help(self, ctx):
        embed = discord.Embed(title=f'<:help:935724279453073429> Commands that currently work', description="and even then, they work like shit")
        embed.add_field(name="ping", value=f'<:ping:935724878735237190> More or less a test to see if the bot will respond')
        embed.add_field(name="rd", value=f'<:ques:935724223886942208> Random responses. Its very nice.', inline=False)
        await ctx.send(embed=embed)


  @commands.command()
  async def rd(self, ctx,):
        responses = ['fuck you',
                     'There is no reason why you shuold use this command',
                     'stfu, and go away',
                     'If you stop using this command, I will give you a treat',
                     'Leave me alone, I have a lot of work to do.',
                     'Is their something better you could be doing?',
                     'This does not benifit you, go away',
                     '<:stop:935727578004733982>',]
        await ctx.send(f'{ctx.author.mention} \n{random.choice(responses)}')

  
# needed per cog
def setup(bot):  bot.add_cog(MiscCogs(bot))