# ----- Imports ----- #
import discord
import json
import os
import time
import random
import requests
import getpass

# ----- From Imports ----- #
from datetime import datetime
from colorama import Fore, Style
from pystyle import Write, System, Colors, Colorate, Anime
from discord.ext import tasks
from threading import Thread
from itertools import cycle
from shutil import get_terminal_size

# ----- Variables ----- #
CONFIG_PATH = 'config.json'
TOKEN_PATH = 'tokens.txt'
SERVERS_PATH = 'servers.json'
PROXIES_PATH = 'proxies.txt'
username = getpass.getuser()

# ----- Logging Class ----- #
class Logger:
    def __init__(self, prefix: str = ".gg/bestnitro"):
        self.WHITE = "\u001b[37m"
        self.MAGENTA = "\033[38;5;97m"
        self.MAGENTAA = "\033[38;2;157;38;255m"
        self.RED = "\033[38;5;196m"
        self.GREEN = "\033[38;5;40m"
        self.YELLOW = "\033[38;5;220m"
        self.BLUE = "\033[38;5;21m"
        self.PINK = "\033[38;5;176m"
        self.CYAN = "\033[96m"
        self.prefix = f"{self.PINK}[{self.MAGENTA}{prefix}{self.PINK}] "

    def message3(self, level: str, message: str, start: int = None, end: int = None) -> str:
        time = self.get_time()
        return f"{self.prefix}[{self.MAGENTAA}{time}{self.PINK}] {self.PINK}[{self.CYAN}{level}{self.PINK}] -> {self.CYAN}{message}{Fore.RESET}"

    def get_time(self) -> str:
        return datetime.now().strftime("%H:%M:%S")

    def success(self, message: str, start: int = None, end: int = None, level: str = "Success") -> None:
        print(self.message3(f"{self.GREEN}{level}", f"{self.GREEN}{message}", start, end))

    def failure(self, message: str, start: int = None, end: int = None, level: str = "Failure") -> None:
        print(self.message3(f"{self.RED}{level}", f"{self.RED}{message}", start, end))
    
    def warning(self, message: str, start: int = None, end: int = None, level: str = "Warning") -> None:
        print(self.message3(f"{self.YELLOW}{level}", f"{self.YELLOW}{message}", start, end))

    def message(self, level: str, message: str, start: int = None, end: int = None) -> None:
        time = self.get_time()
        if start is not None and end is not None:
            print(f"{self.prefix}[{self.MAGENTAA}{time}{self.PINK}] {self.PINK}[{self.CYAN}{level}{self.PINK}] -> {Fore.RESET} {self.CYAN}{message}{Fore.RESET} [{Fore.CYAN}{end - start}s{Style.RESET_ALL}]")
        else:
            print(f"{self.prefix}[{self.MAGENTAA}{time}{self.PINK}] [{Fore.BLUE}{level}{self.PINK}] -> {Fore.RESET} {self.CYAN}{message}{Fore.RESET}")
    
    def message2(self, level: str, message: str, start: int = None, end: int = None) -> None:
        time = self.get_time()
        if start is not None and end is not None:
            print(f"{self.prefix}[{self.MAGENTAA}{time}{self.PINK}] {self.PINK}[{self.CYAN}{level}{self.PINK}] -> {Fore.RESET} {self.CYAN}{message}{Fore.RESET} [{Fore.CYAN}{end - start}s{Style.RESET_ALL}]", end="\r")
        else:
            print(f"{self.prefix}[{self.MAGENTAA}{time}{self.PINK}] {self.PINK}[{Fore.BLUE}{level}{self.PINK}] -> {Fore.RESET} {self.CYAN}{message}{Fore.RESET}", end="\r")

    def question(self, message: str, start: int = None, end: int = None) -> None:
        time = self.get_time()
        i = input(f"{self.prefix}[{self.MAGENTAA}{time}{self.PINK}] {Fore.RESET} {self.PINK}[{Fore.BLUE}?{self.PINK}] -> {Fore.RESET} {self.CYAN}{message}{Fore.RESET}")
        return i

    def info(self, message: str, start: int = None, end: int = None) -> None:
        time = self.get_time()
        print(f"{self.prefix}[{self.MAGENTAA}{time}{self.PINK}] {Fore.RESET} {self.PINK}[{Fore.BLUE}!{self.PINK}] -> {Fore.RESET} {self.CYAN}{message}{Fore.RESET}")
    
    def debug(self, message: str, start: int = None, end: int = None) -> None:
            time = self.get_time()
            print(f"{self.prefix}[{self.MAGENTAA}{time}{self.PINK}] {Fore.RESET} {self.PINK}[{Fore.YELLOW}DEBUG{self.PINK}] -> {Fore.RESET} {self.GREEN}{message}{Fore.RESET}")

