from discord.ext.commands import group
from discord.ext.commands.core import has_guild_permissions

from core import InitedCog

from .core import ExclCatServer


class ExclCat(InitedCog):
	@group()
	async def excl_cat(self, ctx):
		pass
	
	@excl_cat.command()
	async def request(self, ctx):
		await ctx.send("WIP command")
	
	@excl_cat.command()
	@has_guild_permissions(administrator=True)
	async def register(self, ctx, category_id, member_id):
		ExclCatServer(ctx).register_category(category_id, int(member_id))

def setup(bot):
	bot.add_cog(ExclCat(bot))
