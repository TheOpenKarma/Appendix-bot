# QUICK SETTINGS

prefix = 'A!'

print("Starting server...\n")

import discord
from discord.ext import commands
from datetime import datetime
import os

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or(prefix),
    case_insensitive=True,

    # This will show up as "Watching &help"
    activity=discord.Activity(type=discord.ActivityType.watching,
                              name="use A!help for commands"),
    intents=discord.Intents.all())

# This is needed to remove discordpy's built in help command
bot.remove_command('help')

# This is needed for developer command ID checks (only you can run them); add your user ID here
bot.author_id = 885720186186006608


@bot.event
async def on_ready():
    # display loaded
    print("\nAPI loaded " + datetime.now().strftime('%d %b %Y %H:%M'),
          bot.user,
          "User ID " + str(bot.user.id),
          sep='\n  ')

@bot.event
async def on_message(message):
    mention = f'<@!{bot.user.id}>'
    if mention in message.content:
        await message.channel.send("Hello there!")

@bot.event
async def on_server_join(ctx):
    for guild in bot.guilds:
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).say:
                await ctx.message.channel.send('Hello! \n')
                break

# Fill with the path to all of your cogs (in `cogs` folder)
extensions = [
    'cogs.dev_cog_commands',

    'cogs.misc_cogs'
]

# Load and run bot
if __name__ == '__main__':
    for extension in extensions:
        bot.load_extension(extension)

from keep_alive import keep_alive

keep_alive()
bot.run(os.environ["DISCORD_API_TOKEN"])