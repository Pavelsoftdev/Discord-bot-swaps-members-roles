from config import *
import discord
from discord.ext import commands
import os
from discord.utils import get

intents = discord.Intents.default()
intents.message_content = True
intents.members = True 
bot = commands.Bot(command_prefix='!', intents=intents)

async def check_role_on_server(ctx, rol):
     guild = bot.get_guild(SERVER_ID)  
     role = get(guild.roles, name = rol)
     if role is None:
        await ctx.send(f"Помилка! Ha сервері немає ролі - {rol}")
        return


@bot.command()
async def stack(ctx):
    guild = bot.get_guild(SERVER_ID)  
    role1 = get(guild.roles, name=NAME_ROLE1)
    role2 = get(guild.roles, name=NAME_ROLE2)
    
    await check_role_on_server(ctx, NAME_ROLE1)
    await check_role_on_server(ctx, NAME_ROLE2)

    members = role1.members

    for member in members:
        await member.remove_roles(role1) 
        await member.add_roles(role2)


@bot.command()
async def kickk(ctx):
    guild = bot.get_guild(SERVER_ID)  
    role = get(guild.roles, name = KICK_ROLE)
    
    await check_role_on_server(ctx, KICK_ROLE)

    members = role.members
    for member in members:
        await member.kick()  

bot.run(os.getenv('TOKEN'))
