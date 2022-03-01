import discord
import os
from discord.ext import commands, tasks
#from keep_alive import keep_alive

client = discord.Client()
client = commands.Bot(command_prefix = '$')
client.remove_command('help')

import time
import random
import os


@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game('$help'))

  print('Connected to bot: {}'.format(client.user.name))
  print('Bot ID: {}'.format(client.user.id))

  

#COMMANDS GO HERE



#HELP MENU
@client.command()
async def help(ctx):
  embed = discord.Embed(title="🄷🄾🄼🄴🅆🄾🅁🄺 🄷🄴🄻🄿🄴🅁 Help Menu" , value="This is the Help Menu.") 
  embed.add_field(name="Math Help", value="Type $math for math help")
  embed.add_field(name="Timers", value="Type $timers for timers.")
  embed.add_field(name="Other", value="Type $other for other commands.")
  embed.add_field(name="Admin Commands", value=" Type $admin Commands for admin")
  embed.add_field(name="Easter eggs", value="Type $easter_eggs for some cool easter egg commands")
  embed.set_footer(text="Made by _Ven0m#4019 and Mihirsur007#7149")
  await ctx.send(embed=embed)
#MATH HELP
@client.command()
async def math(ctx):
  embed = discord.Embed(title="Math Help Menu", value="")
  embed.add_field(name="Calculator", value="This commands calculates the 2 numbers you provide. **Syntax:** $calculator <number1> <operation> <number2>")
  embed.set_footer(text="Made by _Ven0m#4019 and Mihirsur007#7149")
  await ctx.send(embed=embed)
#TIMERS
@client.command()
async def timers(ctx):
  embed = discord.Embed(title="Timer Menu" , value="") 
  embed.add_field(name="Timer Minutes", value="Times the specified number of minutes. **Syntax:** $timer_minutes <number of minutes>")
  embed.add_field(name="Timer Seconds", value="Times the specified number of seconds. **Syntax:** $timer_seconds <number of seconds>")
  embed.add_field(name="**Note:**", value="**We are still troubleshooting the timers. Please don't use them yet. The using timers makes the bot go offline.**")
  embed.set_footer(text="Made by _Ven0m#4019 and Mihirsur007#7149")
  await ctx.send(embed=embed)
#OTHER
@client.command()
async def other(ctx):
  embed = discord.Embed(title="Other" , value="") 
  embed.add_field(name="Ping Latency", value="Checks the ping latency of this bot and sends it to you. **Syntax:** $ping")
  embed.add_field(name="Server Info", value="This commands displays the server info. **Syntax:** $serverinfo")
  embed.set_footer(text="Made by _Ven0m#4019 and Mihirsur007#7149")
  await ctx.send(embed=embed)
#ADMIN COMMANDS
@client.command()
async def admin(ctx):
  embed = discord.Embed(title="Admin" , value="This is the admin help menu") 
  embed.add_field(name="Kick", value="The kick command kicks the specified user from the server. **Syntax:** $kick @<user>")
  embed.add_field(name="Ban", value="The ban command bans the specified user from the server. **Syntax:** $ban @<user>")
  embed.add_field(name="Clear", value="This commands clears the specified amount of messages in a channel. **Syntax:** -clear <number> **or** -clear all")
  embed.add_field(name="Mute", value="Mutes a us in a voice channel. **Syntax:** $mute @<user>")
  embed.add_field(name="Unmute", value="Unmutes a user in a voice channel. **Syntax:** $unmute @<user>")
  
  embed.set_footer(text="Made by _Ven0m#4019 and Mihirsur007#7149")
  await ctx.send(embed=embed)
#EASTER EGGS
@client.command()
async def easter_eggs(ctx):
  embed = discord.Embed(title="Easter eggs" , value="**Note:** This command is an easte egg itself")
  embed.add_field(name="Apple Database", value="A secret. Test it yourself. **Syntax:** $apple_database")
  embed.add_field(name="Farts Exist", value="This is too funny to explain lol. **Syntax:** $farts_exist") 
  
  embed.set_footer(text="Made by _Ven0m#4019 and Mihirsur007#7149")
  await ctx.send(embed=embed)





#MATH COMMANDS

#Calculator
@client.command()
async def calculator(ctx, num1, operation, num2):
  if operation == "+":
    num3 = int(num1) + int(num2)
    await ctx.channel.send(num1+" + "+num2+" = "+str(num3))
  if operation == "-":
    num3 = int(num1) - int(num2)
    await ctx.channel.send(num1+" - "+num2+" = "+str(num3))
  if operation == "*":
    num3 = int(num1) * int(num2)
    await ctx.channel.send(num1+" * "+num2+" = "+str(num3))
  if operation == "/":
    num3 = int(num1) / int(num2)
    await ctx.channel.send(num1+" / "+num2+" = "+str(num3))








#TIMER COMMANDS

#Timer Minutes
@client.command()
async def timer_minutes(ctx, amount_of_time):
  await ctx.channel.send("Time starts now!")
  if int(amount_of_time) > 5:
    amount_of_time_for_loop = int(amount_of_time) - 5
    for x in range(amount_of_time_for_loop):
      time.sleep(60)
    await ctx.channel.send("5 minutes left")
    time.sleep(60)
    await ctx.channel.send("4 minutes left")
    time.sleep(60)
    await ctx.channel.send("3 minutes left")
    time.sleep(60)
    await ctx.channel.send("2 minutes left")
    time.sleep(60)
    await ctx.channel.send("1 minute left")
    time.sleep(60)
    await ctx.channel.send(ctx.message.author.mention+" TIME UP!")
    return
  else:
    time.sleep(int(amount_of_time) * 60)
    await ctx.channel.send(ctx.message.author.mention+" TIME UP!")

