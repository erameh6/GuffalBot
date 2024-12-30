from discord.ext import commands

class Tap2Win(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='tap2win')
    async def tap2win(self, ctx):
        await ctx.send("Welcome to Tap2Win! Tap quickly to win.")

def setup(bot):
    bot.add_cog(Tap2Win(bot))
