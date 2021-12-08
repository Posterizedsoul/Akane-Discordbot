

#Help cog has been removed because it was causing some weird problems. Add your own if you want to host this bot.
#All the scraping code is/will-be available in Fluby repository.
#Switched to API's instead of scrapping everything on my own and bot runs much faster now.
#This bot is entirely written in Discord.py and will be re-written in other libraries possibly hikari or nextcord or pycord.
#Warning this bot was written for my personal use in my server so some functionality has been removed before uploading to
import cogs
from cogs.imports import *

bot = commands.Bot(command_prefix='oi ')
bot.remove_command('help')
    

@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Game(name = f" on {len(bot.guilds)} servers || use <oi help> for help "))
    print("Bot is still working somehow.")

async def ch_pr():
  await bot.wait_until_ready()
  statuses = ['on nhentai', f'on {len(bot.guilds)} servers', "the most lewd bot you'll ever see", 'use <oi invite> to invite me>']
  while not bot.is_closed():
    status = random.choice(statuses) 
    await bot.change_presence(activity = discord.Game(name = status))
    await asyncio.sleep(18)

extentions = ['cogs.book', 'cogs.general', 'cogs.nsfw','cogs.weeb','cogs.moderation','cogs.music','cogs.spotify_tracker','cogs.snipe']    
for ext in extentions:
    bot.load_extension(ext)

bot.loop.create_task(ch_pr())
bot.run(os.environ['TOKEN'])

