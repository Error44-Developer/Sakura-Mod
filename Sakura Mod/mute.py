@bot.command()
async def mute(ctx, member : discord.Member):
    guild = ctx.guild
    
    for role in guild.roles:
        if role.name == 'Muted':
            await member.add_roles(role)
            await ctx.send('{} has been muted'.format(member.mention))
            return
            
            overwrite = discord.PermissionsOverwrite(send_messages=False)
            newRole = await guild.create_role(name='Muted')
            
            for channel in guild.text_channels:
                await guild.set_permissions(newRole,overwrite=overwrite)
                
            await member.add_roles(newRole)
            await ctx.send('{} has been muted'.format(member.mention))
