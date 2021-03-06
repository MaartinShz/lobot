import os
import requests
import random

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

pyBotSon = commands.Bot(command_prefix="$")

@pyBotSon.event         
async def on_ready():
        print(f'{pyBotSon.user.display_name} has connected to Discord!')
    
async def on_message(message):
    print(message.content)
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
    async def dele(self, ctx, number_of_messages: int):#ctx contexte #number_of_messages -> paramètre n°1 de type int
        messages = await ctx.channel.history(limit=number_of_messages + 1).flatten()
        for each_message in messages:
            await each_message.delete()
    
    @commands.command(name='joke')
    async def joke(self, ctx):
        #r = requests.get('')
        await ctx.send("en maintenance")
        #await ctx.send(file=File('my_file.png'))

    @commands.command(name='dicksize')
    async def dicksize(self, ctx):
        #r = requests.get('')
        await ctx.send(random.randrange(8,28))
        #await ctx.send(file=File('my_file.png'))

pyBotSon.add_cog(PyBotCommand(pyBotSon))
pyBotSon.run(os.getenv("TOKEN"))