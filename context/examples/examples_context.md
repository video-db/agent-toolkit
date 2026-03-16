# VideoDB Tutorials

A collection of tutorials for working with VideoDB, a powerful service for video processing, indexing, and searching.

## Table of Contents

- [Scene Index QuickStart](#scene-index-quickstart)
- [Scene-Level Metadata Indexing](#scene-level-metadata-indexing)
- [VideoDB QuickStart](#videodb-quickstart)
- [Subtitle Guide](#subtitle-guide)
- [Cleanup Guide](#cleanup-guide)
- [Text Asset Guide](#text-asset-guide)

## Scene Index QuickStart

[Source Link](https://github.com/video-db/videodb-cookbook/blob/main/quickstart/Scene%20Index%20QuickStart.ipynb)

# ⚡️ Quick Start: Scene Indexing with VideoDB

<a href="https://colab.research.google.com/github/video-db/videodb-cookbook/blob/main/quickstart/Scene%20Index%20QuickStart.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

This guide provides a quick introduction to scene indexing with VideoDB, enabling powerful visual search and content understanding in your videos. Leverage vision models to extract meaningful information from videos and easily index it using VideoDB.

Use scene indexing to build RAG applications and answer complex queries:

![](https://raw.githubusercontent.com/video-db/videodb-cookbook/main/images/scene_index/intro.png)

## Setup

---

### 📦 Install VideoDB

Install the VideoDB package using pip:

```python
!pip install -U videodb
```

### 🔑 Configure API Key

Import the `os` module and set your VideoDB API key as an environment variable. Replace `"sk-xxxx-yyyyy-zzzz"` with your actual API key.

```python
import os

os.environ["VIDEO_DB_API_KEY"] = "sk-xxxx-yyyyy-zzzz"
```

### 🌐 Connect to VideoDB

Establish a connection to VideoDB and get a collection instance:

```python
from videodb import connect

conn = connect()
coll = conn.get_collection()
```

### 🎥 Upload Video

Upload a video to VideoDB. This example uses a YouTube video URL.

```python
video = coll.upload(url="https://www.youtube.com/watch?v=LejnTJL173Y")
```

## 📇 Index Scenes

---

The `index_scenes` function automatically indexes visual information in your video, extracting meaningful scenes.

```python
index_id = video.index_scenes()
```

### Optional Parameters

Customize scene indexing using optional parameters:

*   **`extraction_type`**: Choose a scene extraction algorithm (e.g., time-based).
*   **`extraction_config`**: Configure the selected extraction algorithm (e.g., time interval for time-based extraction).
*   **`prompt`**: Provide a prompt for a vision model to describe the scenes and frames (e.g., "describe the image in 100 words").
*   **`callback_url`**: Specify a URL to receive a notification when the indexing job is complete.

Refer to the [Scene and Frame Object Guide](https://github.com/video-db/videodb-cookbook/blob/main/guides/video/scene-index/advanced_visual_search.ipynb) for more details.

```python
from videodb import SceneExtractionType, IndexType

index_id = video.index_scenes(
    extraction_type=SceneExtractionType.time_based,
    extraction_config={"time":10, "select_frames": ['first']},
    prompt="describe the image in 100 words",
    # callback_url=callback_url,
)

# Wait for indexing to finish
scene_index = video.get_scene_index(index_id)
scene_index
```

Example output:

```
[{'description': 'The image depicts a man sitting in an office or conference room...',
  'end': 10.01,
  'start': 0.0},
 {'description': 'The image shows a man with a receding hairline, wearing a dark suit...',
  'end': 20.02,
  'start': 10.01},
  ...
]
```

> Note: It may take a few seconds for the index to become available for searching.

```python
# Search your video using the index_id.
# Default Case: search all indexes
# query: "drinking"

res = video.search(query="religious gathering",
                  index_type=IndexType.scene,
                  index_id=index_id)

res.play()
```

This will output a URL that opens a VideoDB player, showcasing the relevant scenes.

## ⚙️ Understanding `index_scenes` Parameters

---

Let's explore the parameters of the `index_scenes` function in more detail:

*   `extraction_type`: Chooses the algorithm for scene extraction.
*   `extraction_config`: Provides configuration details for the chosen algorithm.
*   `prompt`: Instructs the vision model on how to describe each scene.
*   `callback_url`: Specifies a URL to be notified when the indexing job finishes.

### ⚙️ `extraction_type` & `extraction_config`

Videos are essentially sequences of images (frames). The `extraction_type` parameter allows you to select different scene extraction algorithms, which, in turn, influence the selection of relevant frames for description. For more information, see [Scene Extraction Algorithms](https://docs.videodb.io/scene-extraction-algorithms-84).

![](https://raw.githubusercontent.com/video-db/videodb-cookbook/main/images/scene_index/VSF.png)

### ⚙️ `prompt`

The `prompt` is crucial for guiding the vision models. It defines the context and desired output format.

For example, to identify running activity, you might use the following prompt:

> "Describe clearly what is happening in the video. Add 'running_detected' if you see a person running."

For experimenting with custom models and prompts, see [Advanced Visual Search Pipelines](https://github.com/video-db/videodb-cookbook/blob/main/guides/scene-index/advanced_visual_search.ipynb).

### ⚙️ `callback_url`

The `callback_url` receives a notification upon completion of the scene indexing process. Refer to [Callback Details](https://docs.videodb.io/callback-details-66#_lubHL) for more information.

<div style="height:40px;"></div>

## 🗂️ Managing Indexes

---

> 💡 You can create multiple scene indexes for a single video and rank search results based on these indexes.

**List Scene Indexes:**

`video.list_scene_index()` returns a list of available scene indexes, including their `id`, `name`, and `status`.

```python
scene_indexes = video.list_scene_index()
print(scene_indexes)
```

Example output:

```
[{'name': 'Scene Index 2024-07-22 10:06', 'scene_index_id': 'f4db35c5ce45a709', 'status': 'done'}]
```

**Get a Specific Index:**

`video.get_scene_index(index_id)` returns a list of indexed scenes, including `scene_index_id`, `start`, `end`, and `description`.

```python
scene_index = video.get_scene_index(index_id)
print(scene_index)
```

Example output:

```
[{'description': 'The image depicts a man sitting in an office...', 'end': 10.01, 'start': 0.0},
 {'description': 'The image shows a man with a receding hairline...', 'end': 20.02, 'start': 10.01},
 ...]
```

**Delete an Index:**

```python
video.delete_scene_index(index_id)
```

## 🧑‍💻 Deep Dive

---

Explore the following resources and tutorials for more advanced scene indexing techniques:

*   **Custom Annotations Pipeline:** [Custom Annotations](https://github.com/video-db/videodb-cookbook/blob/main/guides/scene-index/custom_annotations.ipynb) - Bring your own scene descriptions and annotations.
*   **Playground for Scene Extractions:** [Playground](https://github.com/video-db/videodb-cookbook/blob/main/guides/scene-index/playground_scene_extraction.ipynb) - Experiment with different extraction algorithms and prompts.
*   **Advanced Visual Search Pipelines:** [Advanced Visual Search](https://github.com/video-db/videodb-cookbook/blob/main/guides/scene-index/advanced_visual_search.ipynb) - Build flexible and powerful visual search workflows.

If you have any questions or feedback, please reach out to us!

*   [Discord](https://discord.gg/py9P639jGz)
*   [GitHub](https://github.com/video-db)
*   [Website](https://videodb.io)
*   [Email](ashu@videodb.io)

---

## Scene-Level Metadata Indexing

[Source Link](https://github.com/video-db/videodb-cookbook/blob/main/quickstart/scene_level_metadata_indexing.ipynb)

# 📌 VideoDB F1 Race Search Pipeline (Turn Detection & Metadata Filtering)

## 🎯 Objective
This notebook demonstrates how to use scene-level metadata filtering to enable precise search and retrieval within an F1 race video.

## 🔍 What We're Doing:
- Upload an F1 race video.
- Extract scenes every 2 seconds (1 frame per scene).
- Describe scenes using AI-generated metadata.
- Index scenes with structured metadata (`camera_view` & `action_type`).
- Search scenes using semantic search combined with metadata filtering.

## 📦 Install VideoDB SDK
Required for connecting and processing video data.

```python
!pip install videodb
```

## 🔑 Set Up API Key
Authenticate with VideoDB to access indexing and search functionalities.
```python
import os

os.environ["VIDEO_DB_API_KEY"] = ""
```

## 🌐 Connect to VideoDB
Establishes a connection to manage video storage, indexing, and search.
```python
from videodb import connect

conn = connect()
coll = conn.get_collection()

print(coll.id)
```

## 🎥 Upload F1 Race Video
Adds the video to VideoDB for further processing.
```python
video = coll.upload(url="https://www.youtube.com/watch?v=2-oslsgSaTI")
print(video.id)
```

## ✂️ Extracting Scenes (Every 2 Seconds)
We split the video into 2-second scenes, extracting a single frame per scene for indexing.
```python
from videodb import SceneExtractionType

scene_collection = video.extract_scenes(
    extraction_type=SceneExtractionType.time_based,
    extraction_config={"time": 2, "select_frames": ["middle"]},
)

print(f"Scene Collection ID: {scene_collection.id}")

scenes = scene_collection.scenes

print(f"Total Scenes Extracted: {len(scenes)}")
```

## 🔍 Generating Scene Metadata
To make scenes searchable, we use AI to describe & categorize each scene with the following structured metadata:

### 📌 Scene-Level Metadata Fields:
#### 1️⃣ `camera_view` → Where is the camera placed?
   - `"road_ahead"` → Driver's POV looking forward.
   - `"helmet_selfie"` → Close-up of driver's helmet.

#### 2️⃣ `action_type` → What is the driver doing?
   - `"clear_road"` → No cars ahead (clean lap).
   - `"chasing"` → Following another car (intense racing moment).

```python
from videodb.scene import Scene

# List to store described scenes
described_scenes = []

for scene in scenes:
    print(f"Scene from {scene.start}s to {scene.end}s")

    # Generate metadata
    camera_view = scene.describe(
        'Select ONLY one of these camera views (DO NOT describe it, JUST return the category name): ["road_ahead", "helmet_selfie"]. If the view does not match exactly, pick the closest one.'
    )

    action_type = scene.describe(
        'Select ONLY one of these options based on the action being performed by the driver (DO NOT describe it, JUST return the category name): ["clear_road", "chasing"]. If the view does not match exactly, pick the closest one.'
    )

    scene_description = scene.describe(
        "Clearly describe a Formula 1 scene by specifying the scene type, the drivers and teams involved, the specific location on the track, and the key action or significance of the moment. Use concise, yet rich language, targeting Formula 1 enthusiasts seeking precise scene descriptions."
    )

    print(f"Camera View: {camera_view} | Action Type: {action_type}")
    print(f"Scene Description: {scene_description}")

    # Create Scene object with metadata
    described_scene = Scene(
        video_id=video.id,
        start=scene.start,
        end=scene.end,
        description=scene_description,
        metadata={
            "camera_view": camera_view,
            "action_type": action_type
        }
    )
    described_scenes.append(described_scene)

print(f"Total Scenes Indexed: {len(described_scenes)}")
```

## 🗂 Indexing Scenes with Metadata
Now that we have generated metadata for each scene, we index them to make them searchable.
```python
if described_scenes:
    scene_index_id = video.index_scenes(
        scenes=described_scenes,
        name="F1 Scenes"
    )
    print(f"Scenes Indexed under ID: {scene_index_id}")
```

## 🔎 Searching Scenes with Metadata & AI
Now that our scenes are indexed, we can search using a combination of:
✅ Semantic Search → AI understands the meaning of the query.
✅ Metadata Filters → Only return relevant scenes based on camera view & action type.

### 🔍 Example 1: Finding Intense Chasing Moments
Search for scenes where a driver is chasing another car, viewed from the driver's perspective.

```python
from videodb import IndexType
from videodb import SearchType

search_results = video.search(
    query = "A skillful chasing scene",
    filter = [{"camera_view": "road_ahead"}, {"action_type": "chasing"}],   # Using metadata filter
    search_type = SearchType.semantic,
    index_type = IndexType.scene,
    result_threshold = 100,
    scene_index_id = scene_index_id  # Our indexed scenes
)
# Play the search results
search_results.play()
```

```html
<iframe
    width="800"
    height="400"
    src="https://console.videodb.io/player?url=https://stream.videodb.io/v3/published/manifests/70048f66-7da5-494f-a2cf-00b983539f5e.m3u8"
    frameborder="0"
    allowfullscreen
></iframe>
```

### 🔍 Example 2: Finding Smooth Solo Driving Moments
Search for scenes with clean, precise turns, where the driver has an open road ahead.
```python
search_results = video.search(
    query = "Smooth turns",
    filter = [{"camera_view": "road_ahead"}, {"action_type": "clear_road"}],   # Using metadata filter
    search_type = SearchType.semantic,
    index_type = IndexType.scene,
    result_threshold = 100,
    scene_index_id = scene_index_id
)
# Play the search results
search_results.play()
```

```html
<iframe
    width="800"
    height="400"
    src="https://console.videodb.io/player?url=https://stream.videodb.io/v3/published/manifests/0c58d2d2-e44d-4ed3-bd8d-b535155f6263.m3u8"
    frameborder="0"
    allowfullscreen
></iframe>
```

## ✅ Conclusion: Precision Search with Scene Metadata
This notebook demonstrated how scene-level metadata indexing enables powerful video search.

We can:
- Precisely filter race footage by camera angles & driver actions.
- Use AI-powered semantic search to find specific race moments.
- Enhance video retrieval for F1 analysis, highlights, and research.

This approach unlocks smarter, metadata-driven video search.

---

## VideoDB QuickStart

[Source Link](https://github.com/video-db/videodb-cookbook/blob/main/quickstart/VideoDB%20Quickstart.ipynb)

# ⚡️ QuickStart: VideoDB

<a href="https://colab.research.google.com/github/video-db/videodb-cookbook/blob/main/quickstart/VideoDB%20Quickstart.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

This notebook provides a quick introduction to [VideoDB](https://videodb.io), demonstrating how to upload, view, index, and search within video content.

### Setup

---

#### 🔧 Install VideoDB

Install the VideoDB Python package:

```python
!pip install -U videodb
```

#### 🔗 Connect to VideoDB

Establish a connection to VideoDB using your API key. You can either pass the API key directly or set the `VIDEO_DB_API_KEY` environment variable.

> 💡 Get your API key from the [VideoDB Console](https://console.videodb.io) (Free for the first 50 uploads, no credit card required!).

```python
from videodb import connect, play_stream

# Replace with your API key
conn = connect(api_key="sk-xxx-yyyyy-zzzz")
```

### Working with a Single Video

---

#### ⬆️ Upload a Video

Upload videos using `conn.upload()`. You can upload from a public URL or a local file path. The `upload` function returns a `Video` object, which provides access to various video methods.

```python
# Upload a video by URL
video = conn.upload(url="https://www.youtube.com/watch?v=wU0PYcCsL6o")
```

<div style="background-color: #ffffcc; color: black; padding: 10px; border-radius: 5px;">
VideoDB supports uploads from Youtube, S3, and any public URL.
</div>

#### 📺 View Your Video

Videos are instantly available for viewing in 720p resolution.

* Generate a streamable URL using `video.generate_stream()`.
* Preview the video using `video.play()`. This will open the video in your default browser/notebook.

<div style="background-color: #ffffcc; color: black; padding: 10px; border-radius: 5px;">
    <strong>Note:</strong> If you are viewing this notebook on GitHub, you won't be able to see the iframe player due to security restrictions. Please open the printed link of the player in your browser.
</div>

```python
video.generate_stream()
video.play()
```

#### ✂️ Get Specific Sections of Videos

Clip specific sections of a video using the `timeline` parameter in `video.generate_stream()`. The timeline accepts start and end times in seconds.

For example, the following will stream the first 10 seconds and then the 120 to 140 second of the uploaded video.

```python
stream_link = video.generate_stream(timeline=[[0,10], [120,140]])
play_stream(stream_link)
```

#### 🔍 Indexing a Video

Indexing enables searching within a video. Invoke the index function on the video object. VideoDB currently offers two types of indexes:

1. `index_spoken_words`: Indexes spoken words in the video. It automatically generates the transcript and makes it ready for search. 20+ languages are supported. Checkout [Language Support](https://docs.videodb.io/language-support-79) to know more.

2. `index_scenes`: Indexes visual information and events of the video. Perfect for finding scenes, activities, objects, emotions in the video. Refer [Scene Index Documentation](https://docs.videodb.io/scene-index-documentation-80) for details.

<div style="background-color: #ffffcc; color: black; padding: 10px; border-radius: 5px;">
    <strong>Note:</strong> Indexing may take time for longer videos.
</div>

```python
# Index spoken content of the video.
video.index_spoken_words()
```

```python
# Index visual information in video frames. You can change the prompt according to your use case.
# You can index a video multiple times with different prompts.
index_id = video.index_scenes(
    prompt="Describe the scene in strictly 100 words"
)

# Wait to Indexing to finish
scene_index = video.get_scene_index(index_id)
scene_index
```

#### Search inside a video:

Search can be performed on indexed videos using `video.search()`. When searching, you have the option to choose the type of search and index. VideoDB offers the following types of search:

`SearchType.semantic` Perfect for question answer kind of queries. This is also the default type of search.

`SearchType.keyword` It matches the exact occurrence of word or sentence you pass in the query parameter of the search function. keyword search is only available to use with single videos.

`IndexType.scene` It search the visual information of the video, Index the video using index_scenes function.

`IndexType.spoken_word` It search the spoken information of the video, Index the video using index_spoken_words function.

```python
from videodb import SearchType, IndexType

result = video.search(query="what's the dream?", search_type=SearchType.semantic, index_type=IndexType.spoken_word)
result.play()
```

```python
# Try with different queries

# "city scene with buses"
query = "mountains"

result = video.search(query=query, search_type=SearchType.semantic, index_type=IndexType.scene)
result.play()
```

##### 📺 View Search Results:

`video.search()` will return a SearchResults object, which contains the sections/shots of videos which semantically match your search query

* `result.get_shots()` - Returns a list of Shot that matched search query
* `result.play()` - This will open the video in your default browser/notebook

##### 🗑️ Cleanup
You can delete the video from database using `video.delete()`

```python
video.delete()
```

### RAG: Working with Multiple Videos

---

`VideoDB` can store and search inside multiple videos with ease. By default, videos are uploaded to your default collection and you have freedom to create and manage more collections, checkout our [Collections docs](https://docs.videodb.io/collections-68) for more details.

If you are an existing llamaIndex user, trying to build RAG pipeline on your video data. You can use VideoDB retriever. Checkout [llama-Index docs](https://docs.llamaindex.ai/en/stable/examples/retrievers/videodb_retriever.html)

##### 🔄 Using Collection to upload multiple Videos

```python
# Get a collection
coll = conn.get_collection()

# Upload Videos to a collection
coll.upload(url="https://www.youtube.com/watch?v=lsODSDmY4CY")
coll.upload(url="https://www.youtube.com/watch?v=vZ4kOr38JhY")
coll.upload(url="https://www.youtube.com/watch?v=uak_dXHh6s4")
```

* `conn.get_collection()` : Returns Collection object, the default collection
* `coll.get_videos()` : Returns list of Video, all videos in collections
* `coll.get_video(video_id)` : Returns Video, respective video object from given video_id
* `coll.delete_video(video_id)` : Deletes the video from Collection

### 📂 Search on Multiple Videos from a collection

You can simply Index all the videos in a collection and use search method on collection to find relevant results.
Here we are indexing spoken content of a collection for quick experiment.

<div style="background-color: #ffffcc; color: black; padding: 10px; border-radius: 5px;">
    <strong>Note:</strong> Index may take time for longer videos</div>

```python
# for simplicity we are just indexing the spoken content of each video.
for video in coll.get_videos():
    video.index_spoken_words()
    print(f"Indexed {video.name}")
```

### Search Inside Collection:

Search can be performed on a collection using `coll.search()`

```python
# search in the collection of videos
results = coll.search(query = "Deep sleep")
results.play()
```

```python
results = coll.search(query= "What are the benifits of morning sunlight?")
results.play()
```

```python
results = coll.search(query= "What are Adaptogens?")
results.play()
```

#### 📺 View Search Results:

`video.search()` will return a SearchResults object, which contains the sections/shots of videos which semantically match your search query

* `result.get_shots()` - Returns a list of Shot that matched search query
* `result.play()` - This will open the video in your default browser/notebook

<div style="background-color: #ffffcc; color: black; padding: 10px; border-radius: 5px;">
As you can see VideoDB fundamentally removes the limitation of files and gives you power to access and stream videos in a very seamless way. Stay tuned for exciting features in our upcoming version and keep building awesome stuff with VideoDB 🤘
</div>

### 🌟 Explore more with Video object
There are multiple methods available on a Video Object, that can be helpful for your use-case.

#### Access Transcript

```python
# words with timestamps
text_json = video.get_transcript()
text = video.get_transcript_text()
print(text)
```

#### Access Visual Scene Descriptions

```python
# Take a look at the scenes
video.get_scene_index(index_id)
```

#### Add Subtitle to a video
It returns a new stream instantly with subtitle added into the video. Subtitle functions has many styling parameters like font, size, background color etc. Check the notebook: [Subtitle Styles](https://github.com/video-db/videodb-cookbook/blob/main/guides/Subtitle.ipynb) for details.

```python
new_stream = video.add_subtitle()
play_stream(new_stream)
```

#### Generate Thumbnail of Video:

You can use `video.generate_thumbnail(time=)` to generate a thumbnail image of video from any timestamp.

```python
from IPython.display import Image

image = video.generate_thumbnail(time=12.0)
Image(url=image.url)
```

##### Delete a video:

* `video.delete()` :deletes a video.

```python
video.delete()
```

<div style="background-color: #ffffcc; color: black; padding: 10px; border-radius: 5px;">
Checkout more examples and tutorials 👉 <a href="https://docs.videodb.io/build-with-videodb-35"> Build with VideoDB </a> to explore what you can build with VideoDB
</div>

---

## Subtitle Guide

[Source Link](https://github.com/video-db/videodb-cookbook/blob/main/guides/Subtitle.ipynb)

## Guide: Subtitles

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/video-db/videodb-cookbook/blob/nb/main/guides/video/Subtitle.ipynb)

## Adding Subtitles to Your Videos
---

This guide demonstrates how to customize subtitle styles using the `SubtitleStyle` class in VideoDB. We'll explore various configuration options and their visual outputs, covering:

* Typography and Style
* Color and Effects
* Positioning and Margins
* Text Transformation
* Borders and Shadow

## 🛠️ Setup
---

### 📦 Installing the VideoDB Package

```python
%pip install videodb
```

### 🔑 API Key Configuration

Before you begin, you'll need a VideoDB API key.

> Get your free API key (for the first 50 uploads, no credit card required!) from the [VideoDB Console](https://console.videodb.io). 🎉

Set the API key as an environment variable:

```python
import os
os.environ["VIDEO_DB_API_KEY"] = ""  # Replace with your actual API key
```

### 🌐 Connecting to VideoDB

Establish a connection to VideoDB and access a collection:

```python
from videodb import connect

conn = connect()
coll = conn.get_collection()
```

### 🎥 Uploading a Video

Upload a base video to add subtitles. We'll use a sample video for this guide:

```python
video = coll.upload(url="https://www.youtube.com/watch?v=il39Ks4mV9g")
video.play()
```

Output should be a playable video within the notebook, directing to the VideoDB console player. Example:

```
'https://console.videodb.io/player?url=https://stream.videodb.io/v3/published/manifests/ef6ef08c-b276-4e1d-b1d0-f0525e697d46.m3u8'
```

> ℹ️ You can also upload videos from your local file system by providing the `file_path` to the `upload()` method.

## 🔊 Indexing Spoken Words

---

To generate subtitles, first index the video's spoken words using `video.index_spoken_words()`:

```python
video.index_spoken_words()
```

A progress bar indicates the indexing process.

```
100%|████████████████████████████████████████████████████████████████████████████████████████████████████| 100/100 [00:32<00:00,  3.04it/s]
```

## 📝 Adding Default Subtitles

---

Add default subtitles to your video using `Video.add_subtitle()`. This method returns a streaming link:

```python
from videodb import play_stream

# Add subtitles to the video
stream_url = video.add_subtitle()

# Play the video with subtitles
play_stream(stream_url)
```

Output should be a playable video within the notebook, directing to the VideoDB console player with subtitles. Example:

```
'https://console.videodb.io/player?url=https://stream.videodb.io/v3/published/manifests/76e0206d-b3af-4a74-9628-54636bf22ddf.m3u8'
```

## 📝 Customizing Subtitle Styles

---

To customize the subtitle style, pass a `SubtitleStyle()` object, configured with your desired styles, to the `Video.add_subtitle()` method.

> ℹ️ Refer to the [SubtitleStyle API Reference](link_to_api_reference - *replace with actual link*) for a complete list of available options.

### 1. Typography and Style

Configure the typography of the subtitles using the following parameters in the `SubtitleStyle()` class:

* `font_name`: The font to use (e.g., "Roboto").
* `font_size`: The font size in pixels.
* `spacing`: Character spacing in pixels.
* `bold`: `True` for bold text, `False` otherwise.
* `italic`: `True` for italic text, `False` otherwise.
* `underline`: `True` for underlined text, `False` otherwise.
* `strike_out`: `True` for strikethrough text, `False` otherwise.

```python
from videodb import SubtitleStyle

stream_url = video.add_subtitle(
    SubtitleStyle(
        font_name="Roboto",
        font_size=12,
        spacing=0,
        bold=False,
        italic=False,
        underline=False,
        strike_out=False,
    )
)
play_stream(stream_url)
```

Output should be a playable video within the notebook, directing to the VideoDB console player with the specified typography. Example:

```
'https://console.videodb.io/player?url=https://stream.videodb.io/v3/published/manifests/86d9e2a6-b0d9-4333-9013-bf355fea051d.m3u8'
```

![](https://github.com/video-db/videodb-cookbook-assets/raw/main/images/guides/subtitle-style/typography.png)

### 2. Color and Effects

Customize the colors of the subtitles using the following parameters:

* `primary_colour`: The main text color.
* `secondary_colour`: Color for karaoke effects or secondary highlighting.
* `outline_colour`: The text outline color.
* `back_colour`: The subtitle background color.

> **ℹ️ Color Format**
>
> `SubtitleStyle` accepts colors in the `&HBBGGRR` hexadecimal format, where BB, GG, and RR represent the blue, green, and red components, respectively. The `&H` prefix is required. For transparency, include an alpha value at the beginning: `&HAABBGGRR`. (AA is the alpha value).

```python
from videodb import SubtitleStyle

stream_url = video.add_subtitle(
    SubtitleStyle(
        primary_colour="&H00A5CFFF",
        secondary_colour="&H00FFFF00",
        outline_colour="&H000341C1",
        back_colour="&H803B3B3B",
    )
)
play_stream(stream_url)
```

Output should be a playable video within the notebook, directing to the VideoDB console player with the specified colors. Example:

```
'https://console.videodb.io/player?url=https://stream.videodb.io/v3/published/manifests/f59f13f4-d2ac-4589-83b7-58cdbb8e9154.m3u8'
```

![](https://github.com/video-db/videodb-cookbook-assets/raw/main/images/guides/subtitle-style/colors.png)

### 3. Position and Margins

Configure the alignment and position of the subtitles using the following parameters:

* `alignment`: The alignment of the subtitle (use `SubtitleAlignment` enum).
* `margin_l`: Left margin in pixels.
* `margin_r`: Right margin in pixels.
* `margin_v`: Top and bottom margin in pixels.

> ℹ️ See the [API Reference](link_to_api_reference - *replace with actual link*) for details on `SubtitleAlignment`.

```python
from videodb import SubtitleStyle, SubtitleAlignment

stream_url = video.add_subtitle(
    SubtitleStyle(
        alignment=SubtitleAlignment.middle_center,
        margin_l=10,
        margin_r=10,
        margin_v=20,
    )
)
play_stream(stream_url)
```

Output should be a playable video within the notebook, directing to the VideoDB console player with the specified position and margins. Example:

```
'https://console.videodb.io/player?url=https://stream.videodb.io/v3/published/manifests/d32a4ae4-e19f-4ca9-9438-4d7b94e327b2.m3u8'
```

![](https://github.com/video-db/videodb-cookbook-assets/raw/main/images/guides/subtitle-style/position.png)

### 4. Text Transformation

Transform the text size and spacing using the following parameters:

* `scale_x`: Horizontal scaling factor.
* `scale_y`: Vertical scaling factor.
* `angle`: Rotation angle in degrees.

```python
from videodb import SubtitleStyle

stream_url = video.add_subtitle(
    SubtitleStyle(
        scale_x=1.5,
        scale_y=3,
        angle=0,
    )
)
play_stream(stream_url)
```

Output should be a playable video within the notebook, directing to the VideoDB console player with the specified transformations. Example:

```
'https://console.videodb.io/player?url=https://stream.videodb.io/v3/published/manifests/f7ebe6d2-a181-46ad-aae3-e824446dc2a4.m3u8'
```

![](https://github.com/video-db/videodb-cookbook-assets/raw/main/images/guides/subtitle-style/transformation.png)

### 5. Borders and Shadow

Add border styles, outlines, and shadows using the following parameters:

* `border_style`: The border style (use `SubtitleBorderStyle` enum).
* `outline`: The width of the text outline in pixels.
* `shadow`: The depth of the shadow behind the text in pixels.

> ℹ️ See the [API Reference](link_to_api_reference - *replace with actual link*) for details on `SubtitleBorderStyle`.

```python
from videodb import SubtitleStyle, SubtitleBorderStyle

stream_url = video.add_subtitle(
    SubtitleStyle(
        shadow=2,
        back_colour="&H00000000",
        border_style=SubtitleBorderStyle.no_border,
    )
)
play_stream(stream_url)
```

Output should be a playable video within the notebook, directing to the VideoDB console player with the specified border and shadow. Example:

```
'https://console.videodb.io/player?url=https://stream.videodb.io/v3/published/manifests/cbbc8812-0fcf-467f-aac6-1976582146bd.m3u8'
```

![](https://github.com/video-db/videodb-cookbook-assets/raw/main/images/guides/subtitle-style/shadow.png)

## 👨‍💻 Next Steps

---

Explore other VideoDB subtitle features and resources:

* [Enhancing Video Captions with VideoDB Subtitle Styling](https://coda.io/d/_dnIYgjBK4eB/_sulRy)


---

## Cleanup Guide

[Source Link](https://github.com/video-db/videodb-cookbook/blob/main/guides/Cleanup.ipynb)

## Guide: Cleaning Up Your VideoDB Account

<a href="https://colab.research.google.com/github/video-db/videodb-cookbook/blob/main/guides/Cleanup.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

⚠️ **WARNING: This notebook will permanently delete media files from your VideoDB account. Data loss is irreversible.** ⚠️

🚨 **IMPORTANT: Before proceeding, carefully review the media files you intend to delete. This action cannot be undone.** 🚨

This guide explains how to remove media files and reclaim storage space within your VideoDB account. It covers:

* Deleting videos
* Deleting audio files
* Deleting images

## 🛠️ Setup

---

Before you begin, ensure you have your [VideoDB](https://videodb.io) API key available.

```python
%pip install videodb
```

```python
import os
from videodb import connect

os.environ["VIDEO_DB_API_KEY"] = "YOUR_KEY_HERE"  # Replace with your actual API key

conn = connect()
```

## Review Collections

---

This section displays information about your collections and the number of media assets within each.

```python
colls = conn.get_collections()

print(f"Found {len(colls)} collections:\n")

for coll in colls:
    videos = coll.get_videos()
    audios = coll.get_audios()
    images = coll.get_images()

    print(f"Collection Name: '{coll.name}' (ID: {coll.id})")
    print(f"  - Videos : {len(videos)}")
    print(f"  - Audio  : {len(audios)}")
    print(f"  - Images : {len(images)}\n")
```

## Select the Target Collection

---

Specify the ID of the collection you wish to clean up.

```python
collection_id = "YOUR_COLLECTION_ID_HERE"  # Replace with the ID of the collection you want to clean.
```

### ⚠️ Delete All Videos

---

**Irreversibly deletes all videos from the selected collection. Use with extreme caution!**

```python
coll = conn.get_collection(collection_id)
videos = coll.get_videos()

for video in videos:
    video.delete()
    print(f"Deleted video: {video.name} (ID: {video.id})")
print("Video deletion complete.")
```

### ⚠️ Delete All Audio

---

**Irreversibly deletes all audio files from the selected collection. Use with extreme caution!**

```python
coll = conn.get_collection(collection_id)
audios = coll.get_audios()

for audio in audios:
    audio.delete()
    print(f"Deleted audio: {audio.name} (ID: {audio.id})")
print("Audio deletion complete.")
```

### ⚠️ Delete All Images

---

**Irreversibly deletes all images from the selected collection. Use with extreme caution!**

```python
coll = conn.get_collection(collection_id)
images = coll.get_images()

for image in images:
    image.delete()
    print(f"Deleted image: {image.name} (ID: {image.id})")
print("Image deletion complete.")
```

---

## Text Asset Guide

[Source Link](https://github.com/video-db/videodb-cookbook/blob/main/guides/TextAsset.ipynb)

# Guide: Text Assets

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/video-db/videodb-cookbook/blob/nb/main/guides/asset/TextAsset.ipynb)

## Overview

This guide introduces `TextAssets` and demonstrates how to overlay text elements on videos using VideoDB. We'll explore customizable configurations for `TextAssets`, including:

* Default Styling
* Font Styling
* Background Box Styling
* Text Shadowing
* Position and Alignment

## Setup

---

### 📦 Installing the VideoDB Package

```python
%pip install videodb
```

### 🔑 API Key

Before proceeding, ensure you have access to VideoDB.

> Get your API key from the [VideoDB Console](https://console.videodb.io). (Free for the first 50 uploads, no credit card required! 🎉)

```python
import os

os.environ["VIDEO_DB_API_KEY"] = ""  # @param {type:"string"}
```

### 🌐 Connecting to VideoDB

```python
from videodb import connect

conn = connect()
coll = conn.get_collection()
```

### 🎥 Uploading a Video

VideoDB utilizes videos as the foundation for creating timelines. For more information, refer to [Timelines and Assets](https://docs.videodb.io/timeline-and-assets-44).

```python
video = coll.upload(url="https://www.youtube.com/watch?v=w4NEOTvstAc")
video.play()
```

## Creating Assets

---

Now, let's create the assets that will be used in our video timeline:

* `VideoAsset`: The base video for the timeline.
* `TextAsset`: The text element to be overlaid on the video.

> Checkout [Timeline and Assets](https://docs.videodb.io/timeline-and-assets-44) for conceptual understanding.

### 🎥 VideoAsset

---

```python
from videodb.asset import VideoAsset

# Create a VideoAsset from the uploaded video
video_asset = VideoAsset(asset_id=video.id, start=0, end=60)
```

### 🔠 TextAsset: Default Styling

---

To create a `TextAsset`, use the `TextAsset` class.

**Parameters:**

* `text` (required): The text to be displayed.
* `duration` (optional): The duration (in seconds) for which the text element should be displayed.

```python
from videodb.asset import TextAsset

text_asset_1 = TextAsset(text="THIS IS A SENTENCE", duration=5)
```

![Default Text Styling](https://github.com/video-db/videodb-cookbook-assets/raw/main/images/guides/text-asset/default_style.png)

### 🔡 TextAsset: Custom Styling

To create a `TextAsset` with custom styling, use the `style` parameter, which accepts a `TextStyle` instance.

> View API Reference for [`TextStyle`](link to TextStyle documentation - if available)

**1. Font Styling**

```python
from videodb.asset import TextAsset, TextStyle

# Create TextAsset with custom font styling using TextStyle
text_asset_2 = TextAsset(
    text="THIS IS A SENTENCE",
    duration=5,
    style=TextStyle(
        font="Inter",
        fontsize=50,
        fontcolor="#FFCFA5",
        bordercolor="#C14103",
        borderw="2",
        box=False,
    ),
)
```

![Font Styling](https://github.com/video-db/videodb-cookbook-assets/raw/main/images/guides/text-asset/font_styling.png)

**2. Configuring Background Box**

```python
from videodb.asset import TextAsset, TextStyle

# Create TextAsset with custom background box styling using TextStyle
text_asset_3 = TextAsset(
    text="THIS IS A SENTENCE",
    duration=5,
    style=TextStyle(
        box=True,
        boxcolor="#FFCFA5",
        boxborderw=10,
        boxw=0,
        boxh=0,
    ),
)
```

![Background Box Styling](https://github.com/video-db/videodb-cookbook-assets/raw/main/images/guides/text-asset/background_box.png)

**3. Configuring Shadows**

```python
from videodb.asset import TextAsset, TextStyle

# Create TextAsset with custom shadow styling using TextStyle
text_asset_4 = TextAsset(
    text="THIS IS A SENTENCE",
    duration=5,
    style=TextStyle(
        shadowcolor="#0AA910",
        shadowx="2",
        shadowy="3",
    ),
)
```

![Shadow Styling](https://github.com/video-db/videodb-cookbook-assets/raw/main/images/guides/text-asset/custom_shadow.png)

**4. Position and Alignment**

```python
from videodb.asset import TextAsset, TextStyle

text_asset_5 = TextAsset(
    text="THIS IS A SENTENCE",
    duration=5,
    style=TextStyle(
        x=50,
        y=50,
        y_align="text",
        text_align="T+L",
        boxcolor="#FFCFA5",
        boxh=100,
        boxw=600,
    ),
)

text_asset_6 = TextAsset(
    text="THIS IS A SENTENCE",
    duration=5,
    style=TextStyle(
        x=50,
        y=50,
        y_align="text",
        text_align="M+C",
        boxcolor="#FFCFA5",
        boxh=100,
        boxw=600,
    ),
)

text_asset_7 = TextAsset(
    text="THIS IS A SENTENCE",
    duration=5,
    style=TextStyle(
        x=50,
        y=50,
        y_align="text",
        text_align="B+R",
        boxcolor="#FFCFA5",
        boxh=100,
        boxw=600,
    ),
)
```

![Text Alignment Top Left](https://github.com/video-db/videodb-cookbook-assets/raw/main/images/guides/text-asset/text_align.png)
![Y Alignment](https://github.com/video-db/videodb-cookbook-assets/raw/main/images/guides/text-asset/y_align.png)

## Viewing the Results

---

### 🎼 Creating a Timeline Using `Timeline`

```python
from videodb.timeline import Timeline

# Initialize a Timeline
timeline = Timeline(conn)

# Add the base VideoAsset inline
timeline.add_inline(video_asset)

# TextAsset with default Styling
timeline.add_overlay(0, text_asset_1)

# TextAsset with Custom Font Styling
timeline.add_overlay(5, text_asset_2)

# TextAsset with Custom Border Box
timeline.add_overlay(10, text_asset_3)

# TextAsset with Custom Shadow
timeline.add_overlay(15, text_asset_4)

# TextAsset with Custom Position and alignment
timeline.add_overlay(20, text_asset_5)
timeline.add_overlay(25, text_asset_6)
timeline.add_overlay(30, text_asset_7)
```

### ▶️ Playing the Video

```python
from videodb import play_stream

stream_url = timeline.generate_stream()
play_stream(stream_url)
```

## 👨‍💻 Next Steps

---

If you have any questions or feedback, feel free to reach out:

* [Discord](https://discord.gg/py9P639jGz)
* [GitHub](https://github.com/video-db)
* [VideoDB](https://videodb.io)
* Email: ashu@videodb.io  |  contact@videodb.io
