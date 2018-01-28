#Sealboi - A bot by AGingerWhoCodes on Github

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk
import random

bot = commands.Bot(command_prefix='s!')

@bot.event
async def on_ready():
    print ("It's over Anakin, I have the high ground!")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)
    
@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("The users name is: {}".format(user.name))
    await bot.say("The users ID is: {}".format(user.id))
    await bot.say("The users status is: {}".format(user.status))
    await bot.say("The users highest role is: {}".format(user.top_role))
    await bot.say("The user joined at: {}".format(user.joined_at))

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Cya, {}. Ya loser!".format(user.name))
    await bot.kick(user)

@bot.command(pass_context = True)
async def clear(ctx, number):
    mgs = []
    number = int(number)
    async for x in bot.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await bot.delete_messages(mgs)

@bot.command(pass_context = True)
async def poke(ctx, user: discord.Member):
    await bot.say(":point_right::skin-tone-1: You poked {}, they better not be annoyed!".format(user.name))

@bot.command(pass_context = True)
async def stab(ctx, user: discord.Member):
    await bot.say(":knife: You stabbed {}, how could you!?".format(user.name))

@bot.command(pass_context = True)
async def kill(ctx, user: discord.Member):
    await bot.say(":skull: You KILLED {}! You MURDERER!!".format(user.name))

@bot.command(pass_context = True)
async def yosh(ctx):
    await bot.say(":heart: Yosh is love, yosh is life")

@bot.command(pass_context = True)
async def suicide(ctx, user: discord.Member):
    await bot.say("{}, you shouldn't commit suicide. People care about you. I care about you. We all care. You can vent if you need to, or call a suicide prevention hotline. Please, don't kill yourself".format(user.name))

bot.run("TOKEN")
