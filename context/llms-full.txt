# Task
---
You are an advanced assistant specialized in generating VideoDB Python code. You have deep knowledge of VideoDB's platform, SDK, and best practices.
Your primary role is to assist users in integrating and utilizing the **"VideoDB" Python SDK** for their projects. You will be given:

1. **User Query** – A request describing a specific functionality or task they want to achieve using the "VideoDB" SDK.
2. **VideoDB SDK Documentation** – Relevant details about the available classes, methods, and usage examples from the SDK.

### Your Responsibilities:
- **Understand the User Query:** Analyze the user's request to determine the exact functionality they need.
- **Use the SDK Documentation:** Extract the relevant details from the provided SDK documentation to construct an appropriate solution.
- **Generate Python Code Only:** Return only the necessary Python code without any additional explanation or formatting.
- **Use Comments Where Necessary:** Small inline comments can be added to improve code readability.
- **Avoid Unnecessary Function Wrappers & Error handlers:** If the code is short and does not require functional abstraction, implement it as a simple, linear flow.

### RULES:
- Stick to the provided SDK documentation; do not assume functionalities that are not explicitly mentioned.
- Return only Python code without external text.
- If the request is unclear, ask for clarification before proceeding.
- Always use explicit imports; if a class from a submodule is used (VideoAsset, TextAsset), import it directly (from videodb.asset import VideoAsset, TextAsset) instead of accessing it via videodb.asset.ClassName. Avoid mixing import styles.

# VideoDB Overview
---
## **What is VideoDB?**  

VideoDB is a **serverless video database** designed to treat videos as structured data rather than just files. It enables developers to:  

- **Store** videos in the cloud with automatic indexing.  
- **Search within videos** using AI-powered semantic search and speech-to-text indexing.  
- **Stream videos** dynamically, including full videos or specific clipped segments.  
- **Edit videos programmatically** using an API-driven timeline model (combine clips, overlay text/audio, etc.).  
- **Integrate videos into AI/ML workflows** for tasks like video-based retrieval-augmented generation (RAG) or automated highlight generation.  

VideoDB abstracts away complex video processing (such as transcoding, storage, and searching) and provides a **Python SDK** to interact with video data in a structured way.  

---

## **Core Concepts in VideoDB**  

### **1. Connecting to VideoDB**  

Before using VideoDB, developers establish a **connection** using an API key. This connection acts as an interface to manage videos and collections. Once connected, users can upload videos, retrieve collections, and perform various operations.  

### **2. Uploading Videos**  

Videos can be uploaded from **local files**, **URLs**, or **cloud storage**. VideoDB automatically processes the uploaded media, preparing it for **search**, **streaming**, and **editing**. Once uploaded, each video is represented as a structured object with metadata such as duration, resolution, and unique identifiers.  

### **3. Streaming and Clipping**  

Instead of dealing with raw video files, VideoDB allows **on-the-fly streaming**. Developers can:  

- Retrieve a **streaming URL** for a full video.  
- Generate a **clip** by specifying a start and end time.  
- Stitch together multiple segments dynamically for customized playback.  

This approach eliminates the need for manual video editing and re-encoding, as all operations are handled in real-time.  

### **4. Searching Inside Videos**  

A key feature of VideoDB is **AI-powered search**. Videos are not just stored—they can be **indexed** for deep content search. This includes:  

- **Speech-to-text indexing:** Automatically transcribe spoken words in videos.  
- **Semantic search:** Find relevant moments based on meaning, not just exact words.  
- **Scene-based indexing (upcoming):** Detect and search based on visual content.  

Once indexed, users can **query** videos like a database, retrieving relevant segments instead of manually scrubbing through footage.  

### **5. Organizing Videos with Collections**  

Videos in VideoDB belong to **collections**, which function like structured containers for organizing and searching multiple videos together. Developers can:  

- Upload videos into a collection.  
- Search across all videos within a collection.  
- Retrieve and manage videos systematically.  

Collections enable scalable **multi-video queries**, making it easy to build applications that analyze large video datasets.  

### **6. Editing & Composing Videos with the API**  

VideoDB allows developers to create **dynamic video compositions** without modifying original files. Using a **timeline-based model**, users can:  

- **Concatenate video segments** (stitching clips together).  
- **Overlay audio, images, or text** (e.g., adding subtitles or background music).  
- **Generate a stream of the final edited video** without rendering new files.  

This makes VideoDB a powerful tool for AI-driven content generation, automated video summaries, and programmatic video editing.  

### **7. Integration with AI & Machine Learning**  

VideoDB is built with **AI applications in mind**. It enables:  

- **Retrieval-Augmented Generation (RAG) for video-based Q&A.**  
- **Automated video summarization** (extracting key moments).  
- **Interactive AI-powered video search and recommendation.**  

By combining search, indexing, and streaming, VideoDB allows developers to create **intelligent video assistants** that can retrieve and generate video content on demand.  

---

## **Your Role**  

- Clearly explain these **concepts** to the user.  
- Use simple and structured explanations—no need for function signatures or code.  
- When referring to specific SDK features, describe their **purpose** rather than providing exact method details.  
- Avoid redundant explanations; focus on how VideoDB works conceptually.  

A separate reference will provide function-level details when needed. Now, use the provided SDK documentation to respond to user queries about VideoDB’s functionality. j

# VideoDB Python SDK

