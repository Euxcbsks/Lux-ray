from basic_import import *
from basic_cmd_import import *

class Error(Inited_cog):
	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		if hasattr(ctx.command, 'on_error'):
			return
		
		error_type = str(type(error))[1:-1].split()[1][1:-1].split('.')[-1]
		message = load_lang(ctx.guild.id)['exception'][error_type]
		message = message.format(command_name = ctx.message.content.split('rl', 1)[1].split()[0])
														#argument_name = ctx.command.usage)
		
		if message != '':
			await ctx.send(message)
		else:
			await ctx.send(error_type)
			await ctx.send(error)

def setup(bot):
	bot.add_cog(Error(bot))