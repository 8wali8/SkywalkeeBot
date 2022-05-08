import discord
import os
import re

secret = os.environ['token']
client = discord.Client()

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))
  
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$'):
    
    if message.content.startswith('$hello'):
      await message.channel.send("Hello!")

    if message.content.startswith('$synopsis'):
      word = message.content.replace("$synopsis ", "")
      SplitWord = re.findall(r'\(.*?\)', word)
      await message.channel.send(SplitWord)
      branch, time, people, actions = SplitWord
      await message.channel.send(branch)
      await message.channel.send(time)
      await message.channel.send(people)
      await message.channel.send(actions)

client.run(secret)