from discord.ext import commands

class Trivia(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='trivia')
    async def trivia(self, ctx):
        await ctx.send("Welcome to Trivia! Let's start the game.")

def setup(bot):
    bot.add_cog(Trivia(bot))
