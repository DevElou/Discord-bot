import discord
from discord.ext import commands
from src.openai_integration import OpenAIIntegration


class AIChat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.openai_key = bot.conf['openai']['api_key']
        self.openai = OpenAIIntegration(self.openai_key)
        
    @commands.hybrid_command()
    async def code(self, ctx, language, *, prompt):
        if (language is None or prompt is None):
            await ctx.send("Please provide a language and a prompt.")
        print(f"{ctx.author} requested code in {language} for the following prompt: {prompt}")
        await ctx.send(f"Processing code in {language}...")
        code_response = ""
        try:
            code_response = self.openai.format_code(language, prompt)
        except Exception as e:
            code_response = f"An error occurred: {e}"
        await ctx.send(f"```{language}\n{code_response}```")
        return code_response
    

    @commands.hybrid_command()
    async def trad(self, ctx, language, *, prompt):
        if (language is None or prompt is None):
            await ctx.send("Please provide a language and a prompt.")

        print(f"{ctx.author} requested a translation from {language} for the following prompt: {prompt}")
        await ctx.send("Translating...")
        translation = ""
        try:
            translation = self.openai.translate(language, prompt)
        except Exception as e:
            translation = f"An error occurred: {e}"
        await ctx.send(f"```{translation}```")
        return translation
    

async def setup(bot):
    await bot.add_cog(AIChat(bot))
