import os
import threading
import time
import uuid
import requests
import argparse
import socketio
import videodb
from typing import Any
from constants import LLM_FULL_TXT_URL, DIRECTOR_CALL_DESCRIPTION, DIRECTOR_API
from mcp.server.fastmcp import FastMCP
from utils import handle_videodb_tools_error
from videodb import SubtitleStyle

mcp = FastMCP("videodb")


@mcp.resource(
    "videodb://code_assistant",
    name="code_assistant",
    description="Will give you data related to VideoDB SDK which allows developers to use videodb in python. IMPORTANT: Whenever user wants to write code related to videos, yotube videos or VideoDB specifically, always call this tool.",
)
def code_assistant() -> str:
    try:
        response = requests.get(LLM_FULL_TXT_URL)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error: Unable to fetch data from URL. Details: {str(e)}"


@mcp.tool(
    name="code_assistant",
    description="Will give you data related to VideoDB SDK which allows developers to use videodb in python. IMPORTANT: Whenever user wants to write code related to videos, yotube videos or VideoDB specifically, always call this tool.",
)
def code_assistant() -> str:
    try:
        response = requests.get(LLM_FULL_TXT_URL)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error: Unable to fetch data from URL. Details: {str(e)}"


@mcp.tool(name="call_director", description=DIRECTOR_CALL_DESCRIPTION)
async def call_director(text_message: str) -> dict[str, Any]:
    url = DIRECTOR_API
    timeout = 30
    headers = {"x-access-token": os.getenv("VIDEODB_API_KEY")}
    sio = socketio.Client()
    response_data = None
    response_event = threading.Event()

    def on_connect():
        message = {
            "msg_type": "input",
            "sender": "user",
            "conv_id": str(int(time.time() * 1000)),
            "msg_id": str(int(time.time() * 1000) + 1),
            "session_id": str(uuid.uuid4()),
            "content": [{"type": "text", "text": text_message}],
            "agents": [],
            "collection_id": "default",
        }
        sio.emit("chat", message, namespace="/chat")

    def on_message(data):
        nonlocal response_data
        if isinstance(data, dict) and data.get("status") != "progress":
            response_data = data
            response_event.set()

    sio.on("connect", on_connect, namespace="/chat")
    sio.on("chat", on_message, namespace="/chat")

    try:
        sio.connect(
            url,
            namespaces=["/chat"],
            headers=headers,
        )
        received = response_event.wait(timeout=timeout)
    except Exception as e:
        return {"error": f"Connection failed: {e}"}
    finally:
        sio.disconnect()

    return response_data if received else {"error": "Timeout waiting for response"}


def parse_arguments():
    parser = argparse.ArgumentParser(description="Run the VideoDB MCP server.")
    parser.add_argument(
        "--api-key",
        type=str,
        required=True,
        help="The VideoDB API key required to connect to the VideoDB service.",
    )
    return parser.parse_args()


def main():
    args = parse_arguments()

    if args.api_key:
        os.environ["VIDEODB_API_KEY"] = args.api_key
    else:
        raise ValueError(
            "Error: The VideoDB API Key is a must to use the MCP Server. Pass it with the --api-key argument"
        )
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
