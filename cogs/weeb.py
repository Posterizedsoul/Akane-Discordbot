
import discord
from discord import client
from discord.embeds import Embed
from discord.ext import commands
import aiohttp
from aiohttp import request
import giphy_client
from giphy_client.rest import ApiException
from bs4 import BeautifulSoup
import asyncio



class Command(commands.Cog):
	def __init__(self, bot):
		self.bot = bot


	@commands.command()
	async def neko(self,ctx, endpoint:str):
	  async with aiohttp.ClientSession() as session:
	    if ctx.channel.is_nsfw() and endpoint == 'lewd':
	      async with session.get("https://neko-love.xyz/api/v1/nekolewd") as r:
	          if r.status == 200:
	            js = await r.json()
	            await ctx.channel.send(js["url"])
	            print(r.json()["url"])
	            await session.close()
	    else:
	      async with session.get("https://neko-love.xyz/api/v1/" + endpoint) as r:
	        if r.status == 200:
	            js = await r.json()
	            await ctx.channel.send(js["url"])
	            print(r.json()["url"])
	            await session.close()

	# waifu
	@commands.command()
	async def waifu(self,ctx, type:str ):
	  default = "sfw"
	  
	  if ((type == 'waifu') or (type == 'neko') or (type == 'trap') or (type == 'blowjob')) and ctx.channel.is_nsfw():
	      async with aiohttp.ClientSession() as session:
	          async with session.get("https://api.waifu.pics/" + "nsfw" + "/" + type) as r:
	              if r.status == 200:
	                  js = await r.json()
	                  await ctx.channel.send(js["url"])
	                  print(r.json()["url"])
	                  await session.close()
			  
	  else:	  
	    async with aiohttp.ClientSession() as session:
	        async with session.get("https://api.waifu.pics/" + default + "/" + type) as r:
	            if r.status == 200:
	                js = await r.json()
	                await ctx.channel.send(js["url"])
	                print(r.json()["url"])
	                await session.close()

def setup(bot):
	bot.add_cog(Command(bot))
