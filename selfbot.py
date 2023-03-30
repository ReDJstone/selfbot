import json
import os.path
import datetime
import random
import urllib.request
from aiohttp import connector
import shelve
import signal
import sys
import re
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='r!', description='ReDJBoT', help_command=None, self_bot=True)

@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Game(name="trolear. :3"))

@bot.event
async def on_message(ctx):
	if ctx.author.id != 983838625957560320:
		print(ctx.content)
		if ctx.author.id == 159985870458322944 and 'Felicidades' in ctx.content and ctx.channel.id == 945227455927566398:
			msg_content1 = re.sub('Felicidades ', '', ctx.content)
			msg_content2 = re.sub('ya eres nivel ', '', msg_content1)
			msg_content3 = re.sub(' sigue asi!', '', msg_content2)
			level_result = msg_content3.split(', ')[1]
			user_result = msg_content3.split(', ')[0]
			if True:
				await channel.send(f'FeLiCiDaDeS {user_result}, yA eReS nIvEl {level_result}, sIgUe AsI!')
				channel = bot.get_channel(945227455789142021)
				user1 = re.sub('<@', '', user_result)
				user2 = re.sub('>', '', user1)
				user = bot.get_user(user2)
				print ('└──── Level UP - {user.name}')

		elif 'r!test' in ctx.content.split(' ')[0] and ctx.author.id == 226408382448402433:
			channel = bot.get_channel(945227455789142021)
			await channel.send('test!')

		elif 'r!ping' in ctx.content.split(' ')[0]:
			print('{} - {} ({}) in {} -> {}'.format(datetime.datetime.now(), ctx.author.name, ctx.author.id, ctx.guild, 'Ping'))
			await ctx.send('Pong! {0}ms'.format(round(bot.latency*1000, 5)))

		elif 'r!mady' in ctx.content.split(' ')[0]:
			if len(ctx.content.split(' ')) != 1:
				await ctx.channel.send('FeLiCiDaDeS <@324520247782539264>, yA eReS nIvEl {}, sIgUe AsI!'.format(ctx.content.split(' ')[1]))
			else:
				await ctx.channel.send(f'FeLiCiDaDeS <@324520247782539264>, hAs SuBiDo De NiVeL!')

dict = eval(open('tokens.txt', 'r').read())
bot.run(dict['redbot'])




'''
	if not ctx.guild:
		await ctx.channel.send('Anda! No esperaba que nadie me mandara un mensaje privado! Gracias! Toma una galleta! :cookie:')
		user = await bot.fetch_user('226408382448402433')
		await user.send('DM from <@{}>: {} // Response: {}'.format(ctx.author, ctx.content, msg))
		return
	elif ctx.author.id == 159985870458322944 and 'Felicidades <@324520247782539264>' in ctx.content and ctx.channel.id == 945227455927566398:
		channel = await bot.get_channel(945227455789142021)
		msg_content1 = re.sub('Felicidades <@324520247782539264>, ya eres nivel ', '', ctx.content)
		level_result = re.sub(' sigue asi!', '', msg_content1)
		channel.send('FeLiCiDaDeS <@324520247782539264>, yA eReS nIvEl {level_result}, sIgUe AsI!')
		return
''' 
'''@bot.command()
async def ping(ctx):
	print('{} - {} ({}) in {} -> {}'.format(datetime.datetime.now(), ctx.author.name, ctx.author.id, ctx.guild, 'Ping'))
	await ctx.send('Pong! {0}ms'.format(round(bot.latency*1000, 5)))

@bot.command()
async def test(ctx):
	return

@bot.command()
async def mady(ctx, arg1=None):
	if arg1:
		ctx.channel.send(f'FeLiCiDaDeS <@324520247782539264>, yA eReS nIvEl {arg1}, sIgUe AsI!')
	else:
		ctx.channel.send(f'FeLiCiDaDeS <@324520247782539264>, hAs SuBiDo De NiVeL!')
'''

















"""
PMS CODE BACKUP

		elif ctx.author.id == 324520247782539264: #Mady
			line_cnt = int(sum(1 for line in open("{}/comandos/mady.txt".format(os.path.dirname(__file__)))))
			rng = random.randint(0, line_cnt-1)
			ReD = await bot.fetch_user('226408382448402433')
			try:
				msg = str(open("{}/comandos/mady.txt".format(os.path.dirname(__file__))).readlines()[rng])
				await ctx.channel.send(msg)
			except IndexError:
				await ReD.send('{}, DMs: {} // IndexError, rng: {}, line_cnt: {}'.format(ctx.author, ctx.content, rng, line_cnt))
				return
			await ReD.send('DM from <@{}>: {} // Response: {}'.format(ctx.author.id, ctx.content, msg))

		elif ctx.author.id == 617078466621341918: #Valy
			line_cnt = int(sum(1 for line in open("{}/comandos/valy.txt".format(os.path.dirname(__file__)))))
			rng = random.randint(0, line_cnt-1)
			ReD = await bot.fetch_user('226408382448402433')
			try:
				msg = str(open("{}/comandos/valy.txt".format(os.path.dirname(__file__))).readlines()[rng])
				await ctx.channel.send(msg)
			except IndexError:
				await ReD.send('{}, DMs: {} // IndexError, rng: {}, line_cnt: {}'.format(ctx.author, ctx.content, rng, line_cnt))
				return
			await ReD.send('DM from <@{}>: {} // Response: {}'.format(ctx.author.id, ctx.content, msg))

		elif ctx.author.id == 622902841568264262: #Ema
			line_cnt = int(sum(1 for line in open("{}/comandos/ema.txt".format(os.path.dirname(__file__)))))
			rng = random.randint(0, line_cnt-1)
			ReD = await bot.fetch_user('226408382448402433')
			try:
				msg = str(open("{}/comandos/ema.txt".format(os.path.dirname(__file__))).readlines()[rng])
				await ctx.channel.send(msg)
			except IndexError:
				await ReD.send('{}, DMs: {} // IndexError, rng: {}, line_cnt: {}'.format(ctx.author, ctx.content, rng, line_cnt))
				return
			await ReD.send('DM from <@{}>: {} // Response: {}'.format(ctx.author.id, ctx.content, msg))

		elif ctx.author.id != 471738412102189057:
			await ctx.channel.send('Anda! No esperaba que nadie me mandara un mensaje privado! Gracias! Toma una galleta! :cookie:')
			user = await bot.fetch_user('226408382448402433')
			await user.send('DM from <@{}>: {} // Response: {}'.format(ctx.author, ctx.content, msg))
	else:
		if '<@!471738412102189057>' in ctx.content and ctx.author != bot.user and 'r!' not in ctx.content:
			line_cnt = int(sum(1 for line in open("{}/comandos/mention.txt".format(os.path.dirname(__file__))))-1)
			rng = random.randint(0, line_cnt)
			await ctx.channel.send(str(open("{}/comandos/mention.txt".format(os.path.dirname(__file__))).readlines()[rng]))
"""





