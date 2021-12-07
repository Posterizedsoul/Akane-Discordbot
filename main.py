
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

extentions = ['cogs.help', 'cogs.book', 'cogs.general', 'cogs.nsfw','cogs.weeb','cogs.moderation','cogs.music','cogs.spotify_tracker','cogs.snipe']    
for ext in extentions:
    bot.load_extension(ext)

bot.loop.create_task(ch_pr())
bot.run(os.environ['TOKEN'])

