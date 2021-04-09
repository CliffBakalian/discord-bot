# bot.py
import os
import sys
import discord
import datetime
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

async def background():
  await client.wait_until_ready()
  CHANNEL_ID = os.getenv('CHANNEL_ID')
  channel = client.get_channel(int(CHANNEL_ID))
  BOT_CHANNEL_ID = os.getenv('BOT_CHANNEL_ID')
  bot_channel = client.get_channel(int(BOT_CHANNEL_ID))
  MONDAY = os.getenv('MONDAY_ID') 
  TUESDAY = os.getenv('TUESDAY_ID')
  WEDNESDAY = os.getenv('WEDNESDAY_ID')
  THURSDAY = os.getenv('THURSDAY_ID')
  FRIDAY = os.getenv('FRIDAY_ID') 
  SATURDAY = os.getenv('SATURDAY_ID') 

  ht = {0: MONDAY, 1: TUESDAY, 2:WEDNESDAY, 3:THURSDAY, 4:FRIDAY, 5:SATURDAY}
  key = datetime.datetime.today().weekday()
  if "food" in sys.argv[1]:
    mention = ht[key]
    await channel.send("Remember to defrost meat if needed " + mention)
  elif "trash" in sys.argv[1]:
    mention = ht[(datetime.datetime.today().date().isocalendar()[1])%6]
    await channel.send(mention + ", don't forget to take out the trash")
#  elif "dehumidifier" in sys.argv[1]:
#    await bot_channel.send(TUESDAY + ", " + SATURDAY + ": Check The Dehumidifier")
  elif "smooth" in sys.argv[1]:
    await bot_channel.send("<:smooth:766378578270224394>")
  os._exit(0)

client.loop.create_task(background())
client.run(TOKEN)

