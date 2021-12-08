import discord
from discord import client
from discord.embeds import Embed
from discord.ext import commands
from random import randint
import requests
import aiohttp
from aiohttp import request
import random
import asyncio


class HelpCommand(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def help(self,ctx):
		try:
			embed = discord.Embed(title = 'HELP COMMANDS')
			embed.add_field(name = 'general', value = 'Click 'u"\u263A",inline = False)
			embed.add_field(name = 'nsfw', value = 'Click ' u"\u26D4" ,inline = False)
			embed.add_field(name = 'weeb', value = 'Click 'u"\U0001F47A", inline = False)

			embed.add_field(name = 'Music', value = 'Click 'u"\U0001F3B5", inline = False)
			embed.add_field(name = 'Moderation ||Only for admins and mods||', value = 'Click 'u"\U0001F6E0", inline = False)

			buttons = [u"\U0001F3E0" , u"\u263A", u"\u26D4", u"\U0001F47A",u"\U0001F3B5",u"\U0001F6E0", u"\U0001F5D1"]


			msg = await ctx.send(embed = embed)
			for button in buttons:
				await msg.add_reaction(button)
			while True:

				try:
					reaction , user = await self.bot.wait_for("reaction_add", check = lambda reaction,user: user == ctx.author and reaction.emoji in buttons and reaction.message.id == msg.id, timeout = 20)
				except asyncio.TimeoutError:


					embed.set_footer(text= "Timeout.")
					await msg.clear_reactions()

				else:
					if reaction.emoji == u"\U0001F3E0":
						embed = discord.Embed(title = 'HELP COMMANDS')
						embed.add_field(name = 'general', value = 'Click 'u"\u263A",inline = False)
						embed.add_field(name = 'nsfw', value = 'Click ' u"\u26D4" ,inline = False)
						embed.add_field(name = 'weeb', value = 'Click 'u"\U0001F47A", inline = False)

						embed.add_field(name = 'Music', value = 'Click 'u"\U0001F3B5", inline = False)
						embed.add_field(name = 'Moderation ||Only for admins and mods||', value = 'Click 'u"\U0001F6E0", inline = False)

						await msg.edit(embed = embed)

					elif reaction.emoji == u"\u263A":
						embed = discord.Embed(title = 'General Commands')
						embed.add_field(name = 'define', value = '`oi define <word_to_define>`', inline = True)
						embed.add_field(name = 'ping', value = '`oi ping`')
						embed.add_field(name = 'mean', value = '`oi mean <word_to_get_meaning>`')
						embed.add_field(name = 'gif', value = '`oi gif <word>`')
						embed.add_field(name = 'spam', value = '`oi spam <no of msg> <msg>`')
						embed.add_field(name = 'DM', value = '`oi DM <no of msg to send> <User> <msg>` **eg: oi DM 10 @hentai I lob hentai**')
						embed.add_field(name = 'book', value = '`oi book <book name>` **eg: oi book Alchemist**')
						embed.add_field(name = 'booru', value = '`oi booru <no> <search term>` **eg: oi booru 10 Doraemon**')
						embed.add_field(name = 'routine', value = 'Shows the routine from the source.')
						await msg.edit(embed = embed)


					elif reaction.emoji ==  u"\u26D4":
						embed = discord.Embed(title = 'NSFW commands', description = 'These Commands work only on NSFW channel')
						embed.add_field(name = 'shub (search_phub)', value = '`oi shub <digit upto 69> <search_term>` **Eg: oi shub 10 milf**')
						embed.add_field(name = 'rhub (random_phub)', value = '`oi rhub <digit upto 69> <random_word>`', inline = False)
						embed.add_field(name = '---------------------------------', value = 'Difference between shub and rhub is that shub scrapes phub using my script while rhub uses phub api', inline = False) 
						embed.add_field(name = 'doujin', value = '**oi doujin <random>/ <nuke_code_in_number> / <safe> / <spam>/ <search> <no_of_search> <search_term>**', inline = False)
						embed.add_field(name = '`Eg: oi doujin random || oi doujin 69420 || oi doujin safe || oi doujin spam || oi doujin search 10 milf`',value = '-', inline = True )

						embed.add_field(name = 'r34', value = '`oi r34 <no_of_image> <search_term>`', inline = False)
						await msg.edit(embed = embed)

					elif reaction.emoji == u"\U0001F47A":
						embed = discord.Embed(title = '**Weeb commands**', description = ' ')
						embed.add_field(name = '`These commands run differently on SFW channels and NSFW channels`', value = '*Its True*')
						embed.add_field(name = 'waifu', value = '**oi waifu <any of the following from sfw/nsfw>**', inline = False)
						embed.add_field(name ='SFW', value = '`waifu, neko, shinobu, megumin, bully, cuddle, cry, hug, awoo, kiss, lick, pat, smug, bonk, yeet, blush, smile, wave, highfive, handhold, nom, bite, glomp, slap, kill, kick, happy, wink, poke, dance, cringe`', inline = True)
						embed.add_field(name = 'NSFW', value = '`waifu, neko, trap, blowjob`', inline = True)

						embed.add_field(name = 'neko', value = '**oi neko <any of the following term from sfw/nsfw>**', inline = False)
						embed.add_field(name = 'SFW', value = '`neko, kitsune, hug, pat, waifu, cry, kiss, slap, smug, punch`', inline = True)
						embed.add_field(name = 'NSFW', value = '`lewd`', inline = True)

						embed.add_field(name = 'ewaifu', value = '**oi ewaiifu <any of the following term from sfw/nsfw>**', inline = False)
						embed.add_field(name = 'SFW', value = '`waifu, all, maid`', inline = True)
						embed.add_field(name = 'NSFW', value = '`ass, ecchi, ero, hentai, maid, milf, oppai, oral, paizuri, selfies, uniform`', inline = True)

						await msg.edit(embed = embed)


					elif reaction.emoji == u"\U0001F3B5":
						embed = discord.Embed(title = '**MUSIC COMMANDS**', description = ' ')
						embed.add_field(name = '`Finally added music commands`', value = '||PAIN||')

						embed.add_field(name = 'connect, join ,cum', value = 'Joins VC', inline = False)
						embed.add_field(name ='disconnect, leave', value = 'leaves VC', inline = False)

						embed.add_field(name = 'play , p', value = 'Plays Music', inline = False)
						embed.add_field(name = 'pause', value = 'Pauses Music', inline = False)
						embed.add_field(name = 'stop', value = 'Stops Music ', inline = False)

						embed.add_field(name = 'previous, back', value = 'Plays previous track', inline = False)
						embed.add_field(name = 'shuffle', value = 'shuffles the queue', inline = False)
						embed.add_field(name = 'repeat', value = 'repeats song')
						embed.add_field(name = 'queue', value = 'shows the queue')
						embed.add_field(name = 'volume', value = 'sets the volume from 0 to 100', inline = False)
						embed.add_field(name = 'up , down', value = 'Increases/decreases the volume by 10', inline = False)
						embed.add_field(name = 'lyrics', value = 'Gives lyrics of the song queried.(Experimental feature)', inline = False)
						embed.add_field(name = 'eq', value = 'sets eq to current song. Available options: flat, boost, metal, piano', inline = False)
						embed.add_field(name = 'adveq', value = 'Advanced equalizer. Available options to set: band and gain', inline = False)
						embed.add_field(name = 'playing, np, now', value = 'Shows the current song information', inline = False)
						embed.add_field(name = 'restart', value = 'Restarts the current song', inline = False)

						await msg.edit(embed = embed)
					elif reaction.emoji == u"\U0001F6E0":
						embed = discord.Embed(title = 'Simple Admin/Mod Commands.')
						embed.add_field(name = 'tempmute', value = 'Temporarily mutes', inline = False)
						embed.add_field(name = 'mute', value = 'Mutes', inline = False)
						embed.add_field(name = 'kick', value = 'kicks', inline = False)
						embed.add_field(name = 'tempban', value = 'temporarily bans', inline = False)
						embed.add_field(name = 'ban', value = 'bans', inline = False)
						embed.add_field(name = 'unban', value = 'Unbans', inline = False)
						await msg.edit(embed = embed)
					elif reaction.emoji ==  u"\U0001F5D1":
						await msg.delete()


					for button in buttons:
						await msg.remove_reaction(button, ctx.author)
		except:
			pass
def setup(bot):
	bot.add_cog(HelpCommand(bot))