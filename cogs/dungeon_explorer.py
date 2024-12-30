from discord.ext import commands

class DungeonExplorer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='dungeon')
    async def dungeon(self, ctx):
        await ctx.send("Welcome to Dungeon Explorer! Embark on your journey.")

def setup(bot):
    bot.add_cog(DungeonExplorer(bot))
