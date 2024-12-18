import discord
import random
from discord.ext import commands
import os

token = ""

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)


def pass_gen(pass_length):
    pass_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@"
    pass_string = ""
    for i in range(pass_length):
        pass_string += random.choice(pass_characters)
    return pass_string


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")


@bot.command()
async def coin(ctx):
    await ctx.send(random.choice(["Орел", "Решка"]))


@bot.command()  # $password 12
async def password(ctx, count_characters=8):
    await ctx.send(pass_gen(count_characters))


@bot.command()
async def mem(ctx):
    path = os.path.abspath("images")
    memes_list = os.listdir(path)
    rand_meme = random.choice(memes_list)
    abs_path = os.path.join(path, rand_meme)
    with open(abs_path, "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


bot.run(token)
