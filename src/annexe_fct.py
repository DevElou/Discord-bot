import discord
import time


async def kick_voice( member:discord.Member):
    await member.move_to(None)

async def decompte(form:int, to:int, ctx):
    for i in range(form, to, -1):
        await ctx.send(i)
        time.sleep(1)