#!/usr/bin/env python3
"""
KEY-BOT-T - A simple key management bot
Issue: I989
"""

class KeyBot:
    """Main KeyBot class for managing keys and bot operations"""
    
    def __init__(self):
        self.keys = {}
        self.name = "KEY-BOT-T"
        self.version = "1.0.0"
    
    def add_key(self, key_name, key_value):
        """Add a new key to the bot's storage"""
        if key_name in self.keys:
            return False, f"Key '{key_name}' already exists"
        self.keys[key_name] = key_value
        return True, f"Key '{key_name}' added successfully"
    
    def get_key(self, key_name):
        """Retrieve a key from the bot's storage"""
        if key_name not in self.keys:
            return None, f"Key '{key_name}' not found"
        return self.keys[key_name], "Key retrieved successfully"
    
    def remove_key(self, key_name):
        """Remove a key from the bot's storage"""
        if key_name not in self.keys:
            return False, f"Key '{key_name}' not found"
        del self.keys[key_name]
        return True, f"Key '{key_name}' removed successfully"
    
    def list_keys(self):
        """List all keys stored in the bot"""
        if not self.keys:
            return [], "No keys stored"
        return list(self.keys.keys()), f"Found {len(self.keys)} key(s)"
    
    def get_info(self):
        """Get bot information"""
        return {
            "name": self.name,
            "version": self.version,
            "key_count": len(self.keys)
        }


def main():
    """Main entry point for the KEY-BOT-T"""
    bot = KeyBot()
    print(f"Welcome to {bot.name} v{bot.version}")
    print("A simple key management bot (Issue I989)")
    print("\nBot initialized successfully!")
    print(f"Current key count: {len(bot.keys)}")


if __name__ == "__main__":
    main()
