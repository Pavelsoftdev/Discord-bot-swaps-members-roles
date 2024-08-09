import discord
from discord.ext import commands
import os
from discord.utils import get

intents = discord.Intents.default()
intents.message_content = True
intents.members = True 
bot = commands.Bot(command_prefix='!', intents=intents)


SERVER_ID = 1269678241417924809

@bot.command()
async def stack(ctx):
    guild = bot.get_guild(SERVER_ID)  

    role1 = get(guild.roles, name="2 курс")
    role2 = get(guild.roles, name="3 курс")
    
    if role1 is None or role2 is None:
        await ctx.send("Немає кopиcтyвaчiв ролей '2 курс' a6o '3 курс'!")
        return
    
    members = role1.members

    for member in members:
        await member.remove_roles(role1) 
        await member.add_roles(role2)


@bot.command()
async def kickk(ctx):
    guild = bot.get_guild(SERVER_ID)  

    role = get(guild.roles, name="4 курс")
    
    if role is None:
        await ctx.send("Немає кopиcтyвaчiв з такою роллю!")
        return

    members = role.members
    for member in members:
        await member.kick()  

bot.run(os.getenv('TOKEN'))
