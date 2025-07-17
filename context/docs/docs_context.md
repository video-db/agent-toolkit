# Quick Start Guide [Source Link](https://docs.videodb.io/quick-start-guide-38)

VideoDB Documentation

Pages

[Welcome to VideoDB Docs](https://docs.videodb.io/)

[Quick Start Guide](https://docs.videodb.io/quick-start-guide-38)

[Visual Search and Indexing](https://docs.videodb.io/visual-search-and-indexing-80)

[Multimodal Search](https://docs.videodb.io/multimodal-search-90)

[Real‑Time Video Pipeline](https://docs.videodb.io/real-time-video-pipeline-113)

[Meeting Recording Agent Quickstart](https://docs.videodb.io/meeting-recording-agent-quickstart-115)

[How VideoDB Solves Complex Visual Analysis Tasks](https://docs.videodb.io/how-videodb-solves-complex-visual-analysis-tasks-112)

[Generative Media Quickstart](https://docs.videodb.io/generative-media-quickstart-110)

[Dynamic Video Streams](https://docs.videodb.io/dynamic-video-streams-44)

[VideoDB MCP Server](https://docs.videodb.io/videodb-mcp-server-109)

[Transcoding Quickstart](https://docs.videodb.io/transcoding-quickstart-114)

[Director - Video Agent Framework](https://docs.videodb.io/director-video-agent-framework-98)

[Open Source Tools](https://docs.videodb.io/open-source-tools-94)

[Examples and Tutorials](https://docs.videodb.io/examples-and-tutorials-35)

[Edge of Knowledge](https://docs.videodb.io/edge-of-knowledge-10)

[Building World's First Video Database](https://docs.videodb.io/building-worlds-first-video-database-25)

[Team](https://docs.videodb.io/team-46)

[Customer Love](https://docs.videodb.io/customer-love-42)

[Temp Doc](https://docs.videodb.io/temp-doc-54)

# Quick Start Guide

[Video Indexing Guide](https://docs.videodb.io/video-indexing-guide-101) [Semantic Search](https://docs.videodb.io/semantic-search-89) [How Accurate is Your Search?](https://docs.videodb.io/how-accurate-is-your-search-88) [Collections](https://docs.videodb.io/collections-68) [Public Collections](https://docs.videodb.io/public-collections-102) [Callback Details](https://docs.videodb.io/callback-details-66) [Ref: Subtitle Styles](https://docs.videodb.io/ref-subtitle-styles-57) [Language Support](https://docs.videodb.io/language-support-79) [Guide: Subtitles](https://docs.videodb.io/guide-subtitles-73)

This notebook is designed to help you get started with VideoDB. Advance concepts are linked in between for deep dive.

[![](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/video-db/videodb-cookbook/blob/main/quickstart/VideoDB%20Quickstart.ipynb)

## Setup

### 🔧 Installing VideoDB in your environment

VideoDB is available as

[python package 📦](https://pypi.org/project/videodb)

!pip install videodb

### 🔗 Setting Up a connection to db

To connect to VideoDB, simply get the API and create a connection. This can be done by either providing your VideoDB API key directly to the constructor or by setting the VIDEO\_DB\_API\_KEY environment variable with your API key.

Get your API key from

[VideoDB Console](https://console.videodb.io/)

. ( Free for first 50 uploads, No credit card required ) 🎉

import videodb

conn = videodb.connect(api\_key="YOUR\_API\_KEY")

## Working with Single Video

### ⬆️ Uploading a video

Now that you have established a connection to VideoDB, you can upload your videos using conn.upload()

You can upload your media by a url or from your local file system

upload method returns a Video object.

\# Upload a video by url

video = conn.upload(url="https://www.youtube.com/watch?v=WDv4AWk0J3U")

\# Upload a video from file system

video\_f = conn.upload(file\_path="./my\_video.mp4")

VideoDB simplifies your upload by supporting links from Youtube, S3 or any Public URL with video

### Pro Tip

If you wish to upload only the audio from a video file, just specify in the "media\_type" field. For instance, you can obtain audio from a YouTube video by doing so.

from videodb import MediaType

audio = conn.upload(url="https://youtu.be/IoDVfXFq5cU?si=BCU7ghvqY3YdCS78", media\_type=MediaType.audio)

The types of media that can be uploaded are defined in the MediaType class.

### 📺 Viewing your video

Your video is instantly available for viewing 720p resolution ⚡️

Generate a streamable url for video using video.generate\_stream()

Preview the video using video.play(). This will open the video in your default browser/notebook

video.generate\_stream()

video.play()

Note: if you are viewing this notebook on github, you won't be able to see iframe player, because of security restrictions. Please open the printed link of player in your browser

Load content from console.videodb.io?

Loading external content may reveal information to 3rd parties. [Learn more](https://help.coda.io/en/articles/1211364-embedding-content-in-your-doc)

Allow

### ⛓️ Stream Specific Sections of videos

You can easily clip specific sections of a video by passing timelineof start and end sections. It accepts seconds. For example Here’s we are streaming only first 10 seconds and then 120 to 140 second of a video

stream\_link = video.generate\_stream(timeline=\[(0,10),(120,140)\])

play\_stream(stream\_link)

### 🗂️ Indexing a Video

To search bits inside a video, you have to first index the video. This can be done by a invoking the index function on the video object. VideoDB offers two type of indexes currently.

index\_spoken\_words: Indexes spoken words in the video. It automatically generate the transcript and makes it ready for search. Checkout

[Language Support](https://docs.videodb.io/language-support-79)

to index different language content.

index\_scenes: Indexes visual concepts and events of the video. Perfect for building security monitoring, drone, and other camera footage. Refer

[Visual Search and Indexing](https://docs.videodb.io/visual-search-and-indexing-80)

Checkout

[Multimodal Search](https://docs.videodb.io/multimodal-search-90)

for unlocking multimodal search in your video library.

⏱️ Indexing may take some time for longer videos, structure it as a batch job with callback in your application. Check

[Callback Details](https://docs.videodb.io/callback-details-66)

\# best for podcasts, elearning, news, etc.

video.index\_spoken\_words()

\# best for camera feeds, moderation usecases etc.

video.index\_scenes(prompt="<your prompt to describe the scenes>")

Upcoming:

Real time feed indexing, setting up real time alerts.

Specific domain Indexes like Football, Baseball, Drone footage, Cricket etc.

### 🔍 Search Inside a Video

Search the segments inside a video. While searching you have options to choose the type of search and index. VideoDB offers following types of search :

SearchType.semanticPerfect for question answer kind of queries. This is also the default type of search.

SearchType.keywordIt matches the exact occurrence of word or sentence you pass in the query parameter of the search function. keyword search is only available to use with single videos.

IndexType.sceneIt search the visual information of the video, Index the video using index\_scenesfunction.

IndexType.spoken\_wordIt search the spoken information of the video, Index the video using index\_spoken\_wordsfunction.

from videodb import SearchType

from videodb import IndexType

result = video.search(query ="What are the benefits of morning sunlight?",

search\_type =SearchType.semantic,

index\_type =IndexType.spoken\_word)

result.play()

Viewing Search Results :

video.search() will return a SearchResults object, which contains the sections/shots of videos which semantically match your search query

result.get\_shots()\- Returns a list of Shot that matched search query

result.play()\- Returns a playable url for video (similar to video.play() you can open this link in browser, or embed it into your website using iframe)

## RAG: Search Inside Multiple Videos

VideoDBcan store and search inside multiple videos with ease. By default, videos are uploaded to your default collection and you have freedom to create and manage more collections, checkout our

[Collections](https://docs.videodb.io/collections-68)

doc for more details.

If you are an existing llamaIndex user, trying to build RAG pipeline on your video data. You can also use VideoDB retriever. Checkout llama docs ⬇️

[![](https://codaio.imgix.net/docs/_s5lUnUCIU/blobs/bl-LqObRP4v0A/7b9d7a007c857e3d084558d9276010d6e2101260ab78ea2dc871e4e1d2dbb358386b5f7d832921deb36cd820d65ed19f472132b189e46194f713725ee712a89368b08dfecb02c4e6bf3b90c6ab944a066ed3362a9b74309bd45495c9f221dcbea0e0b50d?auto=format%2Ccompress&fit=crop&w=227&h=51.416666666666686&dpr=2&crop=focalpoint&fp-x=0.5&fp-y=0.5113278791692889&fp-z=1)](https://docs.llamaindex.ai/en/stable/examples/retrievers/videodb_retriever.html)

🔄 Using Collection to upload multiple Videos

\# Get the default collection

coll = conn.get\_collection()

\# Upload Videos to a collection

coll.upload(url="https://www.youtube.com/watch?v=lsODSDmY4CY")

coll.upload(url="https://www.youtube.com/watch?v=vZ4kOr38JhY")

coll.upload(url="https://www.youtube.com/watch?v=uak\_dXHh6s4")

conn.get\_collection() : Returns Collection object, the default collection

coll.get\_videos() : Returns list of Video, all videos in collections

coll.get\_video(video\_id): Returns Video, respective video object from given video\_id

coll.delete\_video(video\_id): Deletes the video from Collection

### 📂 Search inside multiple videos in a collection

You can simply index all the videos in a collection and use search method on collection to find relevant results. Here we are indexing spoken content of a collection and searching

\# Index all videos in collection

for video in coll.get\_videos():

video.index\_spoken\_words()

Semantic Search in the collection

\# search in the collection of videos

results = coll.search(query ="What is Dopamine?")

results.play()

Let’s try one more search:

results = coll.search(query = "What's the benefit of morning sunlight?")

results.play()

The result here has all the matching bits in a single video stream from your collection. You can use these results in your application right away.

As you can see VideoDB fundamentally removes the limitation of files and gives you power to access and stream videos in a seamless way. Stay tuned for exciting features in our upcoming version and keep building awesome stuff with VideoDB 🤘

## 🌟 Explore more with Video object

There are multiple methods available on a Video Object, that can be helpful for your use-case.

### Access Transcript

\# get text of the spoken content

text\_json = video.get\_transcript()

text = video.get\_transcript\_text()

print(text)

Add Subtitle to a video

It returns a new stream instantly with subtitle added into the video. Subtitle functions has many styling parameters like font, size, background color etc. Check

[Ref: Subtitle Styles](https://docs.videodb.io/ref-subtitle-styles-57)

and

[Guide: Subtitles](https://docs.videodb.io/guide-subtitles-73)

for details.

new\_stream = video.add\_subtitle()

play\_stream(new\_stream)

Get Thumbnail of Video :

video.generate\_thumbnail() : Returns a thumbnail image of video.

Delete a video :

video.delete() : Delete a video.

👉🏼 Checkout

[Dynamic Video Streams](https://docs.videodb.io/dynamic-video-streams-44)

to understand how you can modify the video streams in real-time. This opens doors for many usecases that were never possible with videos.⚡️

👉🏼 Checkout more examples and tutorials 👉

[Examples and Tutorials](https://docs.videodb.io/examples-and-tutorials-35)

to explore what you can build with VideoDB

Setup

🔧 Installing VideoDB in your environment

🔗 Setting Up a connection to db

Working with Single Video

⬆️ Uploading a video

Pro Tip

📺 Viewing your video

⛓️ Stream Specific Sections of videos

🗂️ Indexing a Video

🔍 Search Inside a Video

RAG: Search Inside Multiple Videos

📂 Search inside multiple videos in a collection

🌟 Explore more with Video object

Access Transcript

Want to print your doc?

This is not the way.

Try clicking the ⋯ next to your doc name or using a keyboard shortcut (

CtrlP

) instead.


---

# VideoDB MCP Server [Source Link](https://docs.videodb.io/videodb-mcp-server-109)

VideoDB Documentation

Pages

*   Welcome to VideoDB Docs
*   Quick Start Guide
*   Video Indexing Guide
*   Semantic Search
*   How Accurate is Your Search?
*   Collections
*   Public Collections
*   Callback Details
*   Ref: Subtitle Styles
*   Language Support
*   Guide: Subtitles
*   Visual Search and Indexing
*   Scene Extraction Algorithms
*   Custom Annotations
*   Scene-Level Metadata: Smarter Video Search & Retrieval
*   Advanced Visual Search Pipelines
*   Playground for Scene Extractions
*   Deep Dive into Prompt Engineering : Mastering Video Scene Indexing
*   Multimodal Search
*   Multimodal Search: Quickstart
*   Conference Slide Scraper with VideoDB
*   Real‑Time Video Pipeline
*   Meeting Recording Agent Quickstart
*   How VideoDB Solves Complex Visual Analysis Tasks
*   Generative Media Quickstart
*   Generative Media Pricing
*   Dynamic Video Streams
*   Ref: TextAsset
*   Guide : TextAsset
*   VideoDB MCP Server
*   Transcoding Quickstart
*   Director - Video Agent Framework
*   Agent Creation Playbook
*   How I Built a CRM-integrated Sales Assistant Agent in 1 Hour
*   Make Your Video Sound Studio Quality with Voice Cloning
*   Setup Director Locally
*   Open Source Tools
*   LlamaIndex VideoDB Retriever
*   PromptClip: Use Power of LLM to Create Clips
*   StreamRAG: Connect ChatGPT to VideoDB
*   Examples and Tutorials
*   Dubbing - Replace Soundtrack with New Audio
*   Beep curse words in real-time
*   Remove Unwanted Content from videos
*   Instant Clips of Your Favorite Characters
*   Insert Dynamic Ads in real-time
*   Adding Brand Elements with VideoDB
*   Revolutionize Video Editing with VideoDb: Effortless Ad Placement and Seamless Video Integration
*   Eleven Labs x VideoDB: Adding AI Generated voiceovers to silent footage
*   Elevating Trailers with Automated Narration
*   Add Intro/Outro to Videos
*   Enhancing Video Captions with VideoDB Subtitle Styling
*   Audio overlay + Video + Timeline
*   Building Dynamic Video Streams with VideoDB: Integrating Custom Data and APIs
*   Adding AI Generated Voiceovers with VideoDB and LOVO
*   AI Generated Ad Films for Product Videography: Wellsaid, Open AI & VideoDB
*   Fun with Keyword Search
*   AWS Rekognition and VideoDB - Intelligent Video Clips
*   AWS Rekognition and VideoDB - Effortlessly Remove Inappropriate Content from Video
*   Overlay a Word-Counter on Video Stream
*   Generate Automated Video Outputs with Text Prompts \| DALL-E + ElevenLabs + OpenAI + VideoDB
*   Edge of Knowledge
*   Building Intelligent Machines
*   Part 1 - Define Intelligence
*   Part 2 - Observe and Respond
*   Part 3 - Training a Model
*   Society of Machines
*   Society of Machines
*   Autonomy - Do we have the choice?
*   Emergence - An Intelligence of the collective
*   Drafts
*   From Language Models to World Models: The Next Frontier in AI
*   The Future Series
*   Building World's First Video Database
*   Multimedia: From MP3/MP4 to the Future with VideoDB
*   Introducing VideoDB: The Pinnacle of Synchronized Video Streaming for the Modern Web
*   Dynamic Video Streams
*   Why do we need a Video Database Now?
*   What's a Video Database ?
*   Enhancing AI-Driven Multimedia Applications
*   Misalignment of Today's Web
*   Beyond Traditional Video Infrastructure
*   Research Grants
*   Team
*   Internship: Build the Future of AI-Powered Video Infrastructure
*   Ashutosh Trivedi
*   Playlists
*   Talks - Solving Logical Puzzles with Natural Language Processing - PyCon India 2015
*   Ashish
*   Shivani Desai
*   Gaurav Tyagi
*   Rohit Garg
*   Customer Love
*   Temp Doc

# VideoDB MCP Server

The VideoDB MCP Server can be installed and used in multiple ways. Follow the steps below to set it up.

## Prerequisite: Ensure Python 3.12 or Later is Installed

Before installing the VideoDB MCP Server, verify that Python 3.12 or later is installed on your system.

Check Python version:

`python --version`

If the version is below 3.12, update Python from the [official website](https://www.python.org/downloads/).

# Install and Configure VideoDB MCP Server

> simplest method using uvx

## 1\. Install uv

macOS:

`brew install uv`

For macOS/Linux:

`curl-LsSf<https://astral.sh/uv/install.sh>\|sh`

For Windows:

`powershell -ExecutionPolicy ByPass -c"irm <https://astral.sh/uv/install.ps1> \| iex"`

You can visit the complete installation steps for uv [here](https://astral.sh/uv).

## 2\. Automatic Installation for Clients

To automatically add the MCP Server to Claude, Cursor and Claude Code:

Install for Claude only

`uvx videodb-director-mcp --install=claude`

Install for Cursor only

`uvx videodb-director-mcp --install=cursor`

Install for both Claude and Cursor

`uvx videodb-director-mcp --install=all`

Install for Claude Code

`claude mcp add videodb-director uvx -- videodb-director-mcp --api-key=<VIDEODB_API_KEY>`

## 3\. Update VideoDB MCP package

To ensure you're using the latest version of the MCP server with uvx, start by clearing the cache:

`uv cache clean`

This command removes any outdated cached packages of videodb-director-mcp, allowing uvx to fetch the most recent version.

If you always want to use the latest version of the MCP server, update your command as follows:

`uvx videodb-director-mcp@latest --api-key=<VIDEODB_API_KEY>`

This ensures that uvx pulls the latest release every time you run it.

# Advanced Methods

## 1\. Install the VideoDB MCP Server

### a. Using pipx

We need to install pipx first.

For macOS:

`brew install pipx`

`pipx ensurepath`

For Windows:

`python -m pip install--user pipx`

`python -m pipx ensurepath`

You can now run the MCP Server using:

`pipx run videodb-director-mcp --api-key=VIDEODB_API_KEY`

### b. Install Using pip

Install the package using pip:

`pip install videodb-director-mcp`

The MCP server can now be started with the following command:

`videodb-director-mcp --api-key=VIDEODB_API_KEY`

## 2\. Configuring the MCP Server in Clients

### Claude Desktop

a. Open Configuration File

MacOS/Linux:

`code ~/Library/Application\ Support/Claude/claude_desktop_config.json`

Windows:

`code $env:AppData\Claude\claude_desktop_config.json`

b. Modify Configuration

Using pipx:

```json
{
    "mcpServers":{
        "videodb-director":{
            "command":"pipx",
            "args":["run","videodb-director-mcp","--api-key=<VIDEODB-API-KEY>"]
        }
    }
}
```

Using package installed via pip :

```json
{
    "mcpServers":{
        "videodb-director":{
            "command":"videodb-director-mcp",
            "args":["--api-key=<VIDEODB-API-KEY>"]
        }
    }
}
```

### Cursor Editor

a. Open MCP Settings

Navigate to Settings > Cursor Settings

Click on MCP

Click on Add new Global MCP Server

b. Add Configuration

Using pipx:

```json
{
    "mcpServers":{
        "videodb-director":{
            "command":"pipx",
            "args":["run","videodb-director-mcp","--api-key=<VIDEODB-API-KEY>"]
        }
    }
}
```

Using package installed via pip :

```json
{
    "mcpServers":{
        "videodb-director":{
            "command":"videodb-director-mcp",
            "args":["--api-key=<VIDEODB-API-KEY>"]
        }
    }
}
```

### Claude Code

a. Add configuration

To configure VideoDB Director MCP for Claude code you can run the following command

Using pipx:

`claude mcp add videodb-director pipx -- run videodb-director-mcp --api-key=<VIDEODB_API_KEY>`

Using package installed via pip :

`claude mcp add videodb-director videodb-director-mcp -- --api-key=<VIDEODB_API_KEY>`

b. Verify configuration

You can verify if the MCP Server has been added correctly or not by simply running the following command:

`claude mcp list`

## 3\. Update the VideoDB Director MCP Package

To ensure you're using the latest version of a package installed via pipx or pip, run:

`pip install--upgrade videodb-director-mcp`

This will upgrade the package to its latest available version.


---

