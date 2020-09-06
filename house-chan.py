# bot.py
import os
import re

import discord
import random

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
insults = [
  "you're trash",
  'fuck you',
  'cUnt is a kangaroo word',
  "here's your motivational quote: jellyfish have survived 600 million years without a brain",
  'Im sure your phone screen is brighter than your future',
  "are you a fire alarm? because you're loud and annoying",
  "are you yeast? because you're inbred",
  "suck a dick dumb shit",
  "you leamon-stealing whore",
  "Are you happy? because you're fucking gay",
  "my middle finger gets a boner every time it sees you",
  "you're not invited to my birthday party anymore",
  "you absolute boob",
  "fuckwit",
  "dipshit",
  "you fuckin DONKEY",
  "you dingus",
  "you fuckin wanker",
  "you... artless pignut fly-bitten rapscallion",
  "you're as useful as a needle in a condom factory",
  "I fart in your general direction. Your mother was a hamster and your father smelt of elderberries",
  "you are a classic example of the inverse ratio between the size of the mouth and the size of the brain"
]
inspiration= [
  "Mistakes are proof you are trying",
  "Let your dreams be bigger than your fears",
  "Play nice, Work hard, Stay Kind",
  "There's never a right time to do the wrong thing and there's never a wrong time to do the right thing",
  "You're stronger than the sum of your fears",
  "Be kind, for everyone you meet i fighting a hard battle",
  "All things are difficult before they are easy",
  "Success is no accident",
  "Believe you can and you're halfway there",
  "The future depends on what you do today",
  "It's okay not to know, but it's not okay to not try",
  "The expert in anything was once a beginner",
  "Today a reader, Tomorrow a leader",
  "In a world where you can be anything, be kind",
  "Success is a decision",
  "It doesn't matter how slow you go as long as you don't stop"
]

client = discord.Client()
under = re.compile('(.*\s+know\s+)?[Ww]here\s.*')
hewp = re.compile('\?help')
good = re.compile('[Gg]ood bot')
bad = re.compile('[Bb]ad bot')
pog = re.compile('^\s*[Pp]oggers\s*$')
insult = re.compile('![Rr]oast me')
inspire = re.compile('![Ii]nspire me')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    help_regex = hewp.search(message.content)
    under_regex= under.search(message.content)
    good_regex = good.search(message.content)
    bad_regex = bad.search(message.content)
    pog_regex = pog.search(message.content)
    insult_regex = insult.search(message.content)
    inspire_regex = inspire.search(message.content)
    if help_regex:
        response = "Hewwo,I am House-Chan uwu. I hewp awound the howse.\
        \nYou can order me around like the bot I am:\
        \n\t!inspire me - qives an inspiwationyaw quote UwU\
        \n\t!roast me - i will woast u >.<\n\t?help - dispways this hewp message"
        await message.channel.send(response)
    if pog_regex:
        response = "Don't you mean, Gongers?"
        await message.channel.send(response)
    if  under_regex:
        response = "it's under there"
        await message.channel.send(response)
    if good_regex:
        emoji = '\U0001F633'
        await message.add_reaction(emoji)
    if bad_regex:
        emoji = '\U0001F622'
        await message.add_reaction(emoji)
    if insult_regex:
        response = random.choice(insults)
        await message.channel.send(response)
    if inspire_regex:
        response = random.choice(inspiration)
        await message.channel.send(response)
client.run(TOKEN)