log = Logger()
class Loader:
    def __init__(self, desc="Loading...", end="\r", timeout=0.1):
        self.desc = desc
        self.end = end
        self.timeout = timeout
        self.time = datetime.now().strftime("%H:%M:%S")

        self._thread = Thread(target=self._animate, daemon=True)
        self.steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        self.done = False

    def start(self):
        self._thread.start()
        return self
    
    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{log.PINK}[{log.MAGENTA}.gg/bestnitro{log.PINK}] [{log.MAGENTAA}{self.time}{log.PINK}] {log.PINK}[{Fore.BLUE}Connection{log.PINK}] -> {Fore.RESET} {log.GREEN}{self.desc}{Fore.RESET} {c}", flush=True, end="")
            time.sleep(self.timeout)

    def __enter__(self):
        self.start()

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(f"\r{self.end}", flush=True)

    def __exit__(self, exc_type, exc_value, tb):
        # handle exceptions with those variables ^
        self.stop()

def home():
    os.system('cls' if os.name == 'nt' else 'clear')
    Write.Print(f"""
    \t\t   /$$$$$$   /$$                         /$$              /$$$$$$                            /$$                    
    \t\t  /$$__  $$ | $$                        | $$             /$$__  $$                          | $$                    
    \t\t | $$  \__//$$$$$$    /$$$$$$   /$$$$$$$| $$   /$$      | $$  \__/  /$$$$$$  /$$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$ 
    \t\t |  $$$$$$|_  $$_/   /$$__  $$ /$$_____/| $$  /$$/      |  $$$$$$  /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$ /$$__  $$
    \t\t  \____  $$ | $$    | $$  \ $$| $$      | $$$$$$/        \____  $$| $$$$$$$$| $$  \ $$| $$  | $$| $$$$$$$$| $$  \__/
    \t\t  /$$  \ $$ | $$ /$$| $$  | $$| $$      | $$_  $$        /$$  \ $$| $$_____/| $$  | $$| $$  | $$| $$_____/| $$      
    \t\t |  $$$$$$/ |  $$$$/|  $$$$$$/|  $$$$$$$| $$ \  $$      |  $$$$$$/|  $$$$$$$| $$  | $$|  $$$$$$$|  $$$$$$$| $$      
    \t\t  \______/   \___/   \______/  \_______/|__/  \__/       \______/  \_______/|__/  |__/ \_______/ \_______/|__/                                                                                                              
    \t\t             
    \t\t                                      Welcome {username} | discord.gg/bestnitro  
    \t\t                              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    \t\t  ════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════\n""", Colors.red_to_blue, interval=0.0000)

