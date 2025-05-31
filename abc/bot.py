import sqlite3
import discord
from discord.ext import commands
from logic import DB_Manager
bot = commands.Bot(command_prefix='-', intents=discord.Intents.all())
manager = DB_Manager("Air_Quality.db")
@bot.event
async def on_ready():
    print(f'Bot hazır! {bot.user} olarak giriş yapıldı.')
@bot.command()
async def selam(ctx):
    await ctx.send(f'Selam.')

@bot.command()
async def city(ctx,a123):
    sonuc = manager.city_search(a123)
    for i in sonuc:
        await ctx.send(i)
@bot.command()
async def NO2(ctx,b123):
    sonuc = manager.city_search(b123)
    await ctx.send(sonuc)

@bot.command()
async def SO2(ctx,c123):
    sonuc = manager.city_search(c123)
    await ctx.send(sonuc)

@bot.command()
async def O3(ctx,d123):
    sonuc = manager.city_search(d123)
    await ctx.send(sonuc)



bot.run("MTM3ODQwOTkzMzIxMjQ4NzcxMA.GC_w9b.-pA8SqPd5-1alkts8Yd93oGadaSLmzeVAz-TXw")
    