import json
import os
import platform
from pathlib import Path

def get_api_key() -> str:
    """Prompt the user for their VideoDB MCP API key."""
    print("\n🔑 VideoDB API Key is required for advanced functionality.")
    print("🌐 Get your API key at: https://console.videodb.io/dashboard")
    print("Note: You can leave this empty, but the 'call_director' tool will not be available.\n")
    
    return input("Enter your VideoDB API Key (or press Enter to skip): ").strip()


def load_config(config_path: Path) -> dict:
    """Load configuration from a file, returning an empty dict if unreadable or missing."""
    config_path.parent.mkdir(parents=True, exist_ok=True)
    if config_path.exists():
        try:
            with config_path.open("r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"⚠️ Failed to parse JSON config at: {config_path} — falling back to empty config.")
            return {}   
    print(f"📁 No config file found at: {config_path} — creating a new one.") 
    return {}


def save_config(config_path: Path, config_data: dict) -> None:
    """Save configuration data to a file."""
    with config_path.open("w", encoding="utf-8") as f:
        json.dump(config_data, f, indent=4)


def get_config_path(app: str) -> Path:
    """Return the appropriate config path based on platform and app."""
    if platform.system() == "Windows":
        if app == "claude":
            return Path(os.getenv("APPDATA")) / "Claude" / "claude_desktop_config.json"
        return Path(os.getenv("USERPROFILE")) / ".cursor" / "mcp.json"
    else:
        if app == "claude":
            return Path.home() / "Library" / "Application Support" / "Claude" / "claude_desktop_config.json"
        return Path.home() / ".cursor" / "mcp.json"


def create_mcp_entry(api_key: str, stdio: bool = False) -> dict:
    """Create the MCP server entry config."""
    entry = {
        "command": "uvx",
        "args": ["videodb-director-mcp"]
    }
    if api_key:
        entry["env"] = {"VIDEODB_API_KEY" : api_key}
    if stdio:
        entry["type"] = "stdio"
    return entry


def save_mcp_config(app: str, api_key: str) -> None:
    """Save MCP config for Claude or Cursor."""
    config_path = get_config_path(app)
    config_data = load_config(config_path)
    mcp_servers = config_data.get("mcpServers", {})
    mcp_servers["videodb-director"] = create_mcp_entry(api_key, stdio=(app == "cursor"))
    config_data["mcpServers"] = mcp_servers

    save_config(config_path, config_data)


def install_for_claude() -> None:
    """Install videodb-director-mcp for Claude Desktop."""
    api_key = get_api_key()
    save_mcp_config("claude", api_key)
    print("\n🎉 Claude Desktop configuration complete!")
    print("🔁 Please restart Claude Desktop to apply changes.")
    print("🚀 Enjoy supercharged video capabilities!\n")


def install_for_cursor() -> None:
    """Install videodb-director-mcp for Cursor IDE."""
    api_key = get_api_key()
    save_mcp_config("cursor", api_key)
    print("\n🎉 Cursor IDE configuration complete!")
    print("✅ videodb-director is now available in Cursor.")
    print("🚀 Enjoy supercharged video capabilities!\n")


def install_for_all() -> None:
    """Install videodb-director-mcp for all clients. Currently they are: Claude and Cursor IDE."""
    api_key = get_api_key()
    save_mcp_config("claude", api_key)
    save_mcp_config("cursor", api_key)
    print("\n🎉 Configuration for Claude and Cursor completed successfully!")
    print("🔁 Please restart Claude Desktop to apply changes.")
    print("🚀 Enjoy supercharged video capabilities!\n")
