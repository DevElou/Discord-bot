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
        await ctx.send(f"Processing code in {language}...")
        code_response = ""
        try:
            code_response = self.openai.format_code(language, prompt)
        except Exception as e:
            code_response = f"An error occurred: {e}"
        await ctx.send(f"```{language}\n{code_response}```")
        return code_response
    
    

async def setup(bot):
    await bot.add_cog(AIChat(bot))