home()
class MyClient(discord.Client):
    def __init__(self, token, proxy=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.token = token
        self.proxy = self.format_proxy(proxy)
        self.config = self.load_config()
        self.debug = self.config.get("debug", False)
        self.servers = []
        self.load_servers()
        self.stock_messages = {}
        self.dm_reply = None
        self.use_different_messages = False
        self.stock_path = None
        self.min_delay = 1  # Minimum delay of 1 second
        self.slowmode_intervals = {}

        if self.debug:
            log.debug(f"Initialized MyClient with token: {token} and proxy: {proxy}")
            log.debug(f"Loaded configuration: {self.config}")

    def load_config(self):
        if os.path.exists(CONFIG_PATH):
            with open(CONFIG_PATH, 'r') as f:
                try:
                    config = json.load(f)
                    return config
                except json.JSONDecodeError as e:
                    log.failure(f"Error decoding JSON from {CONFIG_PATH}: {e}")
                    return {}
        else:
            return {}

    def load_servers(self):
        if os.path.exists(SERVERS_PATH):
            if self.debug:
                log.debug(f"Loading servers from {SERVERS_PATH}")
            with open(SERVERS_PATH, 'r') as f:
                try:
                    self.servers = json.load(f)
                    if not isinstance(self.servers, list):
                        log.warning(f"Expected a list but got {type(self.servers)} in {SERVERS_PATH}. Reinitializing.")
                        self.servers = []
                except json.JSONDecodeError as e:
                    log.warning(f"Error decoding JSON from {SERVERS_PATH} : {e}. Reinitializing.")
                    self.servers = []
        else:
            self.servers = []
        if self.debug:
            log.debug(f"Loaded servers: {self.servers}")

    def save_servers(self):
        if self.debug:
            log.debug(f"Saving servers to {SERVERS_PATH}")
        with open(SERVERS_PATH, 'w') as f:
            json.dump(self.servers, f, indent=4)

    async def send_stock_message(self, guild_id, channel_id, message):
        if self.debug:
            log.debug(f"Attempting to send message to Guild {guild_id} Channel {channel_id}")
        guild = self.get_guild(guild_id)
        if guild is None:
            self.log_to_webhook(f"Guild {guild_id} not found", error=True)
            log.failure(f"Guild {guild_id} not found")
            input('')
            return
        channel = guild.get_channel(channel_id)
        if channel is None:
            self.log_to_webhook(f"Channel {channel_id} not found in guild {guild.name}", error=True)
            log.failure(f"Channel {channel_id} not found in guild {guild.name}")
            input('')
            return
        try:
            await channel.send(message)
            self.log_to_webhook(f"Successfully sent message to {guild.name} ({guild_id}) - {channel.name} ({channel_id})", guild, channel)
            log.message("Success", f"Successfully sent message to {guild.name} ({guild_id}) - {channel.name} ({channel_id})")
        except discord.errors.HTTPException as e:
            self.log_to_webhook(f"Failed to send message to {guild.name} ({guild_id}) - {channel.name} ({channel_id}): {str(e)}", guild, channel, error=True)
            log.failure(f"Failed to send message to {guild.name} ({guild_id}) - {channel.name} ({channel_id}): {str(e)}")
        except Exception as e:
            self.log_to_webhook(f"Unexpected error while sending message to {guild.name} ({guild_id}) - {channel.name} ({channel_id}): {str(e)}", guild, channel, error=True)
            log.failure(f"Unexpected error while sending message to {guild.name} ({guild_id}) - {channel.name} ({channel_id}): {str(e)}")

    def log_to_webhook(self, message, guild=None, channel=None, error=False):
        if self.config.get("use_webhook", False):
            embed = {
                "title": "Stock Message Log",
                "description": message,
                "color": 0xff0000 if error else 0x00ff00,
                "thumbnail": {
                    "url": guild.icon.url if guild and guild.icon else ""
                },
                "fields": [
                    {"name": "Guild", "value": guild.name if guild else "N/A", "inline": True},
                    {"name": "Channel", "value": channel.name if channel else "N/A", "inline": True}
                ],
                "footer": {
                    "text": "Stock Message Sender",
                    "icon_url": self.user.avatar.url if self.user.avatar else ""
                }
            }
            requests.post(self.config["webhook_url"], json={"embeds": [embed]})
            if self.debug:
                log.debug('Sent message to webhook')
        else:
            log.debug(f"Message: {message}")

    @staticmethod
    def get_tokens():
        if os.path.exists(TOKEN_PATH):
            with open(TOKEN_PATH, 'r') as f:
                return [line.strip() for line in f]
        return []

    @staticmethod
    def format_proxy(proxy):
        if not proxy:
            return None

        if not proxy.startswith("http://"):
            proxy = "http://" + proxy

        if "@" not in proxy:
            return proxy

        user_pass, ip_port = proxy.split("@")
        user, password = user_pass.split(":")
        ip, port = ip_port.split(":")
        return f"http://{user}:{password}@{ip}:{port}"

    async def on_ready(self):
        if hasattr(self, 'loader'):
            self.loader.stop()  # Stop the loader when the client is ready

        home()
        log.message("Logged In", f'Logged in as {self.user} (ID: {self.user.id})')
        
            
        self.send_messages_loop.start()
        if self.debug:
            log.debug("Message sending loop started")

    def configure(self):
        use_saved = log.question("Use servers from servers.json? (y/n): ").lower() == 'y'
        if not use_saved:
            add_more = True
            while add_more:
                guild_id = int(log.question("Enter Guild ID: "))
                channel_id = int(log.question("Enter Channel ID: "))
                self.servers.append({"guild_id": guild_id, "channel_id": channel_id})
                add_more = log.question("Add another server? (y/n): ").lower() == 'y'
            save_to_file = log.question("Save servers to servers.json? (y/n): ").lower() == 'y'
            if save_to_file:
                self.save_servers()
        
        reply_to_dms = log.question("Reply to DMs? (y/n): ").lower() == 'y'
        if reply_to_dms:
            self.dm_reply = log.question("Enter the DM reply message: ")
        
        self.use_different_messages = log.question("Use different stock messages for different servers? (y/n): ").lower() == 'y'
        if self.use_different_messages:
            for server in self.servers:
                message_path = log.question(f"Enter the stock message or path for Guild {server['guild_id']} Channel {server['channel_id']}: ")
                self.stock_messages[(server['guild_id'], server['channel_id'])] = message_path
        else:
            self.stock_path = log.question("Enter the stock message or path: ")

        if self.debug:
            log.debug(f"Configuration completed. Servers: {self.servers}, DM reply: {self.dm_reply}, Use different messages: {self.use_different_messages}")

    def get_stock_message(self, guild_id=None, channel_id=None):
        if self.debug:
            log.debug(f"Getting stock message for Guild {guild_id} Channel {channel_id}")
        if self.use_different_messages and (guild_id, channel_id) in self.stock_messages:
            path_or_message = self.stock_messages[(guild_id, channel_id)]
        else:
            path_or_message = self.stock_path
        
        if os.path.exists(path_or_message):
            if self.debug:
                log.debug(f"Loading message from file: {path_or_message}")
            with open(path_or_message, 'r', encoding='utf-8') as f:
                return f.read()
        return path_or_message

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if isinstance(message.channel, discord.DMChannel) and self.dm_reply:
            await message.channel.send(self.dm_reply)
            if self.debug:
                log.debug(f"Sent DM reply to {message.author}")

    @tasks.loop(seconds=1)  # Check every second
    async def send_messages_loop(self):
        for server in self.servers:
            guild_id = server['guild_id']
            channel_id = server['channel_id']
            message = self.get_stock_message(guild_id, channel_id) if self.use_different_messages else self.get_stock_message()
            guild = self.get_guild(guild_id)
            if guild:
                channel = guild.get_channel(channel_id)
                if channel:
                    if (guild_id, channel_id) not in self.slowmode_intervals or time.time() >= self.slowmode_intervals[(guild_id, channel_id)]:
                        await self.send_stock_message(guild_id, channel_id, message)
                        self.slowmode_intervals[(guild_id, channel_id)] = time.time() + channel.slowmode_delay
                        if self.debug:
                            log.debug(f"Sent message to Guild {guild_id} Channel {channel_id} and updated slowmode interval")
                else:
                    log.failure(f"Channel {channel_id} not found in guild {guild_id}")
            else:
                log.failure(f"Guild {guild_id} not found")
def truncate_token(token, max_length=10):
    if len(token) > max_length:
        return token[:max_length] + '...'
    else:
        return token
def run_client_with_loader(token, proxy, debug):
    client = MyClient(token, proxy)
    client.configure()
    loader_message = f"Connecting to token {truncate_token(token)}... " if debug else "Connecting to token... "

    loader = Loader(loader_message)
    client.loader = loader  # Assign loader to the client instance

    try:
        with loader:
            if debug:
                client.run(token)
            else:
                client.run(token, log_handler=None)
    except Exception as e:
        log.failure(f"Failed to run client: {e}")


def run_clients(tokens, proxies):
    config = {}
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, 'r') as f:
            try:
                config = json.load(f)
            except json.JSONDecodeError as e:
                log.failure(f"Error decoding JSON from {CONFIG_PATH}: {e}")

    debug = config.get("debug", False)
    
    if len(tokens) == 1:
        token = tokens[0]
        proxy = random.choice(proxies) if proxies else None
        run_client_with_loader(token, proxy, debug)
    else:
        for token in tokens:
            proxy = random.choice(proxies) if proxies else None
            run_client_with_loader(token, proxy, debug)


if __name__ == "__main__":
    tokens = MyClient.get_tokens()
    proxies = []
    if os.path.exists(PROXIES_PATH):
        with open(PROXIES_PATH, 'r') as f:
            proxies = [line.strip() for line in f]
    run_clients(tokens, proxies)
