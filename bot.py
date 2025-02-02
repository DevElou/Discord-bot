import discord
from discord.ext import commands
import yaml
from colorama import Fore, Style
from discord.utils import get

#open config file
try:
    with open('config.yml', 'r') as file:
        conf = yaml.safe_load(file)
    print(f"{Fore.GREEN}✅ Config file loaded successfully!{Style.RESET_ALL}")
except FileNotFoundError:
    print("Config file not found. Please create a config.yml file in the same directory as main.py")

initial_extensions: list[str] = [
    "cogs.tasks",           # tasks.py
    "cogs.ai_chat",         # ai_chat.py
    "cogs.base_commands",   # base_commands.py
]

class AlainBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=conf['bot']['prefix'], intents=discord.Intents.all())
        self.server_id = conf['bot']['server_id']
        self.conf = conf
        self.prefix = conf['bot']['prefix']
        self.log_channel_id = conf['bot']['log_channel_id']
        self.general_channel_id = conf['bot']['general_channel']
        self.online_status = conf['bot']['Online_Status']
        self.online_channel_id = conf['bot']['Online_channel_id']
        self.player_in_voice = conf['bot']['Player_in_voice']
        self.player_in_voice_channel_id = conf['bot']['Player_in_voice_channel_id']
        self.general_channel = self.get_channel(self.general_channel_id)
    
    
    async def setup_hooks(self):
        print(f"{Fore.CYAN}🔗 Setting up hooks...{Style.RESET_ALL}")
        try:
            for extension in initial_extensions:
                print(f"{Fore.CYAN}🔗 Loading {extension}...{Style.RESET_ALL}")
                await self.load_extension(extension)
                print(f"{Fore.GREEN}[✔] Extension {extension} loaded successfully!{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}❌ Failed to load {extension}: {e}{Style.RESET_ALL}")
            
        
        #print(f"{Fore.GREEN}[✔] Hooks loaded!{Style.RESET_ALL}")

    
    async def on_ready(self):
        await self.setup_hooks()
        print("🤖✅ Bot is ready! 🚀")

        
    async def on_member_join(member):
        role = discord.utils.get(member.guild.roles, name="camarade")
        await member.add_roles(role)
    


if __name__ == '__main__':
    bot = AlainBot()
    bot.run(conf['bot']['token'])
    