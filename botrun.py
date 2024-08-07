import discord
from discord.ext import commands
import os
from discord.utils import get

intents = discord.Intents.default()
intents.message_content = True
intents.members = True 
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def stack(ctx):
    guild = bot.get_guild(1269678241417924809)  

    role1 = get(guild.roles, name="2 курс")
    role2 = get(guild.roles, name="3 курс")
    
    members = role1.members

    for member in members:

        await member.remove_roles(role1) 
        await member.add_roles(role2)


bot.run(os.getenv('TOKEN'))