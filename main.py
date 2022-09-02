import discord
import random
import os
from discord.commands import Option

Regel = "Rate eine Zahl zwischen 1 und 100"
Zufall = random.randint(1,100)
Versuche = 0
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
    print(Zufall)

@bot.slash_command(name="rate", description="Rate eine Zahl", guild_ids=[1011591245505761350])
async def rate(ctx, zahl: discord.Option(discord.SlashCommandOptionType.integer)):
    global Zufall
    global Versuche
    if zahl < Zufall:
        await ctx.respond("Zu Klein")
        Versuche = Versuche + 1
        if Versuche == 5:
            if Zufall > 50:
                await ctx.send("Die Zahl ist größer als 50")
            else:
                await ctx.send("Die Zahl ist kleiner als 50")
    if zahl > Zufall:
        await ctx.respond("Zu Groß")
        Versuche = Versuche + 1
        if Versuche == 5:
            if Zufall > 50:
                await ctx.send("Die Zahl ist größer als 50")
            else:
                await ctx.send("Die Zahl ist kleiner als 50")
    if zahl == Zufall:
        await ctx.respond("Richtig!!")
        Versuche = 0
        Zufall = random.randint(1, 100)
        await ctx.send("Neue Zahl")
        print(Zufall)



@bot.slash_command(name="regeln", description="erklärt die Regeln", guild_ids=[1011591245505761350])
async def regeln(ctx):
    await ctx.respond(Regel)

@bot.slash_command(name="github", description="Zeigt die GitHub Page vom Bot", guild_ids=[1011591245505761350])
async def github(ctx):
    await ctx.respond("Hier ist meine Github Page: https://github.com/Kokoio01/Zahlenspielbot")

bot.run("MTAxNDkxMDQyNDQ2Mzk3ODUzNg.GWQmM_.BRtI15WWMh4to-sp1hsuH9wQfxR3HeCcnNvWQs")
