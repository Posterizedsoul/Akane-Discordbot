import discord
from discord.embeds import Embed
from discord.ext import commands
import requests
from aiohttp import request
import giphy_client
from giphy_client.rest import ApiException
from bs4 import BeautifulSoup
import asyncio
from libgen_api import LibgenSearch
s = LibgenSearch()


class bookCommand(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command()

	async def book(self,ctx, *,query:str):
	    
	    current = 0
	    results = s.search_title(query)
	    embed = discord.Embed(title = 'Book Info')    
	    embed.add_field(name = 'ID', value ='-' + results[current]['ID'])
	    embed.add_field(name = 'Author', value ='-' + results[current]['Author'], inline = True )
	    embed.add_field(name = 'Title', value ='-' + results[current]['Title'], inline = True)
	    embed.add_field(name = 'Publisher', value ='-' + results[current]['Publisher'], inline = True)
	    embed.add_field(name = 'Year', value ='-' + results[current]['Year'], inline = True)
	    embed.add_field(name = 'Pages', value ='-' + results[current]['Pages'], inline = True)
	    embed.add_field(name = 'Language', value ='-' + results[current]['Language'],inline = True)
	    embed.add_field(name = 'Size', value ='-' + results[current]['Size'], inline = True)
	    embed.add_field(name = 'Extension', value ='-' + results[current]['Extension'],inline = True)

	    #Mirrors
	    

	    buttons = [ u"\u25C0", u"\u25FC" , u"\u25B6" ,  u"\U0001F5D1", u"\U0001F4BE"]
	    
	    original_page = current
	    msg = await ctx.send(embed = embed)
	    for button in buttons:
	        await msg.add_reaction(button)
	    while True:
	        
	        try:
	            reaction , user = await self.bot.wait_for("reaction_add", check = lambda reaction,user: user == ctx.author and reaction.emoji in buttons and reaction.message.id == msg.id, timeout = 40)
	        except asyncio.TimeoutError:
	            
	            
	            embed.set_footer(text= "CLosed due to Inactivity.")
	            await msg.clear_reactions()
	            await msg.edit(embed = embed)
	        else:
	            previous_page = current
	            #Back
	            
	            if reaction.emoji == u"\u25C0":
	                current -= 1
	                embed = discord.Embed(title = 'Book Info')    
	                embed.add_field(name = 'ID', value = '-' + results[current]['ID'])
	                embed.add_field(name = 'Title', value ='-' + results[current]['Title'], inline = True)
	                embed.add_field(name = 'Author', value ='-' + results[current]['Author'], inline = True )
	                embed.add_field(name = 'Publisher', value ='-' + results[current]['Publisher'], inline = True)
	                embed.add_field(name = 'Year', value ='-' + results[current]['Year'], inline = True)
	                embed.add_field(name = 'Pages', value ='-' + results[current]['Pages'], inline = True)
	                embed.add_field(name = 'Language', value ='-' + results[current]['Language'],inline = True)
	                embed.add_field(name = 'Size', value ='-' + results[current]['Size'], inline = True)
	                embed.add_field(name = 'Extension', value ='-' + results[current]['Extension'],inline = True)
	                await msg.edit(embed = embed)
	            
	            #To the first Page
	            elif reaction.emoji == u"\u25FC":
	                if current > 0:
	                    current = 0
	                    embed = discord.Embed(title = 'Book Info')    
	                    embed.add_field(name = 'ID', value ='-' + results[current]['ID'])
	                    embed.add_field(name = 'Title', value ='-' + results[current]['Title'], inline = True)
	                    embed.add_field(name = 'Author', value ='-' + results[current]['Author'], inline = True )
	                    embed.add_field(name = 'Publisher', value ='-' + results[current]['Publisher'], inline = True)
	                    embed.add_field(name = 'Year', value ='-' + results[current]['Year'], inline = True)
	                    embed.add_field(name = 'Pages', value ='-' + results[current]['Pages'], inline = True)
	                    embed.add_field(name = 'Language', value ='-' + results[current]['Language'],inline = True)
	                    embed.add_field(name = 'Size', value ='-' + results[current]['Size'], inline = True)
	                    embed.add_field(name = 'Extension', value ='-' + results[current]['Extension'],inline = True)
	                    await msg.edit(embed = embed)
	            
	            #forward
	            elif reaction.emoji == u"\u25B6":
	                if current < len(results) -1:
	                    current += 1
	                    embed = discord.Embed(title = 'Book Info')    
	                    embed.add_field(name = 'ID', value ='-' + results[current]['ID'])
	                    embed.add_field(name = 'Title', value ='-' + results[current]['Title'], inline = True)
	                    embed.add_field(name = 'Author', value ='-' + results[current]['Author'], inline = True )
	                    embed.add_field(name = 'Publisher', value ='-' + results[current]['Publisher'], inline = True)
	                    embed.add_field(name = 'Year', value ='-' + results[current]['Year'], inline = True)
	                    embed.add_field(name = 'Pages', value ='-' + results[current]['Pages'], inline = True)
	                    embed.add_field(name = 'Language', value ='-' + results[current]['Language'],inline = True)
	                    embed.add_field(name = 'Size', value ='-' + results[current]['Size'], inline = True)
	                    embed.add_field(name = 'Extension', value ='-' + results[current]['Extension'],inline = True)

	                    #Mirrors
	                    
	                    
	                    await msg.edit(embed = embed)
	            
	            
	            #delete
	            elif reaction.emoji ==  u"\U0001F5D1":
	               
	                await msg.delete()
	                
	                

	            
	            #downloadlinks
	            elif reaction.emoji ==  u"\U0001F4BE":
	                link= []

	                r = requests.get(results[current]['Mirror_1'])
	                soup = BeautifulSoup(r.text, 'lxml')
	                k = soup.find('div', id = 'download')
	                link.append(str(k).split('"')[3])
	            
	                rq = requests.get(results[current]['Mirror_2'])
	                base_url = 'http://libgen.lc/'
	                soup = BeautifulSoup(rq.text, 'lxml')
	                link_alt = soup.find('td', align = 'center')
	                
	                fake_link = base_url+ str(link_alt).split('"')[7].replace('amp;','')
	                link.append(fake_link)
	                
	                embed.add_field(name = 'Download Links || Use 3rd mirror to download manually if 1st and 2nd links dont work.' , value =f' [Download link_1]({link[1]})  [Download_link_2]({link[0]})  [Mirror]({results[current]["Mirror_3"]})',inline = False)
	               
	                await msg.edit(embed = embed)
	            for button in buttons:
	                await msg.remove_reaction(button, ctx.author)


def setup(bot):
	bot.add_cog(bookCommand(bot))