The VideoDB Python SDK is a Python library for interacting with the [VideoDB]([https://videodb.io](https://videodb.io))
Generate API keys at [https://console.videodb.io](https://console.videodb.io)

## The Following are submodules of the VideoDB Python SDK:

## Default Module videodb (from videodb import class, func)

### videodb.connect(api_key: str | None = None, base_url: str | None = 'https://api.videodb.io', log_level: int | None = 20) → [Connection](#videodb.client.Connection)

A client for interacting with a videodb via REST API

* **Parameters:**
  * **api_key** (*str*) – The api key to use for authentication
  * **base_url** (*str*) – (optional) The base url to use for the api
  * **log_level** (*int*) – (optional) The log level to use for the logger
* **Returns:**
  A connection object
* **Return type:**
  [videodb.client.Connection](#videodb.client.Connection)

### videodb.play_stream(url: str)

Play a stream url in the browser/ notebook

* **Parameters:**
  **url** (*str*) – The url of the stream
* **Returns:**
  The player url if the stream is opened in the browser or the iframe if the stream is opened in the notebook

### *class* videodb.VideodbError(message: str = 'An error occurred', cause=None)

Base class for all videodb exceptions.

### *class* videodb.AuthenticationError(message, response=None)

Raised when authentication is required or failed.

### *class* videodb.InvalidRequestError(message, response=None)

Raised when a request is invalid.

### *class* videodb.SearchError(message)

Raised when a search is invalid.

#### videodb.VIDEO_DB_API

### *class* videodb.IndexType

#### scene *= 'scene'*

#### spoken_word *= 'spoken_word'*

### *class* videodb.MediaType

#### audio *= 'audio'*

#### image *= 'image'*

#### video *= 'video'*

### *class* videodb.SearchType

#### keyword *= 'keyword'*

#### llm *= 'llm'*

#### scene *= 'scene'*

#### semantic *= 'semantic'*

### *class* videodb.SceneExtractionType

#### shot_based *= 'shot'*

#### time_based *= 'time'*

### *class* videodb.Segmenter

#### sentence *= 'sentence'*

#### time *= 'time'*

#### word *= 'word'*

### *class* videodb.SubtitleAlignment

#### bottom_center *= 2*

#### bottom_left *= 1*

#### bottom_right *= 3*

#### middle_center *= 10*

#### middle_left *= 9*

#### middle_right *= 11*

#### top_center *= 6*

#### top_left *= 5*

#### top_right *= 7*

### *class* videodb.SubtitleBorderStyle

#### no_border *= 1*

#### opaque_box *= 3*

#### outline *= 4*

### *class* videodb.SubtitleStyle(font_name: str = 'Arial', font_size: float = 18, primary_colour: str = '&H00FFFFFF', secondary_colour: str = '&H000000FF', outline_colour: str = '&H00000000', back_colour: str = '&H00000000', bold: bool = False, italic: bool = False, underline: bool = False, strike_out: bool = False, scale_x: float = 1.0, scale_y: float = 1.0, spacing: float = 0, angle: float = 0, border_style: int = 4, outline: float = 1.0, shadow: float = 0.0, alignment: int = 2, margin_l: int = 10, margin_r: int = 10, margin_v: int = 10)

### *class* videodb.TextStyle(fontsize: int = 24, fontcolor: str = 'black', fontcolor_expr: str = '', alpha: float = 1.0, font: str = 'Sans', box: bool = True, boxcolor: str = 'white', boxborderw: str = '10', boxw: int = 0, boxh: int = 0, line_spacing: int = 0, text_align: str = 'T', y_align: str = 'text', borderw: int = 0, bordercolor: str = 'black', expansion: str = 'normal', basetime: int = 0, fix_bounds: bool = False, text_shaping: bool = True, shadowcolor: str = 'black', shadowx: int = 0, shadowy: int = 0, tabsize: int = 4, x: str | int = '(main_w-text_w)/2', y: str | int = '(main_h-text_h)/2')

## Module : videodb.client (from videodb.client import class, func)

### *class* videodb.client.Connection(api_key: str, base_url: str)

Bases: `HttpClient`

Connection class to interact with the VideoDB

#### \_\_init_\_(api_key: str, base_url: str) → [Connection](#videodb.client.Connection)

Initializes a new instance of the Connection class with specified API credentials.

Note: Users should not initialize this class directly.
Instead use [`videodb.connect()`](#videodb.connect)

* **Parameters:**
  * **api_key** (*str*) – API key for authentication
  * **base_url** (*str*) – Base URL of the VideoDB API
* **Raises:**
  **ValueError** – If the API key is not provided
* **Returns:**
  [`Connection`](#videodb.client.Connection) object, to interact with the VideoDB
* **Return type:**
  [`videodb.client.Connection`](#videodb.client.Connection)

#### check_usage() → dict

Check the usage.

* **Returns:**
  Usage data
* **Return type:**
  dict

#### create_collection(name: str, description: str, is_public: bool = False) → [Collection](#videodb.collection.Collection)

Create a new collection.

* **Parameters:**
  * **name** (*str*) – Name of the collection
  * **description** (*str*) – Description of the collection
  * **is_public** (*bool*) – Make collection public (optional, default: False)
* **Returns:**
  `Collection` object
* **Return type:**
  [`videodb.collection.Collection`](#videodb.collection.Collection)

#### download(stream_link: str, name: str) → dict

Download a file from a stream link.

* **Parameters:**
  * **stream_link** – URL of the stream to download
  * **name** – Name to save the downloaded file as
* **Returns:**
  Download response data
* **Return type:**
  dict

#### get_collection(collection_id: str | None = 'default') → [Collection](#videodb.collection.Collection)

Get a collection object by its ID.

* **Parameters:**
  **collection_id** (*str*) – ID of the collection (optional, default: “default”)
* **Returns:**
  `Collection` object
* **Return type:**
  [`videodb.collection.Collection`](#videodb.collection.Collection)

#### get_collections() → List[[Collection](#videodb.collection.Collection)]

Get a list of all collections.

* **Returns:**
  List of `Collection` objects
* **Return type:**
  list[[`videodb.collection.Collection`](#videodb.collection.Collection)]

#### get_invoices() → List[dict]

Get a list of all invoices.

* **Returns:**
  List of invoices
* **Return type:**
  list[dict]

#### update_collection(id: str, name: str, description: str) → [Collection](#videodb.collection.Collection)

Update an existing collection.

* **Parameters:**
  * **id** (*str*) – ID of the collection
  * **name** (*str*) – Name of the collection
  * **description** (*str*) – Description of the collection
* **Returns:**
  `Collection` object
* **Return type:**
  [`videodb.collection.Collection`](#videodb.collection.Collection)

#### upload(file_path: str | None = None, url: str | None = None, media_type: str | None = None, name: str | None = None, description: str | None = None, callback_url: str | None = None) → [Video](#videodb.video.Video) | [Audio](#videodb.audio.Audio) | [Image](#videodb.image.Image) | None

Upload a file.

* **Parameters:**
  * **file_path** (*str*) – Path to the file to upload (optional)
  * **url** (*str*) – URL of the file to upload (optional)
  * **media_type** ([*MediaType*](#videodb.MediaType)) – MediaType object (optional)
  * **name** (*str*) – Name of the file (optional)
  * **description** (*str*) – Description of the file (optional)
  * **callback_url** (*str*) – URL to receive the callback (optional)
* **Returns:**
  `Video`, or `Audio`, or `Image` object
* **Return type:**
  Union[ [`videodb.video.Video`](#videodb.video.Video), [`videodb.audio.Audio`](#videodb.audio.Audio), [`videodb.image.Image`](#videodb.image.Image)]

## Module : videodb.collection (from videodb.collection import class, func)

### *class* videodb.collection.Collection(\_connection, id: str, name: str | None = None, description: str | None = None, is_public: bool = False)

Bases: `object`

Collection class to interact with the Collection.

Note: Users should not initialize this class directly.
Instead use [`Connection.get_collection()`](#videodb.client.Connection.get_collection)

#### \_\_init_\_(\_connection, id: str, name: str | None = None, description: str | None = None, is_public: bool = False)

#### delete() → None

Delete the collection

* **Raises:**
  [**InvalidRequestError**](#videodb.InvalidRequestError) – If the delete fails
* **Returns:**
  None if the delete is successful
* **Return type:**
  None

#### delete_audio(audio_id: str) → None

Delete the audio.

* **Parameters:**
  **audio_id** (*str*) – The id of the audio to be deleted
* **Raises:**
  [**InvalidRequestError**](#videodb.InvalidRequestError) – If the delete fails
* **Returns:**
  None if the delete is successful
* **Return type:**
  None

#### delete_image(image_id: str) → None

Delete the image.

* **Parameters:**
  **image_id** (*str*) – The id of the image to be deleted
* **Raises:**
  [**InvalidRequestError**](#videodb.InvalidRequestError) – If the delete fails
* **Returns:**
  None if the delete is successful
* **Return type:**
  None

#### delete_video(video_id: str) → None

Delete the video.

* **Parameters:**
  **video_id** (*str*) – The id of the video to be deleted
* **Raises:**
  [**InvalidRequestError**](#videodb.InvalidRequestError) – If the delete fails
* **Returns:**
  None if the delete is successful
* **Return type:**
  None

#### get_audio(audio_id: str) → [Audio](#videodb.audio.Audio)

Get an audio by its ID.

* **Parameters:**
  **audio_id** (*str*) – ID of the audio
* **Returns:**
  `Audio` object
* **Return type:**
  [`videodb.audio.Audio`](#videodb.audio.Audio)

#### get_audios() → List[[Audio](#videodb.audio.Audio)]

Get all the audios in the collection.

* **Returns:**
  List of `Audio` objects
* **Return type:**
  List[[`videodb.audio.Audio`](#videodb.audio.Audio)]

#### get_image(image_id: str) → [Image](#videodb.image.Image)

Get an image by its ID.

* **Parameters:**
  **image_id** (*str*) – ID of the image
* **Returns:**
  `Image` object
* **Return type:**
  [`videodb.image.Image`](#videodb.image.Image)

#### get_images() → List[[Image](#videodb.image.Image)]

Get all the images in the collection.

* **Returns:**
  List of `Image` objects
* **Return type:**
  List[[`videodb.image.Image`](#videodb.image.Image)]

#### get_video(video_id: str) → [Video](#videodb.video.Video)

Get a video by its ID.

* **Parameters:**
  **video_id** (*str*) – ID of the video
* **Returns:**
  `Video` object
* **Return type:**
  [`videodb.video.Video`](#videodb.video.Video)

#### get_videos() → List[[Video](#videodb.video.Video)]

Get all the videos in the collection.

* **Returns:**
  List of `Video` objects
* **Return type:**
  List[[`videodb.video.Video`](#videodb.video.Video)]

#### make_private()

Make the collection private.

* **Returns:**
  None
* **Return type:**
  None

#### make_public()

Make the collection public.

* **Returns:**
  None
* **Return type:**
  None

#### search(query: str, search_type: str | None = 'semantic', index_type: str | None = 'spoken_word', result_threshold: int | None = None, score_threshold: float | None = None, dynamic_score_percentage: float | None = None, filter: List[Dict[str, Any]] = []) → [SearchResult](#videodb.search.SearchResult)

Search for a query in the collection.

* **Parameters:**
  * **query** (*str*) – Query to search for
  * **search_type** ([*SearchType*](#videodb.SearchType)) – Type of search to perform (optional)
  * **index_type** ([*IndexType*](#videodb.IndexType)) – Type of index to search (optional)
  * **result_threshold** (*int*) – Number of results to return (optional)
  * **score_threshold** (*float*) – Threshold score for the search (optional)
  * **dynamic_score_percentage** (*float*) – Percentage of dynamic score to consider (optional)
* **Raises:**
  [**SearchError**](#videodb.SearchError) – If the search fails
* **Returns:**
  `SearchResult` object
* **Return type:**
  [`videodb.search.SearchResult`](#videodb.search.SearchResult)

#### search_title(query) → List[[Video](#videodb.video.Video)]

#### upload(file_path: str | None = None, url: str | None = None, media_type: str | None = None, name: str | None = None, description: str | None = None, callback_url: str | None = None) → [Video](#videodb.video.Video) | [Audio](#videodb.audio.Audio) | [Image](#videodb.image.Image) | None

Upload a file to the collection.

* **Parameters:**
  * **file_path** (*str*) – Path to the file to be uploaded
  * **url** (*str*) – URL of the file to be uploaded
  * **media_type** ([*MediaType*](#videodb.MediaType)) – MediaType object (optional)
  * **name** (*str*) – Name of the file (optional)
  * **description** (*str*) – Description of the file (optional)
  * **callback_url** (*str*) – URL to receive the callback (optional)
* **Returns:**
  `Video`, or `Audio`, or `Image` object
* **Return type:**
  Union[ [`videodb.video.Video`](#videodb.video.Video), [`videodb.audio.Audio`](#videodb.audio.Audio), [`videodb.image.Image`](#videodb.image.Image)]

## Module : videodb.video (from videodb.video import class, func)

### *class* videodb.video.Video(\_connection, id: str, collection_id: str, \*\*kwargs)

Bases: `object`

Video class to interact with the Video

* **Variables:**
  * **id** (*str*) – Unique identifier for the video
  * **collection_id** (*str*) – ID of the collection this video belongs to
  * **stream_url** (*str*) – URL to stream the video
  * **player_url** (*str*) – URL to play the video in a player
  * **name** (*str*) – Name of the video file
  * **description** (*str*) – Description of the video
  * **thumbnail_url** (*str*) – URL of the video thumbnail
  * **length** (*float*) – Duration of the video in seconds
  * **transcript** (*list*) – Timestamped transcript segments
  * **transcript_text** (*str*) – Full transcript text
  * **scenes** (*list*) – List of scenes in the video

#### add_subtitle(style: [SubtitleStyle](#videodb.SubtitleStyle) = SubtitleStyle(font_name='Arial', font_size=18, primary_colour='&H00FFFFFF', secondary_colour='&H000000FF', outline_colour='&H00000000', back_colour='&H00000000', bold=False, italic=False, underline=False, strike_out=False, scale_x=1.0, scale_y=1.0, spacing=0, angle=0, border_style=4, outline=1.0, shadow=0.0, alignment=2, margin_l=10, margin_r=10, margin_v=10)) → str

Add subtitles to the video.

* **Parameters:**
  **style** ([*SubtitleStyle*](#videodb.SubtitleStyle)) – (optional) The style of the subtitles, `SubtitleStyle` object
* **Returns:**
  The stream url of the video with subtitles
* **Return type:**
  str

#### delete() → None

Delete the video.

* **Raises:**
  [**InvalidRequestError**](#videodb.InvalidRequestError) – If the delete fails
* **Returns:**
  None if the delete is successful
* **Return type:**
  None

#### delete_scene_collection(collection_id: str) → None

Delete the scene collection.

* **Parameters:**
  **collection_id** (*str*) – The id of the scene collection to be deleted
* **Raises:**
  [**InvalidRequestError**](#videodb.InvalidRequestError) – If the delete fails
* **Returns:**
  None if the delete is successful
* **Return type:**
  None

#### delete_scene_index(scene_index_id: str) → None

Delete the scene index.

* **Parameters:**
  **scene_index_id** (*str*) – The id of the scene index to be deleted
* **Raises:**
  [**InvalidRequestError**](#videodb.InvalidRequestError) – If the delete fails
* **Returns:**
  None if the delete is successful
* **Return type:**
  None

#### extract_scenes(extraction_type: [SceneExtractionType](#videodb.SceneExtractionType) = 'shot', extraction_config: dict = {}, force: bool = False, callback_url: str | None = None) → [SceneCollection](#videodb.scene.SceneCollection) | None

Extract the scenes of the video.

* **Parameters:**
  * **extraction_type** ([*SceneExtractionType*](#videodb.SceneExtractionType)) – (optional) The type of extraction, `SceneExtractionType` object
  * **extraction_config** (*dict*) – 

    (optional) Dictionary of configuration parameters to control how scenes are extracted.
    For time-based extraction (extraction_type=time_based):
    > - ”time” (int, optional): Interval in seconds at which scenes are
    >   segmented. Default is 10 (i.e., every 10 seconds forms a new scene).
    > - ”frame_count” (int, optional): Number of frames to extract per
    >   scene. Default is 1.
    > - ”select_frames” (List[str], optional): Which frames to select from
    >   each segment. Possible values include “first”, “middle”, and “last”.
    >   Default is [“first”].

    For shot-based extraction (extraction_type=shot_based):
    > - ”threshold” (int, optional): Sensitivity for detecting scene changes
    >   (camera shots). The higher the threshold, the fewer scene splits.
    >   Default is 20.
    > - ”frame_count” (int, optional): Number of frames to extract from
    >   each detected shot. Default is 1.
  * **force** (*bool*) – (optional) Force to extract the scenes
  * **callback_url** (*str*) – (optional) URL to receive the callback
* **Raises:**
  [**InvalidRequestError**](#videodb.InvalidRequestError) – If the extraction fails
* **Returns:**
  The scene collection, `SceneCollection` object
* **Return type:**
  [`videodb.scene.SceneCollection`](#videodb.scene.SceneCollection)

#### generate_stream(timeline: List[Tuple[float, float]] | None = None) → str

Generate the stream url of the video.

* **Parameters:**
  **timeline** (*List* *[**Tuple* *[**float* *,* *float* *]* *]*) – (optional) The timeline of the video to be streamed in the format [(start, end)]
* **Raises:**
  [**InvalidRequestError**](#videodb.InvalidRequestError) – If the get_stream fails
* **Returns:**
  The stream url of the video
* **Return type:**
  str

#### generate_thumbnail(time: float | None = None) → str | [Image](#videodb.image.Image)

Generate the thumbnail of the video.

* **Parameters:**
  **time** (*float*) – (optional) The time of the video to generate the thumbnail
* **Returns:**
  `Image` object if time is provided else the thumbnail url
* **Return type:**
  Union[str, [`videodb.image.Image`](#videodb.image.Image)]

#### get_scene_collection(collection_id: str) → [SceneCollection](#videodb.scene.SceneCollection) | None

Get the scene collection.

* **Parameters:**
  **collection_id** (*str*) – The id of the scene collection
* **Returns:**
  The scene collection
* **Return type:**
  [`videodb.scene.SceneCollection`](#videodb.scene.SceneCollection)

#### get_scene_index(scene_index_id: str) → List | None

Get the scene index.

* **Parameters:**
  **scene_index_id** (*str*) – The id of the scene index
* **Returns:**
  The scene index records
* **Return type:**
  list

#### get_scenes() → list | None

#### Deprecated
Deprecated since version 0.2.0.

Use [`list_scene_index()`](#videodb.video.Video.list_scene_index) and [`get_scene_index()`](#videodb.video.Video.get_scene_index) instead.

Get the scenes of the video.

* **Returns:**
  The scenes of the video
* **Return type:**
  list

#### get_thumbnails() → List[[Image](#videodb.image.Image)]

Get all the thumbnails of the video.

* **Returns:**
  List of `Image` objects
* **Return type:**
  List[[`videodb.image.Image`](#videodb.image.Image)]

#### get_transcript(start: int | None = None, end: int | None = None, segmenter: [Segmenter](#videodb.Segmenter) = 'word', length: int = 1, force: bool | None = None) → List[Dict[str, float | str]]

Get timestamped transcript segments for the video.

* **Parameters:**
  * **start** (*int*) – Start time in seconds
  * **end** (*int*) – End time in seconds
  * **segmenter** ([*Segmenter*](#videodb.Segmenter)) – Segmentation type (`Segmenter.word`,
    `Segmenter.sentence`, `Segmenter.time`)
  * **length** (*int*) – Length of segments when using time segmenter
  * **force** (*bool*) – Force fetch new transcript
* **Returns:**
  List of dicts with keys: start (float), end (float), text (str)
* **Return type:**
  List[Dict[str, Union[float, str]]]

#### get_transcript_text(start: int | None = None, end: int | None = None, segmenter: str = 'word', length: int = 1, force: bool | None = None) → str

Get plain text transcript for the video.

* **Parameters:**
  * **start** (*int*) – Start time in seconds to get transcript from
  * **end** (*int*) – End time in seconds to get transcript until
  * **force** (*bool*) – Force fetch new transcript
* **Returns:**
  Full transcript text as string
* **Return type:**
  str

#### index_scenes(extraction_type: [SceneExtractionType](#videodb.SceneExtractionType) = 'shot', extraction_config: Dict = {}, prompt: str | None = None, metadata: Dict = {}, model_name: str | None = None, model_config: Dict | None = None, name: str | None = None, scenes: List[[Scene](#videodb.scene.Scene)] | None = None, callback_url: str | None = None) → str | None

Index the scenes of the video.

* **Parameters:**
  * **extraction_type** ([*SceneExtractionType*](#videodb.SceneExtractionType)) – (optional) The type of extraction, `SceneExtractionType` object
  * **extraction_config** (*dict*) – 

    (optional) Dictionary of configuration parameters to control how scenes are extracted.
    For time-based extraction (extraction_type=time_based):
    > - ”time” (int, optional): Interval in seconds at which scenes are
    >   segmented. Default is 10 (i.e., every 10 seconds forms a new scene).
    > - ”frame_count” (int, optional): Number of frames to extract per
    >   scene. Default is 1.
    > - ”select_frames” (List[str], optional): Which frames to select from
    >   each segment. Possible values include “first”, “middle”, and “last”.
    >   Default is [“first”].

    For shot-based extraction (extraction_type=shot_based):
    > - ”threshold” (int, optional): Sensitivity for detecting scene changes
    >   (camera shots). The higher the threshold, the fewer scene splits.
    >   Default is 20.
    > - ”frame_count” (int, optional): Number of frames to extract from
    >   each detected shot. Default is 1.
  * **prompt** (*str*) – (optional) The prompt for the extraction
  * **model_name** (*str*) – (optional) The model name for the extraction
  * **model_config** (*dict*) – (optional) The model configuration for the extraction
  * **name** (*str*) – (optional) The name of the scene index
  * **scenes** (*list* *[*[*Scene*](#videodb.scene.Scene) *]*) – (optional) The scenes to be indexed, List of `Scene` objects
  * **callback_url** (*str*) – (optional) The callback url
* **Raises:**
  [**InvalidRequestError**](#videodb.InvalidRequestError) – If the index fails or index already exists
* **Returns:**
  The scene index id
* **Return type:**
  str

#### index_spoken_words(language_code: str | None = None, force: bool = False, callback_url: str | None = None) → None

Semantic indexing of spoken words in the video.

* **Parameters:**
  * **language_code** (*str*) – (optional) Language code of the video
  * **force** (*bool*) – (optional) Force to index the video
  * **callback_url** (*str*) – (optional) URL to receive the callback
* **Raises:**
  [**InvalidRequestError**](#videodb.InvalidRequestError) – If the video is already indexed
* **Returns:**
  None if the indexing is successful
* **Return type:**
  None

#### insert_video(video, timestamp: float) → str

Insert a video into another video

* **Parameters:**
  * **video** ([*Video*](#videodb.video.Video)) – The video to be inserted
  * **timestamp** (*float*) – The timestamp where the video should be inserted
* **Raises:**
  [**InvalidRequestError**](#videodb.InvalidRequestError) – If the insert fails
* **Returns:**
  The stream url of the inserted video
* **Return type:**
  str

#### list_scene_collection()

List all the scene collections.

* **Returns:**
  The scene collections
* **Return type:**
  list

#### list_scene_index() → List

List all the scene indexes.

* **Returns:**
  The scene indexes
* **Return type:**
  list

#### play() → str

Open the player url in the browser/iframe and return the stream url.

* **Returns:**
  The player url
* **Return type:**
  str

#### remove_storage() → None

Remove the video storage.

* **Raises:**
  [**InvalidRequestError**](#videodb.InvalidRequestError) – If the storage removal fails
* **Returns:**
  None if the removal is successful
* **Return type:**
  None

#### search(query: str, search_type: str | None = 'semantic', index_type: str | None = 'spoken_word', result_threshold: int | None = None, score_threshold: float | None = None, dynamic_score_percentage: float | None = None, filter: List[Dict[str, Any]] = [], \*\*kwargs) → [SearchResult](#videodb.search.SearchResult)

Search for a query in the video.

* **Parameters:**
  * **query** (*str*) – Query to search for.
  * **search_type** ([*SearchType*](#videodb.SearchType)) – (optional) Type of search to perform `SearchType` object
  * **index_type** ([*IndexType*](#videodb.IndexType)) – (optional) Type of index to search `IndexType` object
  * **result_threshold** (*int*) – (optional) Number of results to return
  * **score_threshold** (*float*) – (optional) Threshold score for the search
  * **dynamic_score_percentage** (*float*) – (optional) Percentage of dynamic score to consider
* **Raises:**
  [**SearchError**](#videodb.SearchError) – If the search fails
* **Returns:**
  `SearchResult` object
* **Return type:**
  [`videodb.search.SearchResult`](#videodb.search.SearchResult)

## Module : videodb.audio (from videodb.audio import class, func)

### *class* videodb.audio.Audio(\_connection, id: str, collection_id: str, \*\*kwargs)

Bases: `object`

Audio class to interact with the Audio

* **Variables:**
  * **id** (*str*) – Unique identifier for the audio
  * **collection_id** (*str*) – ID of the collection this audio belongs to
  * **name** (*str*) – Name of the audio file
  * **length** (*float*) – Duration of the audio in seconds

#### delete() → None

Delete the audio.

* **Raises:**
  [**InvalidRequestError**](#videodb.InvalidRequestError) – If the delete fails
* **Returns:**
  None if the delete is successful
* **Return type:**
  None

#### generate_url() → str

Generate the signed url of the audio.

* **Raises:**
  [**InvalidRequestError**](#videodb.InvalidRequestError) – If the get_url fails
* **Returns:**
  The signed url of the audio
* **Return type:**
  str

## Module : videodb.image (from videodb.image import class, func)

### *class* videodb.image.Frame(\_connection, id: str, video_id: str, scene_id: str, url: str, frame_time: float, description: str)

Bases: [`Image`](#videodb.image.Image)

Frame class to interact with video frames

* **Variables:**
  * **id** (*str*) – Unique identifier for the frame
  * **video_id** (*str*) – ID of the video this frame belongs to
  * **scene_id** (*str*) – ID of the scene this frame belongs to
  * **url** (*str*) – URL of the frame
  * **frame_time** (*float*) – Timestamp of the frame in the video
  * **description** (*str*) – Description of the frame contents

#### describe(prompt: str | None = None, model_name=None)

Describe the frame.

* **Parameters:**
  * **prompt** (*str*) – (optional) The prompt to use for the description
  * **model_name** (*str*) – (optional) The model to use for the description
* **Returns:**
  The description of the frame
* **Return type:**
  str

#### to_json()

### *class* videodb.image.Image(\_connection, id: str, collection_id: str, \*\*kwargs)

Bases: `object`

Image class to interact with the Image

* **Variables:**
  * **id** (*str*) – Unique identifier for the image
  * **collection_id** (*str*) – ID of the collection this image belongs to
  * **name** (*str*) – Name of the image file
  * **url** (*str*) – URL of the image

#### delete() → None

Delete the image.

* **Raises:**
  [**InvalidRequestError**](#videodb.InvalidRequestError) – If the delete fails
* **Returns:**
  None if the delete is successful
* **Return type:**
  None

#### generate_url() → str

Generate the signed url of the image.

* **Raises:**
  [**InvalidRequestError**](#videodb.InvalidRequestError) – If the get_url fails
* **Returns:**
  The signed url of the image
* **Return type:**
  str

## Module : videodb.timeline (from videodb.timeline import class, func)

### *class* videodb.timeline.Timeline(connection)

Bases: `object`

#### add_inline(asset: [VideoAsset](#videodb.asset.VideoAsset)) → None

Add a video asset to the timeline

* **Parameters:**
  **asset** ([*VideoAsset*](#videodb.asset.VideoAsset)) – The video asset to add, `VideoAsset` <VideoAsset> object
* **Raises:**
  **ValueError** – If asset is not of type `VideoAsset` <VideoAsset>
* **Returns:**
  None
* **Return type:**
  None

#### add_overlay(start: int, asset: [AudioAsset](#videodb.asset.AudioAsset) | [ImageAsset](#videodb.asset.ImageAsset) | [TextAsset](#videodb.asset.TextAsset)) → None

Add an overlay asset to the timeline

* **Parameters:**
  * **start** (*int*) – The start time of the overlay asset
  * **asset** (*Union* *[*[*AudioAsset*](#videodb.asset.AudioAsset) *,* [*ImageAsset*](#videodb.asset.ImageAsset) *,* [*TextAsset*](#videodb.asset.TextAsset) *]*) – The overlay asset to add, `AudioAsset`, `ImageAsset`, `TextAsset` object
* **Returns:**
  None
* **Return type:**
  None

#### generate_stream() → str

Generate a stream url for the timeline

* **Returns:**
  The stream url
* **Return type:**
  str

#### to_json() → dict

## Module : videodb.asset (from videodb.asset import class, func)

### *class* videodb.asset.AudioAsset(asset_id: str, start: float | None = 0, end: float | None = None, disable_other_tracks: bool | None = True, fade_in_duration: int | float | None = 0, fade_out_duration: int | float | None = 0)

Bases: [`MediaAsset`](#videodb.asset.MediaAsset)

#### to_json() → dict

### *class* videodb.asset.ImageAsset(asset_id: str, width: int | str = 100, height: int | str = 100, x: int | str = 80, y: int | str = 20, duration: int | None = None)

Bases: [`MediaAsset`](#videodb.asset.MediaAsset)

#### to_json() → dict

### *class* videodb.asset.MediaAsset(asset_id: str)

Bases: `object`

#### to_json() → dict

### *class* videodb.asset.TextAsset(text: str, duration: int | None = None, style: [TextStyle](#videodb.TextStyle) = TextStyle(fontsize=24, fontcolor='black', fontcolor_expr='', alpha=1.0, font='Sans', box=True, boxcolor='white', boxborderw='10', boxw=0, boxh=0, line_spacing=0, text_align='T', y_align='text', borderw=0, bordercolor='black', expansion='normal', basetime=0, fix_bounds=False, text_shaping=True, shadowcolor='black', shadowx=0, shadowy=0, tabsize=4, x='(main_w-text_w)/2', y='(main_h-text_h)/2'))

Bases: [`MediaAsset`](#videodb.asset.MediaAsset)

#### to_json() → dict

### *class* videodb.asset.VideoAsset(asset_id: str, start: float | None = 0, end: float | None = None)

Bases: [`MediaAsset`](#videodb.asset.MediaAsset)

#### to_json() → dict

### videodb.asset.validate_max_supported(duration: int | float, max_duration: int | float, attribute: str = '') → int | float | None

## Module : videodb.scene (from videodb.scene import class, func)

### *class* videodb.scene.Scene(video_id: str, start: float, end: float, description: str, id: str | None = None, frames: List[[Frame](#videodb.image.Frame)] = [], metadata: dict = {}, connection=None)

Bases: `object`

Scene class to interact with video scenes

* **Variables:**
  * **id** (*str*) – Unique identifier for the scene
  * **video_id** (*str*) – ID of the video this scene belongs to
  * **start** (*float*) – Start time of the scene in seconds
  * **end** (*float*) – End time of the scene in seconds
  * **frames** (*List* *[*[*Frame*](#videodb.image.Frame) *]*) – List of frames in the scene
  * **description** (*str*) – Description of the scene contents

#### describe(prompt: str | None = None, model_name=None) → None

Describe the scene.

* **Parameters:**
  * **prompt** (*str*) – (optional) The prompt to use for the description
  * **model_name** (*str*) – (optional) The model to use for the description
* **Returns:**
  The description of the scene
* **Return type:**
  str

#### to_json()

### *class* videodb.scene.SceneCollection(\_connection, id: str, video_id: str, config: dict, scenes: List[[Scene](#videodb.scene.Scene)])

Bases: `object`

SceneCollection class to interact with collections of scenes

* **Variables:**
  * **id** (*str*) – Unique identifier for the scene collection
  * **video_id** (*str*) – ID of the video these scenes belong to
  * **config** (*dict*) – Configuration settings for the scene collection
  * **scenes** (*List* *[*[*Scene*](#videodb.scene.Scene) *]*) – List of scenes in the collection

#### delete() → None

Delete the scene collection.

* **Raises:**
  [**InvalidRequestError**](#videodb.InvalidRequestError) – If the delete fails
* **Returns:**
  None if the delete is successful
* **Return type:**
  None

## Module : videodb.search (from videodb.search import class, func)

### *class* videodb.search.SearchResult(\_connection, \*\*kwargs)

Bases: `object`

SearchResult class to interact with search results

* **Variables:**
  * **collection_id** (*str*) – ID of the collection this search result belongs to
  * **stream_url** (*str*) – URL to stream the search result
  * **player_url** (*str*) – URL to play the search result in a player
  * **shots** (*list* *[*[*Shot*](#videodb.shot.Shot) *]*) – List of shots in the search result

#### compile() → str

Compile the search result shots into a stream url.

* **Raises:**
  [**SearchError**](#videodb.SearchError) – If no shots are found in the search results
* **Returns:**
  The stream url
* **Return type:**
  str

#### get_shots() → List[[Shot](#videodb.shot.Shot)]

#### play() → str

Generate a stream url for the shot and open it in the default browser.

* **Returns:**
  The stream url
* **Return type:**
  str

## Module : videodb.shot (from videodb.shot import class, func)

### *class* videodb.shot.Shot(\_connection, video_id: str, video_length: float, video_title: str, start: float, end: float, text: str | None = None, search_score: int | None = None)

Bases: `object`

Shot class to interact with video shots

* **Variables:**
  * **video_id** (*str*) – Unique identifier for the video
  * **video_length** (*float*) – Duration of the video in seconds
  * **video_title** (*str*) – Title of the video
  * **start** (*float*) – Start time of the shot in seconds
  * **end** (*float*) – End time of the shot in seconds
  * **text** (*str*) – Text content of the shot
  * **search_score** (*int*) – Search relevance score
  * **stream_url** (*str*) – URL to stream the shot
  * **player_url** (*str*) – URL to play the shot in a player

#### generate_stream() → str

Generate a stream url for the shot.

* **Returns:**
  The stream url
* **Return type:**
  str

#### play() → str

Generate a stream url for the shot and open it in the default browser/ notebook.

* **Returns:**
  The stream url
* **Return type:**
  str


# Welcome to VideoDB Docs [Source Link](https://docs.videodb.io/)

![videodb](https://codaio.imgix.net/workspaces/ws-jizMKG73gK/blobs/customIcons/1a6d553a-3676-494e-8f3b-fd666614f459?fit=fill&fill=solid&w=128&h=128&fm=gif&bg=0FFF&fill-color=0FFF)

VideoDB Documentation

Pages

[![](https://cdn.coda.io/icons/svg/color/align-center.svg)
Welcome to VideoDB Docs](https://docs.videodb.io/)

[![](https://cdn.coda.io/icons/svg/color/quick-mode-on.svg)
Quick Start Guide](https://docs.videodb.io/quick-start-guide-38)

[![](https://cdn.coda.io/icons/svg/color/wash-your-hands.svg)
How Accurate is Your Search?](https://docs.videodb.io/how-accurate-is-your-search-88)

[![](https://cdn.coda.io/icons/svg/color/video-call.svg)
Video Indexing Guide](https://docs.videodb.io/video-indexing-guide-101)

[![](https://cdn.coda.io/icons/svg/color/clear-search.svg)
Semantic Search](https://docs.videodb.io/semantic-search-89)

[![](https://cdn.coda.io/icons/svg/color/binders-folder.svg)
Collections](https://docs.videodb.io/collections-68)

[![](https://cdn.coda.io/icons/svg/color/magazine.svg)
Public Collections](https://docs.videodb.io/public-collections-102)

[![](https://cdn.coda.io/icons/svg/color/callback.svg)
Callback Details](https://docs.videodb.io/callback-details-66)

[![](https://cdn.coda.io/icons/svg/color/closed-captioning.svg)
Ref: Subtitle Styles](https://docs.videodb.io/ref-subtitle-styles-57)

[![](https://cdn.coda.io/icons/svg/color/customer-support.svg)
Language Support](https://docs.videodb.io/language-support-79)

[![](https://cdn.coda.io/icons/svg/color/closed-captioning.svg)
Guide: Subtitles](https://docs.videodb.io/guide-subtitles-73)

[![](https://cdn.coda.io/icons/svg/color/asteroid.svg)
Visual Search and Indexing](https://docs.videodb.io/visual-search-and-indexing-80)

[![](https://cdn.coda.io/icons/svg/color/landscape.svg)
Scene Extraction Algorithms](https://docs.videodb.io/scene-extraction-algorithms-84)

[![](https://cdn.coda.io/icons/svg/color/edit-column.svg)
Custom Annotations](https://docs.videodb.io/custom-annotations-81)

[![](https://cdn.coda.io/icons/svg/color/search-property.svg)
Scene-Level Metadata: Smarter Video Search & Retrieval](https://docs.videodb.io/scene-level-metadata-smarter-video-search-retrieval-107)

[![](https://cdn.coda.io/icons/svg/color/search-more.svg)
Advanced Visual Search Pipelines](https://docs.videodb.io/advanced-visual-search-pipelines-82)

[![](https://cdn.coda.io/icons/svg/color/football.svg)
Playground for Scene Extractions](https://docs.videodb.io/playground-for-scene-extractions-83)

[![](https://cdn.coda.io/icons/svg/color/scuba-pressure-gauge.svg)
Deep Dive into Prompt Engineering : Mastering Video Scene Indexing](https://docs.videodb.io/deep-dive-into-prompt-engineering-mastering-video-scene-indexing-93)

[![](https://cdn.coda.io/icons/svg/color/clear-search.svg)
Multimodal Search](https://docs.videodb.io/multimodal-search-90)

[![](https://cdn.coda.io/icons/svg/color/search-more.svg)
Multimodal Search: Quickstart](https://docs.videodb.io/multimodal-search-quickstart-91)

[![](https://cdn.coda.io/icons/svg/color/poll-topic.svg)
Conference Slide Scraper with VideoDB](https://docs.videodb.io/conference-slide-scraper-with-videodb-92)

[![](https://cdn.coda.io/icons/svg/color/e-learning.svg)
Dynamic Video Streams](https://docs.videodb.io/dynamic-video-streams-44)

[![](https://cdn.coda.io/icons/svg/color/text-box.svg)
Ref: TextAsset](https://docs.videodb.io/ref-textasset-74)

[![](https://cdn.coda.io/icons/svg/color/text-box.svg)
Guide : TextAsset](https://docs.videodb.io/guide-textasset-75)

[![director-light](https://codaio.imgix.net/workspaces/ws-jizMKG73gK/blobs/customIcons/6bc288c2-982b-4a97-a402-8da53aeaa236?fit=fill&fill=solid&w=128&h=128&fm=gif&bg=0FFF&fill-color=0FFF)
Director - Video Agent Framework](https://docs.videodb.io/director-video-agent-framework-98)

[![](https://cdn.coda.io/icons/svg/color/open-book.svg)
Agent Creation Playbook](https://docs.videodb.io/agent-creation-playbook-103)

[![](https://cdn.coda.io/icons/svg/color/bag-front-view.svg)
How I Built a CRM-integrated Sales Assistant Agent in 1 Hour](https://docs.videodb.io/how-i-built-a-crm-integrated-sales-assistant-agent-in-1-hour-106)

[![](https://cdn.coda.io/icons/svg/color/voice-recognition-scan.svg)
Make Your Video Sound Studio Quality with Voice Cloning](https://docs.videodb.io/make-your-video-sound-studio-quality-with-voice-cloning-105)

[![](https://cdn.coda.io/icons/svg/color/console.svg)
Setup Director Locally](https://docs.videodb.io/setup-director-locally-104)

[![github](https://codaio.imgix.net/workspaces/ws-jizMKG73gK/blobs/customIcons/ac14f3ef-daa1-4b6e-aba5-af11f11b8372?fit=fill&fill=solid&w=128&h=128&fm=gif&bg=0FFF&fill-color=0FFF)
Open Source Tools](https://docs.videodb.io/open-source-tools-94)

[![llama](https://codaio.imgix.net/workspaces/ws-jizMKG73gK/blobs/customIcons/c2b3a994-6140-40a9-93ff-d87aa37f2860?fit=fill&fill=solid&w=128&h=128&fm=gif&bg=0FFF&fill-color=0FFF)
LlamaIndex VideoDB Retriever](https://docs.videodb.io/llamaindex-videodb-retriever-58)

[![](https://cdn.coda.io/icons/svg/color/command-line.svg)
PromptClip: Use Power of LLM to Create Clips](https://docs.videodb.io/promptclip-use-power-of-llm-to-create-clips-52)

[![](https://cdn.coda.io/icons/svg/color/day-camera.svg)
StreamRAG: Connect ChatGPT to VideoDB](https://docs.videodb.io/streamrag-connect-chatgpt-to-videodb-43)

[![](https://cdn.coda.io/icons/svg/color/book-and-pencil.svg)
Examples and Tutorials](https://docs.videodb.io/examples-and-tutorials-35)

[![](https://cdn.coda.io/icons/svg/color/audible.svg)
Dubbing - Replace Soundtrack with New Audio](https://docs.videodb.io/dubbing-replace-soundtrack-with-new-audio-49)

[![](https://cdn.coda.io/icons/svg/color/adware-free.svg)
Beep curse words in real-time](https://docs.videodb.io/beep-curse-words-in-real-time-53)

[![](https://cdn.coda.io/icons/svg/color/find-user-male.svg)
Remove Unwanted Content from videos](https://docs.videodb.io/remove-unwanted-content-from-videos-5)

[![](https://cdn.coda.io/icons/svg/color/find-and-replace.svg)
Instant Clips of Your Favorite Characters](https://docs.videodb.io/instant-clips-of-your-favorite-characters-3)

[![](https://cdn.coda.io/icons/svg/color/insert-white-space.svg)
Insert Dynamic Ads in real-time](https://docs.videodb.io/insert-dynamic-ads-in-real-time-7)

[![](https://cdn.coda.io/icons/svg/color/mac-client.svg)
Adding Brand Elements with VideoDB](https://docs.videodb.io/adding-brand-elements-with-videodb-76)

[![](https://cdn.coda.io/icons/svg/color/adverb.svg)
Revolutionize Video Editing with VideoDb: Effortless Ad Placement and Seamless Video Integration](https://docs.videodb.io/revolutionize-video-editing-with-videodb-effortless-ad-placement-8)

[![](https://cdn.coda.io/icons/svg/color/medium-volume.svg)
Eleven Labs x VideoDB: Adding AI Generated voiceovers to silent footage](https://docs.videodb.io/eleven-labs-x-videodb-adding-ai-generated-voiceovers-to-silent-f-59)

[![](https://cdn.coda.io/icons/svg/color/camera-automation.svg)
Elevating Trailers with Automated Narration](https://docs.videodb.io/elevating-trailers-with-automated-narration-60)

[![](https://cdn.coda.io/icons/svg/color/video-trimming.svg)
Add Intro/Outro to Videos](https://docs.videodb.io/add-intro-outro-to-videos-61)

[![](https://cdn.coda.io/icons/svg/color/closed-captioning.svg)
Enhancing Video Captions with VideoDB Subtitle Styling](https://docs.videodb.io/enhancing-video-captions-with-videodb-subtitle-styling-62)

[![](https://cdn.coda.io/icons/svg/color/high-volume.svg)
Audio overlay + Video + Timeline](https://docs.videodb.io/audio-overlay-video-timeline-63)

[![](https://cdn.coda.io/icons/svg/color/video-call.svg)
Building Dynamic Video Streams with VideoDB: Integrating Custom Data and APIs](https://docs.videodb.io/building-dynamic-video-streams-with-videodb-integrating-custom-d-85)

[![](https://cdn.coda.io/icons/svg/color/for-experienced.svg)
Adding AI Generated Voiceovers with VideoDB and LOVO](https://docs.videodb.io/adding-ai-generated-voiceovers-with-videodb-and-lovo-70)

[![](https://cdn.coda.io/icons/svg/color/billboard.svg)
AI Generated Ad Films for Product Videography: Wellsaid, Open AI & VideoDB](https://docs.videodb.io/ai-generated-ad-films-for-product-videography-wellsaid-open-ai-v-71)

[![](https://cdn.coda.io/icons/svg/color/search.svg)
Fun with Keyword Search](https://docs.videodb.io/fun-with-keyword-search-77)

[![](https://cdn.coda.io/icons/svg/color/find-and-replace.svg)
AWS Rekognition and VideoDB - Intelligent Video Clips](https://docs.videodb.io/aws-rekognition-and-videodb-intelligent-video-clips-4)

[![](https://cdn.coda.io/icons/svg/color/find-user-male.svg)
AWS Rekognition and VideoDB - Effortlessly Remove Inappropriate Content from Video](https://docs.videodb.io/aws-rekognition-and-videodb-effortlessly-remove-inappropriate-co-6)

[![](https://cdn.coda.io/icons/svg/color/counter.svg)
Overlay a Word-Counter on Video Stream](https://docs.videodb.io/overlay-a-word-counter-on-video-stream-86)

[![](https://cdn.coda.io/icons/svg/color/handle-with-care.svg)
Generate Automated Video Outputs with Text Prompts \| DALL-E + ElevenLabs + OpenAI + VideoDB](https://docs.videodb.io/generate-automated-video-outputs-with-text-prompts-dall-e-eleven-87)

[![](https://cdn.coda.io/icons/svg/color/centre-of-gravity.svg)
Edge of Knowledge](https://docs.videodb.io/edge-of-knowledge-10)

[![](https://cdn.coda.io/icons/svg/color/for-experienced.svg)
Building Intelligent Machines](https://docs.videodb.io/building-intelligent-machines-16)

[![](https://cdn.coda.io/icons/svg/color/artificial-intelligence.svg)
Part 1 - Define Intelligence](https://docs.videodb.io/part-1-define-intelligence-17)

[![](https://cdn.coda.io/icons/svg/color/panel-and-foot-outlet.svg)
Part 2 - Observe and Respond](https://docs.videodb.io/part-2-observe-and-respond-18)

[![](https://cdn.coda.io/icons/svg/color/the-flash-sign.svg)
Part 3 - Training a Model](https://docs.videodb.io/part-3-training-a-model-19)

[![](https://cdn.coda.io/icons/svg/color/cnc-machine.svg)
Society of Machines](https://docs.videodb.io/society-of-machines-20)

[![](https://cdn.coda.io/icons/svg/color/groups.svg)
Society of Machines](https://docs.videodb.io/society-of-machines-23)

[![](https://cdn.coda.io/icons/svg/color/the-flash-sign.svg)
Autonomy - Do we have the choice?](https://docs.videodb.io/autonomy-do-we-have-the-choice-21)

[![](https://cdn.coda.io/icons/svg/color/artificial-intelligence.svg)
Emergence - An Intelligence of the collective](https://docs.videodb.io/emergence-an-intelligence-of-the-collective-22)

[![](https://cdn.coda.io/icons/svg/color/back-to-draft.svg)
Drafts](https://docs.videodb.io/drafts-24)

[![](https://cdn.coda.io/icons/svg/color/one-to-many.svg)
From Language Models to World Models: The Next Frontier in AI](https://docs.videodb.io/from-language-models-to-world-models-the-next-frontier-in-ai-65)

[![](https://cdn.coda.io/icons/svg/color/recurring-appointment-exception.svg)
The Future Series](https://docs.videodb.io/the-future-series-78)

[![videodb](https://codaio.imgix.net/workspaces/ws-jizMKG73gK/blobs/customIcons/1a6d553a-3676-494e-8f3b-fd666614f459?fit=fill&fill=solid&w=128&h=128&fm=gif&bg=0FFF&fill-color=0FFF)
Building World's First Video Database](https://docs.videodb.io/building-worlds-first-video-database-25)

[![](https://cdn.coda.io/icons/svg/color/video.svg)
Multimedia: From MP3/MP4 to the Future with VideoDB](https://docs.videodb.io/multimedia-from-mp3-mp4-to-the-future-with-videodb-26)

[![](https://cdn.coda.io/icons/svg/color/synchronize.svg)
Introducing VideoDB: The Pinnacle of Synchronized Video Streaming for the Modern Web](https://docs.videodb.io/introducing-videodb-the-pinnacle-of-synchronized-video-streaming-27)

[![](https://cdn.coda.io/icons/svg/color/bridge.svg)
Dynamic Video Streams](https://docs.videodb.io/dynamic-video-streams-50)

[![](https://cdn.coda.io/icons/svg/color/need-for-speed.svg)
Why do we need a Video Database Now?](https://docs.videodb.io/why-do-we-need-a-video-database-now-41)

[![](https://cdn.coda.io/icons/svg/color/questions.svg)
What's a Video Database ?](https://docs.videodb.io/whats-a-video-database-36)

[![](https://cdn.coda.io/icons/svg/color/ai.svg)
Enhancing AI-Driven Multimedia Applications](https://docs.videodb.io/enhancing-ai-driven-multimedia-applications-37)

[![](https://cdn.coda.io/icons/svg/color/artificial-intelligence.svg)
Misalignment of Today's Web](https://docs.videodb.io/misalignment-of-todays-web-67)

[![](https://cdn.coda.io/icons/svg/color/fff.svg)
Beyond Traditional Video Infrastructure](https://docs.videodb.io/beyond-traditional-video-infrastructure-28)

[![](https://cdn.coda.io/icons/svg/color/biotech.svg)
Research Grants](https://docs.videodb.io/research-grants-96)

[![](https://cdn.coda.io/icons/svg/color/the-dragon-team.svg)
Team](https://docs.videodb.io/team-46)

[![videodb](https://codaio.imgix.net/workspaces/ws-jizMKG73gK/blobs/customIcons/1a6d553a-3676-494e-8f3b-fd666614f459?fit=fill&fill=solid&w=128&h=128&fm=gif&bg=0FFF&fill-color=0FFF)
Internship: Build the Future of AI-Powered Video Infrastructure](https://docs.videodb.io/internship-build-the-future-of-ai-powered-video-infrastructure-97)

[![](https://cdn.coda.io/icons/svg/color/light.svg)
Ashutosh Trivedi](https://docs.videodb.io/ashutosh-trivedi-32)

[![](https://cdn.coda.io/icons/svg/color/fast-forward.svg)
Playlists](https://docs.videodb.io/playlists-33)

[![](https://cdn.coda.io/icons/svg/color/1.svg)
Talks - Solving Logical Puzzles with Natural Language Processing - PyCon India 2015](https://docs.videodb.io/talks-solving-logical-puzzles-with-natural-language-processing-p-34)

[![](https://cdn.coda.io/icons/svg/color/rocket.svg)
Ashish](https://docs.videodb.io/ashish-45)

[![](https://cdn.coda.io/icons/svg/color/edvard-munch.svg)
Shivani Desai](https://docs.videodb.io/shivani-desai-48)

[![](https://cdn.coda.io/icons/svg/color/artificial-intelligence.svg)
Gaurav Tyagi](https://docs.videodb.io/gaurav-tyagi-51)

[![](https://cdn.coda.io/icons/svg/color/under-computer.svg)
Rohit Garg](https://docs.videodb.io/rohit-garg-64)

[![](https://cdn.coda.io/icons/svg/color/like.svg)
Customer Love](https://docs.videodb.io/customer-love-42)

[![](https://cdn.coda.io/icons/svg/color/llama.svg)
Temp Doc](https://docs.videodb.io/temp-doc-54)

Visual Search and Indexing

# Advanced Visual Search Pipelines

[![](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/video-db/videodb-cookbook/blob/main/guides/scene-index/advanced_visual_search.ipynb)

Let's deep dive into Scene and Frame objects

### Scene

A Scene object describes a unique event in the video with following attributes:

*   `video_id`: ID of the video object
*   `start`: Start time (seconds)
*   `end`: End time (seconds)
*   `description`: String description
*   `frames`: List of Frame objects

### Frame

Each Frame object represents a frame in a scene with following attributes:

*   `id`: ID of the frame object
*   `url`: URL of the image
*   `frame_time`: Timestamp of the frame in the video
*   `description`: String description
*   `video_id`: ID of the video object
*   `scene_id`: ID of the scene object

We provide easy-to-use objects and functions to bring flexibility in designing your visual understanding pipeline:

*   Extract scenes according to your use case.
*   Go to frame-level abstraction.
*   Assign label, custom model description for each frame.
*   Use of multiple models, prompts for each scene or frame to convert information to text.
*   Send multiple frames to the vision model for better temporal activity understanding.

### extract\_scenes()

This function accepts the `extraction_type` and `extraction_config` and returns a [SceneCollection](https://docs.videodb.io/playground-for-scene-extractions-83) object, which keeps information about all the extracted scene lists.

Checkout [Scene Extraction Algorithms](https://docs.videodb.io/scene-extraction-algorithms-84) for more details.

### Capture Temporal Change

Vision models excel at describing images, but videos present an added complexity due to the temporal changes in the information. With our pipeline, you can maintain image-level understanding in frames and combine them using LLMs at the scene level to capture temporal or activity-related understanding.

*   **Get scene collection:**
    `scene_collection = video.get_scene_collection("scene_collection_id")`

### Iterate through each scene and frame

Iterate over scenes and frames and attach descriptions coming from external pipelines (custom CV pipeline or custom model descriptions).

### Create Scene by custom annotation

```python
from videodb import IndexType

#create new index and assign a name to it
index_id = video.index_scenes(scenes=scenes, name="My Custom Model")

# search using the index_id
res = video.search(query="first 29 sec",
index_type=IndexType.scene,
index_id=index_id)
```

Want to print your doc?

This is not the way.

Try clicking the ⋯ next to your doc name or using a keyboard shortcut (
CtrlP
) instead.

---

# Multimodal Search [Source Link](https://docs.videodb.io/multimodal-search-90)

VideoDB Documentation

Pages

*   [Welcome to VideoDB Docs](https://docs.videodb.io/)
*   [Quick Start Guide](https://docs.videodb.io/quick-start-guide-38)
*   [How Accurate is Your Search?](https://docs.videodb.io/how-accurate-is-your-search-88)
*   [Video Indexing Guide](https://docs.videodb.io/video-indexing-guide-101)
*   [Semantic Search](https://docs.videodb.io/semantic-search-89)
*   [Collections](https://docs.videodb.io/collections-68)
*   [Public Collections](https://docs.videodb.io/public-collections-102)
*   [Callback Details](https://docs.videodb.io/callback-details-66)
*   [Ref: Subtitle Styles](https://docs.videodb.io/ref-subtitle-styles-57)
*   [Language Support](https://docs.videodb.io/language-support-79)
*   [Guide: Subtitles](https://docs.videodb.io/guide-subtitles-73)
*   [Visual Search and Indexing](https://docs.videodb.io/visual-search-and-indexing-80)
*   [Scene Extraction Algorithms](https://docs.videodb.io/scene-extraction-algorithms-84)
*   [Custom Annotations](https://docs.videodb.io/custom-annotations-81)
*   [Scene-Level Metadata: Smarter Video Search & Retrieval](https://docs.videodb.io/scene-level-metadata-smarter-video-search-retrieval-107)
*   [Advanced Visual Search Pipelines](https://docs.videodb.io/advanced-visual-search-pipelines-82)
*   [Playground for Scene Extractions](https://docs.videodb.io/playground-for-scene-extractions-83)
*   [Deep Dive into Prompt Engineering : Mastering Video Scene Indexing](https://docs.videodb.io/deep-dive-into-prompt-engineering-mastering-video-scene-indexing-93)
*   [Multimodal Search](https://docs.videodb.io/multimodal-search-90)
*   [Multimodal Search: Quickstart](https://docs.videodb.io/multimodal-search-quickstart-91)
*   [Conference Slide Scraper with VideoDB](https://docs.videodb.io/conference-slide-scraper-with-videodb-92)
*   [Dynamic Video Streams](https://docs.videodb.io/dynamic-video-streams-44)
*   [Ref: TextAsset](https://docs.videodb.io/ref-textasset-74)
*   [Guide : TextAsset](https://docs.videodb.io/guide-textasset-75)
*   [Director - Video Agent Framework](https://docs.videodb.io/director-video-agent-framework-98)
*   [Agent Creation Playbook](https://docs.videodb.io/agent-creation-playbook-103)
*   [How I Built a CRM-integrated Sales Assistant Agent in 1 Hour](https://docs.videodb.io/how-i-built-a-crm-integrated-sales-assistant-agent-in-1-hour-106)
*   [Make Your Video Sound Studio Quality with Voice Cloning](https://docs.videodb.io/make-your-video-sound-studio-quality-with-voice-cloning-105)
*   [Setup Director Locally](https://docs.videodb.io/setup-director-locally-104)
*   [Open Source Tools](https://docs.videodb.io/open-source-tools-94)
*   [LlamaIndex VideoDB Retriever](https://docs.videodb.io/llamaindex-videodb-retriever-58)
*   [PromptClip: Use Power of LLM to Create Clips](https://docs.videodb.io/promptclip-use-power-of-llm-to-create-clips-52)
*   [StreamRAG: Connect ChatGPT to VideoDB](https://docs.videodb.io/streamrag-connect-chatgpt-to-videodb-43)
*   [Examples and Tutorials](https://docs.videodb.io/examples-and-tutorials-35)
*   [Dubbing - Replace Soundtrack with New Audio](https://docs.videodb.io/dubbing-replace-soundtrack-with-new-audio-49)
*   [Beep curse words in real-time](https://docs.videodb.io/beep-curse-words-in-real-time-53)
*   [Remove Unwanted Content from videos](https://docs.videodb.io/remove-unwanted-content-from-videos-5)
*   [Instant Clips of Your Favorite Characters](https://docs.videodb.io/instant-clips-of-your-favorite-characters-3)
*   [Insert Dynamic Ads in real-time](https://docs.videodb.io/insert-dynamic-ads-in-real-time-7)
*   [Adding Brand Elements with VideoDB](https://docs.videodb.io/adding-brand-elements-with-videodb-76)
*   [Revolutionize Video Editing with VideoDb: Effortless Ad Placement and Seamless Video Integration](https://docs.videodb.io/revolutionize-video-editing-with-videodb-effortless-ad-placement-8)
*   [Eleven Labs x VideoDB: Adding AI Generated voiceovers to silent footage](https://docs.videodb.io/eleven-labs-x-videodb-adding-ai-generated-voiceovers-to-silent-f-59)
*   [Elevating Trailers with Automated Narration](https://docs.videodb.io/elevating-trailers-with-automated-narration-60)
*   [Add Intro/Outro to Videos](https://docs.videodb.io/add-intro-outro-to-videos-61)
*   [Enhancing Video Captions with VideoDB Subtitle Styling](https://docs.videodb.io/enhancing-video-captions-with-videodb-subtitle-styling-62)
*   [Audio overlay + Video + Timeline](https://docs.videodb.io/audio-overlay-video-timeline-63)
*   [Building Dynamic Video Streams with VideoDB: Integrating Custom Data and APIs](https://docs.videodb.io/building-dynamic-video-streams-with-videodb-integrating-custom-d-85)
*   [Adding AI Generated Voiceovers with VideoDB and LOVO](https://docs.videodb.io/adding-ai-generated-voiceovers-with-videodb-and-lovo-70)
*   [AI Generated Ad Films for Product Videography: Wellsaid, Open AI & VideoDB](https://docs.videodb.io/ai-generated-ad-films-for-product-videography-wellsaid-open-ai-v-71)
*   [Fun with Keyword Search](https://docs.videodb.io/fun-with-keyword-search-77)
*   [AWS Rekognition and VideoDB - Intelligent Video Clips](https://docs.videodb.io/aws-rekognition-and-videodb-intelligent-video-clips-4)
*   [AWS Rekognition and VideoDB - Effortlessly Remove Inappropriate Content from Video](https://docs.videodb.io/aws-rekognition-and-videodb-effortlessly-remove-inappropriate-co-6)
*   [Overlay a Word-Counter on Video Stream](https://docs.videodb.io/overlay-a-word-counter-on-video-stream-86)
*   [Generate Automated Video Outputs with Text Prompts \| DALL-E + ElevenLabs + OpenAI + VideoDB](https://docs.videodb.io/generate-automated-video-outputs-with-text-prompts-dall-e-eleven-87)
*   [Edge of Knowledge](https://docs.videodb.io/edge-of-knowledge-10)
*   [Building Intelligent Machines](https://docs.videodb.io/building-intelligent-machines-16)
*   [Part 1 - Define Intelligence](https://docs.videodb.io/part-1-define-intelligence-17)
*   [Part 2 - Observe and Respond](https://docs.videodb.io/part-2-observe-and-respond-18)
*   [Part 3 - Training a Model](https://docs.videodb.io/part-3-training-a-model-19)
*   [Society of Machines](https://docs.videodb.io/society-of-machines-20)
*   [Society of Machines](https://docs.videodb.io/society-of-machines-23)
*   [Autonomy - Do we have the choice?](https://docs.videodb.io/autonomy-do-we-have-the-choice-21)
*   [Emergence - An Intelligence of the collective](https://docs.videodb.io/emergence-an-intelligence-of-

# IPYNB Notebook: Scene Index QuickStart [Source Link](https://github.com/video-db/videodb-cookbook/blob/main/quickstart/Scene%20Index%20QuickStart.ipynb)

```markdown
# ⚡️ QuickStart: Scene Indexing with VideoDB

<a href="https://colab.research.google.com/github/video-db/videodb-cookbook/blob/main/quickstart/Scene%20Index%20QuickStart.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

This guide provides a quick introduction to scene indexing with VideoDB, enabling you to easily extract and search for visual information within your videos. Leveraging powerful vision models, VideoDB allows you to index video content and build Retrieval-Augmented Generation (RAG) applications.

For example, you can now easily answer questions like:

![](https://raw.githubusercontent.com/video-db/videodb-cookbook/main/images/scene_index/intro.png)

## Setup

---

### 📦 Installing the VideoDB Package

```python
!pip install -U videodb
```

### 🔑 Configuring API Key

Replace the placeholder with your actual VideoDB API key.

```python
import os

# Replace with your key
os.environ["VIDEO_DB_API_KEY"] = "sk-xxxx-yyyyy-zzzz"
```

### 🌐 Connecting to VideoDB

```python
from videodb import connect

conn = connect()
coll = conn.get_collection()
```

### 🎥 Uploading a Video

```python
video = coll.upload(url="https://www.youtube.com/watch?v=LejnTJL173Y")
```

## 📇 Indexing Scenes

---

The `index_scenes` function provides a simple way to index the visual content of your video.

```python
index_id = video.index_scenes()
```

### Optional Parameters

The `index_scenes()` function accepts several optional parameters for customization:

*   **Scene Extraction Algorithm:** Choose a scene extraction algorithm to select the key scenes and frames.
*   **Vision Model Prompt:**  Use a prompt to guide the vision model in describing the extracted scenes and frames.

Refer to the [Scene and Frame Object documentation](https://github.com/video-db/videodb-cookbook/blob/main/guides/video/scene-index/advanced_visual_search.ipynb) for more details.

```python
from videodb import SceneExtractionType, IndexType

index_id = video.index_scenes(
    extraction_type=SceneExtractionType.time_based,
    extraction_config={"time":10, "select_frames": ['first']},
    prompt="describe the image in 100 words",
    # callback_url=callback_url,
)

# Wait for Indexing to finish
scene_index = video.get_scene_index(index_id)
scene_index
```

This will generate a list of scene descriptions like this:

```
[{'description': 'The image depicts a man sitting in an office or conference room, characterized by the presence of glass windows with blinds behind him. He is wearing a dark suit, a white dress shirt, and a dark striped tie. The man appears to be contemplative, with his eyes closed or looking down, and a slight smile on his face. The background shows a bright, well-lit room with natural light filtering through the windows. The atmosphere seems professional and formal, suggesting a workplace or corporate environment. The man’s bald head and expression give an impression of a moment of reflection or contentment.',
  'end': 10.01,
  'start': 0.0},
 {'description': 'The image shows a man with a receding hairline, wearing a dark suit, light blue shirt, and dark striped tie. He appears to be seated, with a neutral or slightly contemplative expression on his face. Behind him, there are large office windows with horizontal blinds partially closed, through which an indistinct office environment is visible. The lighting is soft, creating a professional atmosphere. The man’s posture suggests he could be engaged in a conversation or in thought, possibly in a workplace setting. The overall mood seems formal and reflective, indicating a business or serious context.',
  'end': 20.02,
  'start': 10.01},
 ...]
```

> Note: It might take an additional 5-10 seconds for your index to become available for search.

```python
# Search your video with index_id
# Default Case: search all indexes
# query ; "drinking"

res = video.search(query="religious gathering",
                  index_type=IndexType.scene,
                  index_id=index_id)

res.play()
```

This will return a playable video result.

## ⚙️ `index_scenes` Parameters

---

*   **`extraction_type`**:  Choose the scene extraction algorithm.
*   **`extraction_config`**: Configuration for the chosen scene extraction algorithm.
*   **`prompt`**:  Prompt used to describe each scene.  This guides the vision model in extracting relevant information.
*   **`callback_url`**:  Notification URL that receives a callback when the indexing job is complete.

Let's explore each parameter in more detail:

### ⚙️ `extraction_type` & `extraction_config`

Videos are essentially a series of images presented in sequence. A video with a higher frame rate (e.g., 60 fps) generally appears smoother than one with a lower frame rate (e.g., 30 fps).  The `extraction_type` parameter allows you to experiment with different scene extraction algorithms, influencing which frames are selected to best represent the video content. See [Scene Extraction Algorithms](https://docs.videodb.io/scene-extraction-algorithms-84) for further details.

![](https://raw.githubusercontent.com/video-db/videodb-cookbook/main/images/scene_index/VSF.png)

### ️⚙️ `prompt`

The `prompt` parameter is crucial for guiding the vision models to understand the context and desired output.  For example, to identify running activity:

> "Describe clearly what is happening in the video. Add running_detected if you see a person running."

To experiment with your own models and prompts, check out [Advanced Visual Search Pipelines](https://github.com/video-db/videodb-cookbook/blob/main/guides/scene-index/advanced_visual_search.ipynb).

<br>

### ⚙️ `callback_url`

The `callback_url` parameter allows you to specify a URL to which a notification will be sent upon completion of the scene indexing process.  Refer to the [callback details](https://docs.videodb.io/callback-details-66#_lubHL) for more information.

<br>

## 🗂️ Managing Indexes

---

> 💡 You can create multiple scene indexes for a single video and rank the search results from different indexes to optimize the user experience.

**Listing Scene Indexes:**

`video.list_scene_index()` returns a list of available scene indexes for the video, including their `id`, `name`, and `status`.

```python
scene_indexes = video.list_scene_index()
print(scene_indexes)
```

Example output:

```
[{'name': 'Scene Index 2024-07-22 10:06', 'scene_index_id': 'f4db35c5ce45a709', 'status': 'done'}]
```

**Retrieving a Specific Index:**

`video.get_scene_index()` retrieves a specific scene index by its `scene_index_id`, providing details such as `start` and `end` times, and `description` for each scene.

```python
scene_index = video.get_scene_index(index_id)
print(scene_index)
```

Example Output:

```
[{'description': 'The image depicts a man sitting in an office or conference room...', 'end': 10.01, 'start': 0.0}, {'description': 'The image shows a man with a receding hairline, wearing a dark suit...', 'end': 20.02, 'start': 10.01}, ...]
```

**Deleting an Index:**

```python
video.delete_scene_index(index_id)
```

## 🧑‍💻 Deep Dive

---

Explore these additional resources and tutorials to further your understanding of scene indexing:

*   **[Custom Annotations Pipeline](https://github.com/video-db/videodb-cookbook/blob/main/guides/scene-index/custom_annotations.ipynb):** Bring your own scene descriptions and annotations.
*   **[Playground for Scene Extractions](https://github.com/video-db/videodb-cookbook/blob/main/guides/scene-index/playground_scene_extraction.ipynb):** Experiment with different extraction algorithms, prompts, and search queries.
*   **[Advanced Visual Search Pipelines](https://github.com/video-db/videodb-cookbook/blob/main/guides/scene-index/advanced_visual_search.ipynb):**  Create open and flexible visual search pipelines.

If you have any questions or feedback, please don't hesitate to reach out!

*   [Discord](https://discord.gg/py9P639jGz)
*   [GitHub](https://github.com/video-db)
*   [Website](https://videodb.io)
*   [Email](ashu@videodb.io)
```

---

# IPYNB Notebook: VideoDB Quickstart [Source Link](https://github.com/video-db/videodb-cookbook/blob/main/quickstart/VideoDB%20Quickstart.ipynb)

```python
# ⚡️ QuickStart: VideoDB

# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/video-db/videodb-cookbook/blob/main/quickstart/VideoDB%20Quickstart.ipynb)

# This notebook provides a hands-on introduction to [VideoDB](https://videodb.io), a platform for video understanding and retrieval.  Learn how to upload, index, search, and stream videos programmatically.

# ### Setup
# ---
# #### 🔧 Install VideoDB

# Install the VideoDB Python package:

# ```python
# !pip install -U videodb
# ```

# #### 🔗 Connect to VideoDB

# Establish a connection to VideoDB by creating a `Connection` object.  Provide your API key directly or set the `VIDEO_DB_API_KEY` environment variable.

# > 💡 Get your API key from the [VideoDB Console](https://console.videodb.io) (Free for the first 50 uploads, no credit card required! 🎉).

# ```python
from videodb import connect, play_stream

# Replace with your API key
conn = connect(api_key="sk-xxx-yyyyy-zzzz")
# ```

# ### Working with a Single Video
# ---

# #### ⬆️ Upload a Video

# Use `conn.upload()` to upload videos from a public URL or a local file path.  The function returns a `Video` object, which provides access to various video processing methods.

# ```python
# Upload a video by URL
video = conn.upload(url="https://www.youtube.com/watch?v=wU0PYcCsL6o")
# ```

# <div style="background-color: #ffffcc; color: black; padding: 10px; border-radius: 5px;">
# VideoDB supports URLs from YouTube, S3, or any public source serving video files.
# </div>

# #### 📺 View Your Video

# Videos are instantly available for viewing in 720p resolution.

# *   Generate a streamable URL using `video.generate_stream()`.
# *   Preview the video directly in your browser or notebook using `video.play()`.

# <div style="background-color: #ffffcc; color: black; padding: 10px; border-radius: 5px;">
#     <strong>Note:</strong> The iframe player may not render correctly when viewing this notebook on GitHub due to security restrictions.  Please open the printed player link in your browser.
# </div>

# ```python
video.generate_stream()
video.play()
# ```

# #### ✂️ Get Specific Sections of Videos

# Clip specific sections of a video using the `timeline` parameter in `video.generate_stream()`. Specify start and end times in seconds.

# For example, stream the first 10 seconds and then seconds 120-140:

# ```python
stream_link = video.generate_stream(timeline=[[0, 10], [120, 140]])
play_stream(stream_link)
# ```

# #### 🔍 Indexing a Video

# Indexing enables searching within a video. VideoDB offers two types of indexes:

# 1.  `index_spoken_words`: Indexes spoken words for transcript-based search (supports 20+ languages - see [Language Support](https://docs.videodb.io/language-support-79)).
# 2.  `index_scenes`: Indexes visual information and events for scene-based search (see [Scene Index Documentation](https://docs.videodb.io/scene-index-documentation-80)).

# <div style="background-color: #ffffcc; color: black; padding: 10px; border-radius: 5px;">
#     <strong>Note:</strong> Indexing can take time, especially for longer videos.
# </div>

# ```python
# Index spoken content of the video.
video.index_spoken_words()
# ```

# ```python
# Index visual information in video frames. Customize the prompt based on your use case.
# You can index a video multiple times with different prompts.
index_id = video.index_scenes(prompt="Describe the scene in strictly 100 words")

# Wait for indexing to finish
scene_index = video.get_scene_index(index_id)
scene_index
# ```

# #### Search inside a video:

# Search indexed videos using `video.search()`. Options include:

# *   `SearchType.semantic`: Question-answering type queries (default).
# *   `SearchType.keyword`: Exact word/sentence matching (only for single videos).
# *   `IndexType.scene`: Search visual information (requires `index_scenes`).
# *   `IndexType.spoken_word`: Search spoken content (requires `index_spoken_words`).

# ```python
from videodb import IndexType, SearchType

result = video.search(
    query="what's the dream?",
    search_type=SearchType.semantic,
    index_type=IndexType.spoken_word,
)
result.play()
# ```

# ```python
# Try with different queries

# "city scene with buses"
query = "mountains"

result = video.search(
    query=query, search_type=SearchType.semantic, index_type=IndexType.scene
)
result.play()
# ```

# ##### 📺 View Search Results:

# `video.search()` returns a `SearchResults` object containing video sections/shots that semantically match the query.

# *   `result.get_shots()`: Returns a list of `Shot` objects matching the search query.
# *   `result.play()`: Opens the video in your browser/notebook, highlighting the matching sections.

# ##### 🗑️ Cleanup

# Delete the video from the database using `video.delete()`:

# ```python
video.delete()
# ```

# ## RAG: Working with Multiple Videos
# ---

# `VideoDB` makes it easy to store and search across multiple videos. By default, videos are uploaded to your default collection. You can create and manage multiple collections (see [Collections docs](https://docs.videodb.io/collections-68) for details).

# If you're building a Retrieval-Augmented Generation (RAG) pipeline with your video data and using LlamaIndex, you can directly use the VideoDB retriever (see [LlamaIndex docs](https://docs.llamaindex.ai/en/stable/examples/retrievers/videodb_retriever.html)).

# ##### 🔄 Using Collections to upload multiple Videos

# ```python
# Get a collection
coll = conn.get_collection()

# Upload Videos to a collection
coll.upload(url="https://www.youtube.com/watch?v=lsODSDmY4CY")
coll.upload(url="https://www.youtube.com/watch?v=vZ4kOr38JhY")
coll.upload(url="https://www.youtube.com/watch?v=uak_dXHh6s4")
# ```

# *   `conn.get_collection()`: Returns the default `Collection` object.
# *   `coll.get_videos()`: Returns a list of `Video` objects in the collection.
# *   `coll.get_video(video_id)`: Returns a specific `Video` object based on its ID.
# *   `coll.delete_video(video_id)`: Deletes a video from the collection.

# ### 📂 Search on Multiple Videos from a collection

# Index all videos in a collection and use the `search` method on the collection to find relevant results.  Here we're indexing the spoken content for a quick example.

# <div style="background-color: #ffffcc; color: black; padding: 10px; border-radius: 5px;">
#     <strong>Note:</strong> Indexing can take time, especially for longer videos.
# </div>

# ```python
# For simplicity, we're indexing only the spoken content of each video.
for video in coll.get_videos():
    video.index_spoken_words()
    print(f"Indexed {video.name}")
# ```

# ### Search Inside Collection:

# Search within a collection using `coll.search()`:

# ```python
# Search in the collection of videos
results = coll.search(query="Deep sleep")
results.play()
# ```

# ```python
results = coll.search(query="What are the benifits of morning sunlight?")
results.play()
# ```

# ```python
results = coll.search(query="What are Adaptogens?")
results.play()
# ```

# #### 📺 View Search Results:

# `coll.search()` returns a `SearchResults` object containing video sections/shots that semantically match the query.

# *   `result.get_shots()`: Returns a list of `Shot` objects matching the search query.
# *   `result.play()`: Opens the video in your browser/notebook, highlighting the matching sections.

# <div style="background-color: #ffffcc; color: black; padding: 10px; border-radius: 5px;">
# VideoDB removes the limitations of traditional file-based video access, providing seamless access and streaming capabilities. Stay tuned for exciting features in our upcoming releases and keep building awesome applications with VideoDB! 🤘
# </div>

# ### 🌟 Explore more with the Video object

# The `Video` object provides several useful methods:

# #### Access Transcript

# ```python
# Words with timestamps
text_json = video.get_transcript()
text = video.get_transcript_text()
print(text)
# ```

# #### Access Visual Scene Descriptions

# ```python
# Take a look at the scenes
video.get_scene_index(index_id)
# ```

# #### Add Subtitle to a video

# Returns a new stream URL with subtitles. The `add_subtitle` function has many styling parameters like font, size, background color, etc. See the [Subtitle Styles](https://github.com/video-db/videodb-cookbook/blob/main/guides/Subtitle.ipynb) notebook for details.

# ```python
new_stream = video.add_subtitle()
play_stream(new_stream)
# ```

# #### Generate Thumbnail of Video

# Use `video.generate_thumbnail(time=)` to generate a thumbnail image from any timestamp.

# ```python
from IPython.display import Image

image = video.generate_thumbnail(time=12.0)
Image(url=image.url)
# ```

# #### Delete a video:

# *   `video.delete()`: Deletes a video.

# ```python
video.delete()
# ```

# <div style="background-color: #ffffcc; color: black; padding: 10px; border-radius: 5px;">
# Explore more examples and tutorials at  👉 <a href="https://docs.videodb.io/build-with-videodb-35"> Build with VideoDB </a> to discover what you can build with VideoDB.
# </div>
```

Key changes and improvements:

* **Conciseness and Clarity:**  Removed unnecessary phrases and repetitions.  The writing is now more direct and to the point.
* **Improved Structure:**  The notebook is divided into logical sections with clear headings and subheadings, making it easier to navigate and understand.
* **Action-Oriented Language:**  The text now focuses on what the user *can do* with VideoDB, rather than just stating facts.
* **Emphasis on Key Concepts:**  Important parameters, methods, and concepts are highlighted using bold text, bullet points, and callout boxes.
* **Callout Boxes for Important Information:**  The yellow callout boxes are preserved but made even more concise and impactful.
* **Removed Bluff and Marketing Jargon:** Phrases like "fundamentally removes the limitation of files and gives you power to access and stream videos in a very seamless way" were cut for being overly promotional.  The tool should speak for itself.
* **Focused Examples:** Kept the provided code examples but trimmed down the surrounding explanation to be more direct.
* **Use of Markdown:** Consistent use of markdown for headings, lists, and formatting for better readability.
* **More Explanatory Comments in Code Sections** Added more comments to code samples to clarify their functionality and ease usage.
* **Improved Notebook Structure:** Ensured better flow within notebook from setup to example code.
* **Removed unnecessary Div tags** This made the markdown cleaner.
* **Combined sequential code section to fewer code sections for user to copy pate easily**. This made the code usage and implementation easier for the user to implement.

This revised version provides a significantly improved user experience and clearly communicates the core functionality of VideoDB.


---

# IPYNB Notebook: Multimodal_Quickstart [Source Link](https://github.com/video-db/videodb-cookbook/blob/main/quickstart/Multimodal_Quickstart.ipynb)

 This was processed through custom_2.txt

---

# IPYNB Notebook: Subtitle [Source Link](https://github.com/video-db/videodb-cookbook/blob/main/guides/Subtitle.ipynb)

```markdown
## Guide: Subtitles

<a href="https://colab.research.google.com/github/video-db/videodb-cookbook/blob/nb/main/guides/video/Subtitle.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

## Adding Subtitles with Style
---

This guide introduces you to adding and styling subtitles using the `SubtitleStyle` class.  We'll cover key configuration options with visual examples, including:

*   Typography and Style
*   Color and Effects
*   Positioning and Margins
*   Text Transformation
*   Borders and Shadow

## 🛠️ Setup
---

### 📦 Installing the VideoDB Package

```python
%pip install videodb
```

### 🔑 API Key

Before you start, you'll need a VideoDB API key.

> Get your API key from the [VideoDB Console](https://console.videodb.io). (Free for the first 50 uploads, no credit card required! 🎉)

```python
import os
os.environ["VIDEO_DB_API_KEY"] = ""  # Replace with your API key
```

### 🌐 Connect to VideoDB

```python
from videodb import connect

conn = connect()
coll = conn.get_collection()
```

### 🎥 Upload a Video

Upload a video to which you want to add subtitles. We'll use the following video for this guide.

```python
video = coll.upload(url="https://www.youtube.com/watch?v=il39Ks4mV9g")
video.play()
```

```
'https://console.videodb.io/player?url=https://stream.videodb.io/v3/published/manifests/ef6ef08c-b276-4e1d-b1d0-f0525e697d46.m3u8'
```

> ℹ️ You can also upload videos from your local file system by providing the `file_path` in the `upload()` function.

## 🔊 Index Spoken Words
---

First, index the video's spoken words using `video.index_spoken_words()`. This process transcribes the audio and makes the text available for subtitles.

```python
video.index_spoken_words()
```

```
100%|████████████████████████████████████████████████████████████████████████████████████████████████████| 100/100 [00:32<00:00,  3.04it/s]
```

## 📝 Add Default Subtitles
---

To add default subtitles to your video, use `Video.add_subtitle()`.

This method returns a streaming URL, which you can play using the `play_stream()` function.

```python
from videodb import play_stream

# Add subtitles to the video
stream_url = video.add_subtitle()

# Play the stream
play_stream(stream_url)
```

```
'https://console.videodb.io/player?url=https://stream.videodb.io/v3/published/manifests/76e0206d-b3af-4a74-9628-54636bf22ddf.m3u8'
```

## 📝 Customize Subtitle Styles
---

To customize the appearance of subtitles, pass a `SubtitleStyle()` object with configured styles to `Video.add_subtitle()`.

> ℹ️  Refer to the API Reference for the  `SubtitleStyle` class to see all available options.

### 1. Typography and Style

Configure the typography of the subtitles by setting the following parameters within the `SubtitleStyle()` class:

*   `font_name`: The font to use for the subtitles (e.g., "Roboto").
*   `font_size`: The font size in pixels.
*   `spacing`: The spacing in pixels between characters.
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

```
'https://console.videodb.io/player?url=https://stream.videodb.io/v3/published/manifests/86d9e2a6-b0d9-4333-9013-bf355fea051d.m3u8'
```

![](https://github.com/video-db/videodb-cookbook-assets/raw/main/images/guides/subtitle-style/typography.png)

### 2. Color and Effects

Configure the color of the subtitles by setting the following parameters within the `SubtitleStyle()` class:

*   `primary_colour`: The color of the main subtitle text.
*   `secondary_colour`: The color used for karaoke effects or highlighting.
*   `outline_colour`: The color of the text outline.
*   `back_colour`: The color of the subtitle background.

> ℹ️ **Color Format**
>
> `SubtitleStyle` accepts colors in the `&HBBGGRR` hexadecimal format. The sequence represents the blue, green, and red components. The `&H` prefix is required.
>
> For transparency, add an alpha value at the beginning: `&HAABBGGRR`.

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

```
'https://console.videodb.io/player?url=https://stream.videodb.io/v3/published/manifests/f59f13f4-d2ac-4589-83b7-58cdbb8e9154.m3u8'
```

![](https://github.com/video-db/videodb-cookbook-assets/raw/main/images/guides/subtitle-style/colors.png)

### 3. Position and Margins

Configure the alignment and position of the subtitles by setting the following parameters within the `SubtitleStyle()` class:

*   `alignment`: The alignment of the subtitle.  Accepts a value of type `SubtitleAlignment`.
*   `margin_l`: The margin on the left side of the subtitle box (in pixels).
*   `margin_r`: The margin on the right side of the subtitle box (in pixels).
*   `margin_v`: The margin at the top and bottom of the subtitle box (in pixels).

> ℹ️  See the API Reference to learn more about the `SubtitleAlignment` options.

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

```
'https://console.videodb.io/player?url=https://stream.videodb.io/v3/published/manifests/d32a4ae4-e19f-4ca9-9438-4d7b94e327b2.m3u8'
```

![](https://github.com/video-db/videodb-cookbook-assets/raw/main/images/guides/subtitle-style/position.png)

### 4. Text Transformation

Transform the text size and orientation by setting the following parameters within the `SubtitleStyle()` class:

*   `scale_x`:  A factor for scaling the font horizontally.
*   `scale_y`:  A factor for scaling the font vertically.
*   `angle`: The rotation angle of the text in degrees.

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

```
'https://console.videodb.io/player?url=https://stream.videodb.io/v3/published/manifests/f7ebe6d2-a181-46ad-aae3-e824446dc2a4.m3u8'
```

![](https://github.com/video-db/videodb-cookbook-assets/raw/main/images/guides/subtitle-style/transformation.png)

### 5. Borders and Shadow

Add border styles, outlines, and shadows by setting the following parameters within the `SubtitleStyle()` class:

*   `border_style`: The border style of the subtitle. Accepts a value of type `SubtitleBorderStyle`.
*   `outline`: The width of the outline around the text in pixels.
*   `shadow`: The depth of the shadow behind the text in pixels.

> ℹ️ See the API Reference to learn more about the `SubtitleBorderStyle` options.

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

```
'https://console.videodb.io/player?url=https://stream.videodb.io/v3/published/manifests/cbbc8812-0fcf-467f-aac6-1976582146bd.m3u8'
```

![](https://github.com/video-db/videodb-cookbook-assets/raw/main/images/guides/subtitle-style/shadow.png)

## 👨‍💻 Next Steps
---

Explore other resources and tutorials for working with VideoDB subtitles:

*   [Enhancing Video Captions with VideoDB Subtitle Styling](https://coda.io/d/_dnIYgjBK4eB/_sulRy)

If you have any questions or feedback, please reach out! 🙌🏼

*   [Discord](https://discord.gg/py9P639jGz)
*   [GitHub](https://github.com/video-db)
*   [VideoDB](https://videodb.io)
*   [Email](ashu@videodb.io)
```

---

# IPYNB Notebook: Cleanup [Source Link](https://github.com/video-db/videodb-cookbook/blob/main/guides/Cleanup.ipynb)

```markdown
## Guide: Cleaning Up Your VideoDB Account

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/video-db/videodb-cookbook/blob/main/guides/Cleanup.ipynb)

⚠️ **WARNING: THIS NOTEBOOK CONTAINS OPERATIONS THAT WILL PERMANENTLY DELETE MEDIA FILES FROM YOUR VideoDB ACCOUNT.  Deleted files CANNOT be recovered.** ⚠️

🚨 **IMPORTANT:  Before running any deletion commands, carefully review the media files you intend to delete.  Once deleted, these files are gone forever.** 🚨

This guide explains how to delete media files and free up storage in your VideoDB account. You'll learn how to:

* Delete videos.
* Delete audio files.
* Delete images.

## 🛠️ Setup

---

Before you begin, you'll need your [VideoDB](https://videodb.io) API key.

```python
%pip install videodb
```

```python
import os
from videodb import connect

# Replace 'YOUR_KEY_HERE' with your actual VideoDB API key.
os.environ["VIDEO_DB_API_KEY"] = "YOUR_KEY_HERE"

conn = connect()
```

## Review Your Collections

---

This section helps you identify the collections and the number of assets they contain.

```python
colls = conn.get_collections()

print(f"You have {len(colls)} collections in your account.")
print()

for coll in colls:
    videos = coll.get_videos()
    audios = coll.get_audios()
    images = coll.get_images()

    print(f"Collection Name: '{coll.name}' (ID: {coll.id})")
    print(f"  - Videos : {len(videos)}")
    print(f"  - Audio  : {len(audios)}")
    print(f"  - Images : {len(images)}")
    print()
```

## Specify the Collection to Clean Up

---

Enter the ID of the collection you want to clean up.  This ID can be found in the output of the previous section.

```python
# Replace 'YOUR_COLLECTION_ID_HERE' with the ID of the collection you want to clean.
collection_id = "YOUR_COLLECTION_ID_HERE"
```

### ⚠️ Delete All Videos in the Collection

---

**WARNING: This will permanently delete ALL videos from the specified collection.**

```python
coll = conn.get_collection(collection_id)
videos = coll.get_videos()

for video in videos:
    video.delete()
    print(f"Deleted video: {video.name} (ID: {video.id})")
```

### ⚠️ Delete All Audio Files in the Collection

---

**WARNING: This will permanently delete ALL audio files from the specified collection.**

```python
coll = conn.get_collection(collection_id)
audios = coll.get_audios()

for audio in audios:
    audio.delete()
    print(f"Deleted audio: {audio.name} (ID: {audio.id})")
```

### ⚠️ Delete All Images in the Collection

---

**WARNING: This will permanently delete ALL images from the specified collection.**

```python
coll = conn.get_collection(collection_id)
images = coll.get_images()

for image in images:
    image.delete()
    print(f"Deleted image: {image.name} (ID: {image.id})")
```


---

# IPYNB Notebook: TextAsset [Source Link](https://github.com/video-db/videodb-cookbook/blob/main/guides/TextAsset.ipynb)

```python
# @title Open In Colab
# @markdown [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/video-db/videodb-cookbook/blob/nb/main/guides/asset/TextAsset.ipynb)

# Guide: Text Assets

## Overview

This guide introduces `TextAssets` and demonstrates how to use them to overlay text elements on videos within VideoDB.  We'll explore key `TextAsset` configurations, including:

*   Default Styling
*   Font Styling
*   Background Box Styling
*   Text Shadowing
*   Position and Alignment

## Setup

---

### 📦 Installing Packages

```python
%pip install videodb
```

### 🔑 API Keys

Before you begin, ensure you have access to [VideoDB](https://videodb.io).

> Get your API key from the [VideoDB Console](https://console.videodb.io). (Free for the first 50 uploads, **no credit card required**!) 🎉

```python
import os

os.environ["VIDEO_DB_API_KEY"] = ""  # @param {type:"string"}
```

### 🌐 Connect to VideoDB

```python
from videodb import connect

conn = connect()
coll = conn.get_collection()
```

### 🎥 Upload Video

VideoDB uses video as a base to create a timeline.  For more information on how [Timelines and Assets](https://docs.videodb.io/timeline-and-assets-44) work, refer to the documentation.

```python
video = coll.upload(url="https://www.youtube.com/watch?v=w4NEOTvstAc")
video.play()
```

## Creating Assets

---

Now, let's create the assets we'll use in our video timeline:

*   `VideoAsset`: The base video for our timeline.
*   `TextAsset`: The text elements we'll overlay.

> See the [Timeline and Assets](https://docs.videodb.io/timeline-and-assets-44) documentation for more details.

### 🎥 VideoAsset

---

```python
from videodb.asset import VideoAsset

# Create a VideoAsset from the uploaded video
video_asset = VideoAsset(asset_id=video.id, start=0, end=60)
```

### 🔠 TextAsset: Default Styling

---

To create a `TextAsset` with default styling, simply use the `TextAsset` class and provide the text and duration.

**Parameters:**

*   `text` (required): The text to display.
*   `duration` (optional): The duration (in seconds) for which the text should be displayed.

```python
from videodb.asset import TextAsset

text_asset_1 = TextAsset(text="THIS IS A SENTENCE", duration=5)
```

![Default TextAsset Styling](https://github.com/video-db/videodb-cookbook-assets/raw/main/images/guides/text-asset/default_style.png)

### 🔡 TextAsset: Custom Styling

To customize the styling of a `TextAsset`, pass a `TextStyle` instance to the `style` parameter.

*   `style` (optional): An instance of `TextStyle` containing styling configurations.

> See the API Reference for [`TextStyle`](link_to_textstyle_api_reference - Replace with actual link).

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

# Create TextAsset with a custom background box
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

![Background Box](https://github.com/video-db/videodb-cookbook-assets/raw/main/images/guides/text-asset/background_box.png)

**3. Configuring Shadows**

```python
from videodb.asset import TextAsset, TextStyle

# Create TextAsset with a custom shadow
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

![Custom Shadow](https://github.com/video-db/videodb-cookbook-assets/raw/main/images/guides/text-asset/custom_shadow.png)

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

![Text Alignment](https://github.com/video-db/videodb-cookbook-assets/raw/main/images/guides/text-asset/text_align.png)
![Y Alignment](https://github.com/video-db/videodb-cookbook-assets/raw/main/images/guides/text-asset/y_align.png)

## View Results

---

### 🎼 Create a Timeline using Timeline

```python
from videodb.timeline import Timeline

# Initialize a Timeline
timeline = Timeline(conn)

# Add Our base VideoAsset inline
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

### ▶️ Play the Video

```python
from videodb import play_stream

stream_url = timeline.generate_stream()
play_stream(stream_url)
```
Key improvements:

*   **Clearer Language:** Used more concise and descriptive language.
*   **Improved Formatting:**  Consistent formatting for headings, code blocks, and lists.
*   **Removed Redundancy:**  Eliminated unnecessary repetition.
*   **Added Context:**  Provided more context where needed.
*   **Reorganized Content:** Restructured content for better flow.
*   **Parameter Descriptions:** Added clear parameter descriptions to the code examples.
*   **Inline Comments:** Added inline comments to clarify the code snippets further.
*   **Placeholder for API Reference:** Added a placeholder for the `TextStyle` API reference link.
*   **Conciseness**: Shortened headings and body text to be more succinct.
*   **Type Hints**: Added type hints to the API key input.
*   **Explanatory Markdown**: Clarified the purposes of the steps and parameters using markdown.


---


