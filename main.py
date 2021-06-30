import discord
import random as rd
import os
import random
from keep_alive import keep_alive

def add_space(w):
  c=''
  for i in w:
    c=c+i+' '
  return c

client=discord.Client()
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  my_file = open("names.txt", "r")
  content = my_file.read()
  l = content.split()
  my_file.close()

  a=rd.randint(0,len(l))


  if msg.startswith("~play"):
      given_word=l[a].upper()
      length=len(l[a])
      t=6
      p=''
      for k in range(length-2):
        p=p+"*"

      que=given_word[0]+p+given_word[-1]
      que1=add_space(que)

      await message.channel.send(que1)
      
      while que!=given_word:
          await message.channel.send("Enter a letter")
          x = await client.wait_for("message", timeout=60)

          x=x.content.upper()
          if x in  given_word:
              for o in range(length):
                  if given_word[o]==x:
                      c=que[:o]+x+que[o+1:]
                      que=c
              que2=add_space(que)
              await message.channel.send(que2)
          else:
              t=t-1
              if t==0:
                  await message.channel.send("🎮Game over")
                  pot='correct word is '+given_word
                  await message.channel.send(pot)
                  break
              else:
                  await message.channel.send("OOPS you selected a wrong letter")
      if que==given_word:
          await message.channel.send("You won the game🐬🐳")

keep_alive()
client.run(os.getenv('TOKEN'))

