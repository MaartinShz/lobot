import os
import requests
import random
import re

from dotenv import load_dotenv
from discord.ext import commands
from discord import File

load_dotenv()


"""class PyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!")
    
    async def on_ready(self):
        print(f'{self.user.display_name} has connected to Discord!')
    
    async def on_message(self, message):
        print(message.content)
        if message.content.lower()=="hello":
            if message.author.id ==220617008436346880:
                await message.channel.send("Bonjour Père")
            else:
                await message.channel.send("Bonjour "+ message.author.display_name)
pyBotSon = PyBot()
"""

pyBotSon = commands.Bot(command_prefix="!")

@pyBotSon.event
async def on_ready():
        print(f'{pyBotSon.user.display_name} has connected to Discord!')

@pyBotSon.listen()
async def on_message(message):
    #print(message.content)
    if message.content.lower()=="hello":
        if message.author.id ==220617008436346880:
            await message.channel.send("Bonjour Père")
        else:
            await message.channel.send("Bonjour "+ message.author.display_name)

class PyBotCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='test')
    async def test(self, ctx):
        await ctx.send("test OK")
    
    @commands.command(name='del')
    async def delete(self, ctx, number_of_messages: int):#ctx contexte #number_of_messages -> paramètre n°1 de type int
        messages = await ctx.channel.history(limit=number_of_messages + 1).flatten()
        for each_message in messages:
            await each_message.delete()
    
    @commands.command(name='joke')
    async def joke(self, ctx):
        r = requests.get('https://www.cyanidevf.fr/image-aleatoire/')
        image = re.findall('src=\"(https://www.cyanidevf.fr/wp-content/uploads/[0-9]*/[0-9]*/[a-z]*[-]?[0-9]?[.]png)',str(r.content))[0]
        await ctx.send(image)
        
    @commands.command(name='')
    async def fonction(self, ctx):
        
        await ctx.send("en maintenance")


pyBotSon.add_cog(PyBotCommand(pyBotSon))
pyBotSon.run(os.getenv("TOKEN"))