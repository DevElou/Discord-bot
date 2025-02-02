import discord
from discord.ext import commands,tasks


class Tasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.print_online.start()
        self.print_in_voice.start()

    def cog_unload(self):
        self.print_online.cancel()
        self.print_in_voice.cancel()

    @tasks.loop(seconds=600)
    async def print_online(self):
        online_channel = self.bot.get_channel(self.bot.online_channel_id)
        counter_online = 0
        guild = self.bot.get_guild(self.bot.server_id)
        for member in guild.members:
            if (member.status == discord.Status.online or member.status == discord.Status.idle or member.status == discord.Status.dnd) and member.bot == False:
                counter_online += 1
        print(f"⇒Online count has been updated to {counter_online}")
        await online_channel.edit(name =f"⇒User Online: {counter_online}")

    #print user in voice
    @tasks.loop(seconds=600)
    async def print_in_voice(self):
        player_in_voice_channel = self.bot.get_channel(self.bot.player_in_voice_channel_id)
        counter_voice = 0
        guild = self.bot.get_guild(self.bot.server_id)
        for member in guild.members:
            if member.voice:
                counter_voice += 1  
        print(f"⇒Voice count has been updated to {counter_voice}")
        await player_in_voice_channel.edit(name =f"⇒User in voice: {counter_voice}")


async def setup(bot):
    await bot.add_cog(Tasks(bot))
    