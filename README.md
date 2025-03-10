# SELFCORD ORIGINALS Token Checker 🚀🔐

Welcome to **SELFCORD ORIGINALS Token Checker**! This tool is designed to help you verify Discord tokens by attempting to log in via Discord’s API. It features an animated 3D-style banner, asynchronous token validation, and is ready to be obfuscated for extra security. 😎💥

---

## Overview ✨
The **SELFCORD ORIGINALS Token Checker** is a Python script that:
- Reads Discord tokens from a file (`tokens.txt`)
- Uses Discord API (via `discord.py-self`) and a spoofed TLS request (with `tls_client`) to verify tokens
- Displays an awesome animated 3D-style banner using `Colorama`
- Outputs valid tokens back to the file  
  
This script is built with portability and security in mind. It’s perfect for anyone who needs to verify tokens and protect their code.

---

## Features 💎
- **Animated Banner:** Enjoy a colorful, 3D-style banner animation on startup! 🎨
- **Asynchronous Processing:** Efficiently checks tokens using Python’s `asyncio`.
- **Token Extraction:** Uses regex to automatically extract tokens from various text formats.
- **Extensible & Customizable:** Easily modify or extend the script to suit your needs.

---

## Requirements 📦
- **Python 3.10+**
- [discord.py](https://pypi.org/project/discord.py-self/)
- [tls_client](https://pypi.org/project/tls-client/)
- [Colorama](https://pypi.org/project/colorama/)

---

## Installation 🛠️
1. **Clone or Download the Repository:**
   ```bash
   git clone https://github.com/TravellerOf2022/TokenChecker.git
   cd TokenChecker
