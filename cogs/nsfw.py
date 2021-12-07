import discord
from discord.embeds import Embed
from discord.ext import commands
from random import randint
import requests
import aiohttp
from aiohttp import request
import giphy_client
from giphy_client.rest import ApiException
import pornhub
import wikipedia
from hentai import Hentai, Format
from hentai import Utils, Sort, Option, Tag
from bs4 import BeautifulSoup
from pornhub_api import PornhubApi
import random
import asyncio
from requests import request
import validators

class Command(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def doujin(self,ctx,safe = None,  search_results = None , *,text = None):
	    try:
		    if ctx.channel.is_nsfw() and safe == "random":
		        rando = randint(1, 369000)
		        doujin = Hentai(rando)
		        doujin_page = doujin.image_urls
		        buttons = [ u"\U0001F3E0" ,u"\u25C0", u"\u25FC" , u"\u25B6" , u"\U0001F5D1",    u"\U0001F4BE"]
		        current = 0
		        embed = discord.Embed()
		        if Hentai.exists(doujin.id):
		          embed = discord.Embed(title = doujin.title())
		          embed.add_field(name= "tags", value = [tag.name for tag in doujin.tag])
		          embed.add_field(name = "Nuke Code", value = doujin.id, inline = True)
		          embed.add_field(name = "Upload date", value = doujin.upload_date, inline = True)
		          print(doujin.image_urls)
		          embed.add_field(name="Sauce Link", value=f"https://nhentai.net/g/{rando}")
		        
		        msg = await ctx.send(embed = embed)
		        
		        for button in buttons:
		            await msg.add_reaction(button)
		        while True:
		            
		            try:
		                reaction , user = await self.bot.wait_for("reaction_add", check = lambda reaction,user: user == ctx.author and reaction.emoji in buttons and reaction.message.id == msg.id, timeout = 30.0)
		            except asyncio.TimeoutError:
		                embed.set_footer(text= "Timeout.")
		                await msg.clear_reactions()
		                await msg.edit(embed = embed)
		            else:
		                
		                previous_page = current
		                if reaction.emoji == u"\U0001F3E0":
		                  embed = discord.Embed(title = doujin.title())
		                  embed.add_field(name= "tags", value = [tag.name for tag in doujin.tag])
		                  embed.add_field(name = "Nuke Code", value = doujin.id, inline = True)
		                  embed.add_field(name = "Upload date", value = doujin.upload_date, inline = True)
		                  print(doujin.image_urls)
		                  embed.add_field(name="Sauce Link", value=f"https://nhentai.net/g/{rando}")  
		                  await msg.edit(embed = embed)
		                elif reaction.emoji == u"\u25C0" :
		                    if current != 0:

		                      current -= 1
		                      embed.set_image(url =f"{doujin_page[current]}")
		                    
		                elif reaction.emoji == u"\u25FC" :
		                    if current != 0:
		                        current = 0
		                        
		                        embed.set_image(url =f"{doujin_page[current]}")
		                elif reaction.emoji == u"\u25B6" :
		                    if current < len(doujin.image_urls) -1 : 
		                        current += 1
		                        
		                        
		                        embed.set_image(url =f"{doujin_page[current]}")
		                        
		                elif reaction.emoji ==  u"\U0001F5D1":
		                    
		                    await msg.delete()
		          
		                    
		                
		                elif reaction.emoji ==  u"\U0001F4BE":
		                  e = discord.Embed(title = 'Click here to download', url = f'https://nhentai-discord-bot-web.herokuapp.com/download/{rando}')
		                  
		                  await ctx.channel.send(embed = e)
		                for button in buttons:
		                    await msg.remove_reaction(button, ctx.author)
		                

		                if current != previous_page:
		                    await msg.edit(embed = embed)

		      
		    
		    elif safe == 'safe':
		        rand = randint(1, 375000)
		        doujin = Hentai(rand)
		        if Hentai.exists(doujin.id):
		            embed = discord.Embed(title = doujin.title(), description = "Click the title to download", url = f'https://nhentai-discord-bot-web.herokuapp.com/download/{rand}')
		            embed.add_field(name= "tags", value = [tag.name for tag in doujin.tag])
		            embed.add_field(name = "Nuke Code", value = doujin.id, inline = True)
		            embed.add_field(name = "Upload date", value = doujin.upload_date, inline = True)
		            print(doujin.image_urls)
		            embed.add_field(name="Sauce Link", value=f"https://nhentai.net/g/{rand}")
		            
		            await ctx.channel.send(embed = embed)
		           
		    elif safe == "spam" and ctx.channel.is_nsfw():
		        rand = randint(1, 375463)
		        doujin = Hentai(rand)
		        for doujins in doujin.image_urls:
		            await ctx.channel.send(doujins)
		    
		    elif safe.isdigit():
		      doujin = Hentai(safe)
		      doujin_page = doujin.image_urls
		      buttons = [ u"\u25C0", u"\u25FC" , u"\u25B6" , u"\U0001F5D1", u"\U0001F4BE"]
		      current = 0
		      embed = discord.Embed()
		      if Hentai.exists(doujin.id):
		        embed = discord.Embed(title = doujin.title())
		        embed.add_field(name= "tags", value = [tag.name for tag in doujin.tag])
		        embed.add_field(name = "Nuke Code", value = doujin.id, inline = True)
		        embed.add_field(name = "Upload date", value = doujin.upload_date, inline = True)
		        print(doujin.image_urls)
		        embed.add_field(name="Sauce Link", value=f"https://nhentai.net/g/{safe}")
		        
		      
		      msg = await ctx.send(embed = embed)
		      
		      for button in buttons:
		          await msg.add_reaction(button)
		      while True:
		          
		          try:
		              reaction , user = await bot.wait_for("reaction_add", check = lambda reaction,user: user == ctx.author and reaction.emoji in buttons and reaction.message.id == msg.id, timeout = 60.0)
		          except asyncio.TimeoutError:
		              embed = self.bot.doujin_page[current-1]
		              embed.set_footer(text= "Timeout.")
		              await msg.clear_reactions()
		          
		          else:
		              previous_page = current
		              if reaction.emoji == u"\u25C0" :
		                  if current != 0:

		                    current -= 1
		                    embed.set_image(url =f"{doujin_page[current]}")
		                    await ctx.send(embed = Embed)
		              elif reaction.emoji == u"\u25FC" :
		                  if current != 0:
		                      current = 0
		                      
		                      embed.set_image(url =f"{doujin_page[current]}")
		              elif reaction.emoji == u"\u25B6" :
		                  if current < len(doujin.image_urls) -1 : 
		                      current += 1
		                      embed.set_image(url =f"{doujin_page[current]}")
		                      
		              elif reaction.emoji ==  u"\U0001F5D1":
		               
		                await msg.delete()
		                
		              
		              elif reaction.emoji ==    u"\U0001F4BE":
		                  e = discord.Embed(title = 'Click here to download', url = f'https://nhentai-discord-bot-web.herokuapp.com/download/{safe}')
		                  await ctx.channel.send(embed = e)
		              for button in buttons:
		                  await msg.remove_reaction(button, ctx.author)
		              

		              if current != previous_page:
		                  embed.set_image(url =f"{doujin_page[current]}")
		                  await msg.edit(embed = embed)

		    elif safe == 'search' and search_results.isdigit() and str(text):
		      if text.lower() == 'bibek' or text.lower() == 'bb' or text.lower() == 'bbg':
		        pass
		      elif int(search_results) > 69:
		        await ctx.channel.send("69 is the limit kid. Grow your pp first")
		        pass
		      else:        
		        page = 1
		        data = requests.get(f"https://nhentai.net/search/?q={text}&sort=popular&page={str(page)}").text
		        soup = BeautifulSoup(data, 'html.parser')
		        names_html = soup.findAll('div', class_='caption')
		        links_html = soup.findAll('a', class_='cover')
		        results_html = soup.find('h1')
		        names = [x.text for x in names_html]
		        results = results_html.text
		        links = [x.get("href").split("/")[2] for x in links_html]
		        await ctx.channel.send("Found" + results+"|| Search results of \""+text+"\"")
		        await ctx.channel.send(f'First {search_results} search results')
		        for i in range(int(search_results)):
		            await ctx.channel.send(f"{i + 1}. [{links[i]}]     {names[i]}\n")
		            print(f"{i + 1}. [{links[i]}]     {names[i]}\n")


		    else:pass
	    except:
		    await ctx.channel.send('No Mod/Admin Perms given.')





	
	@commands.command()
	async def shub(self,ctx, no:int ,*,query:str):
	  api = PornhubApi()
	  data = api.search.search({query})
	  embed = discord.Embed(Title = 'Your Search')
	  if no > 69:
	    await ctx.channel.send('Stop! Get some help')
	  else:
	    run = True
	    while run:
	      for vid in data.videos:
	        
	        embed.add_field(name = 'Title', value = vid.title, inline = False)
	        embed.add_field(name = 'Video', value = 'https://www.pornhub.com/view_video.php?viewkey='+str(vid.video_id), inline = True)
	        no -= 1
	        if no == 0:
	          run = False
	          break
	      await ctx.channel.send(embed = embed)

	@commands.command()
	async def rhub(self,ctx, num:int,word1:str):
	    if ctx.channel.is_nsfw():
	        bot = pornhub.PornHub(keywords=[f'{word1}'])
	        for video in bot.getVideos(num,page=10):
	            embed = discord.Embed(title = video['name'], description = video['url'], Color = discord.Color.blue())
	            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
	            embed.set_thumbnail(url= video["background"])
	            embed.add_field(name="Duration", value= video['duration'], inline=True)
	            embed.add_field(name="Rating", value=video['rating'], inline=True)
	            

	            await ctx.send(embed = embed)
	            print(video)
	            print(video["url"])




	@commands.command()
	async def r34(self,ctx,n:int,*,tag:str):
	  image, tagg = [], []
	  base_url = 'https://rule34.xxx/index.php?page=post&s=list&tags='
	  base_view_url = 'https://rule34.xxx/index.php?page=post&s=view&id='
	  url = base_url+tag
	  page = requests.get(url)
	  soup = BeautifulSoup(page.content,'lxml')

	  valzkai = soup.find_all('span',class_='thumb')
	  for i in range(n):
	    a=valzkai[i].a['id']
	    a=a.replace('p','')
	    view_url=base_view_url + str(a)
	    view_page = requests.get(view_url)
	    view_soup = BeautifulSoup(view_page.content,'lxml')
	    aki=view_soup.find('div',id='content')
	    attribute_array=aki.find('div',class_='link-list').find_all('a')
	    flag_image_src=1  

	    while flag_image_src==1:
	      for a in attribute_array:
	        valid=validators.url(a['href'])
	        if valid:
	          image_src_link=a['href']
	          image.append(image_src_link)
	          flag_image_src=0

	  tags = soup.find_all('span',class_='thumb')
	  for tag in tags:
	      k = " " + str(tag)
	      real_deal = k.split('alt="')[1].split('"')[0]
	      tagg.append(real_deal)

	  if ctx.channel.is_nsfw():

	    buttons = [ u"\u25C0", u"\u25FC" , u"\u25B6" , u"\U0001F5D1"]
	    current = 0
	    embed = discord.Embed()
	    
	    embed = discord.Embed(title = "R34")
	    embed.set_image(url =f"{image[current]}") 
	    embed.set_footer(text = tagg[current])
	    msg = await ctx.channel.send(embed = embed)
	    
	    for button in buttons:
	        await msg.add_reaction(button)
	    while True:

	        
	      try:
	          reaction , user = await self.bot.wait_for("reaction_add", check = lambda reaction,user: user == ctx.author and reaction.emoji in buttons and reaction.message.id == msg.id, timeout = 60.0)
	      except asyncio.TimeoutError:
	          embed = bot.image[current]
	          embed.set_footer(text= "Timeout.")
	          await msg.clear_reactions()
	          await msg.edit(embed = embed)
	      else:

	        previous_page = current
	        if reaction.emoji == u"\u25C0" :
	            current -= 1
	            embed.set_image(url =f"{image[current]}")
	            
	            embed.set_footer(text = tagg[current])
	            await msg.edit(embed = embed)
	        
	        
	        elif reaction.emoji == u"\u25FC" :
	            if current > 0:
	                current = 0
	                embed.set_image(url =f"{image[current]}")
	                embed.set_footer(text = tagg[current])
	                await msg.edit(embed = embed)

	        elif reaction.emoji == u"\u25B6" :
	            if current < len(image) -1 : 
	                current += 1
	                embed.set_image(url =f"{image[current]}")
	                
	                embed.set_footer(text = tagg[current])
	                await msg.edit(embed = embed)

	        elif reaction.emoji ==  u"\U0001F5D1":
	            
	            
	            await msg.delete()
	                           
	        for button in buttons:
	            await msg.remove_reaction(button, ctx.author)
	        

	        if current != previous_page:
	            embed.set_image(url =f"{image[current]}")
	            await msg.edit(embed = embed)        


def setup(bot):
	bot.add_cog(Command(bot))
