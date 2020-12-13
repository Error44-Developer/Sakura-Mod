@bot.command()
async def unmute(ctx, member : discord.Member)
	guild = ctx.guild
	
	for role in guild.roles:
		if role.name == 'Muted':
			await member.remove_roles(role)
			await ctx.send('{} has been unmuted'.format(member.mention))
