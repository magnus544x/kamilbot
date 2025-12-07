import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot online jako {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)} ms 🏓")

@bot.command()
async def test(ctx):
    await ctx.send("Działa 24/7 na Railway! 🚀")


bot.run("MTM5ODAyOTgxNzk5NTMyOTU5Nw.GO-CLQ.n_bYmTcCrL4Ckpesw4DxHntcj_0W1daHaIC_OU")   # ← tutaj wklejasz nowy token (za chwilę bezpiecznie)
