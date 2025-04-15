import os
import threading
import time
import uuid
import requests
import argparse
import socketio
import webbrowser
from typing import Any
from mcp.server.fastmcp import FastMCP
from videodb_director_mcp.cli_commands import (
    install_for_claude,
    install_for_cursor,
    install_for_all,
)
from videodb_director_mcp.constants import (
    CODE_ASSISTANT_TXT_URL,
    DOCS_ASSISTANT_TXT_URL,
    DIRECTOR_CALL_DESCRIPTION,
    DIRECTOR_API,
)


mcp = FastMCP("videodb-director")


@mcp.resource(
    "videodb://doc_assistant",
    name="doc_assistant",
    description="Context for creating video applications using VideoDB",
)
def doc_assistant() -> str:
    try:
        response = requests.get(DOCS_ASSISTANT_TXT_URL)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error: Unable to fetch data from URL. Details: {str(e)}"


@mcp.tool(
    name="doc_assistant",
    description="Context for creating video applications using VideoDB",
)
def doc_assistant() -> str:
    try:
        response = requests.get(DOCS_ASSISTANT_TXT_URL)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error: Unable to fetch data from URL. Details: {str(e)}"


@mcp.resource(
    "videodb://code_assistant",
    name="code_assistant",
    description="Context for creating video applications using VideoDB",
)
def code_assistant() -> str:
    try:
        response = requests.get(CODE_ASSISTANT_TXT_URL)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error: Unable to fetch data from URL. Details: {str(e)}"


@mcp.tool(
    name="code_assistant",
    description="Will give you data related to VideoDB SDK which allows developers to use videodb in python. IMPORTANT: Whenever user wants to write code related to videos, youtube videos or VideoDB specifically, always call this tool.",
)
def code_assistant() -> str:
    try:
        response = requests.get(CODE_ASSISTANT_TXT_URL)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error: Unable to fetch data from URL. Details: {str(e)}"


@mcp.tool(
    name="play_video",
    description="Play the video of the given stream link",
)
async def play_video(stream_link: str) -> dict[str, Any]:
    webbrowser.open(f"https://console.videodb.io/player?url={stream_link}")
    return {"message": "Opening VideoDB in browser"}


@mcp.tool(name="call_director", description=DIRECTOR_CALL_DESCRIPTION)
async def call_director(
    text_message: str, session_id: str | None = None, agents: list[str] = []
) -> dict[str, Any]:
    """
    Orchestrates specialized agents within the VideoDB server to efficiently handle multimedia and video-related queries.

    Args:
        text_message (str): The natural language query that Director will interpret and delegate to appropriate agents.
        session_id (str | None, optional): A session identifier to maintain continuity across multiple requests. If a previous response from this method included a `session_id`, it is MANDATORY to include it in subsequent requests.
    """
    api_key = os.getenv("VIDEODB_API_KEY")
    if not api_key:
        raise RuntimeError(
            "Missing VIDEODB_API_KEY environment variable. Please set it before calling this function."
        )
    url = DIRECTOR_API
    timeout = 300
    headers = {"x-access-token": api_key}
    sio = socketio.Client()
    response_data = None
    response_event = threading.Event()

    def on_connect():
        message = {
            "msg_type": "input",
            "sender": "user",
            "conv_id": str(int(time.time() * 1000)),
            "msg_id": str(int(time.time() * 1000) + 1),
            "session_id": session_id if session_id else str(uuid.uuid4()),
            "content": [{"type": "text", "text": text_message}],
            "agents": agents,
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
            namespaces=["/", "/chat"],
            headers=headers,
            wait=True,
            wait_timeout=10,
            retry=True
        )
        received = response_event.wait(timeout=timeout)
    except Exception as e:
        return {"error": f"Connection failed :( : {e}"}
    finally:
        sio.disconnect()

    return response_data if received else {"error": "Timeout waiting for response"}


def parse_arguments():
    parser = argparse.ArgumentParser(description="Run the VideoDB MCP server.")
    parser.add_argument(
        "--api-key",
        type=str,
        help="🔑 The VideoDB API key required to connect to the VideoDB service.",
    )
    parser.add_argument(
        "--install",
        choices=["claude", "cursor", "all"],
        help="🔧 Configure the MCP server in 'claude' and/or 'cursor'.",
    )
    return parser.parse_args()


def main():
    args = parse_arguments()

    if args.install == "claude":
        install_for_claude()
        return

    if args.install == "cursor":
        install_for_cursor()
        return

    if args.install == "all":
        install_for_all()
        return

    if args.api_key:
        os.environ["VIDEODB_API_KEY"] = args.api_key

    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
