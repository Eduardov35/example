import random
import discord
from discord.ext import commands
from bot_logic import gen_pass
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def copia(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def suma(ctx, arg1, arg2):
    await ctx.send(int(arg1) + int(arg2))
    
@bot.command()
async def multiplicar(ctx, arg1, arg2):
    await ctx.send(int(arg1) * int(arg2))

@bot.command()
async def resta(ctx, arg1, arg2):
    await ctx.send(int(arg1) - int(arg2))  
    
@bot.command()
async def dividir(ctx, arg1, arg2):
    await ctx.send(int(arg1) // int(arg2))
    
@bot.command()
async def numazar(ctx, arg1, arg2):
    await ctx.send(random.randint(int(arg1), int(arg2)))
    

bot.run("MTE1NTIwMDA0NjQ4MTAyMzAwMQ.G9_3uR.qD4t0nTlcn4QjzrgJUkmEL1DW08odb6GY1Ie_0")
