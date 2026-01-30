# KEY-BOT-T

A simple key management bot implemented for Issue I989.

## Overview

KEY-BOT-T is a Python-based bot that provides basic key management functionality. It allows you to:
- Add keys with values
- Retrieve keys
- Remove keys
- List all stored keys

**⚠️ Security Notice**: This is a simple in-memory implementation intended for educational purposes. All data is stored in plain text in memory and is lost when the program exits. **DO NOT use this for storing sensitive credentials or production data.**

## Installation

No external dependencies are required. Simply clone the repository:

```bash
git clone https://github.com/fakherddit/KEY-BOT-T.git
cd KEY-BOT-T
```

## Usage

### Basic Usage

Run the bot:

```bash
python keybot.py
```

### Using as a Module

```python
from keybot import KeyBot

# Create a bot instance
bot = KeyBot()

# Add a key
success, message = bot.add_key("api_key", "your-secret-key")
print(message)

# Get a key
value, message = bot.get_key("api_key")
print(f"Key value: {value}")

# List all keys
keys, message = bot.list_keys()
print(f"Keys: {keys}")

# Remove a key
success, message = bot.remove_key("api_key")
print(message)

# Get bot info
info = bot.get_info()
print(f"Bot: {info['name']} v{info['version']}")
```

## Features

- ✅ Simple key-value storage
- ✅ Add, get, remove, and list operations
- ✅ No external dependencies
- ✅ Clean Python implementation
- ✅ Issue I989 implementation

## Development

This project was created to address Issue I989.

## License

MIT License