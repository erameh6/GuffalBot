import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Add command files
bot.load_extension('cogs.trivia')
bot.load_extension('cogs.word_hunt')
bot.load_extension('cogs.dungeon_explorer')
bot.load_extension('cogs.tap2win')

bot.run('YOUR_BOT_TOKEN')  # Replace with your bot token