#Timer Seconds
@client.command()
async def timer_seconds(ctx, amount_of_time):
  await ctx.channel.send("Time starts now!")
  if int(amount_of_time) > 5:
    amount_of_time_for_loop = int(amount_of_time) - 5
    for x in range(amount_of_time_for_loop):
      time.sleep(1)
    await ctx.channel.send("5")
    time.sleep(1)
    await ctx.channel.send("4")
    time.sleep(1)
    await ctx.channel.send("3")
    time.sleep(1)
    await ctx.channel.send("2")
    time.sleep(1)
    await ctx.channel.send("1")
    time.sleep(1)
    await ctx.channel.send(ctx.message.author.mention+" TIME UP!")
    return
  else:
    time.sleep(int(amount_of_time))
    await ctx.channel.send(ctx.message.author.mention+" TIME UP!")








#OTHER COMMANDS

#Ping Latency Command
@client.command(pass_context=True)
async def ping(ctx):
  message = await ctx.channel.send("Pong")
  before = time.monotonic()
  await message.edit(content="Pong!")
  ping = (time.monotonic() - before) * 1000
  await message.edit(content=f"Pong! `{int(ping)}ms`")

#Server Info Command
@client.command()
async def serverinfo(ctx):
  name = str(ctx.guild.name)
  description = str(ctx.guild.description)

  if name == "Study Group":
    owner = "_Ven0m#4019"
  else:
    owner = str(ctx.guild.owner)
  
  id = str(ctx.guild.id)
  region = str(ctx.guild.region)
  memberCount = str(ctx.guild.member_count)

  icon = str(ctx.guild.icon_url)


  if description == "None":
    embed = discord.Embed(
        title=name + "Server Information",
        description="",
        color=discord.Color.blue()
      )
  else:
    embed = discord.Embed(
        title=name + " Server Information",
        description=description,
        color=discord.Color.blue()
      )
  embed.set_thumbnail(url=icon)
  embed.add_field(name="Owner", value=owner, inline=True)
  embed.add_field(name="Server ID", value=id, inline=True)
  embed.add_field(name="Region", value=region, inline=True)
  embed.add_field(name="Member Count", value=memberCount, inline=True)
  await ctx.send(embed=embed)

#ADMIN COMMANDS


#Kick command
@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member : discord.Member, *, reason=None):
  channel_dm = await member.create_dm()
  name = str(ctx.guild.name)
  if reason == None:
    await channel_dm.send("You were kicked from "+name+".")
    await ctx.channel.send(f"{member.mention} was kicked.")
    await member.kick(reason=reason)
  else:
    await channel_dm.send("You were kicked from "+name+" "+str(reason)+".")
    await ctx.channel.send(f"{member.mention} was kicked "+str(reason)+".")
    await member.kick(reason=reason)

#Ban command
@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member : discord.Member, *, reason=None):
  channel_dm = await member.create_dm()
  name = str(ctx.guild.name)
  if reason == None:
    await channel_dm.send("You were banned from "+name+".")
    await ctx.channel.send(f"{member.mention} was banned.")
    await member.ban(reason=reason)
  else:
    await channel_dm.send("You were banned from "+name+" "+str(reason)+".")
    await ctx.channel.send(f"{member.mention} was banned "+str(reason)+".")
    await member.ban(reason=reason)


#Clear Command
@client.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount):
  if amount == "all":
    i = 0
    while i == 0:
      await ctx.channel.purge(limit=10)
  else:
    amount2 = int(amount) + 1
    await ctx.channel.purge(limit = int(amount2))

#Mute User in Voice Channel
@client.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member : discord.Member):
  await member.edit(mute = True)
  await ctx.send(f"{member.mention} is muted!")

#Unmute User in Voice Channel
@client.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, member : discord.Member):
  await member.edit(mute = False)
  await ctx.send(f"{member.mention} is unmuted!")



"""EASTER EGGS"""

#Apple Database
@client.command()
async def apple_database(ctx):
  await ctx.channel.send("Loading...")
  for x in range(2):
    time.sleep(10)
  await ctx.channel.send("Loading done. Showing Apple's new plans.")
  time.sleep(5)
  for x in range(10):
    await ctx.channel.send(f"{ctx.message.author.mention} no u xD")
  time.sleep(2)
  await ctx.channel.send("Loading 1,000,000 messages...")
  time.sleep(1)
  await ctx.channel.send("Loading...")

#Farts Exist
@client.command()
async def farts_exist(ctx, member : discord.Member=None):
  if member == None:
    await ctx.channel.send(f"{ctx.message.author.mention} I farted! 🤪")
  else:
    await ctx.channel.send(f"{member.mention} I farted! 🤪")








#keep_alive()
token = "ODA5OTAyNTE3MDc2MDk5MDky.YCb2fw.zMyNDYD7A4KVNRDevxE03wAwn2Q"
client.run(token)
