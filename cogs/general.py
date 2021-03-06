import discord
from discord import client
from discord.embeds import Embed
from discord.ext import commands
from random import randint
import requests
import aiohttp
from aiohttp import request
import giphy_client
from giphy_client.rest import ApiException
import wikipedia
from bs4 import BeautifulSoup
from pornhub_api import PornhubApi
import random
import asyncio
from requests import request
import lxml

class Command(commands.Cog):
	def __init__(self, bot):
		self.bot = bot


	@commands.command()
	async def ping(self,ctx):
	    await ctx.send(f'Your ping is {self.bot.latency * 1000} ms')


	@commands.command()
	async def spam(self,ctx, amount: int, *, message):
	    for i in range(amount):
	        if amount >= 69:
	            await ctx.send("69 is the limit ")

	            break
	        else:
	            await ctx.send(message)
	        pass

	@commands.command()
	async def DM(self,ctx, amount: int, user: discord.User, *, message=None):
	    if message == None:
	        await ctx.send('At least put a Message.')
	    else:
	        if amount <= 69:

	          for i in range(amount):
	              await user.send(message)
	          await ctx.channel.purge(limit=1)
	          await ctx.author.send("Done")
	        else:
	          await ctx.channel.send('69 is the limit')

	@commands.command()
	async def purge(self,ctx, amount: int):
	    await ctx.channel.purge(limit=amount+1)


	@commands.command()
	async def define(self,ctx, *,word):
	    try:
	      search = wikipedia.summary(
	          word, sentences=5, chars=2000, auto_suggest=True, redirect=True)
	      msg = discord.Embed(title='Here, I found this.',
	                          description=search, colour=discord.Colour.gold())

	      await ctx.channel.send(content=None, embed=msg)
	    except:
	      embed = discord.Embed(title = "No exact Match")
	      await ctx.send(embed = embed)
	
	@commands.command()
	async def gif(self,ctx, *, search):
	    api_key = "YourAPIKEY"
	    embed = discord.Embed(title=f"Requested by {ctx.author}")
	    async with aiohttp.ClientSession() as session:
	        # search
	        if search:
	            embed.description = search
	            async with session.get(f'http://api.giphy.com/v1/gifs/search?q={search}&api_key={api_key}&limit=10') as response:
	                data = await response.json()
	                gif_choice = random.randint(0, 9)
	                embed.set_image(
	                    url=data['data'][gif_choice]['images']['original']['url'])
	                await session.close()
	        
	        else:
	            async with session.get(f'http://api.giphy.com/v1/gifs/random?api_key={api_key}&limit=10') as response:
	                data = await response.json()
	                embed.set_image(url=data['data']['images']['original']['url'])
	                await session.close()
	    await ctx.send(embed=embed)



	app_id = "YourAppID"
	app_key = "YourAppKey"
	language_code = "en-us"
	endpoint = "entries"


	@commands.command()
	async def mean(self,ctx, *, word):

	    response = requests.get(
	        f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
	    if response.status_code == 404:
	        await ctx.send("No such word")
	        return
	    else:
	        wordx = response.json()
	        the_dictionary = wordx[0]

	        phonetics = the_dictionary['phonetics']
	        texts = phonetics[0]
	        text = texts['text']

	        meanings = the_dictionary['meanings']
	        definitions = meanings[0]
	        definition = definitions['definitions']

	        meaningg = definition[0]
	        meaning = meaningg['definition']

	        example = meaningg.get('example', ['None'])
	        synonymslist = meaningg.get("synonyms", ['None'])

	        synonyms = ','.join(synonymslist)
	        deffinal = discord.Embed(title=f"`{word.upper()}`")
	        deffinal.add_field(name="Definition", value=f"{meaning} \n")
	        deffinal.add_field(name='Example', value=f"{example} \n")
	        deffinal.add_field(name='Phonetic', value=f"{text}")

	        if synonyms:
	            deffinal.add_field(name="Synonyms", value=synonyms)
	            

	        await ctx.channel.send(embed=deffinal)

	@commands.command()
	async def booru(self,ctx, no:int,*,query:str):
		try:
			image_links = []
			if no < 35:
				for i in range(0, no):
					URL = f'https://safebooru.org/index.php?page=post&s=list&tags={query}'
					base_url = 'https://safebooru.org/'
					r = requests.get(URL)
					soup = BeautifulSoup(r.text, 'lxml')

					data = soup.find_all('span', class_ = 'thumb')
					pre_url = str(data[i]).split('<a')[1].split('"')[1]
					img_url = (base_url + pre_url).replace('amp;', '')
					img_request = requests.get(img_url)
					img_soup = BeautifulSoup(img_request.text, 'lxml')
					pre_img = img_soup.find_all('img', id = 'image')
					for image in pre_img:
						k = image_links.append(image['src'])

			buttons = [ u"\u25C0", u"\u25FC" , u"\u25B6" , u"\U0001F5D1"]
			current = 0
			embed = discord.Embed(Title = "SafeBooru")
			embed.set_image(url = image_links[current])
	        
	      
			msg = await ctx.send(embed = embed)

			for button in buttons:
				await msg.add_reaction(button)
			while True:

				try:
					reaction , user = await self.bot.wait_for("reaction_add", check = lambda reaction,user: user == ctx.author and reaction.emoji in buttons and reaction.message.id == msg.id, timeout = 60.0)
				except asyncio.TimeoutError:

					embed.set_footer(text= "Timeout.")
					await msg.clear_reactions()
	          
				else:
					previous_page = current
					if reaction.emoji == u"\u25C0" :
						current -= 1
						embed.set_image(url =f"{image_links[current]}")
						await ctx.send(embed = Embed)
	              
					elif reaction.emoji == u"\u25FC" :
						if current > 0:
							current = 0
							embed.set_image(url =f"{image_links[current]}")
					elif reaction.emoji == u"\u25B6" :
						if current < (len(image_links) -1) : 
							current += 1
							embed.set_image(url =f"{image_links[current]}")
	              
					elif reaction.emoji ==  u"\U0001F5D1":

						await msg.delete()
	                
					for button in buttons:
						await msg.remove_reaction(button, ctx.author)
	              

					if current != previous_page:
						embed.set_image(url =f"{image_links[current]}")
						await msg.edit(embed = embed)
		except:
			pass
	
	
	@commands.command()
	async def invite(self, ctx):
		embed = discord.Embed(title = "Admin/Moderator Permissions required (explicitly) else embed and moderation system won't work", url = 'YourBOTInvitelinkhere')
		await ctx.channel.send(embed = embed)

def setup(bot):
	bot.add_cog(Command(bot))

