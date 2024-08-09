import discord
from discord.ext import commands
import os
from discord.utils import get

intents = discord.Intents.default()
intents.message_content = True
intents.members = True 
bot = commands.Bot(command_prefix='!', intents=intents)


SERVER_ID = 1269678241417924809
NAME_ROLE1 = "2 курс"
NAME_ROLE2 = "3 курс"
KICK_ROLE = "4 курс"
@bot.command()
async def stack(ctx):
    guild = bot.get_guild(SERVER_ID)  

    role1 = get(guild.roles, name=NAME_ROLE1)
    role2 = get(guild.roles, name=NAME_ROLE2)
    
    if role1 is None or role2 is None:
        await ctx.send(f"Ha сервері немає a6o ролі {NAME_ROLE1} a6o {NAME_ROLE2}")
        return
    
    members = role1.members

    for member in members:
        await member.remove_roles(role1) 
        await member.add_roles(role2)


@bot.command()
async def kickk(ctx):
    guild = bot.get_guild(SERVER_ID)  

    role = get(guild.roles, name = KICK_ROLE)
    
    if role is None:
        await ctx.send(f"Ha cepвepi немає poлi {KICK_ROLE}")
        return

    members = role.members
    for member in members:
        await member.kick()  

bot.run(os.getenv('TOKEN'))
