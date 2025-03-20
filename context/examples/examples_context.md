```markdown
# IPYNB Notebook: Scene Index QuickStart [Source Link](https://github.com/video-db/videodb-cookbook/blob/main/quickstart/Scene%20Index%20QuickStart.ipynb)

```markdown
# ⚡️ Quickstart: Scene Indexing with VideoDB

<a href="https://colab.research.google.com/github/video-db/videodb-cookbook/blob/main/quickstart/Scene%20Index%20QuickStart.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

This guide provides a quick introduction to scene indexing with VideoDB, enabling you to easily extract and search for visual information within your videos. Leverage the power of vision models and VideoDB to build powerful retrieval augmented generation (RAG) systems.

For example, quickly search for "religious gatherings" within a video:

![](https://raw.githubusercontent.com/video-db/videodb-cookbook/main/images/scene_index/intro.png)

## Setup
---

### 📦 Install VideoDB

Install the VideoDB package using pip:

```python
!pip install -U videodb
```

### 🔑  Set your API Key

```python
import os

# Replace with your actual API key
os.environ["VIDEO_DB_API_KEY"] = "sk-xxxx-yyyyy-zzzz"
```

### 🌐 Connect to VideoDB

```python
from videodb import connect

conn = connect()
coll = conn.get_collection()
```

### 🎥 Upload a Video

Upload a video to your VideoDB collection. Here, we're using a YouTube URL for demonstration:

```python
video = coll.upload(url="https://www.youtube.com/watch?v=LejnTJL173Y")
```

## 📇 Index Scenes
---

The `index_scenes` function analyzes your video and creates an index of its visual content.

```python
index_id = video.index_scenes()
```

### Optional Parameters for Customization

The `index_scenes()` function offers several optional parameters for fine-tuning the indexing process:

*   **`extraction_type`**:  Choose the scene extraction algorithm (e.g., time-based, content-based).
*   **`extraction_config`**: Configure the chosen extraction algorithm (e.g., specify time intervals for time-based extraction).
*   **`prompt`**: Use a prompt to guide the vision model in describing scenes and frames. This allows you to tailor the descriptions to your specific needs.

For more detailed information on Scene and Frame objects, see [Advanced Visual Search](https://github.com/video-db/videodb-cookbook/blob/main/guides/video/scene-index/advanced_visual_search.ipynb).

```python
from videodb import SceneExtractionType, IndexType

index_id = video.index_scenes(
    extraction_type=SceneExtractionType.time_based,
    extraction_config={"time": 10, "select_frames": ['first']},
    prompt="describe the image in 100 words",
)

# Wait for indexing to finish and retrieve the scene index
scene_index = video.get_scene_index(index_id)
scene_index
```

```output
[{'description': 'The image depicts a man sitting in an office or conference room, characterized by the presence of glass windows with blinds behind him. He is wearing a dark suit, a white dress shirt, and a dark striped tie. The man appears to be contemplative, with his eyes closed or looking down, and a slight smile on his face. The background shows a bright, well-lit room with natural light filtering through the windows. The atmosphere seems professional and formal, suggesting a workplace or corporate environment. The man’s bald head and expression give an impression of a moment of reflection or contentment.',
  'end': 10.01,
  'start': 0.0},
 {'description': 'The image shows a man with a receding hairline, wearing a dark suit, light blue shirt, and dark striped tie. He appears to be seated, with a neutral or slightly contemplative expression on his face. Behind him, there are large office windows with horizontal blinds partially closed, through which an indistinct office environment is visible. The lighting is soft, creating a professional atmosphere. The man’s posture suggests he could be engaged in a conversation or in thought, possibly in a workplace setting. The overall mood seems formal and reflective, indicating a business or serious context.',
  'end': 20.02,
  'start': 10.01},
  ... # Output truncated for brevity
 ]
```

> **Note:** Allow 5-10 seconds for the index to become available for searching after creation.

Now, search your video using the `index_id`.

```python
res = video.search(query="religious gathering",
                  index_type=IndexType.scene,
                  index_id=index_id)

res.play()
```

This will return a URL to play the video, highlighting the sections that match your search query.

## ⚙️ Scene Index Parameters

Here's a breakdown of the parameters for the `index_scenes` function:

*   **`extraction_type`**: Determines the algorithm used to identify and extract scenes from the video.
*   **`extraction_config`**: Provides specific settings for the chosen `extraction_type`.
*   **`prompt`**:  A text prompt that guides the vision model in describing each scene. This allows you to focus on specific content or activities.
*   **`callback_url`**: (Optional) A URL to receive a notification when the indexing process is complete.

### Deeper Dive into Parameters

#### ⚙️ `extraction_type` & `extraction_config`

Videos are essentially sequences of images. The `extraction_type` and `extraction_config` parameters let you control how these images are analyzed and grouped into scenes. Experiment with different algorithms to identify the most relevant frames for describing your videos. See the [Scene Extraction Algorithms documentation](https://docs.videodb.io/scene-extraction-algorithms-84) for more details.

![](https://raw.githubusercontent.com/video-db/videodb-cookbook/main/images/scene_index/VSF.png)

#### ⚙️ `prompt`

The `prompt` parameter is crucial for guiding the vision model and tailoring the generated descriptions. For example, to identify running activity:

> "Describe clearly what is happening in the video. Add `running_detected` if you see a person running."

To experiment with your own models and prompts, check out [Advanced Visual Search Pipelines](https://github.com/video-db/videodb-cookbook/blob/main/guides/scene-index/advanced_visual_search.ipynb).

#### ⚙️ `callback_url`

The `callback_url` allows you to receive asynchronous notifications when the indexing job is finished. See the [callback details documentation](https://docs.videodb.io/callback-details-66#_lubHL) for more information.

<div style="height:40px;"></div>

## 🗂️ Managing Indexes
---

> 💡 Create multiple scene indexes for a single video and rank search results based on relevance for your users.

**List all scene indexes for a video:**

The `video.list_scene_index()` method returns a list of available scene indexes, including their `id`, `name`, and `status`.

```python
scene_indexes = video.list_scene_index()
print(scene_indexes)
```

```output
[{'name': 'Scene Index 2024-07-22 10:06', 'scene_index_id': 'f4db35c5ce45a709', 'status': 'done'}]
```

**Get a specific index:**

The `video.get_scene_index()` method retrieves a specific scene index based on its `scene_index_id`, providing details like `start`, `end`, and `description` for each scene.

```python
scene_index = video.get_scene_index(index_id)
print(scene_index)
```

```output
[{'description': 'The image depicts a man sitting in an office or conference room, characterized by the presence of glass windows with blinds behind him. He is wearing a dark suit, a white dress shirt, and a dark striped tie. The man appears to be contemplative, with his eyes closed or looking down, and a slight smile on his face. The background shows a bright, well-lit room with natural light filtering through the windows. The atmosphere seems professional and formal, suggesting a workplace or corporate environment. The man’s bald head and expression give an impression of a moment of reflection or contentment.', 'end': 10.01, 'start': 0.0}, {'description': 'The image shows a man with a receding hairline, wearing a dark suit, light blue shirt, and dark striped tie. He appears to be seated, with a neutral or slightly contemplative expression on his face. Behind him, there are large office windows with horizontal blinds partially closed, through which an indistinct office environment is visible. The lighting is soft, creating a professional atmosphere. The man’s posture suggests he could be engaged in a conversation or in thought, possibly in a workplace setting. The overall mood seems formal and reflective, indicating a business or serious context.', 'end': 20.02, 'start': 10.01}, ... ]
```

**Delete an index:**

```python
video.delete_scene_index(index_id)
```

## 🧑‍💻 Deep Dive

Explore these resources for more in-depth information on scene indexing:

*   **[Custom Annotations Pipeline](https://github.com/video-db/videodb-cookbook/blob/main/guides/scene-index/custom_annotations.ipynb)**: Bring your own scene descriptions and annotations.
*   **[Playground for Scene Extractions](https://github.com/video-db/videodb-cookbook/blob/main/guides/scene-index/playground_scene_extraction.ipynb)**: Experiment with different extraction algorithms, prompts, and search strategies.
*   **[Advanced Visual Search Pipelines](https://github.com/video-db/videodb-cookbook/blob/main/guides/scene-index/advanced_visual_search.ipynb)**: Create flexible and powerful visual search solutions.

If you have any questions or feedback, please reach out!

*   [Discord](https://discord.gg/py9P639jGz)
*   [GitHub](https://github.com/video-db)
*   [Website](https://videodb.io)
*   [Email](ashu@videodb.io)
```

---

# IPYNB Notebook: VideoDB Quickstart [Source Link](https://github.com/video-db/videodb-cookbook/blob/main/quickstart/VideoDB%20Quickstart.ipynb)

```markdown
# ⚡️ QuickStart: VideoDB

<a href="https://colab.research.google.com/github/video-db/videodb-cookbook/blob/main/quickstart/VideoDB%20Quickstart.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

This notebook provides a hands-on introduction to [VideoDB](https://videodb.io), a platform for indexing, searching, and streaming video content. You'll learn how to upload videos, generate streamable URLs, perform semantic and keyword searches, and integrate VideoDB into Retrieval Augmented Generation (RAG) pipelines.

<div style="height:40px;"></div>

### Setup
---

#### 🔧 Install VideoDB

Install the VideoDB Python package using pip:

```python
!pip install -U videodb
```

#### 🔑 Connect to VideoDB

Establish a connection to VideoDB using your API key. You can either pass the API key directly or set it as the `VIDEO_DB_API_KEY` environment variable.

> 💡 Get your API key from the [VideoDB Console](https://console.videodb.io). (Free for the first 50 uploads, no credit card required!) 🎉

```python
from videodb import connect, play_stream

# Replace with your API key
conn = connect(api_key="sk-xxx-yyyyy-zzzz")
```

<div style="height:40px;"></div>

### Working with a Single Video
---

#### ⬆️ Upload a Video

Upload a video using `conn.upload()`. You can upload from a public URL or a local file path. The `upload` function returns a `Video` object, which provides access to various video methods.

```python
# Upload a video by URL
video = conn.upload(url="https://www.youtube.com/watch?v=wU0PYcCsL6o")
```

<div style="background-color: #ffffcc; color: black; padding: 10px; border-radius: 5px;">
VideoDB simplifies uploads by supporting links from YouTube, S3, or any public URL with video content.
</div>

#### 📺 View Your Video

Videos are instantly available for viewing at 720p resolution.

*   Generate a streamable URL using `video.generate_stream()`.
*   Preview the video in your browser/notebook using `video.play()`.

<div style="background-color: #ffffcc; color: black; padding: 10px; border-radius: 5px;">
    <strong>Note:</strong> If viewing this notebook on GitHub, the embedded player might not work due to security restrictions. Please open the printed URL in your browser to view the video.
</div>

```python
video.generate_stream()
video.play()
```

```text
'https://console.videodb.io/player?url=https://stream.videodb.io/v3/published/manifests/0645b883-5e48-4136-a5bc-f046b3a166a2.m3u8'
```

#### ✂️ Get Specific Video Sections

Clip specific sections of a video by providing a timeline of start and end times (in seconds) to `video.generate_stream()`.

For example, the following streams only the first 10 seconds and then seconds 120 to 140 of the uploaded video:

```python
stream_link = video.generate_stream(timeline=[[0, 10], [120, 140]])
play_stream(stream_link)
```

```text
'https://console.videodb.io/player?url=https://stream.videodb.io/v3/published/manifests/d0a049ff-be6e-41f7-826e-4a6e411f7bab.m3u8'
```

#### 🔍 Indexing a Video

To enable search within a video, you must first index it. VideoDB currently offers two types of indexes:

1.  `index_spoken_words`: Indexes spoken words within the video and automatically generates a searchable transcript. Supports 20+ languages. See [Language Support](https://docs.videodb.io/language-support-79) for more information.
2.  `index_scenes`: Indexes visual information and events in the video, enabling you to find specific scenes, activities, objects, or emotions. Refer to the [Scene Index Documentation](https://docs.videodb.io/scene-index-documentation-80) for details.

<div style="background-color: #ffffcc; color: black; padding: 10px; border-radius: 5px;">
    <strong>Note:</strong> Indexing may take time, especially for longer videos.
</div>

```python
# Index spoken content of the video
video.index_spoken_words()
```

```text
100%|████████████████████████████████████████████████████████████████████████████████████████████████████| 100/100 [00:18<00:00,  5.40it/s]
```

```python
# Index visual information in video frames. Customize the prompt for your use case.
# You can index a video multiple times with different prompts.
index_id = video.index_scenes(
    prompt="Describe the scene in strictly 100 words"
)

# Wait for indexing to finish
scene_index = video.get_scene_index(index_id)
scene_index
```

```text
[{'description': "This stunning scene captures the majestic beauty of a snow-covered mountain peak piercing through a clear blue sky. The jagged ridgeline glistens under the sunlight, displaying a breathtaking expanse of pure white. Surrounding peaks and ridges stretch across the horizon, some shrouded in mist and clouds, adding depth to the expansive, tranquil landscape. The stark contrast between the bright snow, dark rocky outcrops, and the azure sky creates a dramatic and awe-inspiring view. The serenity and grandeur of this high-altitude environment evoke a sense of wonder and contemplation, showcasing nature's pristine and rugged beauty in its purest form.", 'end': 5.8, 'start': 0.0}, {'description': "A man rides a bicycle on a bustling city street, surrounded by towering high-rise buildings. He's in motion, his posture leaning slightly forward as if to accelerate. Pedestrians walk along the sidewalks, some carrying bags or talking on their phones. The weather appears mild, with the cyclist wearing casual clothes suitable for a pleasant day. Traffic signs and streetlights indicate it is a busy urban area. The buildings vary in architectural styles, from modern glass towers to older, more ornate structures. The scene captures a typical day in a lively, possibly metropolitan, street setting.", 'end': 10.24, 'start': 5.8}, ... ]
```

#### 🔎 Search Inside a Video

Search indexed videos using `video.search()`. Available search types and indexes include:

*   `SearchType.semantic`: For question-answering-style queries (default).
*   `SearchType.keyword`: For exact word or sentence matching (only available for single videos).
*   `IndexType.scene`: Search visual information (requires `index_scenes`).
*   `IndexType.spoken_word`: Search spoken content (requires `index_spoken_words`).

```python
from videodb import SearchType, IndexType

result = video.search(query="what's the dream?", search_type=SearchType.semantic, index_type=IndexType.spoken_word)
result.play()
```

```text
'https://console.videodb.io/player?url=https://stream.videodb.io/v3/published/manifests/de284dc9-1aa9-440b-b407-b8fc5aa07273.m3u8'
```

```python
# Try with different queries
query = "mountains"

result = video.search(query=query, search_type=SearchType.semantic, index_type=IndexType.scene)
result.play()
```

```text
'https://console.videodb.io/player?url=https://stream.videodb.io/v3/published/manifests/72baa6ff-2758-49bb-b8d6-237f44e4b6c1.m3u8'
```

##### 📺 View Search Results

`video.search()` returns a `SearchResults` object containing sections/shots semantically matching your query:

*   `result.get_shots()`: Returns a list of `Shot` objects that matched the search query.
*   `result.play()`: Opens the video in your browser/notebook, highlighting the relevant segments.

##### 🗑️ Cleanup

Delete the video from VideoDB using `video.delete()`:

```python
video.delete()
```

<div style="height:40px;"></div>

## RAG: Working with Multiple Videos
---

`VideoDB` simplifies storing and searching across multiple videos. By default, videos are uploaded to your default collection. You can create and manage multiple collections. See our [Collections documentation](https://docs.videodb.io/collections-68) for details.

If you're using LlamaIndex to build RAG pipelines on your video data, leverage the VideoDB retriever. See [LlamaIndex documentation](https://docs.llamaindex.ai/en/stable/examples/retrievers/videodb_retriever.html).

#### 🔄 Uploading Multiple Videos to a Collection

```python
# Get the default collection
coll = conn.get_collection()

# Upload videos to the collection
coll.upload(url="https://www.youtube.com/watch?v=lsODSDmY4CY")
coll.upload(url="https://www.youtube.com/watch?v=vZ4kOr38JhY")
coll.upload(url="https://www.youtube.com/watch?v=uak_dXHh6s4")
```

```text
Video(id=m-6d1b1bf6-a2ba-4786-a3a8-8efbabfee28c, collection_id=c-a2dc1100-1faa-4394-803c-ca808da09c47, stream_url=https://d27qzqw9ehjjni.cloudfront.net/v3/published/manifests/4e41464d-0ca6-40da-86f7-3e803ff8d840.m3u8, player_url=https://console.videodb.io/player?url=https://d27qzqw9ehjjni.cloudfront.net/v3/published/manifests/4e41464d-0ca6-40da-86f7-3e803ff8d840.m3u8, name=AMA #3: Adaptogens, Fasting & Fertility, Bluetooth/EMF Risks, Cognitive Load Limits & More, description=None, thumbnail_url=None, length=1921.2193)
```

Collection methods:

*   `conn.get_collection()`: Returns the default `Collection` object.
*   `coll.get_videos()`: Returns a list of `Video` objects within the collection.
*   `coll.get_video(video_id)`: Returns a specific `Video` object by its ID.
*   `coll.delete_video(video_id)`: Deletes a video from the collection.

### 📂 Searching Across Multiple Videos in a Collection

Index all videos in a collection and use the `search` method to find relevant results. Here, we index the spoken content for a quick demonstration.

<div style="background-color: #ffffcc; color: black; padding: 10px; border-radius: 5px;">
    <strong>Note:</strong> Indexing can take time, particularly for longer videos.
</div>

```python
# Index the spoken content of each video
for video in coll.get_videos():
    video.index_spoken_words()
    print(f"Indexed {video.name}")
```

```text
Indexed AMA #3: Adaptogens, Fasting & Fertility, Bluetooth/EMF Risks, Cognitive Load Limits & More
Indexed AMA #1: Leveraging Ultradian Cycles, How to Protect Your Brain, Seed Oils Examined and More
Indexed AMA #2: Improve Sleep, Reduce Sugar Cravings, Optimal Protein Intake, Stretching Frequency & More
```

### Search Inside a Collection

Search across videos within a collection using `coll.search()`:

```python
# Search in the collection of videos
results = coll.search(query="Deep sleep")
results.play()
```

```text
'https://console.videodb.io/player?url=https://d27qzqw9ehjjni.cloudfront.net/v3/published/manifests/fdd420dd-b104-43dd-9a0f-d3f0afd5b718.m3u8'
```

```python
results = coll.search(query="What are the benefits of morning sunlight?")
results.play()
```

```text
'https://console.videodb.io/player?url=https://d27qzqw9ehjjni.cloudfront.net/v3/published/manifests/60cc252f-abf9-497d-93db-0a53dbffdcf0.m3u8'
```

```python
results = coll.search(query="What are Adaptogens?")
results.play()
```

```text
'https://console.videodb.io/player?url=https://d27qzqw9ehjjni.cloudfront.net/v3/published/manifests/9f690de4-758e-4ac8-9316-916a30e01e72.m3u8'
```

#### 📺 View Search Results

`coll.search()` returns a `SearchResults` object containing sections/shots from videos that semantically match your query:

*   `result.get_shots()`: Returns a list of `Shot` objects that matched the search query.
*   `result.play()`: Opens the video in your browser/notebook, highlighting the relevant segments.

<div style="background-color: #ffffcc; color: black; padding: 10px; border-radius: 5px;">
As you can see, VideoDB fundamentally removes file limitations and empowers you to access and stream videos seamlessly. Stay tuned for more exciting features in upcoming versions and keep building awesome projects with VideoDB! 🤘
</div>

<div style="height:40px;"></div>

### 🌟 Explore More with the Video Object

Several methods are available on the `Video` object to enhance your workflows.

#### Access Transcripts

```python
text_json = video.get_transcript()
text = video.get_transcript_text()
print(text)
```

```text
- If you awaken from this illusion and you understand that black implies white, self implies other, life implies death, or shall I say death implies life, you can feel yourself not as a stranger in the world, not as something here on probation, not as something that has arrived here by fluke, but you can begin to feel your own existence as absolutely fundamental. I'm not trying to sell you on this idea in the sense of converting you to it. I want you to play with it. I want you to think of its possibilities. I'm not trying to prove it. I'm just putting it forward as a possibility of life to think about. So then - let's suppose that you were able every night to dream any dream you wanted to dream and that you could, for example, have the power within one night to dream 75 years of time or any length of time you wanted to have. And you would naturally, as you began on this adventure of dreams, you would fulfill all your wishes. You would have every kind of pleasure conceived. And after several nights of 75 years of total pleasure each, you would say, well, that was pretty great, but now let's. Let's have a surprise. Let's have a dream which isn't under control. Well, something is going to happen to me that I don't know what it's going to be. And you would dig that and come out of that and say, wow, that was a close shave, wasn't it? Then you would get more and more adventurous and you would make further and further out gambles as to what you would dream. And finally you would dream where you are now. You would dream the dream of living the life that you are actually living - today. That would be within the infinite multiplicity of choices you would have of playing that you weren't goddesse. Because the whole nature of the godhead, according to this idea, is to play that hes not. So in this idea, then, everybody is fundamentally the ultimate reality. Not God in a politically kingly sense, but God in the sense of being the self, the deep down basic whatever there is. And you're all that, only you're pretending you're - nothing. -
```

#### Access Visual Scene Descriptions

```python
video.get_scene_index(index_id)
```

```text
[{'description': 'Snow-covered mountain peaks dominate the scene, shrouded in a blanket of ice and snow. The sharp ridges and steep slopes are breathtaking, with one prominent peak in the foreground. The sun shines brightly, casting shadows that accentuate the rugged terrain. In the distance, a series of jagged summits stretch across the horizon, partially obscured by wisps of clouds. The deep blue sky contrasts starkly with the white snow, creating a dramatic and serene landscape. The vastness and majesty of the mountains evoke a sense of awe, showcasing the raw beauty of the natural world.', 'end': 5.8, 'start': 0.0}, {'description': 'A vibrant, bustling festival scene filled with bright decorations and lively atmosphere. A diverse crowd of people in colorful outfits enjoys the festivities, some dancing, others taking photos or buying food from various stalls. Flags and streamers adorn the area, and a stage features a lively performance. Children run around playfully, adding to the joyous ambiance. The sky is clear with the sun shining brightly. The scene is spirited and packed with cultural elements, showcasing a blend of tradition and modernity, capturing the essence of a community coming together in celebration, laughter, and shared happiness.', 'end': 10.24, 'start': 5.8}, ...]
```

#### Add Subtitles to a Video

`video.add_subtitle()` returns a new stream instantly with subtitles added to the video. Many styling parameters, such as font, size, and background color, are available. See the [Subtitle Styles notebook](https://github.com/video-db/videodb-cookbook/blob/main/guides/Subtitle.ipynb) for details.

```python
new_stream = video.add_subtitle()
play_stream(new_stream)
```

```text
'https://console.videodb.io/player?url=https://stream.videodb.io/v3/published/manifests/c4f9baf4-180e-4cdb-b48d-407c71fe4080.m3u8'
```

#### Generate a Thumbnail

Use `video.generate_thumbnail(time=)` to generate a thumbnail image from any timestamp.

```python
from IPython.display import Image

image = video.generate_thumbnail(time=12.0)
Image(url=image.url)
```

##### Delete a video

*   `video.delete()`: Deletes a video.

```python
video.delete()
```

<div style="background-color: #ffffcc; color: black; padding: 10px; border-radius: 5px;">
Explore more examples and tutorials at 👉 <a href="https://docs.videodb.io/build-with-videodb-35">Build with VideoDB</a> to discover what you can build with VideoDB.
</div>
```

---

# IPYNB Notebook: Multimodal_Quickstart [Source Link](https://github.com/video-db/videodb-cookbook/blob/main/quickstart/Multimodal_Quickstart.ipynb)

 This was processed through custom_2.txt

---

# IPYNB Notebook: Subtitle [Source Link](https://github.com/video-db/videodb-cookbook/blob/main/guides/Subtitle.ipynb)

```markdown
## Guide: Styling Subtitles with VideoDB

<a href="https://colab.research.google.com/github/video-db/videodb-cookbook/blob/nb/main/guides/video/Subtitle.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

This guide demonstrates how to customize subtitle styles using the `SubtitleStyle` class in VideoDB. You'll see visual examples of different configurations, covering:

*   **Typography and Style:** Font, size, spacing, and text styling (bold, italic, underline, strikethrough).
*   **Color and Effects:** Text, outline, and background colors with transparency.
*   **Positioning and Margins:** Alignment and margins for optimal placement.
*   **Text Transformation:** Scaling and rotation of the subtitle text.
*   **Borders and Shadow:** Adding borders and shadows for enhanced readability.

## 🛠️ Setup

### 📦 Installing the VideoDB Package

```python
%pip install videodb
```

### 🔑 API Key

You'll need a VideoDB API key to proceed.

> Get your API key from the [VideoDB Console](https://console.videodb.io). (Free for the first 50 uploads, no credit card required! 🎉)

```python
import os
os.environ["VIDEO_DB_API_KEY"] = ""
```

### 🌐 Connecting to VideoDB

```python
from videodb import connect

conn = connect()
coll = conn.get_collection()
```

### 🎥 Uploading a Video

Upload a base video to which we'll add subtitles. We'll use this example video for the guide.

```python
video = coll.upload(url="https://www.youtube.com/watch?v=il39Ks4mV9g")
video.play()
```

> ℹ️ You can also upload videos from your local file system by providing the `file_path` to the `upload()` method.

## 🔊 Indexing Spoken Words

Before adding subtitles, index the video's spoken words using `video.index_spoken_words()`. This generates the necessary transcript for the subtitles.

```python
video.index_spoken_words()
```

```
100%|████████████████████████████████████████████████████████████████████████████████████████████████████| 100/100 [00:32<00:00,  3.04it/s]
```

## 📝 Adding Default Subtitles

The simplest way to add subtitles is using `Video.add_subtitle()`. This will generate subtitles with default styling.

The method returns a streaming URL which can be played using `play_stream()`.

```python
from videodb import play_stream

# Add subtitles to the video
stream_url = video.add_subtitle()

# Play the stream with subtitles
play_stream(stream_url)
```

## 📝 Customizing Subtitle Styles

To customize the appearance of subtitles, pass a `SubtitleStyle()` object with your desired configurations to the `Video.add_subtitle()` method.

> ℹ️ Refer to the API Reference for the `SubtitleStyle` class to see all available options.

### 1. Typography and Style

Control the typography of your subtitles using these `SubtitleStyle()` parameters:

*   `font_name`: The font to use (e.g., "Roboto", "Arial").
*   `font_size`: The font size in pixels.
*   `spacing`: Spacing between characters in pixels.
*   `bold`: Set to `True` for bold text.
*   `italic`: Set to `True` for italic text.
*   `underline`: Set to `True` for underlined text.
*   `strike_out`: Set to `True` for strikethrough text.

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

![](