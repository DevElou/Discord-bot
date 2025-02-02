import discord
from discord.ext import commands

import random
import src.annexe_fct as af


class BaseCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.bot.latency*1000)}ms")

    @commands.command(pass_context = True)
    async def join(self, ctx):
        try:
            channel = ctx.author.voice.channel
            voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
            if channel and voice == None:  # If the user is in a channel and the bot is not connected to a channel
                await ctx.send("J'arrive...")
                await channel.connect()

            else:
                await ctx.send("Désolé je suis déjà dans un channel")  # If the bot is already connected
        except AttributeError:
            return await ctx.send("L'utilisateur n'est pas connecté dans un channel")  # Error message

        
    @commands.command(pass_context = True)
    async def leave(self, ctx):
        try:
            voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
            if voice.is_connected():
                await voice.disconnect()
        except:
            print('Je ne suis pas connecté')

    @commands.command()
    async def roulette(self, ctx):
        channel = ctx.author.voice.channel  
        await self.join(ctx)
        await ctx.send("La roulette tourne...")
        player_in_voice = channel.members
        random_player = random.choice(player_in_voice)

        while random_player.bot:
            random_player = random.choice(player_in_voice)
        await af.decompte(3, 0, ctx)
        await ctx.send(f"Bisous {random_player.mention} <3")
        await af.kick_voice( random_player)

async def setup(bot):
    await bot.add_cog(BaseCommands(bot))
