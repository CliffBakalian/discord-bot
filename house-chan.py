# bot.py
import os

import discord
import datetime
import calendar 
from discord.ext import commands

GUILD = os.getenv('my dudes')

client = discord.Client()

def findDay(date): 
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday() 
    return (calendar.day_name[born]) 

async def background():
  await client.wait_until_ready()
  key = datetime.datetime.today().weekday()
  if key < 6:
    mention = ht[key]
    await channel.send("Remember to defrost meat if needed " + BA)
  os._exit(0)

client.loop.create_task(background())
client.run(TOKEN)