"""
BOT COMMANDS BACKUP

@bot.command()
async def clear(ctx):
	async for message in ctx.channel.history():
		if message.author == bot.user:
			await message.delete()

@bot.command()
async def ip(ctx):
	ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
	await ctx.channel.send('{}'.format(ip), delete_after=10)
	print(f"Current IP Address: {ip}")

@bot.command()
def  help(ctx):
	print('{} - {} ({}) in {} -> {}'.format(datetime.datetime.now(), ctx.author.name, ctx.author.id, ctx.guild, 'Help'))
	des = "
	Mi prefix es r! , y mis comandos:\n
	> help: Acabas de usarlo... :P\n
	> ping: Respuesta para testear.\n
	> momentazo: Muestra un momento guardado!\n
	> insulta: A quién hay que matar? >:(\n
	Hecho en Python!\n
	"
	embed = discord.Embed(title="Soy ReDJBoT!",url="https://cdn.discordapp.com/avatars/809827305295314967/babea11271bbf5a89d5bf15220e7c278.webp?size=1024",description= des,
	timestamp = datetime.datetime.now(),
	color = discord.Color.red())
	embed.set_footer(text = "Solicitado por: {}".format(ctx.author.name))
	embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)

	await ctx.send(embed = embed)

@bot.command()
async def momentazo(ctx, arg1=None):
	print('{} - {} ({}) in {} -> {}'.format(datetime.datetime.now(), ctx.author.name, ctx.author.id, ctx.guild, 'Momentazo'))
	tit = ''
	des = ''
	endnum = 0
	line_cnt = int(sum(1 for line in open("{}/comandos/momentazos.txt".format(os.path.dirname(__file__))))/2-1)
	if not arg1:
		rng = random.randint(0, line_cnt)
		tit = 'Momentazo {}:'.format(rng+1)
		des = str(open("{}/comandos/momentazos.txt".format(os.path.dirname(__file__))).readlines()[rng*2])
		if open("{}/comandos/momentazos.txt".format(os.path.dirname(__file__))).readlines()[rng*2+1] != '\n':
			endnum = rng*2+1
	else:
		moment = 0
		derp = 0
		try:
			moment = int(arg1)
		except:
			derp = 1
			tit = 'Pero- (?)'
			des = 'Pa qué cojones querrías poner algo distinto a números aquí?? >:('

		if derp == 0:
			if moment == 0 or moment < 0:
				tit = 'Vaaya...'
				des = 'Poniendo números negativos (o 0). Mmmmhm. Muy original. ¬¬'
			elif moment > line_cnt+1:
				tit = 'Uh! Se te fue! :D'
				des = 'No tengo tantos momentazos! ...... Todavía! ;)'
			else:
				tit = 'Momentazo {}:'.format(arg1)
				des = str(open("{}/comandos/momentazos.txt".format(os.path.dirname(__file__))).readlines()[moment*2-2])
				if open("{}/comandos/momentazos.txt".format(os.path.dirname(__file__))).readlines()[moment*2-1] != '\n':
					endnum = moment*2-1

	embed = discord.Embed(title=tit,
						  description=des,
						  timestamp=datetime.datetime.now(),
						  color=discord.Color.red())
	if endnum != 0:
		embed.set_image(url=open("{}/comandos/momentazos.txt".format(os.path.dirname(__file__))).readlines()[endnum])
	embed.set_footer(text="Solicitado por: {}".format(ctx.author.name))
	embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)

	await ctx.send(embed = embed)

@bot.command()
async def insulta(ctx, arg1=None):

	print('{} - {} ({}) in {} -> {}'.format(datetime.datetime.now(), ctx.author.name, ctx.author.id, ctx.guild, 'Insulto'))

	mention = f'<@!{bot.user.id}>'
	if arg1 == mention:
		await ctx.channel.send('No voy a insultarme a mí mismo porque tú quieras, <@{}>!'.format(ctx.author.id))
	elif arg1:
	   target = arg1
	else:
	   target = '<@{}>'.format(ctx.author.id)

	line_cnt = int(sum(1 for line in open("{}/comandos/insultos.txt".format(os.path.dirname(__file__))))-1)
	rng = random.randint(0, line_cnt)
	frase = str(open("{}/comandos/insultos.txt".format(os.path.dirname(__file__))).readlines()[rng])
	await ctx.channel.send('{}, {}'.format(target, frase))
"""
