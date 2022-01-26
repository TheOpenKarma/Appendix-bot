import discord
from discord.ext import commands

class DevCogCommands(commands.Cog, name='Developer Commands'):

  def __init__(self, bot):
    self.bot = bot

  async def cog_check(self, ctx):
    # ONLY the bot author ID (set in main.py) can run these commands!
    return ctx.message.author.id == self.bot.author_id
  
  @commands.command(name="channel_id")
  async def get_curr_channel_id(self, ctx, *args):
    await ctx.send(f'Current channel id: `{ctx.message.channel.id}`')

  @commands.command(name='reload', aliases=['rl'])
  async def reload(self, ctx, cog):
    '''
    Reloads a cog.
    '''
    extensions = self.bot.extensions  # A list of the bot's cogs/extensions.
    if cog == 'all':  # Lets you reload all cogs at once
      for extension in extensions:
        self.bot.unload_extension(cog)
        self.bot.load_extension(cog)
      await ctx.send('Done')
    if cog in extensions:
      self.bot.unload_extension(cog)  # Unloads the cog
      self.bot.load_extension(cog)  # Loads the cog
      await ctx.send('Done')  # Sends a message where content='Done'
    else:
      await ctx.send(f'Unknown cog `{cog}`')  # If the cog isn't found/loaded.
  
  @commands.command(name="unload", aliases=['ul']) 
  async def unload(self, ctx, cog):
    '''
    Unload a cog.
    '''
    extensions = self.bot.extensions
    if cog not in extensions:
      await ctx.send("Cog is not loaded!")
      return
    self.bot.unload_extension(cog)
    await ctx.send(f"`{cog}` has successfully been unloaded.")
  
  @commands.command(name="load")
  async def load(self, ctx, cog):
    '''
    Loads a cog.
    '''
    try:

      self.bot.load_extension(cog)
      await ctx.send(f"`{cog}` has successfully been loaded.")

    except commands.errors.ExtensionNotFound:
      await ctx.send(f"`{cog}` does not exist!")

  @commands.command(name="listcogs", aliases=['lc'])
  async def listcogs(self, ctx):
    '''
    Returns a list of all enabled cogs.
    '''
    base_string = "```css\n"  # Gives some styling to the list (on pc side)
    base_string += "\n".join([str(cog) for cog in self.bot.extensions])
    base_string += "\n```"
    await ctx.send(base_string)

  



# needed per cog: references class defined above
def setup(bot):  bot.add_cog(DevCogCommands(bot))