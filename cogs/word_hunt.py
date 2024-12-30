from discord.ext import commands

class WordHunt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='wordhunt')
    async def wordhunt(self, ctx):
        await ctx.send("Welcome to Word Hunt! Find the hidden words.")

def setup(bot):
    bot.add_cog(WordHunt(bot))
