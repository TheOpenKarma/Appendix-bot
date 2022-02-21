import discord
from discord.ext import commands
import random

class GameCogCommands (commands.Cog, name='GamingCommands'):

  def __init__(self, bot):
    self.bot = bot


  @commands.command()
  async def game(self, ctx):
        embed = discord.Embed(title="Sadly, this isn't operational at the moment", description="But the developer of this bot is currently trying to implement this into the commands")
        embed.add_field(name="sorry for the inconvenience", value=f'{ctx.author.mention}')
        await ctx.send (embed=embed)

    


def setup(bot):  bot.add_cog(GameCogCommands(bot))