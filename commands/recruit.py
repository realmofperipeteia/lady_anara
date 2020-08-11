@client.command(aliases=['r'])
@commands.has_any_role('Honor Society🌟','Arcane Recovery💞','Praetorium Magi✨','Warriors Way💪','The Coalition💠','Jasmine Dragon 🌸')
async def recruit(ctx, member: discord.Member):
  if discord.utils.get(ctx.message.author.roles, name='Honor Society🌟'):
    guild_role=ctx.guild.get_role(716092569859260418)
    guild_msg='🌟 Honor Society 🌟'
    guild_logo='https://i.ibb.co/f8mM8TT/Guild-2.png'
  if discord.utils.get(ctx.message.author.roles, name='Arcane Recovery💞'):
    guild_role=ctx.guild.get_role(716089005011370086)
    guild_msg='💞 Arcane Recovery 💞'
    guild_logo='https://i.ibb.co/jrw717x/guild-ar.jpg'
  if discord.utils.get(ctx.message.author.roles, name='Praetorium Magi✨'):
    guild_role=ctx.guild.get_role(717228975201452055)
    guild_msg='✨ Praetorium Magi ✨'
    guild_logo='https://i.ibb.co/tcVZmKQ/guild-pm.png'
  if discord.utils.get(ctx.message.author.roles, name='Warriors Way💪'):
    guild_role=ctx.guild.get_role(719906048730988594)
    guild_msg='💪 Warriors Way 💪'
    guild_logo='https://i.ibb.co/gtnR91t/guild-ww.png'
  if discord.utils.get(ctx.message.author.roles, name='The Coalition💠'):
    guild_role=ctx.guild.get_role(739014983383515188)
    guild_msg='💠 The Coalition 💠'
    guild_logo='https://i.ibb.co/fvMhwyn/guild-tc.jpg'
  if discord.utils.get(ctx.message.author.roles, name='Jasmine Dragon 🌸'):
    guild_role=ctx.guild.get_role(742522974820892692)
    guild_msg='🌸 Jasmine Dragon 🌸'
    guild_logo='https://i.ibb.co/Xb80F4X/guild-jd.jpg'
  embed=discord.Embed(title='Guild membership offer', colour=discord.Colour.blue())
  embed.set_thumbnail(url=guild_logo)
  embed.add_field(name=guild_msg, value=f'**{ctx.message.author.display_name}** has offered **{member.display_name}** membership in their guild!')
  msg=await ctx.channel.send(embed = embed)
  await msg.add_reaction('✅')
  await msg.add_reaction('❎')
  r=discord.Reaction  
  def check(r, member):
    return member.id == ctx.author.id and r.message.channel.id == ctx.channel.id and \
      str(r.emoji) in ['✅', '❎']
  try:
    reaction, member = await client.wait_for('reaction_add', check = check, timeout = 120)
  except asyncio.TimeoutError:
    await ctx.send(f'Invite timed out.')
    return
  else:
    if str(reaction.emoji) == '✅':
        await member.add_roles(guild_role)
        return await ctx.channel.send(f'{member.display_name} has accepted the invite!')
    if str(reaction.emoji) == '❎':
        return await ctx.channel.send(f'{member.display_name} has rejected the invite.')
