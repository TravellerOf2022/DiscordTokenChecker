import discord
import tls_client
import base64
import os
import re
import asyncio
import time
import sys
from colorama import init, Fore, Style

# Initialize Colorama
init(autoreset=True)

TOKENS_FILE = "./tokens.txt"

# Animated Unicode 3D-style Banner for SELFCORD ORIGINALS
def animate_banner():
    banner = r"""

 ░▒▓███████▓▒░▒▓████████▓▒░▒▓█▓▒░      ░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓███████▓▒░  
░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
 ░▒▓██████▓▒░░▒▓██████▓▒░ ░▒▓█▓▒░      ░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
       ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
       ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓███████▓▒░░▒▓████████▓▒░▒▓████████▓▒░▒▓█▓▒░      ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░  
                                                                                                         
                                                                                                         
 ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░       ░▒▓███████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░▒▓█▓▒▒▓███▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░       ░▒▓██████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░ 
 ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░  
                                                                                                         
                                                                                                         


                          Token Checker
    """
    # Define a gradient of colors
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    # Animate the banner several times (cycle colors for a 3D animated feel)
    for i in range(20):
        color = colors[i % len(colors)]
        # Clear screen (works on Windows and Unix)
        os.system("cls" if os.name == "nt" else "clear")
        sys.stdout.write(color + banner + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(0.3)

# Initialize Discord Client without intents
class TokenChecker(discord.Client):
    def __init__(self, token, valid_tokens):
        super().__init__()
        self.token = token
        self.valid_tokens = valid_tokens

    async def on_ready(self):
        print(f"[VALID] {self.user} ({self.user.id}) is logged in.")
        self.valid_tokens.append(self.token)
        await self.close()

    async def on_error(self, event, *args, **kwargs):
        print(f"[ERROR] An error occurred in event {event}")

# Function to extract token from mixed formats
def extract_token(line):
    token_pattern = r"([A-Za-z\d._-]{24,})\.[\w-]+\.[\w-]+"
    match = re.search(token_pattern, line)
    return match.group(0) if match else None

# Load tokens from file
def load_tokens():
    if not os.path.exists(TOKENS_FILE):
        return []
    with open(TOKENS_FILE, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    return [extract_token(line) for line in lines if extract_token(line)]

# Spoofed request to Discord API using tls_client
def is_token_valid(token):
    session = tls_client.Session(client_identifier="chrome_114")
    headers = {
        "Authorization": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "X-Super-Properties": base64.b64encode(b'{"os":"Windows","browser":"Chrome","release_channel":"stable"}').decode(),
        "Content-Type": "application/json"
    }
    response = session.get("https://discord.com/api/v9/users/@me", headers=headers)
    return response.status_code == 200

# Async function to check a token (sequentially for stability)
async def check_token(token, valid_tokens):
    try:
        client = TokenChecker(token, valid_tokens)
        await client.start(token, reconnect=False)  # Ensures clean exit
    except discord.LoginFailure:
        print(f"[DEAD] {token[:20]}... (Invalid)")
    except discord.HTTPException as e:
        print(f"[ERROR] {token[:20]}... (HTTP Exception: {e})")
    except Exception as e:
        print(f"[ERROR] {token[:20]}... ({str(e)})")
    finally:
        await client.close()
        await asyncio.sleep(1)  # Delay to prevent rate limits

# Main function (Runs sequentially to avoid SSL issues)
async def main():
    animate_banner()  # Show the animated banner at startup

    tokens = load_tokens()
    valid_tokens = []

    for token in tokens:
        if is_token_valid(token):
            await check_token(token, valid_tokens)

    # Update valid tokens file
    with open(TOKENS_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(valid_tokens))
    print(f"\n[UPDATED] Saved {len(valid_tokens)} valid tokens.")

# Run script with proper event loop handling for Windows
if __name__ == "__main__":
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        print("\n[EXIT] Script interrupted.")
    except Exception as e:
        print(f"[FATAL ERROR] {e}")
    finally:
        loop.run_until_complete(asyncio.sleep(1))  # Allow cleanup
        loop.close()
