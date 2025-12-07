import discord
import os
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

# <<< TU WSZYSTKIE KANAŁY Z TWOJEJ LISTY >>>
channels = [
    ("ttvonline1_tvhd1", "https://security.freefreaks.top/ttvonline1_tvhd1.m3u8"),
    ("TVN", "https://security.freefreaks.top/tvn.m3u8"),
    ("Polsat", "https://security.freefreaks.top/polsuper_sdtv.m3u8"),
    ("TVP 2", "https://security.freefreaks.top/tvp2_Hdtvts.m3u8"),
    ("TVN24", "https://security.freefreaks.top/tvn24najlepszyt.m3u8"),
    ("TVP 1 HD", "https://security.freefreaks.top/tvp_1hdtvd.m3u8"),
    ("Puls 2", "https://security.freefreaks.top/pulstv.m3u8"),
    ("Top Kids TV", "https://security.freefreaks.top/top_kidstvhdtvhtv2.m3u8"),
    ("TVP 3", "https://security.freefreaks.top/czworkatv.m3u8"),
    ("TV Seriale 24", "https://security.freefreaks.top/tv_serial24taws.m3u8"),
    ("TVP 2 HD", "https://security.freefreaks.top/tvp_2_hdtteoa.m3u8"),
    ("Turbomaniak TV", "https://security.freefreaks.top/turbomaniak_tvhd.m3u8"),
    ("T7 HD", "https://security.freefreaks.top/t7hd.m3u8"),
    ("Eleven Sports 1", "https://security.freefreaks.top/elevenspo1.m3u8"),
    ("Polsat Film HD", "https://security.freefreaks.top/polsatfilmhdtv.m3u8"),
    ("Kino Polska", "https://security.freefreaks.top/kino_polska_tv.m3u8"),
    ("TVS", "https://security.freefreaks.top/tvs_tv2.m3u8"),
    ("TVP Sport", "https://security.freefreaks.top/sportTVP_channeed.m3u8"),
    # ← możesz dodać resztę, jak chcesz (ja wkleiłem tylko początek, żeby nie było za długo)
]

@bot.event
async def on_ready():
    print(f"Bot online jako {bot.user} – {len(channels)} kanałów gotowych!")

@bot.command()
async def lista(ctx):
    tekst = "\n".join([f"`{i+1}.` {name}" for i, (name, url) in enumerate(channels)])
    embed = discord.Embed(title="Dostępne kanały IPTV", description=tekst, color=0x00ff00)
    await ctx.send(embed=embed)

@bot.command()
async def play(ctx, nr: int):
    if nr < 1 or nr > len(channels):
        return await ctx.send(f"Podaj numer od 1 do {len(channels)}")

    if not ctx.author.voice:
        return await ctx.send("Wejdź na kanał głosowy!")

    name, url = channels[nr-1]
    vc = await ctx.author.voice.channel.connect()

    await ctx.send(f"Odtwarzam: **{name}**")

    vc.play(discord.FFmpegPCMAudio(url, before_options="-re -stream_loop -1"))
    while vc.is_playing() or vc.is_paused():
        await asyncio.sleep(1)
    await vc.disconnect()

@bot.command()
async def stop(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("Zatrzymano")

bot.run(os.getenv("TOKEN"))
