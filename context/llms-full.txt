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

VideoDB Documentation

Pages

[Welcome to VideoDB Docs](https://docs.videodb.io/)

[Quick Start Guide](https://docs.videodb.io/quick-start-guide-38)

[Visual Search and Indexing](https://docs.videodb.io/visual-search-and-indexing-80)

[Multimodal Search](https://docs.videodb.io/multimodal-search-90)

[Dynamic Video Streams](https://docs.videodb.io/dynamic-video-streams-44)

[Director - Video Agent Framework](https://docs.videodb.io/director-video-agent-framework-98)

[Open Source Tools](https://docs.videodb.io/open-source-tools-94)

[Examples and Tutorials](https://docs.videodb.io/examples-and-tutorials-35)

[Edge of Knowledge](https://docs.videodb.io/edge-of-knowledge-10)

[Building World's First Video Database](https://docs.videodb.io/building-worlds-first-video-database-25)

[Team](https://docs.videodb.io/team-46)

[Customer Love](https://docs.videodb.io/customer-love-42)

[Temp Doc](https://docs.videodb.io/temp-doc-54)

# Welcome to VideoDB Docs

Video Database for your AI Applications

Hello 🙏

Happy to see you here!

### Latest Updates

Director - Video Agent Framework](https://docs.videodb.io/director-video-agent-framework-98)

— AI video agents framework for next-gen video interactions and workflows

📖 Listen for a quick walkthrough of this doc 👇

The Future of Video: VideoDB's Revolutionary 'Video as Data' Approach \| Tech Talk

The Future of Video: VideoDB's Revolutionary 'Video as Data' Approach \| Tech Talk - YouTube

[The Future of Video: VideoDB's Revolutionary 'Video as Data' Approach \| Tech Talk](https://www.youtube.com/watch?v=3RtUuxQeZgc)

### Quick Start

Get your API key at

[VideoDB Console](https://console.videodb.io/auth)

Use our

[Python SDK](https://github.com/video-db/videodb-python)

to build.

Here’s our

[Quick Start Guide](https://docs.videodb.io/quick-start-guide-38)

Checkout

[Examples and Tutorials](https://docs.videodb.io/examples-and-tutorials-35)

Check

[Open Source Tools](https://docs.videodb.io/open-source-tools-94)

to help you build

[Research Grants](https://docs.videodb.io/research-grants-96)

### Explore More

Follow us on

[Github](https://github.com/video-db)

Engage with us on our

[Discord](https://discord.gg/py9P639jGz)

Checkout our

[Youtube](https://www.youtube.com/@video_db)

Talk to our

[Pricing Assistant](https://chat.openai.com/g/g-VucvsTaEn-videodb-pricing)

[Customer Love](https://docs.videodb.io/customer-love-42)

### Edge of Knowledge

Today we are witnessing once a lifetime revolution on internet. We are deep thinkers of AI and here’s our deep dive and fundamental AI series.

A series on basics and fundamentals of ML

[Building Intelligent Machines](https://docs.videodb.io/building-intelligent-machines-16)

A series on Agents - The future of internet 👉

[Society of Machines](https://docs.videodb.io/society-of-machines-20)

### Curiosity

Curious to know about Video Database and its principles 👉

[What's a Video Database ?](https://docs.videodb.io/whats-a-video-database-36)

[Why do we need a Video Database Now?](https://docs.videodb.io/why-do-we-need-a-video-database-now-41)

[The Future Series](https://docs.videodb.io/the-future-series-78)

### Theory for deep divers

Want to go deep into the audio video systems 👉

[Building World's First Video Database](https://docs.videodb.io/building-worlds-first-video-database-25)

[Multimedia: From MP3/MP4 to the Future with VideoDB](https://docs.videodb.io/multimedia-from-mp3-mp4-to-the-future-with-videodb-26)

[Misalignment of Today's Web](https://docs.videodb.io/misalignment-of-todays-web-67)

[Dynamic Video Streams](https://docs.videodb.io/dynamic-video-streams-50)

### Team

We specialize in developing cutting-edge AI applications for multimedia, We are a diverse group of experts in multimedia, AI and innovative user experience design.

[Ashutosh Trivedi](https://docs.videodb.io/ashutosh-trivedi-32)

[Ashish](https://docs.videodb.io/ashish-45)

[Shivani Desai](https://docs.videodb.io/shivani-desai-48)

[Gaurav Tyagi](https://docs.videodb.io/gaurav-tyagi-51)

[Rohit Garg](https://docs.videodb.io/rohit-garg-64)

... and a few more hard working individuals who don’t care about their name being here. 🙌

Want to print your doc?

This is not the way.

Try clicking the ⋯ next to your doc name or using a keyboard shortcut (

CtrlP

) instead.


---

# How Accurate is Your Search? [Source Link](https://docs.videodb.io/how-accurate-is-your-search-88)

![videodb](https://codaio.imgix.net/workspaces/ws-jizMKG73gK/blobs/customIcons/1a6d553a-3676-494e-8f3b-fd666614f459?fit=fill&fill=solid&w=128&h=128&fm=gif&bg=0FFF&fill-color=0FFF)

VideoDB Documentation

Pages

[![](https://cdn.coda.io/icons/svg/color/align-center.svg)\\
\\
Welcome to VideoDB Docs](https://docs.videodb.io/)

[![](https://cdn.coda.io/icons/svg/color/quick-mode-on.svg)\\
\\
Quick Start Guide](https://docs.videodb.io/quick-start-guide-38)

[![icon picker](https://cdn.coda.io/icons/svg/color/wash-your-hands.svg)\\
\\
How Accurate is Your Search?](https://docs.videodb.io/how-accurate-is-your-search-88)

[![](https://cdn.coda.io/icons/svg/color/video-call.svg)\\
\\
Video Indexing Guide](https://docs.videodb.io/video-indexing-guide-101)

[![](https://cdn.coda.io/icons/svg/color/clear-search.svg)\\
\\
Semantic Search](https://docs.videodb.io/semantic-search-89)

[![](https://cdn.coda.io/icons/svg/color/binders-folder.svg)\\
\\
Collections](https://docs.videodb.io/collections-68)

[![](https://cdn.coda.io/icons/svg/color/magazine.svg)\\
\\
Public Collections](https://docs.videodb.io/public-collections-102)

[![](https://cdn.coda.io/icons/svg/color/callback.svg)\\
\\
Callback Details](https://docs.videodb.io/callback-details-66)

[![](https://cdn.coda.io/icons/svg/color/closed-captioning.svg)\\
\\
Ref: Subtitle Styles](https://docs.videodb.io/ref-subtitle-styles-57)

[![](https://cdn.coda.io/icons/svg/color/customer-support.svg)\\
\\
Language Support](https://docs.videodb.io/language-support-79)

[![](https://cdn.coda.io/icons/svg/color/closed-captioning.svg)\\
\\
Guide: Subtitles](https://docs.videodb.io/guide-subtitles-73)

[![](https://cdn.coda.io/icons/svg/color/asteroid.svg)\\
\\
Visual Search and Indexing](https://docs.videodb.io/visual-search-and-indexing-80)

[![](https://cdn.coda.io/icons/svg/color/clear-search.svg)\\
\\
Multimodal Search](https://docs.videodb.io/multimodal-search-90)

[![](https://cdn.coda.io/icons/svg/color/e-learning.svg)\\
\\
Dynamic Video Streams](https://docs.videodb.io/dynamic-video-streams-44)

[![director-light](https://codaio.imgix.net/workspaces/ws-jizMKG73gK/blobs/customIcons/6bc288c2-982b-4a97-a402-8da53aeaa236?fit=fill&fill=solid&w=128&h=128&fm=gif&bg=0FFF&fill-color=0FFF)\\
\\
Director - Video Agent Framework](https://docs.videodb.io/director-video-agent-framework-98)

[![github](https://codaio.imgix.net/workspaces/ws-jizMKG73gK/blobs/customIcons/ac14f3ef-daa1-4b6e-aba5-af11f11b8372?fit=fill&fill=solid&w=128&h=128&fm=gif&bg=0FFF&fill-color=0FFF)\\
\\
Open Source Tools](https://docs.videodb.io/open-source-tools-94)

[![](https://cdn.coda.io/icons/svg/color/book-and-pencil.svg)\\
\\
Examples and Tutorials](https://docs.videodb.io/examples-and-tutorials-35)

[![](https://cdn.coda.io/icons/svg/color/centre-of-gravity.svg)\\
\\
Edge of Knowledge](https://docs.videodb.io/edge-of-knowledge-10)

[![videodb](https://codaio.imgix.net/workspaces/ws-jizMKG73gK/blobs/customIcons/1a6d553a-3676-494e-8f3b-fd666614f459?fit=fill&fill=solid&w=128&h=128&fm=gif&bg=0FFF&fill-color=0FFF)\\
\\
Building World's First Video Database](https://docs.videodb.io/building-worlds-first-video-database-25)

[![](https://cdn.coda.io/icons/svg/color/the-dragon-team.svg)\\
\\
Team](https://docs.videodb.io/team-46)

[![](https://cdn.coda.io/icons/svg/color/like.svg)\\
\\
Customer Love](https://docs.videodb.io/customer-love-42)

[![](https://cdn.coda.io/icons/svg/color/llama.svg)\\
\\
Temp Doc](https://docs.videodb.io/temp-doc-54)

Quick Start Guide

# ![icon picker](https://cdn.coda.io/icons/svg/color/wash-your-hands.svg)         How Accurate is Your Search?

### Introduction

When you index your data and retrieve it with certain parameters, how do you measure the effectiveness of your search? This is where search evaluation comes in. By using test data, queries, and their results, you can assess the performance of indexes, search parameters, and other related factors. This evaluation helps you understand how well your search system is working and identify areas for improvement.

### Example

To keep it super simple let’s use a

[countdown video](https://www.youtube.com/watch?v=tWoo8i_VkvI)

of 30 seconds.

Loading…

We can imagine information in video indexed as documents which are “timestamps + some textual information” describing the visuals as there is no audio in this video”.

We can use the structure as

timestamp : (start, end ),description: “string”

So, if we use index\_scenes function

At (1, 2) - 29 seconds is displayed

At (2, 3) - 28 seconds is displayed

...

This continues until:

At (29, 30) - 1 second is displayed

### Ground Truth

It is the the ideal expected result. To evaluate the performance of search we need some test queries and the expected results.

Let's say for the query "Six" the expected result documents are at the following timestamps:

We will call this list of timestamps our ground truth for the query "Six."

### Evaluation Metrics

To evaluate the effectiveness of our search functionality, we'll can experiment with our query "Six" with various search parameters. 📊

The search results can be categorized as follows:

Retrieved Documents 🔍:

Retrieved Relevant Documents: Matches our ground truth ✅

Retrieved Irrelevant Documents: Don't match our ground truth ❌

Non-Retrieved Documents 🚫:

Non-Retrieved Relevant Documents: In our ground truth but not in results 😕

Non-Retrieved Irrelevant Documents: Neither in ground truth nor results 👍

We can further classify these categories in terms of search accuracy:

True Positives (TP) 🎯: Retrieved Relevant Documents

We wanted them, and we got them 🙌

False Positives (FP) 🎭: Retrieved Irrelevant Documents

We didn't want them, but we got them 🤔

False Negatives (FN) 😢: Non-Retrieved Relevant Documents

We wanted them, but we didn't get them 😓

True Negatives (TN) 🚫: Non-Retrieved Irrelevant Documents

We didn't want them, and we didn't get them 👌

💡 This classification helps us assess the precision and recall of our search algorithm, enabling further optimization.

### Accuracy

Accuracy measures how well our search algorithm retrieves required documents while excluding irrelevant ones. It can be calculated as follows:

In other words, accuracy is the ratio of correctly classified documents (both retrieved relevant and non-retrieved irrelevant) to the total number of documents. 📊

To get a more comprehensive evaluation of search performance, it's crucial to consider other metrics such as precision, recall, and F1-score in addition to accuracy. 💡🔬

### Precision and Recall

Precision is percentage of relevant retrieved docs out of all retrieved docs. It answers the question: "Of the documents our search returned, how many were actually relevant?"

Recall indicates the percentage of relevant documents that were successfully retrieved. It addresses the question: "Out of all the relevant documents, how many did our search find?" 🔍

### The Precision-Recall Trade-off

These metrics often have an inverse relationship, leading to a trade-off:

Recall 📈:

Measures the model's ability to find all relevant cases in a dataset.

Increases or remains constant as more documents are retrieved.

Never decreases with an increase in retrieved documents.

Precision 📉:

Refers to the proportion of correct positive identifications.

Typically decreases as more documents are retrieved.

Drops due to increased likelihood of including false positives.

### Search in VideoDB

Let’s understand the search interface provided by VideoDB and measure results with the above metric.

This function performs a search on video content with various customizable parameters:

query: The search query string.

search\_type: Determines the search method. Keyword search on single video level returns all the documents .

SearchType.semantic(default): For question-answering queries. ( across 1000s of videos/ collection ) Checkout

[![](https://cdn.coda.io/icons/svg/color/clear-search.svg)\\
Semantic Search](https://docs.videodb.io/semantic-search-89)

for detailed understanding.

SearchType.keyword: Matches exact occurrences where the given query is present as a sub-string (single video only).

index\_type: Specifies the index to search:

IndexType.spoken\_word(default): Searches spoken content.

IndexType.scene: Searches visual content.

result\_threshold: Initial filter for top N matching documents (default: 5).

score\_threshold: Absolute threshold filter for relevance scores (default: 0.2).

dynamic\_score\_percentage: Adaptive filtering mechanism:

Useful when there is a significant gap between top results and tail results after score\_threshold filter. Retains top x% of the score range.

Calculation: dynamic\_threshold = max\_score \- (range \* dynamic\_score\_percentage)

default: 20%

This interface allows for flexible and precise searching of video content, with options to fine-tune result filtering based on relevance scores and dynamic thresholds.

### Experiment

Follow this notebook to explore experiments on fine-tuning search results and gain a deeper understanding of the methods involved

[![](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/video-db/videodb-cookbook/blob/main/guides/VideoDB_Search_and_Evaluation.ipynb)

Here’s a basic outcome of the default settings for both search types on the query "six" for the above video:

1\. Semantic Search Default:

2\. Keyword Search:

### Outcome

As you can see, keyword search is best suited for queries like "teen" and "six." However, if the queries are in natural language, such as "find me a 6" then semantic search is more appropriate.

Keyword search would struggle to find relevant results for such natural language queries.

### Search + LLM

For complex queries like "Find me all the numbers greater than six" a basic search will not work effectively since it merely matches the query with documents in vector space and returns the matching documents.

In such cases, you can apply a loose filter to get all the documents that match the query. However, you will need to add an additional layer of intelligence using a Large Language Model (LLM). The matched documents can then be passed to the LLM to curate a response that accurately answers the query.

Introduction

Example

Ground Truth

Evaluation Metrics

Accuracy

Precision and Recall

The Precision-Recall Trade-off

Search in VideoDB

Experiment

Outcome

Search + LLM

Want to print your doc?

This is not the way.

![](https://cdn.coda.io/assets/6ee7d0564a67/img/import_google_docs.png)

Try clicking the ⋯ next to your doc name or using a keyboard shortcut (

CtrlP

) instead.


---

# Video Indexing Guide [Source Link](https://docs.videodb.io/video-indexing-guide-101)

![videodb](https://codaio.imgix.net/workspaces/ws-jizMKG73gK/blobs/customIcons/1a6d553a-3676-494e-8f3b-fd666614f459?fit=fill&fill=solid&w=128&h=128&fm=gif&bg=0FFF&fill-color=0FFF)

VideoDB Documentation

Pages

[![](https://cdn.coda.io/icons/svg/color/align-center.svg)\\
\\
Welcome to VideoDB Docs](https://docs.videodb.io/)

[![](https://cdn.coda.io/icons/svg/color/quick-mode-on.svg)\\
\\
Quick Start Guide](https://docs.videodb.io/quick-start-guide-38)

[![](https://cdn.coda.io/icons/svg/color/wash-your-hands.svg)\\
\\
How Accurate is Your Search?](https://docs.videodb.io/how-accurate-is-your-search-88)

[![icon picker](https://cdn.coda.io/icons/svg/color/video-call.svg)\\
\\
Video Indexing Guide](https://docs.videodb.io/video-indexing-guide-101)

[![](https://cdn.coda.io/icons/svg/color/clear-search.svg)\\
\\
Semantic Search](https://docs.videodb.io/semantic-search-89)

[![](https://cdn.coda.io/icons/svg/color/binders-folder.svg)\\
\\
Collections](https://docs.videodb.io/collections-68)

[![](https://cdn.coda.io/icons/svg/color/magazine.svg)\\
\\
Public Collections](https://docs.videodb.io/public-collections-102)

[![](https://cdn.coda.io/icons/svg/color/callback.svg)\\
\\
Callback Details](https://docs.videodb.io/callback-details-66)

[![](https://cdn.coda.io/icons/svg/color/closed-captioning.svg)\\
\\
Ref: Subtitle Styles](https://docs.videodb.io/ref-subtitle-styles-57)

[![](https://cdn.coda.io/icons/svg/color/customer-support.svg)\\
\\
Language Support](https://docs.videodb.io/language-support-79)

[![](https://cdn.coda.io/icons/svg/color/closed-captioning.svg)\\
\\
Guide: Subtitles](https://docs.videodb.io/guide-subtitles-73)

[![](https://cdn.coda.io/icons/svg/color/asteroid.svg)\\
\\
Visual Search and Indexing](https://docs.videodb.io/visual-search-and-indexing-80)

[![](https://cdn.coda.io/icons/svg/color/clear-search.svg)\\
\\
Multimodal Search](https://docs.videodb.io/multimodal-search-90)

[![](https://cdn.coda.io/icons/svg/color/e-learning.svg)\\
\\
Dynamic Video Streams](https://docs.videodb.io/dynamic-video-streams-44)

[![director-light](https://codaio.imgix.net/workspaces/ws-jizMKG73gK/blobs/customIcons/6bc288c2-982b-4a97-a402-8da53aeaa236?fit=fill&fill=solid&w=128&h=128&fm=gif&bg=0FFF&fill-color=0FFF)\\
\\
Director - Video Agent Framework](https://docs.videodb.io/director-video-agent-framework-98)

[![github](https://codaio.imgix.net/workspaces/ws-jizMKG73gK/blobs/customIcons/ac14f3ef-daa1-4b6e-aba5-af11f11b8372?fit=fill&fill=solid&w=128&h=128&fm=gif&bg=0FFF&fill-color=0FFF)\\
\\
Open Source Tools](https://docs.videodb.io/open-source-tools-94)

[![](https://cdn.coda.io/icons/svg/color/book-and-pencil.svg)\\
\\
Examples and Tutorials](https://docs.videodb.io/examples-and-tutorials-35)

[![](https://cdn.coda.io/icons/svg/color/centre-of-gravity.svg)\\
\\
Edge of Knowledge](https://docs.videodb.io/edge-of-knowledge-10)

[![videodb](https://codaio.imgix.net/workspaces/ws-jizMKG73gK/blobs/customIcons/1a6d553a-3676-494e-8f3b-fd666614f459?fit=fill&fill=solid&w=128&h=128&fm=gif&bg=0FFF&fill-color=0FFF)\\
\\
Building World's First Video Database](https://docs.videodb.io/building-worlds-first-video-database-25)

[![](https://cdn.coda.io/icons/svg/color/the-dragon-team.svg)\\
\\
Team](https://docs.videodb.io/team-46)

[![](https://cdn.coda.io/icons/svg/color/like.svg)\\
\\
Customer Love](https://docs.videodb.io/customer-love-42)

[![](https://cdn.coda.io/icons/svg/color/llama.svg)\\
\\
Temp Doc](https://docs.videodb.io/temp-doc-54)

Quick Start Guide

# ![icon picker](https://cdn.coda.io/icons/svg/color/video-call.svg) Video Indexing Guide

[![](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1B2-caHqnTfx2gRVEXn3p9n0nAd6U641m?usp=sharing)

## Unlocking the Power of Video Indexing with VideoDB

Imagine sitting down to rewatch your favorite movie, eager to revisit that thrilling car chase or the moment the hero delivers the iconic one-liner. You load up the video, and the hunt begins: sliding the playback bar, overshooting, rewinding, and starting all over again. Frustrating, isn’t it?

Now, think about listening to a five-hour podcast filled with fascinating information. You remember the host diving into quantum entanglement somewhere in the middle, but where exactly? Do you scrub through the audio hoping to find it or simply give up?

What if you could skip all this frustration and instantly jump to the exact part you’re looking for, every single time?

That’s the magic of indexes in VideoDB. They act as maps for your videos, marking key points and making it effortless to navigate directly to the content that matters most to you.

![With and without indexes.png](https://codaio.imgix.net/docs/_s5lUnUCIU/blobs/bl-xCH0NsktsH/dc4386c92bbfb54d3a13f716e26a61be5d3d636f84833ae9754479684204466e5fb7dd042d7dca65ff25d2be5518ab991e182632cb7396db342bd925248988cae35c6997d1d4e9e38521fb65deb0f65b57e73483d0493f55ccfa57358d52ab0650c16661?auto=format%2Ccompress&fit=max)

### What Are Indexes in VideoDB?

Indexes in VideoDB are like your personal guide to video content, turning complex, unstructured media into something searchable and organized. Think of them as metadata-powered assistants that help you locate not just spoken words, but also visuals—timestamping everything along the way.

Here’s how it works:

Videos are organized into Collections, much like folders contain files on your computer.

Each video is a continuous stream of visuals, audio, or both.

Indexing divides videos into scenes based on the prompts provided.

Videos can have multiple indexes, each focused on a specific aspect of the video. The focus of the index is determined by the prompts you use when creating it.

Example: Imagine you’re working with a video of someone giving a speech on stage:

If you prompt, “Describe the environment”, the index will capture details like the lighting, background, and stage setup.

If you prompt, “Describe the person”, the index will focus on their clothing, expressions, and gestures.

```python
# Upload the video to a collection
video = coll.upload(
url ="Public URL of the video"
)

# Index to capture the environment details
environment_index_id = video.index_scenes(
prompt ="Describe the environment"
)

# Index to capture details of the speaker
person_index_id = video.index_scenes(
prompt ="Describe the person"
)
```

This flexibility lets you create multiple indexes for the same content, tailored to your unique needs. With multimodal indexing, VideoDB combines spoken content and visual scenes, giving you a complete understanding of your video.

![Multiple Indexes.png](https://codaio.imgix.net/docs/_s5lUnUCIU/blobs/bl-ipnspuoNXW/79b0a70998275eb92411e6258de3afef749a5116181c895a50f9273ccf13f714c434cf1e52ec93d5b26832152a1bb3441a7d2125ed788289da4caa88650cd9c181326406dac62d0835fb77863c8f04fb9137b7c9a44a74479a3c4a153d96df2fb0b1f4c0?auto=format%2Ccompress&fit=max)

### Types of Indexes in VideoDB

Spoken Content Index

What It Is:
Using Automatic Speech Recognition (ASR), VideoDB transcribes spoken words into text, with every word precisely timestamped. This allows you to search for phrases or keywords and instantly navigate to those moments.

Scenarios Where It Shines:

Educational Content:
Imagine being a student studying for exams. Your professor’s lecture spans hours of video, but you recall a brief mention of plate tectonics. Instead of scrubbing through the entire video, you type “plate tectonics” into VideoDB, and the index directs you to the exact timestamp.

Customer Support Recordings:
A support representative analyzing a 10-minute customer call needs to find when the customer raised a key issue. With spoken content indexing, they can pinpoint the moment within seconds, speeding up the process.

Media Libraries:
Think of a five-hour podcast on astronomy. You’re only interested in the section where the host discusses quantum entanglement. Instead of wading through hours of audio, spoken content indexing takes you directly to that part, saving valuable time.

Scene/Visual Index

What It Is:
Visual indexing analyzes video content by detecting scene boundaries, objects, and actions. It timestamps and tags these elements, making it easy to locate specific scenes or objects.

Scenarios Where It Shines:

Surveillance Footage:
You’re a security analyst reviewing hours of highway CCTV recordings. A red sedan was involved in a robbery, and you need to find every instance of it. Manually combing through footage would take hours—or days. Scene indexing filters the footage to show only the moments where the red sedan appears, dramatically speeding up your investigation.

Sports Highlights:
A sports editor needs to compile a highlight reel of all the dropped catches in a cricket match. Instead of watching the entire game, scene indexing identifies each relevant moment, making the editing process faster and more efficient.

## How We Can Use Multiple Indexes While Searching a Collection or Video

Now that we’ve explored how indexing works, let’s dive into how we can use multiple scene indexes to retrieve the exact segments we need from videos.

Whenever we need to retrieve a specific segment, we rely on the indexes we’ve created. A single scene index might sometimes suffice, but often, especially when we’re looking for nuanced or layered results, one index isn’t enough. This is where multiple scene indexes come into play—allowing us to combine or filter results for more precise retrieval.

Think of it like how our brain processes complex memories. Memory recall is often multi-layered.

For instance, if you think about rainy days when school was closed, your brain might simultaneously recall the image of raindrops falling, the sound of thunder, and even the earthy smell after the rain. Together, these layers of memory build a vivid and detailed recollection.

In a similar way, VideoDB’s indexing system allows you to create and use multiple scene indexes, each capturing a different aspect of the video. By combining or intersecting results from these indexes, you can refine your search for better accuracy and relevance. We will explore this with a practical example:

### Multi-Index Search

Let’s return to the robbery investigation example. You’re analyzing hours of CCTV footage, and witnesses report that the suspect used a red sedan that was driving recklessly.

To narrow down the search, you create two scene indexes:

Scene Index 1: Focused on the color and model of vehicles passing through the streets.

Scene Index 2: Focused on the movement patterns of vehicles (e.g., speeding, swerving).

Here’s how you’d use these indexes:

First, use Scene Index 1 to filter all footage where red sedans appear.

Then, apply Scene Index 2 to further narrow it down to moments where the red sedans were driving recklessly.

By layering these two indexes, you can pinpoint the exact segments of footage most relevant to the investigation.

```python
# Upload the video to a collection and create two scene index
video = coll.upload( url ="Public URL of the video")

car_index = video.index_scenes( prompt ="Identify the color and model of each car")

mov_index = video.index_scenes( prompt ="Analyze the movement pattern of each car")

# Perform search for 'red sedans' on car index
car_result = video.search(
query ="Show all the segments where a 'red sedan' appears in the scene",
index_type = IndexType.scene,
index_id = car_index_id
)

# Perform search for 'reckless driving' on movement index
mov_result = video.search(
query ="Show all the segments where a car is driving recklessly",
index_type = IndexType.scene,
index_id = mov_index_id
)

# Combine the search results using an intersection function
multi_index_result = get_intersection( car_result, mov_result )

# Generate a streamable link from the multi index result
stream_link = video.generate_stream(multi_index_result)
```

The intersection function combines the results of both indexes, ensuring that only segments where both conditions (e.g., 'red sedan' and 'reckless driving') are met are returned.

### Bonus Example

Indexing the color ofeach car

```python
vehicle_index = traffic_video.index_scenes(
extraction_type=SceneExtractionType.time_based,
extraction_config={"time":1,"frame_count":1},
prompt="Identify the color and type of each vehicle"
)
```

In the extraction\_config parameter, we set the time to 1 second and frame\_count to 1. This is because detecting the color of each car only requires a single frame, which is sufficient to determine its color.

Indexing the motion of each car

```python
wait_index = traffic_video.index_scenes(
extraction_type=SceneExtractionType.time_based,
extraction_config={"time":4,"frame_count":5},
prompt="Identify when a car is stopping"
)
```

For the extraction\_config parameter, we've set time to 4 seconds and frame\_count to 5. This configuration is necessary because to detect whether a car has stopped, we need to observe its relative position across multiple frames within a 4-second interval. If the car's position remains consistent across these frames, it indicates that the car has come to a stop.

### Conclusion

By using multiple indexes, VideoDB doesn’t just save time—it transforms how you interact with videos. Whether you’re working with spoken content, visual elements, or a combination, indexing empowers you to retrieve highly accurate and context-specific results.

The ability to structure unorganized video content into searchable, interactive data opens up endless possibilities for developers and creators. From managing large media libraries to analyzing hours of surveillance footage or building smarter educational tools, VideoDB’s indexing technology enables you to:

Focus on the exact parts of your content that matter.

Save time and effort while improving accuracy and efficiency.

![info](https://cdn.coda.io/icons/svg/color/info.svg)

You can read more about visual indexing pipeline 👉

[![](https://cdn.coda.io/icons/svg/color/asteroid.svg)\\
Visual Search and Indexing](https://docs.videodb.io/visual-search-and-indexing-80)

Check Multimodal indexing and search pipeline at

[![](https://cdn.coda.io/icons/svg/color/clear-search.svg)\\
Multimodal Search](https://docs.videodb.io/multimodal-search-90)

Unlocking the Power of Video Indexing with VideoDB

What Are Indexes in VideoDB?

Types of Indexes in VideoDB

How We Can Use Multiple Indexes While Searching a Collection or Video

Multi-Index Search

Bonus Example

Conclusion

Want to print your doc?

This is not the way.

![](https://cdn.coda.io/assets/6ee7d0564a67/img/import_google_docs.png)

Try clicking the ⋯ next to your doc name or using a keyboard shortcut (CtrlP) instead.


---

# Semantic Search [Source Link](https://docs.videodb.io/semantic-search-89)

![videodb](https://codaio.imgix.net/workspaces/ws-jizMKG73gK/blobs/customIcons/1a6d553a-3676-494e-8f3b-fd666614f459?fit=fill&fill=solid&w=128&h=128&fm=gif&bg=0FFF&fill-color=0FFF)

VideoDB Documentation

Pages

[![](https://cdn.coda.io/icons/svg/color/align-center.svg)\\
\\
Welcome to VideoDB Docs](https://docs.videodb.io/)

[![](https://cdn.coda.io/icons/svg/color/quick-mode-on.svg)\\
\\
Quick Start Guide](https://docs.videodb.io/quick-start-guide-38)

[![](https://cdn.coda.io/icons/svg/color/wash-your-hands.svg)\\
\\
How Accurate is Your Search?](https://docs.videodb.io/how-accurate-is-your-search-88)

[![](https://cdn.coda.io/icons/svg/color/video-call.svg)\\
\\
Video Indexing Guide](https://docs.videodb.io/video-indexing-guide-101)

[![icon picker](https://cdn.coda.io/icons/svg/color/clear-search.svg)\\
\\
Semantic Search](https://docs.videodb.io/semantic-search-89)

[![](https://cdn.coda.io/icons/svg/color/binders-folder.svg)\\
\\
Collections](https://docs.videodb.io/collections-68)

[![](https://cdn.coda.io/icons/svg/color/magazine.svg)\\
\\
Public Collections](https://docs.videodb.io/public-collections-102)

[![](https://cdn.coda.io/icons/svg/color/callback.svg)\\
\\
Callback Details](https://docs.videodb.io/callback-details-66)

[![](https://cdn.coda.io/icons/svg/color/closed-captioning.svg)\\
\\
Ref: Subtitle Styles](https://docs.videodb.io/ref-subtitle-styles-57)

[![](https://cdn.coda.io/icons/svg/color/customer-support.svg)\\
\\
Language Support](https://docs.videodb.io/language-support-79)

[![](https://cdn.coda.io/icons/svg/color/closed-captioning.svg)\\
\\
Guide: Subtitles](https://docs.videodb.io/guide-subtitles-73)

[![](https://cdn.coda.io/icons/svg/color/asteroid.svg)\\
\\
Visual Search and Indexing](https://docs.videodb.io/visual-search-and-indexing-80)

[![](https://cdn.coda.io/icons/svg/color/landscape.svg)\\
\\
Scene Extraction Algorithms](https://docs.videodb.io/scene-extraction-algorithms-84)

[![](https://cdn.coda.io/icons/svg/color/edit-column.svg)\\
\\
Custom Annotations](https://docs.videodb.io/custom-annotations-81)

[![](https://cdn.coda.io/icons/svg/color/search-property.svg)\\
\\
Scene-Level Metadata: Smarter Video Search & Retrieval](https://docs.videodb.io/scene-level-metadata-smarter-video-search-retrieval-107)

[![](https://cdn.coda.io/icons/svg/color/search-more.svg)\\
\\
Advanced Visual Search Pipelines](https://docs.videodb.io/advanced-visual-search-pipelines-82)

[![](https://cdn.coda.io/icons/svg/color/football.svg)\\
\\
Playground for Scene Extractions](https://docs.videodb.io/playground-for-scene-extractions-83)

[![](https://cdn.coda.io/icons/svg/color/scuba-pressure-gauge.svg)\\
\\
Deep Dive into Prompt Engineering : Mastering Video Scene Indexing](https://docs.videodb.io/deep-dive-into-prompt-engineering-mastering-video-scene-indexing-93)

[![](https://cdn.coda.io/icons/svg/color/clear-search.svg)\\
\\
Multimodal Search](https://docs.videodb.io/multimodal-search-90)

[![](https://cdn.coda.io/icons/svg/color/search-more.svg)\\
\\
Multimodal Search: Quickstart](https://docs.videodb.io/multimodal-search-quickstart-91)

[![](https://cdn.coda.io/icons/svg/color/poll-topic.svg)\\
\\
Conference Slide Scraper with VideoDB](https://docs.videodb.io/conference-slide-scraper-with-videodb-92)

[![](https://cdn.coda.io/icons/svg/color/e-learning.svg)\\
\\
Dynamic Video Streams](https://docs.videodb.io/dynamic-video-streams-44)

[![](https://cdn.coda.io/icons/svg/color/text-box.svg)\\
\\
Ref: TextAsset](https://docs.videodb.io/ref-textasset-74)

[![](https://cdn.coda.io/icons/svg/color/text-box.svg)\\
\\
Guide : TextAsset](https://docs.videodb.io/guide-textasset-75)

[![director-light](https://codaio.imgix.net/workspaces/ws-jizMKG73gK/blobs/customIcons/6bc288c2-982b-4a97-a402-8da53aeaa236?fit=fill&fill=solid&w=128&h=128&fm=gif&bg=0FFF&fill-color=0FFF)\\
\\
Director - Video Agent Framework](https://docs.videodb.io/director-video-agent-framework-98)

[![](https://cdn.coda.io/icons/svg/color/open-book.svg)\\
\\
Agent Creation Playbook](https://docs.videodb.io/agent-creation-playbook-103)

[![](https://cdn.coda.io/icons/svg/color/bag-front-view.svg)\\
\\
How I Built a CRM-integrated Sales Assistant Agent in 1 Hour](https://docs.videodb.io/how-i-built-a-crm-integrated-sales-assistant-agent-in-1-hour-106)

[![](https://cdn.coda.io/icons/svg/color/voice-recognition-scan.svg)\\
\\
Make Your Video Sound Studio Quality with Voice Cloning](https://docs.videodb.io/make-your-video-sound-studio-quality-with-voice-cloning-105)

[![](https://cdn.coda.io/icons/svg/color/console.svg)\\
\\
Setup Director Locally](https://docs.videodb.io/setup-director-locally-104)

[![github](https://codaio.imgix.net/workspaces/ws-jizMKG73gK/blobs/customIcons/ac14f3ef-daa1-4b6e-aba5-af11f11b8372?fit=fill&fill=solid&w=128&h=128&fm=gif&bg=0FFF&fill-color=0FFF)\\
\\
Open Source Tools](https://docs.videodb.io/open-source-tools-94)

[![llama](https://codaio.imgix.net/workspaces/ws-jizMKG73gK/blobs/customIcons/c2b3a994-6140-40a9-93ff-d87aa37f2860?fit=fill&fill=solid&w=128&h=128&fm=gif&bg=0FFF&fill-color=0FFF)\\
\\
LlamaIndex VideoDB Retriever](https://docs.videodb.io/llamaindex-videodb-retriever-58)

[![](https://cdn.coda.io/icons/svg/color/command-line.svg)\\
\\
PromptClip: Use Power of LLM to Create Clips](https://docs.videodb.io/promptclip-use-power-of-llm-to-create-clips-52)

[![](https://cdn.coda.io/icons/svg/color/day-camera.svg)\\
\\
StreamRAG: Connect ChatGPT to VideoDB](https://docs.videodb.io/streamrag-connect-chatgpt-to-videodb-43)

[![](https://cdn.coda.io/icons/svg/color/book-and-pencil.svg)\\
\\
Examples and Tutorials](https://docs.videodb.io/examples-and-tutorials-35)

[![](https://cdn.coda.io/icons/svg/color/audible.svg)\\
\\
Dubbing - Replace Soundtrack with New Audio](https://docs.videodb.io/dubbing-replace-soundtrack-with-new-audio-49)

[![](https://cdn.coda.io/icons/svg/color/adware-free.svg)\\
\\
Beep curse words in real-time](https://docs.videodb.io/beep-curse-words-in-real-time-53)

[![](https://cdn.coda.io/icons/svg/color/find-user-male.svg)\\
\\
Remove Unwanted Content from videos](https://docs.videodb.io/remove-unwanted-content-from-videos-5)

[![](https://cdn.coda.io/icons/svg/color/find-and-replace.svg)\\
\\
Instant Clips of Your Favorite Characters](https://docs.videodb.io/instant-clips-of-your-favorite-characters-3)

[![](https://cdn.coda.io/icons/svg/color/insert-white-space.svg)\\
\\
Insert Dynamic Ads in real-time](https://docs.videodb.io/insert-dynamic-ads-in-real-time-7)

[![](https://cdn.coda.io/icons/svg/color/mac-client.svg)\\
\\
Adding Brand Elements with VideoDB](https://docs.videodb.io/adding-brand-elements-with-videodb-76)

[![](https://cdn.coda.io/icons/svg/color/adverb.svg)\\
\\
Revolutionize Video Editing with VideoDb: Effortless Ad Placement and Seamless Video Integration](https://docs.videodb.io/revolutionize-video-editing-with-videodb-effortless-ad-placement-8)

[![](https://cdn.coda.io/icons/svg/color/medium-volume.svg)\\
\\
Eleven Labs x VideoDB: Adding AI Generated voiceovers to silent footage](https://docs.videodb.io/eleven-labs-x-videodb-adding-ai-generated-voiceovers-to-silent-f-59)

[![](https://cdn.coda.io/icons/svg/color/camera-automation.svg)\\
\\
Elevating Trailers with Automated Narration](https://docs.videodb.io/elevating-trailers-with-automated-narration-60)

[![](https://cdn.coda.io/icons/svg/color/video-trimming.svg)\\
\\
Add Intro/Outro to Videos](https://docs.videodb.io/add-intro-outro-to-videos-61)

[![](https://cdn.coda.io/icons/svg/color/closed-captioning.svg)\\
\\
Enhancing Video Captions with VideoDB Subtitle Styling](https://docs.videodb.io/enhancing-video-captions-with-videodb-subtitle-styling-62)

[![](https://cdn.coda.io/icons/svg/color/high-volume.svg)\\
\\
Audio overlay + Video + Timeline](https://docs.videodb.io/audio-overlay-video-timeline-63)

[![](https://cdn.coda.io/icons/svg/color/video-call.svg)\\
\\
Building Dynamic Video Streams with VideoDB: Integrating Custom Data and APIs](https://docs.videodb.io/building-dynamic-video-streams-with-videodb-integrating-custom-d-85)

[![](https://cdn.coda.io/icons/svg/color/for-experienced.svg)\\
\\
Adding AI Generated Voiceovers with VideoDB and LOVO](https://docs.videodb.io/adding-ai-generated-voiceovers-with-videodb-and-lovo-70)

[![](https://cdn.coda.io/icons/svg/color/billboard.svg)\\
\\
AI Generated Ad Films for Product Videography: Wellsaid, Open AI & VideoDB](https://docs.videodb.io/ai-generated-ad-films-for-product-videography-wellsaid-open-ai-v-71)

[![](https://cdn.coda.io/icons/svg/color/search.svg)\\
\\
Fun with Keyword Search](https://docs.videodb.io/fun-with-keyword-search-77)

[![](https://cdn.coda.io/icons/svg/color/find-and-replace.svg)\\
\\
AWS Rekognition and VideoDB - Intelligent Video Clips](https://docs.videodb.io/aws-rekognition-and-videodb-intelligent-video-clips-4)

[![](https://cdn.coda.io/icons/svg/color/find-user-male.svg)\\
\\
AWS Rekognition and VideoDB - Effortlessly Remove Inappropriate Content from Video](https://docs.videodb.io/aws-rekognition-and-videodb-effortlessly-remove-inappropriate-co-6)

[![](https://cdn.coda.io/icons/svg/color/counter.svg)\\
\\
Overlay a Word-Counter on Video Stream](https://docs.videodb.io/overlay-a-word-counter-on-video-stream-86)

[![](https://cdn.coda.io/icons/svg/color/handle-with-care.svg)\\
\\
Generate Automated Video Outputs with Text Prompts \| DALL-E + ElevenLabs + OpenAI + VideoDB](https://docs.videodb.io/generate-automated-video-outputs-with-text-prompts-dall-e-eleven-87)

[![](https://cdn.coda.io/icons/svg/color/centre-of-gravity.svg)\\
\\
Edge of Knowledge](https://docs.videodb.io/edge-of-knowledge-10)

[![](https://cdn.coda.io/icons/svg/color/for-experienced.svg)\\
\\
Building Intelligent Machines](https://docs.videodb.io/building-intelligent-machines-16)

[![](https://cdn.coda.io/icons/svg/color/artificial-intelligence.svg)\\
\\
Part 1 - Define Intelligence](https://docs.videodb.io/part-1-define-intelligence-17)

[![](https://cdn.coda.io/icons/svg/color/panel-and-foot-outlet.svg)\\
\\
Part 2 - Observe and Respond](https://docs.videodb.io/part-2-observe-and-respond-18)

[![](https://cdn.coda.io/icons/svg/color/the-flash-sign.svg)\\
\\
Part 3 - Training a Model](https://docs.videodb.io/part-3-training-a-model-19)

[![](https://cdn.coda.io/icons/svg/color/cnc-machine.svg)\\
\\
Society of Machines](https://docs.videodb.io/society-of-machines-20)

[![](https://cdn.coda.io/icons/svg/color/groups.svg)\\
\\
Society of Machines](https://docs.videodb.io/society-of-machines-23)

[![](https://cdn.coda.io/icons/svg/color/the-flash-sign.svg)\\
\\
Autonomy - Do we have the choice?](https://docs.videodb.io/autonomy-do-we-have-the-choice-21)

[![](https://cdn.coda.io/icons/svg/color/artificial-intelligence.svg)\\
\\
Emergence - An Intelligence of the collective](https://docs.videodb.io/emergence-an-intelligence-of-the-collective-22)

[![](https://cdn.coda.io/icons/svg/color/back-to-draft.svg)\\
\\
Drafts](https://docs.videodb.io/drafts-24)

[![](https://cdn.coda.io/icons/svg/color/one-to-many.svg)\\
\\
From Language Models to World Models: The Next Frontier in AI](https://docs.videodb.io/from-language-models-to-world-models-the-next-frontier-in-ai-65)

[![](https://cdn.coda.io/icons/svg/color/recurring-appointment-exception.svg)\\
\\
The Future Series](https://docs.videodb.io/the-future-series-78)

[![videodb](https://codaio.imgix.net/workspaces/ws-jizMKG73gK/blobs/customIcons/1a6d553a-3676-494e-8f3b-fd666614f459?fit=fill&fill=solid&w=128&h=128&fm=gif&bg=0FFF&fill-color=0FFF)\\
\\
Building World's First Video Database](https://docs.videodb.io/building-worlds-first-video-database-25)

[![](https://cdn.coda.io/icons/svg/color/video.svg)\\
\\
Multimedia: From MP3/MP4 to the Future with VideoDB](https://docs.videodb.io/multimedia-from-mp3-mp4-to-the-future-with-videodb-26)

[![](https://cdn.coda.io/icons/svg/color/synchronize.svg)\\
\\
Introducing VideoDB: The Pinnacle of Synchronized Video Streaming for the Modern Web](https://docs.videodb.io/introducing-videodb-the-pinnacle-of-synchronized-video-streaming-27)

[![](https://cdn.coda.io/icons/svg/color/bridge.svg)\\
\\
Dynamic Video Streams](https://docs.videodb.io/dynamic-video-streams-50)

[![](https://cdn.coda.io/icons/svg/color/need-for-speed.svg)\\
\\
Why do we need a Video Database Now?](https://docs.videodb.io/why-do-we-need-a-video-database-now-41)

[![](https://cdn.coda.io/icons/svg/color/questions.svg)\\
\\
What's a Video Database ?](https://docs.videodb.io/whats-a-video-database-36)

[![](https://cdn.coda.io/icons/svg/color/ai.svg)\\
\\
Enhancing AI-Driven Multimedia Applications](https://docs.videodb.io/enhancing-ai-driven-multimedia-applications-37)

[![](https://cdn.coda.io/icons/svg/color/artificial-intelligence.svg)\\
\\
Misalignment of Today's Web](https://docs.videodb.io/misalignment-of-todays-web-67)

[![](https://cdn.coda.io/icons/svg/color/fff.svg)\\
\\
Beyond Traditional Video Infrastructure](https://docs.videodb.io/beyond-traditional-video-infrastructure-28)

[![](https://cdn.coda.io/icons/svg/color/biotech.svg)\\
\\
Research Grants](https://docs.videodb.io/research-grants-96)

[![](https://cdn.coda.io/icons/svg/color/the-dragon-team.svg)\\
\\
Team](https://docs.videodb.io/team-46)

[![videodb](https://codaio.imgix.net/workspaces/ws-jizMKG73gK/blobs/customIcons/1a6d553a-3676-494e-8f3b-fd666614f459?fit=fill&fill=solid&w=128&h=128&fm=gif&bg=0FFF&fill-color=0FFF)\\
\\
Internship: Build the Future of AI-Powered Video Infrastructure](https://docs.videodb.io/internship-build-the-future-of-ai-powered-video-infrastructure-97)

[![](https://cdn.coda.io/icons/svg/color/light.svg)\\
\\
Ashutosh Trivedi](https://docs.videodb.io/ashutosh-trivedi-32)

[![](https://cdn.coda.io/icons/svg/color/fast-forward.svg)\\
\\
Playlists](https://docs.videodb.io/playlists-33)

[![](https://cdn.coda.io/icons/svg/color/1.svg)\\
\\
Talks - Solving Logical Puzzles with Natural Language Processing - PyCon India 2015](https://docs.videodb.io/talks-solving-logical-puzzles-with-natural-language-processing-p-34)

[![](https://cdn.coda.io/icons/svg/color/rocket.svg)\\
\\
Ashish](https://docs.videodb.io/ashish-45)

[![](https://cdn.coda.io/icons/svg/color/edvard-munch.svg)\\
\\
Shivani Desai](https://docs.videodb.io/shivani-desai-48)

[![](https://cdn.coda.io/icons/svg/color/artificial-intelligence.svg)\\
\\
Gaurav Tyagi](https://docs.videodb.io/gaurav-tyagi-51)

[![](https://cdn.coda.io/icons/svg/color/under-computer.svg)\\
\\
Rohit Garg](https://docs.videodb.io/rohit-garg-64)

[![](https://cdn.coda.io/icons/svg/color/like.svg)\\
\\
Customer Love](https://docs.videodb.io/customer-love-42)

[![](https://cdn.coda.io/icons/svg/color/llama.svg)\\
\\
Temp Doc](https://docs.videodb.io/temp-doc-54)

Quick Start Guide

# ![icon picker](https://cdn.coda.io/icons/svg/color/clear-search.svg) Semantic Search

Semantic search operates on the conceptual meaning of a query rather than simple string matching. This approach allows for more intelligent and context-aware results. Key Features of Semantic Search:

Concept-Based Querying

Users can pose questions or use natural language.

The system understands the intent behind the query.

Vector Embeddings

Queries and documents are transformed into high-dimensional vector spaces.

These spaces capture semantic relationships between words and concepts.

Similarity Algorithms

K-Nearest Neighbors (KNN) or other vector similarity algorithms are employed.

Cosine similarity (angle between vectors) is a common measure.

Query-Document Matching

The query's vector is compared to indexed document vectors.

Documents with the closest vector representations are returned.

Scoring Mechanism

Each returned document is assigned a relevance score.

Scores typically reflect the degree of semantic similarity to the query.

![5. Semantic Search Parameters.png](https://codaio.imgix.net/docs/_s5lUnUCIU/blobs/bl-_WgNBDTBko/d969dd1f4e58b5bd8de41807f5aef19f5a7004b8830f958ec8857400fcda563da6769c420d3aec09842c0a8f1143e2bb2a152ea098e3f28a77699553f6187a8b64a79a74a4d98ffc655040a23bd0ea0ea2e7623e16b84f1cc888926f33057858c2a1e3bf?auto=format%2Ccompress&fit=max)

Want to print your doc?

This is not the way.

![](https://cdn.coda.io/assets/6ee7d0564a67/img/import_google_docs.png)

Try clicking the ⋯ next to your doc name or using a keyboard shortcut (

CtrlP

) instead.


---

# Collections [Source Link](https://docs.videodb.io/collections-68)

VideoDB Documentation

Pages

[Welcome to VideoDB Docs](https://docs.videodb.io/)

[Quick Start Guide](https://docs.videodb.io/quick-start-guide-38)

[How Accurate is Your Search?](https://docs.videodb.io/how-accurate-is-your-search-88)

[Video Indexing Guide](https://docs.videodb.io/video-indexing-guide-101)

[Semantic Search](https://docs.videodb.io/semantic-search-89)

[Collections](https://docs.videodb.io/collections-68)

[Public Collections](https://docs.videodb.io/public-collections-102)

[Callback Details](https://docs.videodb.io/callback-details-66)

[Ref: Subtitle Styles](https://docs.videodb.io/ref-subtitle-styles-57)

[Language Support](https://docs.videodb.io/language-support-79)

[Guide: Subtitles](https://docs.videodb.io/guide-subtitles-73)

[Visual Search and Indexing](https://docs.videodb.io/visual-search-and-indexing-80)

[Multimodal Search](https://docs.videodb.io/multimodal-search-90)

[Dynamic Video Streams](https://docs.videodb.io/dynamic-video-streams-44)

[Director - Video Agent Framework](https://docs.videodb.io/director-video-agent-framework-98)

[Open Source Tools](https://docs.videodb.io/open-source-tools-94)

[Examples and Tutorials](https://docs.videodb.io/examples-and-tutorials-35)

[Edge of Knowledge](https://docs.videodb.io/edge-of-knowledge-10)

[Building World's First Video Database](https://docs.videodb.io/building-worlds-first-video-database-25)

[Team](https://docs.videodb.io/team-46)

[Customer Love](https://docs.videodb.io/customer-love-42)

[Temp Doc](https://docs.videodb.io/temp-doc-54)

Quick Start Guide

# Collections

Collections are simple way to organize your uploads. Working with collections is straightforward. This helps in media organization and search efficiency.

Collection search would restrict the query to find information in only that collection, giving developers freedom to manage and organize videos for their RAG applications.

Create a new collection by calling create\_collectionfunction in the connection object.

conn.create\_collection(name: str, description: str)

Each collection would have a unique id starting with “c-xxx-xxxx-xxx”. You can pass the name and description when you create one.

\# create a new collection

new\_collection = conn.create\_collection(name =" test collection", description = "test description")

print(new\_collection)

List all the collections you have created by calling the function get\_collections

\# list all collections

collections = conn.get\_collections()

for c in collections:

print(c)

Get the collection by it’s unique id “c-xxx-xxxx-xxx”.

collection = conn.get\_collection("c-bc849eee-dc5f-48c2-bd37-bb541c88c8ca")

print(collection)

You can update the name and description of the collection by update\_collection function

\# update a collection

collection = conn.update\_collection("collection\_id","new\_name","new\_desc")

print(collection)

### Upload media to a Collection

When the collection is created you can use that to upload new video, audio, and images.

from videodb import MediaType

\# create collection

new\_collection = conn.create\_collection("test collection","test description")

print(new\_collection)

\# upload video

video = new\_collection.upload(url="https://youtu.be/a9\_\_D53WsUs?si=b1dmcLJbilNwC3H6")

print(video)

\# upload audio

audio = new\_collection.upload(url="https://youtu.be/MU0Yp0qmYEs?si=slWZ0HisObM14xjF", media\_type=MediaType.audio)

print(audio)

\# upload image

image = new\_collection.upload(url="https://www.freepnglogos.com/uploads/logo-ig-png/logo-ig-instagram-new-logo-vector-download-13.png", media\_type=MediaType.image)

print(image)

### List all the media in a Collection (video/audio/image)

Use get methods to list audios, videos and images in the collection. We have provided individual get methods to make it simple and intuitive for you.

\# list videos

videos = new\_collection.get\_videos()

for v in videos:

print(v)

\# list audios

audios = new\_collection.get\_audios()

for a in audios:

print(a)

\# list images

images = new\_collection.get\_images()

for img in images:

print(img)

### Search inside a Collection

The most useful thing about collections is to restrict search to a specific set of videos. This can come really handy in building complex RAG applications.

from videodb import SearchType

\# index spoken words

video.index\_spoken\_words()

\# search inside a collection

result = new\_collection.search("what is aws?", search\_type=SearchType.semantic)

print(result)

stream\_url = result.compile()

play\_stream(stream\_url)

## More on Collection

Checkout

[Public Collections](https://docs.videodb.io/public-collections-102)

to understand easy sharing of your collection with others.

Checkout

[Callback Details](https://docs.videodb.io/callback-details-66)

for asynchronous upload and indexing opearations.

Upload media to a Collection

List all the media in a Collection (video/audio/image)

Search inside a Collection

More on Collection

Want to print your doc?

This is not the way.

Try clicking the ⋯ next to your doc name or using a keyboard shortcut (CtrlP) instead.


---

# Public Collections [Source Link](https://docs.videodb.io/public-collections-102)

VideoDB Documentation

Pages

[Welcome to VideoDB Docs](https://docs.videodb.io/)

[Quick Start Guide](https://docs.videodb.io/quick-start-guide-38)

[How Accurate is Your Search?](https://docs.videodb.io/how-accurate-is-your-search-88)

[Video Indexing Guide](https://docs.videodb.io/video-indexing-guide-101)

[Semantic Search](https://docs.videodb.io/semantic-search-89)

[Collections](https://docs.videodb.io/collections-68)

[Public Collections](https://docs.videodb.io/public-collections-102)

[Callback Details](https://docs.videodb.io/callback-details-66)

[Ref: Subtitle Styles](https://docs.videodb.io/ref-subtitle-styles-57)

[Language Support](https://docs.videodb.io/language-support-79)

[Guide: Subtitles](https://docs.videodb.io/guide-subtitles-73)

[Visual Search and Indexing](https://docs.videodb.io/visual-search-and-indexing-80)

[Scene Extraction Algorithms](https://docs.videodb.io/scene-extraction-algorithms-84)

[Custom Annotations](https://docs.videodb.io/custom-annotations-81)

[Scene-Level Metadata: Smarter Video Search & Retrieval](https://docs.videodb.io/scene-level-metadata-smarter-video-search-retrieval-107)

[Advanced Visual Search Pipelines](https://docs.videodb.io/advanced-visual-search-pipelines-82)

[Playground for Scene Extractions](https://docs.videodb.io/playground-for-scene-extractions-83)

[Deep Dive into Prompt Engineering : Mastering Video Scene Indexing](https://docs.videodb.io/deep-dive-into-prompt-engineering-mastering-video-scene-indexing-93)

[Multimodal Search](https://docs.videodb.io/multimodal-search-90)

[Multimodal Search: Quickstart](https://docs.videodb.io/multimodal-search-quickstart-91)

[Conference Slide Scraper with VideoDB](https://docs.videodb.io/conference-slide-scraper-with-videodb-92)

[Dynamic Video Streams](https://docs.videodb.io/dynamic-video-streams-44)

[Ref: TextAsset](https://docs.videodb.io/ref-textasset-74)

[Guide : TextAsset](https://docs.videodb.io/guide-textasset-75)

[Director - Video Agent Framework](https://docs.videodb.io/director-video-agent-framework-98)

[Agent Creation Playbook](https://docs.videodb.io/agent-creation-playbook-103)

[How I Built a CRM-integrated Sales Assistant Agent in 1 Hour](https://docs.videodb.io/how-i-built-a-crm-integrated-sales-assistant-agent-in-1-hour-106)

[Make Your Video Sound Studio Quality with Voice Cloning](https://docs.videodb.io/make-your-video-sound-studio-quality-with-voice-cloning-105)

[Setup Director Locally](https://docs.videodb.io/setup-director-locally-104)

[Open Source Tools](https://docs.videodb.io/open-source-tools-94)

[LlamaIndex VideoDB Retriever](https://docs.videodb.io/llamaindex-videodb-retriever-58)

[PromptClip: Use Power of LLM to Create Clips](https://docs.videodb.io/promptclip-use-power-of-llm-to-create-clips-52)

[StreamRAG: Connect ChatGPT to VideoDB](https://docs.videodb.io/streamrag-connect-chatgpt-to-videodb-43)

[Examples and Tutorials](https://docs.videodb.io/examples-and-tutorials-35)

[Dubbing - Replace Soundtrack with New Audio](https://docs.videodb.io/dubbing-replace-soundtrack-with-new-audio-49)

[Beep curse words in real-time](https://docs.videodb.io/beep-curse-words-in-real-time-53)

[Remove Unwanted Content from videos](https://docs.videodb.io/remove-unwanted-content-from-videos-5)

[Instant Clips of Your Favorite Characters](https://docs.videodb.io/instant-clips-of-your-favorite-characters-3)

[Insert Dynamic Ads in real-time](https://docs.videodb.io/insert-dynamic-ads-in-real-time-7)

[Adding Brand Elements with VideoDB](https://docs.videodb.io/adding-brand-elements-with-videodb-76)

[Revolutionize Video Editing with VideoDb: Effortless Ad Placement and Seamless Video Integration](https://docs.videodb.io/revolutionize-video-editing-with-videodb-effortless-ad-placement-8)

[Eleven Labs x VideoDB: Adding AI Generated voiceovers to silent footage](https://docs.videodb.io/eleven-labs-x-videodb-adding-ai-generated-voiceovers-to-silent-f-59)

[Elevating Trailers with Automated Narration](https://docs.videodb.io/elevating-trailers-with-automated-narration-60)

[Add Intro/Outro to Videos](https://docs.videodb.io/add-intro-outro-to-videos-61)

[Enhancing Video Captions with VideoDB Subtitle Styling](https://docs.videodb.io/enhancing-video-captions-with-videodb-subtitle-styling-62)

[Audio overlay + Video + Timeline](https://docs.videodb.io/audio-overlay-video-timeline-63)

[Building Dynamic Video Streams with VideoDB: Integrating Custom Data and APIs](https://docs.videodb.io/building-dynamic-video-streams-with-videodb-integrating-custom-d-85)

[Adding AI Generated Voiceovers with VideoDB and LOVO](https://docs.videodb.io/adding-ai-generated-voiceovers-with-videodb-and-lovo-70)

[AI Generated Ad Films for Product Videography: Wellsaid, Open AI & VideoDB](https://docs.videodb.io/ai-generated-ad-films-for-product-videography-wellsaid-open-ai-v-71)

[Fun with Keyword Search](https://docs.videodb.io/fun-with-keyword-search-77)

[AWS Rekognition and VideoDB - Intelligent Video Clips](https://docs.videodb.io/aws-rekognition-and-videodb-intelligent-video-clips-4)

[AWS Rekognition and VideoDB - Effortlessly Remove Inappropriate Content from Video](https://docs.videodb.io/aws-rekognition-and-videodb-effortlessly-remove-inappropriate-co-6)

[Overlay a Word-Counter on Video Stream](https://docs.videodb.io/overlay-a-word-counter-on-video-stream-86)

[Generate Automated Video Outputs with Text Prompts \| DALL-E + ElevenLabs + OpenAI + VideoDB](https://docs.videodb.io/generate-automated-video-outputs-with-text-prompts-dall-e-eleven-87)

[Edge of Knowledge](https://docs.videodb.io/edge-of-knowledge-10)

[Building Intelligent Machines](https://docs.videodb.io/building-intelligent-machines-16)

[Part 1 - Define Intelligence](https://docs.videodb.io/part-1-define-intelligence-17)

[Part 2 - Observe and Respond](https://docs.videodb.io/part-2-observe-and-respond-18)

[Part 3 - Training a Model](https://docs.videodb.io/part-3-training-a-model-19)

[Society of Machines](https://docs.videodb.io/society-of-machines-20)

[Society of Machines](https://docs.videodb.io/society-of-machines-23)

[Autonomy - Do we have the choice?](https://docs.videodb.io/autonomy-do-we-have-the-choice-21)

[Emergence - An Intelligence of the collective](https://docs.videodb.io/emergence-an-intelligence-of-the-collective-22)

[Drafts](https://docs.videodb.io/drafts-24)

[From Language Models to World Models: The Next Frontier in AI](https://docs.videodb.io/from-language-models-to-world-models-the-next-frontier-in-ai-65)

[The Future Series](https://docs.videodb.io/the-future-series-78)

[Building World's First Video Database](https://docs.videodb.io/building-worlds-first-video-database-25)

[Multimedia: From MP3/MP4 to the Future with VideoDB](https://docs.videodb.io/multimedia-from-mp3-mp4-to-the-future-with-videodb-26)

[Introducing VideoDB: The Pinnacle of Synchronized Video Streaming for the Modern Web](https://docs.videodb.io/introducing-videodb-the-pinnacle-of-synchronized-video-streaming-27)

[Dynamic Video Streams](https://docs.videodb.io/dynamic-video-streams-50)

[Why do we need a Video Database Now?](https://docs.videodb.io/why-do-we-need-a-video-database-now-41)

[What's a Video Database ?](https://docs.videodb.io/whats-a-video-database-36)

[Enhancing AI-Driven Multimedia Applications](https://docs.videodb.io/enhancing-ai-driven-multimedia-applications-37)

[Misalignment of Today's Web](https://docs.videodb.io/misalignment-of-todays-web-67)

[Beyond Traditional Video Infrastructure](https://docs.videodb.io/beyond-traditional-video-infrastructure-28)

[Research Grants](https://docs.videodb.io/research-grants-96)

[Team](https://docs.videodb.io/team-46)

[Internship: Build the Future of AI-Powered Video Infrastructure](https://docs.videodb.io/internship-build-the-future-of-ai-powered-video-infrastructure-97)

[Ashutosh Trivedi](https://docs.videodb.io/ashutosh-trivedi-32)

[Playlists](https://docs.videodb.io/playlists-33)

[Talks - Solving Logical Puzzles with Natural Language Processing - PyCon India 2015](https://docs.videodb.io/talks-solving-logical-puzzles-with-natural-language-processing-p-34)

[Ashish](https://docs.videodb.io/ashish-45)

[Shivani Desai](https://docs.videodb.io/shivani-desai-48)

[Gaurav Tyagi](https://docs.videodb.io/gaurav-tyagi-51)

[Rohit Garg](https://docs.videodb.io/rohit-garg-64)

[Customer Love](https://docs.videodb.io/customer-love-42)

[Temp Doc](https://docs.videodb.io/temp-doc-54)

Quick Start Guide

# Public Collections

Public Collections allow you to share a collection of media (videos, audios, images) and intelligence with anyone. When a collection is public:

Anyone with the collection ID can access (read-only) the media within that collection.

Anyone can list and use the indexes of this collection and access the scene descriptions.

By default, all new collections are private unless explicitly made public.

## 1\. Creating a New Public Collection

When you create a new collection using create\_collection function, you can mark it public by setting the is\_public parameter to True. This makes the collection immediately accessible to other users (read-only) by sharing the collection ID with them.

public\_collection = conn.create\_collection(

name="Sample Collection",

description="Sample Collection Description",

is\_public=True

)

print(public\_collection.is\_public)\# Should print True

Parameters:

name: (Required) A string specifying the collection’s name.

description: (Required) A string describing the collection.

is\_public: (Optional, boolean) Defaults to False. Set to True to make the collection public.

## 2\. Changing Collection Visibility

You can always toggle visibility of any existing collection. Use make\_public() to make any collection public, or make\_public() to switch it back to your private collection.

\# Make collection private

public\_collection.make\_private()

print(public\_collection.is\_public)\# Should print False

\# Make collection public again

public\_collection.make\_public()

print(public\_collection.is\_public)\# Should print True

## 3\. Accessing a Public Collection

Any user can access a public collection using its collection ID. Once you have the collection object, you can retrieve videos, audios, or images within it.

\# Replace with the actual public collection ID

collection = conn.get\_collection("PUBLIC\_COLLECTION\_ID")

\# Retrieve all videos

videos = collection.get\_videos()

video = collection.get\_video("VIDEO\_ID\_OF\_PUBLIC\_COLLECTION")

\# Retrieve all audios

audios = collection.get\_audios()

audio = collection.get\_audio("AUDIO\_ID\_OF\_PUBLIC\_COLLECTION")

\# Retrieve all images

images = collection.get\_images()

image = collection.get\_image("IMAGE\_ID\_OF\_PUBLIC\_COLLECTION")

Sample Code:

\# VideoDB's OCR Benchmark Public Collection

collection = conn.get\_collection("c-c0a2c223-e377-4625-94bf-910501c2a31c")

videos = collection.list\_videos()

\#Stock Market Ticker 01

video = collection.get\_video("m-z-0194c27c-f30c-7803-b2ca-8f1026c940a2")

## 4\. Working with Scene Collections and Scene Indexes (Videos)

You can list and retrieve scene collections and scene indexes for a public video.

public\_collection = conn.get\_collection("PUBLIC\_COLLECTION\_ID")

video = public\_collection.get\_video("VIDEO\_ID")

\# List and retrieve scene collections

scene\_collections = video.list\_scene\_collection()

scene\_collection = video.get\_scene\_collection(

scene\_collections\[0\].get("scene\_collection\_id")

)

\# List and retrieve scene indexes

scene\_indexes = video.list\_scene\_index()

scene\_index = video.get\_scene\_index(scene\_indexes\[0\].get("scene\_index\_id"))

Sample Code:

\# VideoDB's OCR Benchmark Public Collection

collection = conn.get\_collection("c-c0a2c223-e377-4625-94bf-910501c2a31c")

\# Stock Market Ticker 01

video = collection.get\_video("m-z-0194c27c-f30c-7803-b2ca-8f1026c940a2")

scene\_collections = video.list\_scene\_collection()

scene\_collection = video.get\_scene\_collection(

scene\_collections\[0\].get("scene\_collection\_id")

)

## Upcoming Updates:

Copy function to copy the whole collection with it’s indexes.

Search using existing spoken and visual indexes on public collections.

Get transcription of spoken indexed videos.

Want to print your doc?

This is not the way.

![](https://cdn.coda.io/assets/6ee7d0564a67/img/import_google_docs.png)

Try clicking the ⋯ next to your doc name or using a keyboard shortcut (

CtrlP

) instead.


---

# Callback Details [Source Link](https://docs.videodb.io/callback-details-66)

VideoDB Documentation

Pages

[Welcome to VideoDB Docs](https://docs.videodb.io/)

[Quick Start Guide](https://docs.videodb.io/quick-start-guide-38)

[How Accurate is Your Search?](https://docs.videodb.io/how-accurate-is-your-search-88)

[Video Indexing Guide](https://docs.videodb.io/video-indexing-guide-101)

[Semantic Search](https://docs.videodb.io/semantic-search-89)

[Collections](https://docs.videodb.io/collections-68)

[Public Collections](https://docs.videodb.io/public-collections-102)

[Callback Details](https://docs.videodb.io/callback-details-66)

[Ref: Subtitle Styles](https://docs.videodb.io/ref-subtitle-styles-57)

[Language Support](https://docs.videodb.io/language-support-79)

[Guide: Subtitles](https://docs.videodb.io/guide-subtitles-73)

[Visual Search and Indexing](https://docs.videodb.io/visual-search-and-indexing-80)

[Scene Extraction Algorithms](https://docs.videodb.io/scene-extraction-algorithms-84)

[Custom Annotations](https://docs.videodb.io/custom-annotations-81)

[Scene-Level Metadata: Smarter Video Search & Retrieval](https://docs.videodb.io/scene-level-metadata-smarter-video-search-retrieval-107)

[Advanced Visual Search Pipelines](https://docs.videodb.io/advanced-visual-search-pipelines-82)

[Playground for Scene Extractions](https://docs.videodb.io/playground-for-scene-extractions-83)

[Deep Dive into Prompt Engineering : Mastering Video Scene Indexing](https://docs.videodb.io/deep-dive-into-prompt-engineering-mastering-video-scene-indexing-93)

[Multimodal Search](https://docs.videodb.io/multimodal-search-90)

[Multimodal Search: Quickstart](https://docs.videodb.io/multimodal-search-quickstart-91)

[Conference Slide Scraper with VideoDB](https://docs.videodb.io/conference-slide-scraper-with-videodb-92)

[Dynamic Video Streams](https://docs.videodb.io/dynamic-video-streams-44)

[Ref: TextAsset](https://docs.videodb.io/ref-textasset-74)

[Guide : TextAsset](https://docs.videodb.io/guide-textasset-75)

[Director - Video Agent Framework](https://docs.videodb.io/director-video-agent-framework-98)

[Agent Creation Playbook](https://docs.videodb.io/agent-creation-playbook-103)

[How I Built a CRM-integrated Sales Assistant Agent in 1 Hour](https://docs.videodb.io/how-i-built-a-crm-integrated-sales-assistant-agent-in-1-hour-106)

[Make Your Video Sound Studio Quality with Voice Cloning](https://docs.videodb.io/make-your-video-sound-studio-quality-with-voice-cloning-105)

[Setup Director Locally](https://docs.videodb.io/setup-director-locally-104)

[Open Source Tools](https://docs.videodb.io/open-source-tools-94)

[LlamaIndex VideoDB Retriever](https://docs.videodb.io/llamaindex-videodb-retriever-58)

[PromptClip: Use Power of LLM to Create Clips](https://docs.videodb.io/promptclip-use-power-of-llm-to-create-clips-52)

[StreamRAG: Connect ChatGPT to VideoDB](https://docs.videodb.io/streamrag-connect-chatgpt-to-videodb-43)

[Examples and Tutorials](https://docs.videodb.io/examples-and-tutorials-35)

[Dubbing - Replace Soundtrack with New Audio](https://docs.videodb.io/dubbing-replace-soundtrack-with-new-audio-49)

[Beep curse words in real-time](https://docs.videodb.io/beep-curse-words-in-real-time-53)

[Remove Unwanted Content from videos](https://docs.videodb.io/remove-unwanted-content-from-videos-5)

[Instant Clips of Your Favorite Characters](https://docs.videodb.io/instant-clips-of-your-favorite-characters-3)

[Insert Dynamic Ads in real-time](https://docs.videodb.io/insert-dynamic-ads-in-real-time-7)

[Adding Brand Elements with VideoDB](https://docs.videodb.io/adding-brand-elements-with-videodb-76)

[Revolutionize Video Editing with VideoDb: Effortless Ad Placement and Seamless Video Integration](https://docs.videodb.io/revolutionize-video-editing-with-videodb-effortless-ad-placement-8)

[Eleven Labs x VideoDB: Adding AI Generated voiceovers to silent footage](https://docs.videodb.io/eleven-labs-x-videodb-adding-ai-generated-voiceovers-to-silent-f-59)

[Elevating Trailers with Automated Narration](https://docs.videodb.io/elevating-trailers-with-automated-narration-60)

[Add Intro/Outro to Videos](https://docs.videodb.io/add-intro-outro-to-videos-61)

[Enhancing Video Captions with VideoDB Subtitle Styling](https://docs.videodb.io/enhancing-video-captions-with-videodb-subtitle-styling-62)

[Audio overlay + Video + Timeline](https://docs.videodb.io/audio-overlay-video-timeline-63)

[Building Dynamic Video Streams with VideoDB: Integrating Custom Data and APIs](https://docs.videodb.io/building-dynamic-video-streams-with-videodb-integrating-custom-d-85)

[Adding AI Generated Voiceovers with VideoDB and LOVO](https://docs.videodb.io/adding-ai-generated-voiceovers-with-videodb-and-lovo-70)

[AI Generated Ad Films for Product Videography: Wellsaid, Open AI & VideoDB](https://docs.videodb.io/ai-generated-ad-films-for-product-videography-wellsaid-open-ai-v-71)

[Fun with Keyword Search](https://docs.videodb.io/fun-with-keyword-search-77)

[AWS Rekognition and VideoDB - Intelligent Video Clips](https://docs.videodb.io/aws-rekognition-and-videodb-intelligent-video-clips-4)

[AWS Rekognition and VideoDB - Effortlessly Remove Inappropriate Content from Video](https://docs.videodb.io/aws-rekognition-and-videodb-effortlessly-remove-inappropriate-co-6)

[Overlay a Word-Counter on Video Stream](https://docs.videodb.io/overlay-a-word-counter-on-video-stream-86)

[Generate Automated Video Outputs with Text Prompts \| DALL-E + ElevenLabs + OpenAI + VideoDB](https://docs.videodb.io/generate-automated-video-outputs-with-text-prompts-dall-e-eleven-87)

[Edge of Knowledge](https://docs.videodb.io/edge-of-knowledge-10)

[Building Intelligent Machines](https://docs.videodb.io/building-intelligent-machines-16)

[Part 1 - Define Intelligence](https://docs.videodb.io/part-1-define-intelligence-17)

[Part 2 - Observe and Respond](https://docs.videodb.io/part-2-observe-and-respond-18)

[Part 3 - Training a Model](https://docs.videodb.io/part-3-training-a-model-19)

[Society of Machines](https://docs.videodb.io/society-of-machines-20)

[Society of Machines](https://docs.videodb.io/society-of-machines-23)

[Autonomy - Do we have the choice?](https://docs.videodb.io/autonomy-do-we-have-the-choice-21)

[Emergence - An Intelligence of the collective](https://docs.videodb.io/emergence-an-intelligence-of-the-collective-22)

[Drafts](https://docs.videodb.io/drafts-24)

[From Language Models to World Models: The Next Frontier in AI](https://docs.videodb.io/from-language-models-to-world-models-the-next-frontier-in-ai-65)

[The Future Series](https://docs.videodb.io/the-future-series-78)

[Building World's First Video Database](https://docs.videodb.io/building-worlds-first-video-database-25)

[Multimedia: From MP3/MP4 to the Future with VideoDB](https://docs.videodb.io/multimedia-from-mp3-mp4-to-the-future-with-videodb-26)

[Introducing VideoDB: The Pinnacle of Synchronized Video Streaming for the Modern Web](https://docs.videodb.io/introducing-videodb-the-pinnacle-of-synchronized-video-streaming-27)

[Dynamic Video Streams](https://docs.videodb.io/dynamic-video-streams-50)

[Why do we need a Video Database Now?](https://docs.videodb.io/why-do-we-need-a-video-database-now-41)

[What's a Video Database ?](https://docs.videodb.io/whats-a-video-database-36)

[Enhancing AI-Driven Multimedia Applications](https://docs.videodb.io/enhancing-ai-driven-multimedia-applications-37)

[Misalignment of Today's Web](https://docs.videodb.io/misalignment-of-todays-web-67)

[Beyond Traditional Video Infrastructure](https://docs.videodb.io/beyond-traditional-video-infrastructure-28)

[Research Grants](https://docs.videodb.io/research-grants-96)

[Team](https://docs.videodb.io/team-46)

[Internship: Build the Future of AI-Powered Video Infrastructure](https://docs.videodb.io/internship-build-the-future-of-ai-powered-video-infrastructure-97)

[Ashutosh Trivedi](https://docs.videodb.io/ashutosh-trivedi-32)

[Playlists](https://docs.videodb.io/playlists-33)

[Talks - Solving Logical Puzzles with Natural Language Processing - PyCon India 2015](https://docs.videodb.io/talks-solving-logical-puzzles-with-natural-language-processing-p-34)

[Ashish](https://docs.videodb.io/ashish-45)

[Shivani Desai](https://docs.videodb.io/shivani-desai-48)

[Gaurav Tyagi](https://docs.videodb.io/gaurav-tyagi-51)

[Rohit Garg](https://docs.videodb.io/rohit-garg-64)

[Customer Love](https://docs.videodb.io/customer-love-42)

[Temp Doc](https://docs.videodb.io/temp-doc-54)

Quick Start Guide

# Callback Details

# Upload

You can pass callback url in upload function. Here are the details of callback responses.

### 👍🏼 Successful Video Upload

### 👍🏼 Successful Audio Upload

### 👍🏼 Successful Image upload

## Errors in Upload

If the uploaded file is corrupted 👎🏻

### Invalid file 👎🏻

If the file is Invalid or wrong media\_type is passed in the upload function.

Upload function supported media\_type is available in the class MediaType which are 👉🏼 \["video", "image", "audio"\]

### Issue with Download 🔴

If the download link is incorrect/ private or our servers are not able to download file from the link.

⁠

# Index spoken words

Indexing a video is an asynchronous job. We do provide progress bar on our python sdk for developer experience. But it’s only good for communicating the progress on Jupyter or colab notebooks.

⁠

When you move it to to production, you can use callbacks for your backend workflows. Pass callback url while calling the function

### Successfully Indexed 👍🏼

### Error in Indexing job 👎🏻

⁠

# Index scenes

Similar to other indexing operations scene index is also an async job. You can pass callback in the function.

### 👍🏼 Successfully Indexed

### 👎🏻 Error in Indexing

# Extract Scenes

### 👍🏼 Successfully extracted

### 👎🏻 Error in Extracting

Want to print your doc?

This is not the way.

Try clicking the ⋯ next to your doc name or using a keyboard shortcut (

CtrlP

) instead.


---

# Ref: Subtitle Styles [Source Link](https://docs.videodb.io/ref-subtitle-styles-57)

VideoDB Documentation

Pages

[Welcome to VideoDB Docs](https://docs.videodb.io/)

[Quick Start Guide](https://docs.videodb.io/quick-start-guide-38)

[How Accurate is Your Search?](https://docs.videodb.io/how-accurate-is-your-search-88)

[Video Indexing Guide](https://docs.videodb.io/video-indexing-guide-101)

[Semantic Search](https://docs.videodb.io/semantic-search-89)

[Collections](https://docs.videodb.io/collections-68)

[Public Collections](https://docs.videodb.io/public-collections-102)

[Callback Details](https://docs.videodb.io/callback-details-66)

[Ref: Subtitle Styles](https://docs.videodb.io/ref-subtitle-styles-57)

[Language Support](https://docs.videodb.io/language-support-79)

[Guide: Subtitles](https://docs.videodb.io/guide-subtitles-73)

[Visual Search and Indexing](https://docs.videodb.io/visual-search-and-indexing-80)

[Scene Extraction Algorithms](https://docs.videodb.io/scene-extraction-algorithms-84)

[Custom Annotations](https://docs.videodb.io/custom-annotations-81)

[Scene-Level Metadata: Smarter Video Search & Retrieval](https://docs.videodb.io/scene-level-metadata-smarter-video-search-retrieval-107)

[Advanced Visual Search Pipelines](https://docs.videodb.io/advanced-visual-search-pipelines-82)

[Playground for Scene Extractions](https://docs.videodb.io/playground-for-scene-extractions-83)

[Deep Dive into Prompt Engineering : Mastering Video Scene Indexing](https://docs.videodb.io/deep-dive-into-prompt-engineering-mastering-video-scene-indexing-93)

[Multimodal Search](https://docs.videodb.io/multimodal-search-90)

[Multimodal Search: Quickstart](https://docs.videodb.io/multimodal-search-quickstart-91)

[Conference Slide Scraper with VideoDB](https://docs.videodb.io/conference-slide-scraper-with-videodb-92)

[Dynamic Video Streams](https://docs.videodb.io/dynamic-video-streams-44)

[Ref: TextAsset](https://docs.videodb.io/ref-textasset-74)

[Guide : TextAsset](https://docs.videodb.io/guide-textasset-75)

[Director - Video Agent Framework](https://docs.videodb.io/director-video-agent-framework-98)

[Agent Creation Playbook](https://docs.videodb.io/agent-creation-playbook-103)

[How I Built a CRM-integrated Sales Assistant Agent in 1 Hour](https://docs.videodb.io/how-i-built-a-crm-integrated-sales-assistant-agent-in-1-hour-106)

[Make Your Video Sound Studio Quality with Voice Cloning](https://docs.videodb.io/make-your-video-sound-studio-quality-with-voice-cloning-105)

[Setup Director Locally](https://docs.videodb.io/setup-director-locally-104)

[Open Source Tools](https://docs.videodb.io/open-source-tools-94)

[LlamaIndex VideoDB Retriever](https://docs.videodb.io/llamaindex-videodb-retriever-58)

[PromptClip: Use Power of LLM to Create Clips](https://docs.videodb.io/promptclip-use-power-of-llm-to-create-clips-52)

[StreamRAG: Connect ChatGPT to VideoDB](https://docs.videodb.io/streamrag-connect-chatgpt-to-videodb-43)

[Examples and Tutorials](https://docs.videodb.io/examples-and-tutorials-35)

[Dubbing - Replace Soundtrack with New Audio](https://docs.videodb.io/dubbing-replace-soundtrack-with-new-audio-49)

[Beep curse words in real-time](https://docs.videodb.io/beep-curse-words-in-real-time-53)

[Remove Unwanted Content from videos](https://docs.videodb.io/remove-unwanted-content-from-videos-5)

[Instant Clips of Your Favorite Characters](https://docs.videodb.io/instant-clips-of-your-favorite-characters-3)

[Insert Dynamic Ads in real-time](https://docs.videodb.io/insert-dynamic-ads-in-real-time-7)

[Adding Brand Elements with VideoDB](https://docs.videodb.io/adding-brand-elements-with-videodb-76)

[Revolutionize Video Editing with VideoDb: Effortless Ad Placement and Seamless Video Integration](https://docs.videodb.io/revolutionize-video-editing-with-videodb-effortless-ad-placement-8)

[Eleven Labs x VideoDB: Adding AI Generated voiceovers to silent footage](https://docs.videodb.io/eleven-labs-x-videodb-adding-ai-generated-voiceovers-to-silent-f-59)

[Elevating Trailers with Automated Narration](https://docs.videodb.io/elevating-trailers-with-automated-narration-60)

[Add Intro/Outro to Videos](https://docs.videodb.io/add-intro-outro-to-videos-61)

[Enhancing Video Captions with VideoDB Subtitle Styling](https://docs.videodb.io/enhancing-video-captions-with-videodb-subtitle-styling-62)

[Audio overlay + Video + Timeline](https://docs.videodb.io/audio-overlay-video-timeline-63)

[Building Dynamic Video Streams with VideoDB: Integrating Custom Data and APIs](https://docs.videodb.io/building-dynamic-video-streams-with-videodb-integrating-custom-d-85)

[Adding AI Generated Voiceovers with VideoDB and LOVO](https://docs.videodb.io/adding-ai-generated-voiceovers-with-videodb-and-lovo-70)

[AI Generated Ad Films for Product Videography: Wellsaid, Open AI & VideoDB](https://docs.videodb.io/ai-generated-ad-films-for-product-videography-wellsaid-open-ai-v-71)

[Fun with Keyword Search](https://docs.videodb.io/fun-with-keyword-search-77)

[AWS Rekognition and VideoDB - Intelligent Video Clips](https://docs.videodb.io/aws-rekognition-and-videodb-intelligent-video-clips-4)

[AWS Rekognition and VideoDB - Effortlessly Remove Inappropriate Content from Video](https://docs.videodb.io/aws-rekognition-and-videodb-effortlessly-remove-inappropriate-co-6)

[Overlay a Word-Counter on Video Stream](https://docs.videodb.io/overlay-a-word-counter-on-video-stream-86)

[Generate Automated Video Outputs with Text Prompts \| DALL-E + ElevenLabs + OpenAI + VideoDB](https://docs.videodb.io/generate-automated-video-outputs-with-text-prompts-dall-e-eleven-87)

[Edge of Knowledge](https://docs.videodb.io/edge-of-knowledge-10)

[Building Intelligent Machines](https://docs.videodb.io/building-intelligent-machines-16)

[Part 1 - Define Intelligence](https://docs.videodb.io/part-1-define-intelligence-17)

[Part 2 - Observe and Respond](https://docs.videodb.io/part-2-observe-and-respond-18)

[Part 3 - Training a Model](https://docs.videodb.io/part-3-training-a-model-19)

[Society of Machines](https://docs.videodb.io/society-of-machines-20)

[Society of Machines](https://docs.videodb.io/society-of-machines-23)

[Autonomy - Do we have the choice?](https://docs.videodb.io/autonomy-do-we-have-the-choice-21)

[Emergence - An Intelligence of the collective](https://docs.videodb.io/emergence-an-intelligence-of-the-collective-22)

[Drafts](https://docs.videodb.io/drafts-24)

[From Language Models to World Models: The Next Frontier in AI](https://docs.videodb.io/from-language-models-to-world-models-the-next-frontier-in-ai-65)

[The Future Series](https://docs.videodb.io/the-future-series-78)

[Building World's First Video Database](https://docs.videodb.io/building-worlds-first-video-database-25)

[Multimedia: From MP3/MP4 to the Future with VideoDB](https://docs.videodb.io/multimedia-from-mp3-mp4-to-the-future-with-videodb-26)

[Introducing VideoDB: The Pinnacle of Synchronized Video Streaming for the Modern Web](https://docs.videodb.io/introducing-videodb-the-pinnacle-of-synchronized-video-streaming-27)

[Dynamic Video Streams](https://docs.videodb.io/dynamic-video-streams-50)

[Why do we need a Video Database Now?](https://docs.videodb.io/why-do-we-need-a-video-database-now-41)

[What's a Video Database ?](https://docs.videodb.io/whats-a-video-database-36)

[Enhancing AI-Driven Multimedia Applications](https://docs.videodb.io/enhancing-ai-driven-multimedia-applications-37)

[Misalignment of Today's Web](https://docs.videodb.io/misalignment-of-todays-web-67)

[Beyond Traditional Video Infrastructure](https://docs.videodb.io/beyond-traditional-video-infrastructure-28)

[Research Grants](https://docs.videodb.io/research-grants-96)

[Team](https://docs.videodb.io/team-46)

[Internship: Build the Future of AI-Powered Video Infrastructure](https://docs.videodb.io/internship-build-the-future-of-ai-powered-video-infrastructure-97)

[Ashutosh Trivedi](https://docs.videodb.io/ashutosh-trivedi-32)

[Playlists](https://docs.videodb.io/playlists-33)

[Talks - Solving Logical Puzzles with Natural Language Processing - PyCon India 2015](https://docs.videodb.io/talks-solving-logical-puzzles-with-natural-language-processing-p-34)

[Ashish](https://docs.videodb.io/ashish-45)

[Shivani Desai](https://docs.videodb.io/shivani-desai-48)

[Gaurav Tyagi](https://docs.videodb.io/gaurav-tyagi-51)

[Rohit Garg](https://docs.videodb.io/rohit-garg-64)

[Customer Love](https://docs.videodb.io/customer-love-42)

[Temp Doc](https://docs.videodb.io/temp-doc-54)

Quick Start Guide

# Ref: Subtitle Styles

video.add\_subtitle(SubtitleStyle())function supports many parameters for styling your captions or subtitles according to your brand and guidelines. You can create your own

Typography and Style

Color and Effects

Positioning and Margins

Text Transformation

Borders and Shadow,

This document provides an API Reference to the parameters of SubtitleStylefunction.

Checkout

[Guide: Subtitles](https://docs.videodb.io/guide-subtitles-73)

to dive deep into the outputs of these parameters

## Import

Import SubtitleStyle from VideoDB module

from videodb import SubtitleStyle, connect

conn =connect()

coll = conn.get\_collection()

video = coll.get\_video("MY\_VIDEO\_ID")

video.add\_subtitle(

SubtitleStyle(

font\_name=<>,

font\_size=<>,

spacing=<>,

....

....

)

)

## SubtitleStyle

This function supports following parameters for styling 👇

### font\_name

The name of the font to use for the subtitles.

Default: "Arial"

Type:str

Checkout List of

[Supported Fonts](https://docs.videodb.io/ref-subtitle-styles-57)

### font\_size

The size of the subtitle text in points.

Default: 18

Type:float

### primary\_colour

The color of the main subtitle text in &HBBGGRR or&HAABBGGRR format. Checkout

[Color Format](https://docs.videodb.io/ref-subtitle-styles-57)

for the details.

Default: "&H00FFFFFF" (white)

Type:str

### secondary\_colour

The color used for secondary effects like karaoke

Default:"&H000000FF"(red)

Type:str

Checkout

[Color Format](https://docs.videodb.io/ref-subtitle-styles-57)

for the format details.

### outline\_colour

The color of the text outline.

Default: "&H00000000" (black)

Type:str

Checkout

[Color Format](https://docs.videodb.io/ref-subtitle-styles-57)

for the format details.

### back\_colour

The background color of the subtitle box

Default: "&H00000000" (black)

Type:str

Checkout

[Color Format](https://docs.videodb.io/ref-subtitle-styles-57)

for the format details.

### bold

Indicates if the subtitle text is bold.

Default: False

Type: bool

### italic

Indicates if the subtitle text is italicized.

Default: False

Type: bool

### underline

Indicates if the subtitle text is underlined.

Default: False

Type: bool

### strike\_out

Indicates if the subtitle text has a strikethrough.

Default: False

Type: bool

### scale\_x

The horizontal scale of the subtitle text in percentage.

Default: 1.0(100%, no scaling)

Type:float

### scale\_y

The vertical scale of the subtitle text in percentage.

Default: 1.0 (100%, no scaling)

Type:float

### spacing

Space between characters in pixels.

Default: 0

Type:float

### angle

The rotation angle of the subtitle text in degrees.

Default: 0 (no rotation)

Type:float

### border\_style

The style of the border around the text

Default:SubtitleBorderStyle.outline

Type:int orSubtitleBorderStyle

This field accepts following value.

SubtitleBorderStyle.no\_borderor1

SubtitleBorderStyle.opaque\_box or3

SubtitleBorderStyle.outline or4

Usage:

from videodb import SubtitleStyle,SubtitleBorderStyle, connect

conn =connect()

coll = conn.get\_collection()

video = coll.get\_video("MY\_VIDEO\_ID")

video.add\_subtitle(

SubtitleStyle(

border\_style=SubtitleBorderStyle.outline

)

)

### outline

The width (px) of the outline around the text.

Default: 1.0(px)

Type:float

### shadow

The depth of the shadow behind the text in pixels.

Default: 0.0

Type:float

### alignment

The position of the subtitle text on the screen, typically an enumerated type following the SSA/ASS standard.

Default: SubtitleAlignment.bottom\_center

Type:SubtitleAlignmentor int

This field accepts following value.

SubtitleAlignment.bottom\_leftor1

SubtitleAlignment.bottom\_center or2

SubtitleAlignment.bottom\_rightor 3

SubtitleAlignment.middle\_left or 8, 9

SubtitleAlignment.middle\_centeror10

SubtitleAlignment.middle\_rightor 11

SubtitleAlignment.top\_leftor4,5

SubtitleAlignment.top\_center or6

SubtitleAlignment.top\_rightor7

Usage:

from videodb import SubtitleStyle, SubtitleAlignment, connect

conn =connect()

coll = conn.get\_collection()

video = coll.get\_video("MY\_VIDEO\_ID")

video.add\_subtitle(

SubtitleStyle(

alignment=SubtitleAlignment.middle\_center

)

)

### margin\_l

The left margin in pixels.

Default: 10

Type:int

### margin\_r

The right margin in pixels.

Default: 10

Type:int

### margin\_v

The vertical margin (both top and bottom) in pixels.

Default: 10

Type:int

## Color Format

SubtitleStyle accepts colors in the &HBBGGRR hexadecimal format, where the sequence represents the blue, green, and red components,

&H prefix is required in this color format.

And when transparency is needed, an alpha value is placed at the beginning, yielding &HAABBGGRR.

## Supported Fonts

Currently VideoDB supports following Fonts 👇

​

​

Checkout

[Guide: Subtitles](https://docs.videodb.io/guide-subtitles-73)

to dive deep into the outputs of these parameters.

Import

SubtitleStyle

font\_name

font\_size

primary\_colour

secondary\_colour

outline\_colour

back\_colour

bold

italic

underline

strike\_out

scale\_x

scale\_y

spacing

angle

border\_style

outline

shadow

alignment

margin\_l

margin\_r

margin\_v

Color Format

Supported Fonts

Want to print your doc?

This is not the way.

Try clicking the ⋯ next to your doc name or using a keyboard shortcut (

CtrlP

) instead.


---

# Language Support [Source Link](https://docs.videodb.io/language-support-79)

VideoDB Documentation

Pages

Welcome to VideoDB Docs
Quick Start Guide
How Accurate is Your Search?
Video Indexing Guide
Semantic Search
Collections
Public Collections
Callback Details
Ref: Subtitle Styles
Language Support
Guide: Subtitles
Visual Search and Indexing
Scene Extraction Algorithms
Custom Annotations
Scene-Level Metadata: Smarter Video Search & Retrieval
Advanced Visual Search Pipelines
Playground for Scene Extractions
Deep Dive into Prompt Engineering : Mastering Video Scene Indexing
Multimodal Search
Multimodal Search: Quickstart
Conference Slide Scraper with VideoDB
Dynamic Video Streams
Ref: TextAsset
Guide : TextAsset
Director - Video Agent Framework
Agent Creation Playbook
How I Built a CRM-integrated Sales Assistant Agent in 1 Hour
Make Your Video Sound Studio Quality with Voice Cloning
Setup Director Locally
Open Source Tools
LlamaIndex VideoDB Retriever
PromptClip: Use Power of LLM to Create Clips
StreamRAG: Connect ChatGPT to VideoDB
Examples and Tutorials
Dubbing - Replace Soundtrack with New Audio
Beep curse words in real-time
Remove Unwanted Content from videos
Instant Clips of Your Favorite Characters
Insert Dynamic Ads in real-time
Adding Brand Elements with VideoDB
Revolutionize Video Editing with VideoDb: Effortless Ad Placement and Seamless Video Integration
Eleven Labs x VideoDB: Adding AI Generated voiceovers to silent footage
Elevating Trailers with Automated Narration
Add Intro/Outro to Videos
Enhancing Video Captions with VideoDB Subtitle Styling
Audio overlay + Video + Timeline
Building Dynamic Video Streams with VideoDB: Integrating Custom Data and APIs
Adding AI Generated Voiceovers with VideoDB and LOVO
AI Generated Ad Films for Product Videography: Wellsaid, Open AI & VideoDB
Fun with Keyword Search
AWS Rekognition and VideoDB - Intelligent Video Clips
AWS Rekognition and VideoDB - Effortlessly Remove Inappropriate Content from Video
Overlay a Word-Counter on Video Stream
Generate Automated Video Outputs with Text Prompts \| DALL-E + ElevenLabs + OpenAI + VideoDB
Edge of Knowledge
Building Intelligent Machines
Part 1 - Define Intelligence
Part 2 - Observe and Respond
Part 3 - Training a Model
Society of Machines
Society of Machines
Autonomy - Do we have the choice?
Emergence - An Intelligence of the collective
Drafts
From Language Models to World Models: The Next Frontier in AI
The Future Series
Building World's First Video Database
Multimedia: From MP3/MP4 to the Future with VideoDB
Introducing VideoDB: The Pinnacle of Synchronized Video Streaming for the Modern Web
Dynamic Video Streams
Why do we need a Video Database Now?
What's a Video Database ?
Enhancing AI-Driven Multimedia Applications
Misalignment of Today's Web
Beyond Traditional Video Infrastructure
Research Grants
Team
Internship: Build the Future of AI-Powered Video Infrastructure
Ashutosh Trivedi
Playlists
Talks - Solving Logical Puzzles with Natural Language Processing - PyCon India 2015
Ashish
Shivani Desai
Gaurav Tyagi
Rohit Garg
Customer Love
Temp Doc

Quick Start Guide

# Language Support

VideoDB supports multiple languages for indexing the spoken content in the videos. You can just pass the language code in indexing function index\_spoken\_words

hindi\_video.index\_spoken\_words(language\_code="hi")

### Auto detect languages:

English , Spanish , French, German, Italian, Portuguese and Dutch would be auto detected, you can skip passing the language code while indexing.

### Supported Languages

Here are the supported language and their language\_code

{

"Global English": "en",

"Australian English": "en\_au",

"British English": "en\_uk",

"American English": "en\_us",

"Spanish": "es",

"French": "fr",

"German": "de",

"Italian": "it",

"Portuguese": "pt",

"Dutch": "nl",

"Hindi": "hi",

"Japanese": "ja",

"Chinese": "zh",

"Finnish": "fi",

"Korean": "ko",

"Polish": "pl",

"Russian": "ru",

"Turkish": "tr",

"Ukrainian": "uk",

"Vietnamese": "vi",

}

Want to print your doc?

This is not the way.

Try clicking the ⋯ next to your doc name or using a keyboard shortcut (CtrlP) instead.


---

# Guide: Subtitles [Source Link](https://docs.videodb.io/guide-subtitles-73)

VideoDB Documentation

Pages

[Welcome to VideoDB Docs](https://docs.videodb.io/)

[Quick Start Guide](https://docs.videodb.io/quick-start-guide-38)

[How Accurate is Your Search?](https://docs.videodb.io/how-accurate-is-your-search-88)

[Video Indexing Guide](https://docs.videodb.io/video-indexing-guide-101)

[Semantic Search](https://docs.videodb.io/semantic-search-89)

[Collections](https://docs.videodb.io/collections-68)

[Public Collections](https://docs.videodb.io/public-collections-102)

[Callback Details](https://docs.videodb.io/callback-details-66)

[Ref: Subtitle Styles](https://docs.videodb.io/ref-subtitle-styles-57)

[Language Support](https://docs.videodb.io/language-support-79)

[Guide: Subtitles](https://docs.videodb.io/guide-subtitles-73)

[Visual Search and Indexing](https://docs.videodb.io/visual-search-and-indexing-80)

[Scene Extraction Algorithms](https://docs.videodb.io/scene-extraction-algorithms-84)

[Custom Annotations](https://docs.videodb.io/custom-annotations-81)

[Scene-Level Metadata: Smarter Video Search & Retrieval](https://docs.videodb.io/scene-level-metadata-smarter-video-search-retrieval-107)

[Advanced Visual Search Pipelines](https://docs.videodb.io/advanced-visual-search-pipelines-82)

[Playground for Scene Extractions](https://docs.videodb.io/playground-for-scene-extractions-83)

[Deep Dive into Prompt Engineering : Mastering Video Scene Indexing](https://docs.videodb.io/deep-dive-into-prompt-engineering-mastering-video-scene-indexing-93)

[Multimodal Search](https://docs.videodb.io/multimodal-search-90)

[Multimodal Search: Quickstart](https://docs.videodb.io/multimodal-search-quickstart-91)

[Conference Slide Scraper with VideoDB](https://docs.videodb.io/conference-slide-scraper-with-videodb-92)

[Dynamic Video Streams](https://docs.videodb.io/dynamic-video-streams-44)

[Ref: TextAsset](https://docs.videodb.io/ref-textasset-74)

[Guide : TextAsset](https://docs.videodb.io/guide-textasset-75)

[Director - Video Agent Framework](https://docs.videodb.io/director-video-agent-framework-98)

[Agent Creation Playbook](https://docs.videodb.io/agent-creation-playbook-103)

[How I Built a CRM-integrated Sales Assistant Agent in 1 Hour](https://docs.videodb.io/how-i-built-a-crm-integrated-sales-assistant-agent-in-1-hour-106)

[Make Your Video Sound Studio Quality with Voice Cloning](https://docs.videodb.io/make-your-video-sound-studio-quality-with-voice-cloning-105)

[Setup Director Locally](https://docs.videodb.io/setup-director-locally-104)

[Open Source Tools](https://docs.videodb.io/open-source-tools-94)

[LlamaIndex VideoDB Retriever](https://docs.videodb.io/llamaindex-videodb-retriever-58)

[PromptClip: Use Power of LLM to Create Clips](https://docs.videodb.io/promptclip-use-power-of-llm-to-create-clips-52)

[StreamRAG: Connect ChatGPT to VideoDB](https://docs.videodb.io/streamrag-connect-chatgpt-to-videodb-43)

[Examples and Tutorials](https://docs.videodb.io/examples-and-tutorials-35)

[Dubbing - Replace Soundtrack with New Audio](https://docs.videodb.io/dubbing-replace-soundtrack-with-new-audio-49)

[Beep curse words in real-time](https://docs.videodb.io/beep-curse-words-in-real-time-53)

[Remove Unwanted Content from videos](https://docs.videodb.io/remove-unwanted-content-from-videos-5)

[Instant Clips of Your Favorite Characters](https://docs.videodb.io/instant-clips-of-your-favorite-characters-3)

[Insert Dynamic Ads in real-time](https://docs.videodb.io/insert-dynamic-ads-in-real-time-7)

[Adding Brand Elements with VideoDB](https://docs.videodb.io/adding-brand-elements-with-videodb-76)

[Revolutionize Video Editing with VideoDb: Effortless Ad Placement and Seamless Video Integration](https://docs.videodb.io/revolutionize-video-editing-with-videodb-effortless-ad-placement-8)

[Eleven Labs x VideoDB: Adding AI Generated voiceovers to silent footage](https://docs.videodb.io/eleven-labs-x-videodb-adding-ai-generated-voiceovers-to-silent-f-59)

[Elevating Trailers with Automated Narration](https://docs.videodb.io/elevating-trailers-with-automated-narration-60)

[Add Intro/Outro to Videos](https://docs.videodb.io/add-intro-outro-to-videos-61)

[Enhancing Video Captions with VideoDB Subtitle Styling](https://docs.videodb.io/enhancing-video-captions-with-videodb-subtitle-styling-62)

[Audio overlay + Video + Timeline](https://docs.videodb.io/audio-overlay-video-timeline-63)

[Building Dynamic Video Streams with VideoDB: Integrating Custom Data and APIs](https://docs.videodb.io/building-dynamic-video-streams-with-videodb-integrating-custom-d-85)

[Adding AI Generated Voiceovers with VideoDB and LOVO](https://docs.videodb.io/adding-ai-generated-voiceovers-with-videodb-and-lovo-70)

[AI Generated Ad Films for Product Videography: Wellsaid, Open AI & VideoDB](https://docs.videodb.io/ai-generated-ad-films-for-product-videography-wellsaid-open-ai-v-71)

[Fun with Keyword Search](https://docs.videodb.io/fun-with-keyword-search-77)

[AWS Rekognition and VideoDB - Intelligent Video Clips](https://docs.videodb.io/aws-rekognition-and-videodb-intelligent-video-clips-4)

[AWS Rekognition and VideoDB - Effortlessly Remove Inappropriate Content from Video](https://docs.videodb.io/aws-rekognition-and-videodb-effortlessly-remove-inappropriate-co-6)

[Overlay a Word-Counter on Video Stream](https://docs.videodb.io/overlay-a-word-counter-on-video-stream-86)

[Generate Automated Video Outputs with Text Prompts \| DALL-E + ElevenLabs + OpenAI + VideoDB](https://docs.videodb.io/generate-automated-video-outputs-with-text-prompts-dall-e-eleven-87)

[Edge of Knowledge](https://docs.videodb.io/edge-of-knowledge-10)

[Building Intelligent Machines](https://docs.videodb.io/building-intelligent-machines-16)

[Part 1 - Define Intelligence](https://docs.videodb.io/part-1-define-intelligence-17)

[Part 2 - Observe and Respond](https://docs.videodb.io/part-2-observe-and-respond-18)

[Part 3 - Training a Model](https://docs.videodb.io/part-3-training-a-model-19)

[Society of Machines](https://docs.videodb.io/society-of-machines-20)

[Society of Machines](https://docs.videodb.io/society-of-machines-23)

[Autonomy - Do we have the choice?](https://docs.videodb.io/autonomy-do-we-have-the-choice-21)

[Emergence - An Intelligence of the collective](https://docs.videodb.io/emergence-an-intelligence-of-the-collective-22)

[Drafts](https://docs.videodb.io/drafts-24)

[From Language Models to World Models: The Next Frontier in AI](https://docs.videodb.io/from-language-models-to-world-models-the-next-frontier-in-ai-65)

[The Future Series](https://docs.videodb.io/the-future-series-78)

[Building World's First Video Database](https://docs.videodb.io/building-worlds-first-video-database-25)

[Multimedia: From MP3/MP4 to the Future with VideoDB](https://docs.videodb.io/multimedia-from-mp3-mp4-to-the-future-with-videodb-26)

[Introducing VideoDB: The Pinnacle of Synchronized Video Streaming for the Modern Web](https://docs.videodb.io/introducing-videodb-the-pinnacle-of-synchronized-video-streaming-27)

[Dynamic Video Streams](https://docs.videodb.io/dynamic-video-streams-50)

[Why do we need a Video Database Now?](https://docs.videodb.io/why-do-we-need-a-video-database-now-41)

[What's a Video Database ?](https://docs.videodb.io/whats-a-video-database-36)

[Enhancing AI-Driven Multimedia Applications](https://docs.videodb.io/enhancing-ai-driven-multimedia-applications-37)

[Misalignment of Today's Web](https://docs.videodb.io/misalignment-of-todays-web-67)

[Beyond Traditional Video Infrastructure](https://docs.videodb.io/beyond-traditional-video-infrastructure-28)

[Research Grants](https://docs.videodb.io/research-grants-96)

[Team](https://docs.videodb.io/team-46)

[Internship: Build the Future of AI-Powered Video Infrastructure](https://docs.videodb.io/internship-build-the-future-of-ai-powered-video-infrastructure-97)

[Ashutosh Trivedi](https://docs.videodb.io/ashutosh-trivedi-32)

[Playlists](https://docs.videodb.io/playlists-33)

[Talks - Solving Logical Puzzles with Natural Language Processing - PyCon India 2015](https://docs.videodb.io/talks-solving-logical-puzzles-with-natural-language-processing-p-34)

[Ashish](https://docs.videodb.io/ashish-45)

[Shivani Desai](https://docs.videodb.io/shivani-desai-48)

[Gaurav Tyagi](https://docs.videodb.io/gaurav-tyagi-51)

[Rohit Garg](https://docs.videodb.io/rohit-garg-64)

[Customer Love](https://docs.videodb.io/customer-love-42)

[Temp Doc](https://docs.videodb.io/temp-doc-54)

Quick Start Guide

# Guide: Subtitles

[![](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/video-db/videodb-cookbook/blob/main/guides/Subtitle.ipynb)

## Adding Subtitles

This guide gives you an introduction to adding Subtitle Styles by showing you visual outputs of the configurations available for the SubtitleStyle class, such as

Typography and Style

Color and Effects

Positioning and Margins

Text Transformation

Borders and Shadow

## 🛠️ Setup

### 📦 Installing packages

%pip install videodb

### 🔑 API Keys

Before proceeding, ensure access to

[VideoDB](https://videodb.io/)

Get your API key from

[VideoDB Console](https://console.videodb.io/)
. ( Free for first 50 uploads, No credit card required ) 🎉

import os

os.environ\["VIDEO\_DB\_API\_KEY"\]=""

### 🌐 Connect to VideoDB

from videodb import connect

conn = connect()

coll = conn.get\_collection()

### 🎥 Upload Video

Upload a base video to add subtitle. For this guide, we’ll use following video

video = coll.upload(url="https://www.youtube.com/watch?v=il39Ks4mV9g")

video.play()

You can upload from your local file system too by passing file\_path in upload()

## 🔊 Index Spoken Words

First, we need to index the video using video.index\_spoken\_words() function.This ensures the availability of the transcript. Without this step VideoDB wouldn’t be able to add captions to any video.

video.index\_spoken\_words()

## 📝 Default Subtitles

To add subtitles to your video you can use video.add\_subtitle() .

This method returns a
[streaming link](https://docs.videodb.io/unraveling-multimedia-from-mp3-mp4-to-the-future-with-videodb-26#_luGNZ)
, that you can play using play\_stream() method

from videodb import play\_stream

\# Add Subtitle to Video

stream\_url = video.add\_subtitle()

\# Play stream

play\_stream(stream\_url)

## 💅 Custom Styled Subtitles

To customise the style of subtitle, passSubtitleStytle()with configured styles tovideo.add\_subtitle()

View API Reference for SubtitleStyle class 💅

### 1\. Typography and Style

Configure Typography of the Subtitle by passing following parameters to SubtitleStyle() class

font\_name : The name of the font to use for the subtitles.

font\_size : The size(px) of the font

spacing : Spacing(px) between characters

bold: Set to True for bold text

italic : Set to True for italic text

underline : Set to True for underlined text

strike\_out : Set toTrue for strike-through text

from videodb import SubtitleStyle, play\_stream

stream\_url = video.add\_subtitle(

SubtitleStyle(

font\_name="Roboto",

font\_size=12,

spacing=0,

bold=False,

italic=False,

underline=False,

strike\_out=False

)

)

play\_stream(stream\_url)

![1 (1).png](https://codaio.imgix.net/docs/_s5lUnUCIU/blobs/bl-eA02oPyF0t/bf09e67ea357e286e052404972177a064b28ff474d30581b06b6533b7cf360d8f5f4b5e60c79844e9e37a03f4333c96f40c5af94fd0de5d639daef63fa24eb3a99c20a1e24f69eeddb33c3b12c909ea7352b69b7b6d9317ba36b406a846ae88efd63857e?auto=format%2Ccompress&fit=max)

### 2\. Color and Effects

Configure color of Subtitle by passing following parameters to SubtitleStyle() class

primary\_colour: The color of the main subtitle text.

secondary\_colour : The color used for karaoke or secondary effects.

outline\_colour : The color of the outline of the text.

back\_colour: The color of the subtitle background.

Format of Color

SubtitleStyle accepts colors in the &HBBGGRR hexadecimal format, where the sequence represents the blue, green, and red components,

&H prefix is required in this color format.

And when transparency is needed, an alpha value is placed at the beginning, yielding &HAABBGGRR.

from videodb import SubtitleStyle

stream\_url = video.add\_subtitle(

SubtitleStyle(

primary\_colour ="&H00A5CFFF",

secondary\_colour ="&H00FFFF00",

outline\_colour ="&H000341C1",

back\_colour ="&H803B3B3B",

)

)

play\_stream(stream\_url)

![2.png](https://codaio.imgix.net/docs/_s5lUnUCIU/blobs/bl-Ha_PSqmsVS/a6ebda91ff28cf30672254c305371b13fb09a4cb6d90506a80c2bd3a4b7f2a2a35e3145a00ef2e3e0094b6ca07b826a2e9639c59b62d1289d47011adc24e03c809b80ce2f2a6b18fdbeae134ca13fea6c03cb9b31fe9f82d24a8ef8e85e28446efb56cf9?auto=format%2Ccompress&fit=max)

### 3\. Position and Margins

Configure alignment and position of Subtitle by passing following parameters to SubtitleStyle() class

alignment : Alignment of subtitle. Accepts a value a type SubtitleAlignment

margin\_l : Sets margin area on left side of Subtitle box

margin\_r : Sets margin area on right side of Subtitle box

margin\_v : Sets margin area of top and bottom of Subtitle box

View API Reference to know more about SubtitleAlignment

from videodb import SubtitleStyle, SubtitleAlignment

stream\_url = video.add\_subtitle(

SubtitleStyle(

alignment =SubtitleAlignment.middle\_center,

margin\_l =10,

margin\_r =10,

margin\_v =20,

)

)

play\_stream(stream\_url)

![3.png](https://codaio.imgix.net/docs/_s5lUnUCIU/blobs/bl-Ns4CGsQJtg/c7141f3d370e816e200096c04723829d596f81c180b943782d9c8c38645d444e9dc3a836ce866b6936bdbe9cca770eafd7decad46b52a3221d1f34b892139827ca84142b65712f74cb858c5af13dfb4554d8714936e4deb1ddb3f97f63caad16219fa3bb?auto=format%2Ccompress&fit=max)

### 4\. Text Transformation

Transform the text size and spacing by passing following parameters to SubtitleStyle() class

scale\_x : Factor for scaling of the font horizontally

scale\_y : Factor for scaling of the font vertically

angle : Rotation angle(degress) of the text

from videodb import SubtitleStyle

stream\_url = video.add\_subtitle(

SubtitleStyle(

scale\_x=1.5,

scale\_y=3,

angle=0,

)

)

play\_stream(stream\_url)

![4 (1).png](https://codaio.imgix.net/docs/_s5lUnUCIU/blobs/bl-2KhyB-qvsP/22c8db309f6cac65a380027a9ae88e2f368e8be2f5e7f8eb2dbdb8b9e5d6575ec0a667a86a35a8641302270288da8a5e151e8ae782d8f1535be6c8425b3ad83aaf52688120a46613d79d5c7a8b791d6d835b15662758635492b820daeffa939c55a02a15?auto=format%2Ccompress&fit=max)

### 5\. Borders and Shadow

Add border style, outline and shadow by passing following parameters to SubtitleStyle() class

border\_style : Border style of subtitle. Accepts a value a typeSubtitleBorderStyle

outline: The width(px) of the outline around the text.

shadow : The depth(px) of the shadow behind the text

View API Reference to know more about SubtitleBorderStyle

from videodb import SubtitleStyle, SubtitleBorderStyle

stream\_url = video.add\_subtitle(

style=SubtitleStyle(

shadow=2,

back\_colour="&H00000000",

border\_style=SubtitleBorderStyle.no\_border,

)

)

play\_stream(stream\_url)

![5.png](https://codaio.imgix.net/docs/_s5lUnUCIU/blobs/bl-kWlndGvEzi/58b98f25313ddc0fc3f1b9fc1a2cafc0d9412970a541b320738008682a206b75e7d40ac3121ed202d04b274362c95cf36236837bd59e9027efc7ea04063567c9d63058cbdc4803bdd1a569694f4eb1c5f1a37f47c55bbe2564a0382e945e0f1966a83450?auto=format%2Ccompress&fit=max)

## 👨‍💻 Next Steps

Check out the other resources and tutorials using Subtitle and Subtitle Styling 💅.

[Enhancing Video Captions with VideoDB Subtitle Styling](https://docs.videodb.io/enhancing-video-captions-with-videodb-subtitle-styling-62)

If you have any questions or feedback. Feel free to reach out to us 🙌🏼

[Discord](https://discord.gg/py9P639jGz)

[GitHub](https://github.com/video-db)

[Email](mailto:ashu@videodb.io)

Adding Subtitles

🛠️ Setup

📦 Installing packages

🔑 API Keys

🌐 Connect to VideoDB

🎥 Upload Video

🔊 Index Spoken Words

📝 Default Subtitles

💅 Custom Styled Subtitles

1\. Typography and Style

2\. Color and Effects

3\. Position and Margins

4\. Text Transformation

5\. Borders and Shadow

👨‍💻 Next Steps


---

# Scene Extraction Algorithms [Source Link](https://docs.videodb.io/scene-extraction-algorithms-84)

VideoDB Documentation

Pages

[Welcome to VideoDB Docs](https://docs.videodb.io/)

[Quick Start Guide](https://docs.videodb.io/quick-start-guide-38)

[How Accurate is Your Search?](https://docs.videodb.io/how-accurate-is-your-search-88)

[Video Indexing Guide](https://docs.videodb.io/video-indexing-guide-101)

[Semantic Search](https://docs.videodb.io/semantic-search-89)

[Collections](https://docs.videodb.io/collections-68)

[Public Collections](https://docs.videodb.io/public-collections-102)

[Callback Details](https://docs.videodb.io/callback-details-66)

[Ref: Subtitle Styles](https://docs.videodb.io/ref-subtitle-styles-57)

[Language Support](https://docs.videodb.io/language-support-79)

[Guide: Subtitles](https://docs.videodb.io/guide-subtitles-73)

[Visual Search and Indexing](https://docs.videodb.io/visual-search-and-indexing-80)

[Scene Extraction Algorithms](https://docs.videodb.io/scene-extraction-algorithms-84)

[Custom Annotations](https://docs.videodb.io/custom-annotations-81)

[Scene-Level Metadata: Smarter Video Search & Retrieval](https://docs.videodb.io/scene-level-metadata-smarter-video-search-retrieval-107)

[Advanced Visual Search Pipelines](https://docs.videodb.io/advanced-visual-search-pipelines-82)

[Playground for Scene Extractions](https://docs.videodb.io/playground-for-scene-extractions-83)

[Deep Dive into Prompt Engineering : Mastering Video Scene Indexing](https://docs.videodb.io/deep-dive-into-prompt-engineering-mastering-video-scene-indexing-93)

[Multimodal Search](https://docs.videodb.io/multimodal-search-90)

[Multimodal Search: Quickstart](https://docs.videodb.io/multimodal-search-quickstart-91)

[Conference Slide Scraper with VideoDB](https://docs.videodb.io/conference-slide-scraper-with-videodb-92)

[Dynamic Video Streams](https://docs.videodb.io/dynamic-video-streams-44)

[Ref: TextAsset](https://docs.videodb.io/ref-textasset-74)

[Guide : TextAsset](https://docs.videodb.io/guide-textasset-75)

[Director - Video Agent Framework](https://docs.videodb.io/director-video-agent-framework-98)

[Agent Creation Playbook](https://docs.videodb.io/agent-creation-playbook-103)

[How I Built a CRM-integrated Sales Assistant Agent in 1 Hour](https://docs.videodb.io/how-i-built-a-crm-integrated-sales-assistant-agent-in-1-hour-106)

[Make Your Video Sound Studio Quality with Voice Cloning](https://docs.videodb.io/make-your-video-sound-studio-quality-with-voice-cloning-105)

[Setup Director Locally](https://docs.videodb.io/setup-director-locally-104)

[Open Source Tools](https://docs.videodb.io/open-source-tools-94)

[LlamaIndex VideoDB Retriever](https://docs.videodb.io/llamaindex-videodb-retriever-58)

[PromptClip: Use Power of LLM to Create Clips](https://docs.videodb.io/promptclip-use-power-of-llm-to-create-clips-52)

[StreamRAG: Connect ChatGPT to VideoDB](https://docs.videodb.io/streamrag-connect-chatgpt-to-videodb-43)

[Examples and Tutorials](https://docs.videodb.io/examples-and-tutorials-35)

[Dubbing - Replace Soundtrack with New Audio](https://docs.videodb.io/dubbing-replace-soundtrack-with-new-audio-49)

[Beep curse words in real-time](https://docs.videodb.io/beep-curse-words-in-real-time-53)

[Remove Unwanted Content from videos](https://docs.videodb.io/remove-unwanted-content-from-videos-5)

[Instant Clips of Your Favorite Characters](https://docs.videodb.io/instant-clips-of-your-favorite-characters-3)

[Insert Dynamic Ads in real-time](https://docs.videodb.io/insert-dynamic-ads-in-real-time-7)

[Adding Brand Elements with VideoDB](https://docs.videodb.io/adding-brand-elements-with-videodb-76)

[Revolutionize Video Editing with VideoDb: Effortless Ad Placement and Seamless Video Integration](https://docs.videodb.io/revolutionize-video-editing-with-videodb-effortless-ad-placement-8)

[Eleven Labs x VideoDB: Adding AI Generated voiceovers to silent footage](https://docs.videodb.io/eleven-labs-x-videodb-adding-ai-generated-voiceovers-to-silent-f-59)

[Elevating Trailers with Automated Narration](https://docs.videodb.io/elevating-trailers-with-automated-narration-60)

[Add Intro/Outro to Videos](https://docs.videodb.io/add-intro-outro-to-videos-61)

[Enhancing Video Captions with VideoDB Subtitle Styling](https://docs.videodb.io/enhancing-video-captions-with-videodb-subtitle-styling-62)

[Audio overlay + Video + Timeline](https://docs.videodb.io/audio-overlay-video-timeline-63)

[Building Dynamic Video Streams with VideoDB: Integrating Custom Data and APIs](https://docs.videodb.io/building-dynamic-video-streams-with-videodb-integrating-custom-d-85)

[Adding AI Generated Voiceovers with VideoDB and LOVO](https://docs.videodb.io/adding-ai-generated-voiceovers-with-videodb-and-lovo-70)

[AI Generated Ad Films for Product Videography: Wellsaid, Open AI & VideoDB](https://docs.videodb.io/ai-generated-ad-films-for-product-videography-wellsaid-open-ai-v-71)

[Fun with Keyword Search](https://docs.videodb.io/fun-with-keyword-search-77)

[AWS Rekognition and VideoDB - Intelligent Video Clips](https://docs.videodb.io/aws-rekognition-and-videodb-intelligent-video-clips-4)

[AWS Rekognition and VideoDB - Effortlessly Remove Inappropriate Content from Video](https://docs.videodb.io/aws-rekognition-and-videodb-effortlessly-remove-inappropriate-co-6)

[Overlay a Word-Counter on Video Stream](https://docs.videodb.io/overlay-a-word-counter-on-video-stream-86)

[Generate Automated Video Outputs with Text Prompts \| DALL-E + ElevenLabs + OpenAI + VideoDB](https://docs.videodb.io/generate-automated-video-outputs-with-text-prompts-dall-e-eleven-87)

[Edge of Knowledge](https://docs.videodb.io/edge-of-knowledge-10)

[Building Intelligent Machines](https://docs.videodb.io/building-intelligent-machines-16)

[Part 1 - Define Intelligence](https://docs.videodb.io/part-1-define-intelligence-17)

[Part 2 - Observe and Respond](https://docs.videodb.io/part-2-observe-and-respond-18)

[Part 3 - Training a Model](https://docs.videodb.io/part-3-training-a-model-19)

[Society of Machines](https://docs.videodb.io/society-of-machines-20)

[Society of Machines](https://docs.videodb.io/society-of-machines-23)

[Autonomy - Do we have the choice?](https://docs.videodb.io/autonomy-do-we-have-the-choice-21)

[Emergence - An Intelligence of the collective](https://docs.videodb.io/emergence-an-intelligence-of-the-collective-22)

[Drafts](https://docs.videodb.io/drafts-24)

[From Language Models to World Models: The Next Frontier in AI](https://docs.videodb.io/from-language-models-to-world-models-the-next-frontier-in-ai-65)

[The Future Series](https://docs.videodb.io/the-future-series-78)

[Building World's First Video Database](https://docs.videodb.io/building-worlds-first-video-database-25)

[Multimedia: From MP3/MP4 to the Future with VideoDB](https://docs.videodb.io/multimedia-from-mp3-mp4-to-the-future-with-videodb-26)

[Introducing VideoDB: The Pinnacle of Synchronized Video Streaming for the Modern Web](https://docs.videodb.io/introducing-videodb-the-pinnacle-of-synchronized-video-streaming-27)

[Dynamic Video Streams](https://docs.videodb.io/dynamic-video-streams-50)

[Why do we need a Video Database Now?](https://docs.videodb.io/why-do-we-need-a-video-database-now-41)

[What's a Video Database ?](https://docs.videodb.io/whats-a-video-database-36)

[Enhancing AI-Driven Multimedia Applications](https://docs.videodb.io/enhancing-ai-driven-multimedia-applications-37)

[Misalignment of Today's Web](https://docs.videodb.io/misalignment-of-todays-web-67)

[Beyond Traditional Video Infrastructure](https://docs.videodb.io/beyond-traditional-video-infrastructure-28)

[Research Grants](https://docs.videodb.io/research-grants-96)

[Team](https://docs.videodb.io/team-46)

[Internship: Build the Future of AI-Powered Video Infrastructure](https://docs.videodb.io/internship-build-the-future-of-ai-powered-video-infrastructure-97)

[Ashutosh Trivedi](https://docs.videodb.io/ashutosh-trivedi-32)

[Playlists](https://docs.videodb.io/playlists-33)

[Talks - Solving Logical Puzzles with Natural Language Processing - PyCon India 2015](https://docs.videodb.io/talks-solving-logical-puzzles-with-natural-language-processing-p-34)

[Ashish](https://docs.videodb.io/ashish-45)

[Shivani Desai](https://docs.videodb.io/shivani-desai-48)

[Gaurav Tyagi](https://docs.videodb.io/gaurav-tyagi-51)

[Rohit Garg](https://docs.videodb.io/rohit-garg-64)

[Customer Love](https://docs.videodb.io/customer-love-42)

[Temp Doc](https://docs.videodb.io/temp-doc-54)

Visual Search and Indexing

# Scene Extraction Algorithms

## SceneExtractionType

A video is a series of images that are called frames, these frames can be processed using multimodal modals or computer vision pipelines. There are many ways to identify the temporal change of concepts in the video.

SceneExtractionTypeand extraction\_configcan be used with two functions as parameters for scene identification.

It can be passed to index\_scenes() function as an argument.

It can be pass as an argument to extract\_scenes() function.

Checkout

[Advanced Visual Search Pipelines](https://docs.videodb.io/advanced-visual-search-pipelines-82)

for Scene and Frame object details.

Time based extraction is a simple way to break video into scenes. You define a frequency at which you want to split the video in scenes, for example, you may consider every 10 second as a one scene. This method is useful when you have no information about the nature of video or the video is random & dynamic. You can even create scenes with 1 second time interval.

This method has following extraction\_config:

time : The interval (in seconds) at which scenes are segmented. Default value is 10 — which means every 10 seconds segment is a scene.

frame\_count: The number of frames to extract per scene. This allows you to increase the number of frames collected for more context. Default value is 1.

select\_frames: A list of frames to select from each segment. The list can contain strings from \["first", "middle", or "last"\] which selects the respective frames. Default value is \["first"\]

Note: You can use either select\_frames or frame\_count strategy to extract frames for the scene.

wait\_index= traffic\_video.index\_scenes(

extraction\_type=SceneExtractionType.time\_based,

extraction\_config={"time":4,"frame\_count":5},

prompt="Identify when multiple cars are slowing down or waiting. Mention that cars are waiting or stopping and also specify the lane as left, middle, or right. For example, you can say \`cars in the middle lanes are waiting\`.",

name="wait\_index"

)

extraction\_type=SceneExtractionType.time\_based,

extraction\_config={"time":10,"select\_frames":\['first'\]},

Videos share context between timestamps. A scene is a logical segment of a video that completes a concept. You can identify scene changes based on visual content within the video.

Key factors for calculating changes are significant changes in the visual content, such as transitions, lights and movement.

This method has following extraction\_config:

threshold: Determines the sensitivity of the model towards scene changes within the video. Default value is 20, which known to be good for detecting camera shot changes from a video.

frame\_count: Accepts a number that specifies how many frames to pick from each shot. Default value is 1. Increasing this number will result in more frames being selected from each shot, which could provide a more detailed analysis of the scene.

extraction\_type=SceneExtractionType.shot\_based,

extraction\_config={"threshold":20, "frame\_count":4},

Want to print your doc?

This is not the way.

Try clicking the ⋯ next to your doc name or using a keyboard shortcut (

CtrlP

) instead.


---

# Custom Annotations [Source Link](https://docs.videodb.io/custom-annotations-81)

![videodb](https://codaio.imgix.net/workspaces/ws-jizMKG73gK/blobs/customIcons/1a6d553a-3676-494e-8f3b-fd666614f459?fit=fill&fill=solid&w=128&h=128&fm=gif&bg=0FFF&fill-color=0FFF)

VideoDB Documentation

Pages

[![](https://cdn.coda.io/icons/svg/color/align-center.svg)\\
\\
Welcome to VideoDB Docs](https://docs.videodb.io/)

[![](https://cdn.coda.io/icons/svg/color/quick-mode-on.svg)\\
\\
Quick Start Guide](https://docs.videodb.io/quick-start-guide-38)

[![](https://cdn.coda.io/icons/svg/color/wash-your-hands.svg)\\
\\
How Accurate is Your Search?](https://docs.videodb.io/how-accurate-is-your-search-88)

[![](https://cdn.coda.io/icons/svg/color/video-call.svg)\\
\\
Video Indexing Guide](https://docs.videodb.io/video-indexing-guide-101)

[![](https://cdn.coda.io/icons/svg/color/clear-search.svg)\\
\\
Semantic Search](https://docs.videodb.io/semantic-search-89)

[![](https://cdn.coda.io/icons/svg/color/binders-folder.svg)\\
\\
Collections](https://docs.videodb.io/collections-68)

[![](https://cdn.coda.io/icons/svg/color/magazine.svg)\\
\\
Public Collections](https://docs.videodb.io/public-collections-102)

[![](https://cdn.coda.io/icons/svg/color/callback.svg)\\
\\
Callback Details](https://docs.videodb.io/callback-details-66)

[![](https://cdn.coda.io/icons/svg/color/closed-captioning.svg)\\
\\
Ref: Subtitle Styles](https://docs.videodb.io/ref-subtitle-styles-57)

[![](https://cdn.coda.io/icons/svg/color/customer-support.svg)\\
\\
Language Support](https://docs.videodb.io/language-support-79)

[![](https://cdn.coda.io/icons/svg/color/closed-captioning.svg)\\
\\
Guide: Subtitles](https://docs.videodb.io/guide-subtitles-73)

[![](https://cdn.coda.io/icons/svg/color/asteroid.svg)\\
\\
Visual Search and Indexing](https://docs.videodb.io/visual-search-and-indexing-80)

[![](https://cdn.coda.io/icons/svg/color/landscape.svg)\\
\\
Scene Extraction Algorithms](https://docs.videodb.io/scene-extraction-algorithms-84)

[![icon picker](https://cdn.coda.io/icons/svg/color/edit-column.svg)\\
\\
Custom Annotations](https://docs.videodb.io/custom-annotations-81)

[![](https://cdn.coda.io/icons/svg/color/search-property.svg)\\
\\
Scene-Level Metadata: Smarter Video Search & Retrieval](https://docs.videodb.io/scene-level-metadata-smarter-video-search-retrieval-107)

[![](https://cdn.coda.io/icons/svg/color/search-more.svg)\\
\\
Advanced Visual Search Pipelines](https://docs.videodb.io/advanced-visual-search-pipelines-82)

[![](https://cdn.coda.io/icons/svg/color/football.svg)\\
\\
Playground for Scene Extractions](https://docs.videodb.io/playground-for-scene-extractions-83)

[![](https://cdn.coda.io/icons/svg/color/scuba-pressure-gauge.svg)\\
\\
Deep Dive into Prompt Engineering : Mastering Video Scene Indexing](https://docs.videodb.io/deep-dive-into-prompt-engineering-mastering-video-scene-indexing-93)

[![](https://cdn.coda.io/icons/svg/color/clear-search.svg)\\
\\
Multimodal Search](https://docs.videodb.io/multimodal-search-90)

[![](https://cdn.coda.io/icons/svg/color/search-more.svg)\\
\\
Multimodal Search: Quickstart](https://docs.videodb.io/multimodal-search-quickstart-91)

[![](https://cdn.coda.io/icons/svg/color/poll-topic.svg)\\
\\
Conference Slide Scraper with VideoDB](https://docs.videodb.io/conference-slide-scraper-with-videodb-92)

[![](https://cdn.coda.io/icons/svg/color/e-learning.svg)\\
\\
Dynamic Video Streams](https://docs.videodb.io/dynamic-video-streams-44)

[![](https://cdn.coda.io/icons/svg/color/text-box.svg)\\
\\
Ref: TextAsset](https://docs.videodb.io/ref-textasset-74)

[![](https://cdn.coda.io/icons/svg/color/text-box.svg)\\
\\
Guide : TextAsset](https://docs.videodb.io/guide-textasset-75)

[![director-light](https://codaio.imgix.net/workspaces/ws-jizMKG73gK/blobs/customIcons/6bc288c2-982b-4a97-a402-8da53aeaa236?fit=fill&fill=solid&w=128&h=128&fm=gif&bg=0FFF&fill-color=0FFF)\\
\\
Director - Video Agent Framework](https://docs.videodb.io/director-video-agent-framework-98)

[![](https://cdn.coda.io/icons/svg/color/open-book.svg)\\
\\
Agent Creation Playbook](https://docs.videodb.io/agent-creation-playbook-103)

[![](https://cdn.coda.io/icons/svg/color/bag-front-view.svg)\\
\\
How I Built a CRM-integrated Sales Assistant Agent in 1 Hour](https://docs.videodb.io/how-i-built-a-crm-integrated-sales-assistant-agent-in-1-hour-106)

[![](https://cdn.coda.io/icons/svg/color/voice-recognition-scan.svg)\\
\\
Make Your Video Sound Studio Quality with Voice Cloning](https://docs.videodb.io/make-your-video-sound-studio-quality-with-voice-cloning-105)

[![](https://cdn.coda.io/icons/svg/color/console.svg)\\
\\
Setup Director Locally](https://docs.videodb.io/setup-director-locally-104)

[![github](https://codaio.imgix.net/workspaces/ws-jizMKG73gK/blobs/customIcons/ac14f3ef-daa1-4b6e-aba5-af11f11b8372?fit=fill&fill=solid&w=128&h=128&fm=gif&bg=0FFF&fill-color=0FFF)\\
\\
Open Source Tools](https://docs.videodb.io/open-source-tools-94)

[![llama](https://codaio.imgix.net/workspaces/ws-jizMKG73gK/blobs/customIcons/c2b3a994-6140-40a9-93ff-d87aa37f2860?fit=fill&fill=solid&w=128&h=128&fm=gif&bg=0FFF&fill-color=0FFF)\\
\\
LlamaIndex VideoDB Retriever](https://docs.videodb.io/llamaindex-videodb-retriever-58)

[![](https://cdn.coda.io/icons/svg/color/command-line.svg)\\
\\
PromptClip: Use Power of LLM to Create Clips](https://docs.videodb.io/promptclip-use-power-of-llm-to-create-clips-52)

[![](https://cdn.coda.io/icons/svg/color/day-camera.svg)\\
\\
StreamRAG: Connect ChatGPT to VideoDB](https://docs.videodb.io/streamrag-connect-chatgpt-to-videodb-43)

[![](https://cdn.coda.io/icons/svg/color/book-and-pencil.svg)\\
\\
Examples and Tutorials](https://docs.videodb.io/examples-and-tutorials-35)

[![](https://cdn.coda.io/icons/svg/color/audible.svg)\\
\\
Dubbing - Replace Soundtrack with New Audio](https://docs.videodb.io/dubbing-replace-soundtrack-with-new-audio-49)

[![](https://cdn.coda.io/icons/svg/color/adware-free.svg)\\
\\
Beep curse words in real-time](https://docs.videodb.io/beep-curse-words-in-real-time-53)

[![](https://cdn.coda.io/icons/svg/color/find-user-male.svg)\\
\\
Remove Unwanted Content from videos](https://docs.videodb.io/remove-unwanted-content-from-videos-5)

[![](https://cdn.coda.io/icons/svg/color/find-and-replace.svg)\\
\\
Instant Clips of Your Favorite Characters](https://docs.videodb.io/instant-clips-of-your-favorite-characters-3)

[![](https://cdn.coda.io/icons/svg/color/insert-white-space.svg)\\
\\
Insert Dynamic Ads in real-time](https://docs.videodb.io/insert-dynamic-ads-in-real-time-7)

[![](https://cdn.coda.io/icons/svg/color/mac-client.svg)\\
\\
Adding Brand Elements with VideoDB](https://docs.videodb.io/adding-brand-elements-with-videodb-76)

[![](https://cdn.coda.io/icons/svg/color/adverb.svg)\\
\\
Revolutionize Video Editing with VideoDb: Effortless Ad Placement and Seamless Video Integration](https://docs.videodb.io/revolutionize-video-editing-with-videodb-effortless-ad-placement-8)

[![](https://cdn.coda.io/icons/svg/color/medium-volume.svg)\\
\\
Eleven Labs x VideoDB: Adding AI Generated voiceovers to silent footage](https://docs.videodb.io/eleven-labs-x-videodb-adding-ai-generated-voiceovers-to-silent-f-59)

[![](https://cdn.coda.io/icons/svg/color/camera-automation.svg)\\
\\
Elevating Trailers with Automated Narration](https://docs.videodb.io/elevating-trailers-with-automated-narration-60)

[![](https://cdn.coda.io/icons/svg/color/video-trimming.svg)\\
\\
Add Intro/Outro to Videos](https://docs.videodb.io/add-intro-outro-to-videos-61)

[![](https://cdn.coda.io/icons/svg/color/closed-captioning.svg)\\
\\
Enhancing Video Captions with VideoDB Subtitle Styling](https://docs.videodb.io/enhancing-video-captions-with-videodb-subtitle-styling-62)

[![](https://cdn.coda.io/icons/svg/color/high-volume.svg)\\
\\
Audio overlay + Video + Timeline](https://docs.videodb.io/audio-overlay-video-timeline-63)

[![](https://cdn.coda.io/icons/svg/color/video-call.svg)\\
\\
Building Dynamic Video Streams with VideoDB: Integrating Custom Data and APIs](https://docs.videodb.io/building-dynamic-video-streams-with-videodb-integrating-custom-d-85)

[![](https://cdn.coda.io/icons/svg/color/for-experienced.svg)\\
\\
Adding AI Generated Voiceovers with VideoDB and LOVO](https://docs.videodb.io/adding-ai-generated-voiceovers-with-videodb-and-lovo-70)

[![](https://cdn.coda.io/icons/svg/color/billboard.svg)\\
\\
AI Generated Ad Films for Product Videography: Wellsaid, Open AI & VideoDB](https://docs.videodb.io/ai-generated-ad-films-for-product-videography-wellsaid-open-ai-v-71)

[![](https://cdn.coda.io/icons/svg/color/search.svg)\\
\\
Fun with Keyword Search](https://docs.videodb.io/fun-with-keyword-search-77)

[![](https://cdn.coda.io/icons/svg/color/find-and-replace.svg)\\
\\
AWS Rekognition and VideoDB - Intelligent Video Clips](https://docs.videodb.io/aws-rekognition-and-videodb-intelligent-video-clips-4)

[![](https://cdn.coda.io/icons/svg/color/find-user-male.svg)\\
\\
AWS Rekognition and VideoDB - Effortlessly Remove Inappropriate Content from Video](https://docs.videodb.io/aws-rekognition-and-videodb-effortlessly-remove-inappropriate-co-6)

[![](https://cdn.coda.io/icons/svg/color/counter.svg)\\
\\
Overlay a Word-Counter on Video Stream](https://docs.videodb.io/overlay-a-word-counter-on-video-stream-86)

[![](https://cdn.coda.io/icons/svg/color/handle-with-care.svg)\\
\\
Generate Automated Video Outputs with Text Prompts \| DALL-E + ElevenLabs + OpenAI + VideoDB](https://docs.videodb.io/generate-automated-video-outputs-with-text-prompts-dall-e-eleven-87)

[![](https://cdn.coda.io/icons/svg/color/centre-of-gravity.svg)\\
\\
Edge of Knowledge](https://docs.videodb.io/edge-of-knowledge-10)

[![](https://cdn.coda.io/icons/svg/color/for-experienced.svg)\\
\\
Building Intelligent Machines](https://docs.videodb.io/building-intelligent-machines-16)

[![](https://cdn.coda.io/icons/svg/color/artificial-intelligence.svg)\\
\\
Part 1 - Define Intelligence](https://docs.videodb.io/part-1-define-intelligence-17)

[![](https://cdn.coda.io/icons/svg/color/panel-and-foot-outlet.svg)\\
\\
Part 2 - Observe and Respond](https://docs.videodb.io/part-2-observe-and-respond-18)

[![](https://cdn.coda.io/icons/svg/color/the-flash-sign.svg)\\
\\
Part 3 - Training a Model](https://docs.videodb.io/part-3-training-a-model-19)

[![](https://cdn.coda.io/icons/svg/color/cnc-machine.svg)\\
\\
Society of Machines](https://docs.videodb.io/society-of-machines-20)

[![](https://cdn.coda.io/icons/svg/color/groups.svg)\\
\\
Society of Machines](https://docs.videodb.io/society-of-machines-23)

[![](https://cdn.coda.io/icons/svg/color/the-flash-sign.svg)\\
\\
Autonomy - Do we have the choice?](https://docs.videodb.io/autonomy-do-we-have-the-choice-21)

[![](https://cdn.coda.io/icons/svg/color/artificial-intelligence.svg)\\
\\
Emergence - An Intelligence of the collective](https://docs.videodb.io/emergence-an-intelligence-of-the-collective-22)

[![](https://cdn.coda.io/icons/svg/color/back-to-draft.svg)\\
\\
Drafts](https://docs.videodb.io/drafts-24)

[![](https://cdn.coda.io/icons/svg/color/one-to-many.svg)\\
\\
From Language Models to World Models: The Next Frontier in AI](https://docs.videodb.io/from-language-models-to-world-models-the-next-frontier-in-ai-65)

[![](https://cdn.coda.io/icons/svg/color/recurring-appointment-exception.svg)\\
\\
The Future Series](https://docs.videodb.io/the-future-series-78)

[![videodb](https://codaio.imgix.net/workspaces/ws-jizMKG73gK/blobs/customIcons/1a6d553a-3676-494e-8f3b-fd666614f459?fit=fill&fill=solid&w=128&h=128&fm=gif&bg=0FFF&fill-color=0FFF)\\
\\
Building World's First Video Database](https://docs.videodb.io/building-worlds-first-video-database-25)

[![](https://cdn.coda.io/icons/svg/color/video.svg)\\
\\
Multimedia: From MP3/MP4 to the Future with VideoDB](https://docs.videodb.io/multimedia-from-mp3-mp4-to-the-future-with-videodb-26)

[![](https://cdn.coda.io/icons/svg/color/synchronize.svg)\\
\\
Introducing VideoDB: The Pinnacle of Synchronized Video Streaming for the Modern Web](https://docs.videodb.io/introducing-videodb-the-pinnacle-of-synchronized-video-streaming-27)

[![](https://cdn.coda.io/icons/svg/color/bridge.svg)\\
\\
Dynamic Video Streams](https://docs.videodb.io/dynamic-video-streams-50)

[![](https://cdn.coda.io/icons/svg/color/need-for-speed.svg)\\
\\
Why do we need a Video Database Now?](https://docs.videodb.io/why-do-we-need-a-video-database-now-41)

[![](https://cdn.coda.io/icons/svg/color/questions.svg)\\
\\
What's a Video Database ?](https://docs.videodb.io/whats-a-video-database-36)

[![](https://cdn.coda.io/icons/svg/color/ai.svg)\\
\\
Enhancing AI-Driven Multimedia Applications](https://docs.videodb.io/enhancing-ai-driven-multimedia-applications-37)

[![](https://cdn.coda.io/icons/svg/color/artificial-intelligence.svg)\\
\\
Misalignment of Today's Web](https://docs.videodb.io/misalignment-of-todays-web-67)

[![](https://cdn.coda.io/icons/svg/color/fff.svg)\\
\\
Beyond Traditional Video Infrastructure](https://docs.videodb.io/beyond-traditional-video-infrastructure-28)

[![](https://cdn.coda.io/icons/svg/color/biotech.svg)\\
\\
Research Grants](https://docs.videodb.io/research-grants-96)

[![](https://cdn.coda.io/icons/svg/color/the-dragon-team.svg)\\
\\
Team](https://docs.videodb.io/team-46)

[![videodb](https://codaio.imgix.net/workspaces/ws-jizMKG73gK/blobs/customIcons/1a6d553a-3676-494e-8f3b-fd666614f459?fit=fill&fill=solid&w=128&h=128&fm=gif&bg=0FFF&fill-color=0FFF)\\
\\
Internship: Build the Future of AI-Powered Video Infrastructure](https://docs.videodb.io/internship-build-the-future-of-ai-powered-video-infrastructure-97)

[![](https://cdn.coda.io/icons/svg/color/light.svg)\\
\\
Ashutosh Trivedi](https://docs.videodb.io/ashutosh-trivedi-32)

[![](https://cdn.coda.io/icons/svg/color/fast-forward.svg)\\
\\
Playlists](https://docs.videodb.io/playlists-33)

[![](https://cdn.coda.io/icons/svg/color/1.svg)\\
\\
Talks - Solving Logical Puzzles with Natural Language Processing - PyCon India 2015](https://docs.videodb.io/talks-solving-logical-puzzles-with-natural-language-processing-p-34)

[![](https://cdn.coda.io/icons/svg/color/rocket.svg)\\
\\
Ashish](https://docs.videodb.io/ashish-45)

[![](https://cdn.coda.io/icons/svg/color/edvard-munch.svg)\\
\\
Shivani Desai](https://docs.videodb.io/shivani-desai-48)

[![](https://cdn.coda.io/icons/svg/color/artificial-intelligence.svg)\\
\\
Gaurav Tyagi](https://docs.videodb.io/gaurav-tyagi-51)

[![](https://cdn.coda.io/icons/svg/color/under-computer.svg)\\
\\
Rohit Garg](https://docs.videodb.io/rohit-garg-64)

[![](https://cdn.coda.io/icons/svg/color/like.svg)\\
\\
Customer Love](https://docs.videodb.io/customer-love-42)

[![](https://cdn.coda.io/icons/svg/color/llama.svg)\\
\\
Temp Doc](https://docs.videodb.io/temp-doc-54)

Visual Search and Indexing

# ![icon picker](https://cdn.coda.io/icons/svg/color/edit-column.svg)         Custom Annotations

⁠

[![](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/video-db/videodb-cookbook/blob/main/guides/scene-index/custom_annotations.ipynb)

⁠

⁠

Enhance your understanding of videos by using our simple annotation and tagging pipeline. To enable this, you can create a new Scene object. Then, pass your annotations in the description field and index them using index\_scenes() function.

⁠

![Screenshot 2024-07-04 at 12.23.02 PM.jpg](https://codaio.imgix.net/docs/_s5lUnUCIU/blobs/bl-sFF1gD6ccn/2b6d908fe9b544290d09b9d340cfa6ad521c2972dfe9756d8fe83c2d23a780a9838651fdfdf681a6eabb393922d6be3bd616d8af5e3b3edf3442b9f292d748a9660886c1bff1ece139e09954eec5c71a2748f019da510b9240d16fa88d5801faa410f129?auto=format%2Ccompress&fit=max)

⁠

⁠

![light](https://cdn.coda.io/icons/svg/color/light.svg)

VideoDB allows multiple indexes on video objects. This is advantageous as it allows you to attach additional context to each scene, enhancing the search functionality.

## Scene:

![info](https://cdn.coda.io/icons/svg/color/info.svg)

A Scene object describes a unique event in the video. From a timeline perspective it’s a timestamp range.

video\_id : id of the video object

start : seconds

end : seconds

description : string description

Each scene object has another attribute, frames, which contains a list of

[Frame](https://docs.videodb.io/advanced-visual-search-pipelines-82)

⁠

objects. However, we don't need them here for custom annotation pipelines because we are bringing the description from outside.

### Create a new Scene

Create new Scene objects and add your custom annotation as description.

from videodb.scene import Scene

\# create scene object and patch your description

scene1 = Scene(

video\_id=video.id,

start=0,

end=100,

description="Detective Martin is being interviewed by the police.",)

scene2 = Scene(

video\_id=video.id,

start=600,

end=900,

description="A religious gathering. People are praying and singing")

\# create a list of scene objects

scenes = \[scene1, scene2\]

### Index and search scenes

Index using the list of scene objects and use the index\_id for search

from videodb import IndexType

#create new index and assign it a name

index\_id = video.index\_scenes(scenes=scenes, name="My Custom Annotations#1")

\# search using the index\_id

res = video.search(query="religious gathering", index\_type=IndexType.scene, index\_id=index\_id)

res.play()

![ok](https://cdn.coda.io/icons/svg/color/ok.svg)

Custom annotations unlock additional features

Adding application context into the search pipeline.

Generate unique descriptions from your own custom vision model.

Index manual annotations.

Read more about Scene object in

[![](https://cdn.coda.io/icons/svg/color/search-more.svg)\\
Advanced Visual Search Pipelines](https://docs.videodb.io/advanced-visual-search-pipelines-82)

⁠

Scene:

Create a new Scene

Index and search scenes

Want to print your doc?

This is not the way.

![](https://cdn.coda.io/assets/6ee7d0564a67/img/import_google_docs.png)

Try clicking the ⋯ next to your doc name or using a keyboard shortcut (

CtrlP

) instead.

---

# Scene-Level Metadata: Smarter Video Search & Retrieval [Source Link](https://docs.videodb.io/scene-level-metadata-smarter-video-search-retrieval-107)

![videodb](https://codaio.imgix.net/workspaces/ws-jizMKG73gK/blobs/customIcons/1a6d553a-3676-494e-8f3b-fd666614f459?fit=fill&fill=solid&w=128&h=128&fm=gif&bg=0FFF&fill-color=0FFF)

VideoDB Documentation

Pages

[![](https://cdn.coda.io/icons/svg/color/align-center.svg)\\
\\
Welcome to VideoDB Docs](https://docs.videodb.io/)

[![](https://cdn.coda.io/icons/svg/color/quick-mode-on.svg)\\
\\
Quick Start Guide](https://docs.videodb.io/quick-start-guide-38)

[![](https://cdn.coda.io/icons/svg/color/asteroid.svg)\\
\\
Visual Search and Indexing](https://docs.videodb.io/visual-search-and-indexing-80)

[![](https://cdn.coda.io/icons/svg/color/landscape.svg)\\
\\
Scene Extraction Algorithms](https://docs.videodb.io/scene-extraction-algorithms-84)

[![](https://cdn.coda.io/icons/svg/color/edit-column.svg)\\
\\
Custom Annotations](https://docs.videodb.io/custom-annotations-81)

[![icon picker](https://cdn.coda.io/icons/svg/color/search-property.svg)\\
\\
Scene-Level Metadata: Smarter Video Search & Retrieval](https://docs.videodb.io/scene-level-metadata-smarter-video-search-retrieval-107)

[![](https://cdn.coda.io/icons/svg/color/search-more.svg)\\
\\
Advanced Visual Search Pipelines](https://docs.videodb.io/advanced-visual-search-pipelines-82)

[![](https://cdn.coda.io/icons/svg/color/football.svg)\\
\\
Playground for Scene Extractions](https://docs.videodb.io/playground-for-scene-extractions-83)

[![](https://cdn.coda.io/icons/svg/color/scuba-pressure-gauge.svg)\\
\\
Deep Dive into Prompt Engineering : Mastering Video Scene Indexing](https://docs.videodb.io/deep-dive-into-prompt-engineering-mastering-video-scene-indexing-93)

[![](https://cdn.coda.io/icons/svg/color/clear-search.svg)\\
\\
Multimodal Search](https://docs.videodb.io/multimodal-search-90)

[![](https://cdn.coda.io/icons/svg/color/e-learning.svg)\\
\\
Dynamic Video Streams](https://docs.videodb.io/dynamic-video-streams-44)

[![director-light](https://codaio.imgix.net/workspaces/ws-jizMKG73gK/blobs/customIcons/6bc288c2-982b-4a97-a402-8da53aeaa236?fit=fill&fill=solid&w=128&h=128&fm=gif&bg=0FFF&fill-color=0FFF)\\
\\
Director - Video Agent Framework](https://docs.videodb.io/director-video-agent-framework-98)

[![github](https://codaio.imgix.net/workspaces/ws-jizMKG73gK/blobs/customIcons/ac14f3ef-daa1-4b6e-aba5-af11f11b8372?fit=fill&fill=solid&w=128&h=128&fm=gif&bg=0FFF&fill-color=0FFF)\\
\\
Open Source Tools](https://docs.videodb.io/open-source-tools-94)

[![](https://cdn.coda.io/icons/svg/color/book-and-pencil.svg)\\
\\
Examples and Tutorials](https://docs.videodb.io/examples-and-tutorials-35)

[![](https://cdn.coda.io/icons/svg/color/centre-of-gravity.svg)\\
\\
Edge of Knowledge](https://docs.videodb.io/edge-of-knowledge-10)

[![videodb](https://codaio.imgix.net/workspaces/ws-jizMKG73gK/blobs/customIcons/1a6d553a-3676-494e-8f3b-fd666614f459?fit=fill&fill=solid&w=128&h=128&fm=gif&bg=0FFF&fill-color=0FFF)\\
\\
Building World's First Video Database](https://docs.videodb.io/building-worlds-first-video-database-25)

[![](https://cdn.coda.io/icons/svg/color/the-dragon-team.svg)\\
\\
Team](https://docs.videodb.io/team-46)

[![](https://cdn.coda.io/icons/svg/color/like.svg)\\
\\
Customer Love](https://docs.videodb.io/customer-love-42)

[![](https://cdn.coda.io/icons/svg/color/llama.svg)\\
\\
Temp Doc](https://docs.videodb.io/temp-doc-54)

Visual Search and Indexing

# ![icon picker](https://cdn.coda.io/icons/svg/color/search-property.svg) Scene-Level Metadata: Smarter Video Search & Retrieval

[![](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1OuqMdG44liBMQ0eG1xDDcZW-UK-Hr0ji?usp=sharing)

## Introduction

James and Mark are video engineers at leading sports entertainment companies, responsible for managing, storing, and editing vast amounts of sports footage. Their work requires them to extract and highlight the most exciting moments from hours of raw video.

Both rely on VideoDB to streamline their workflow, but their approaches differ.

Mark follows the traditional method: he indexes the entire video and runs a search for relevant scenes. VideoDB processes every indexed scene, analyzing descriptions either semantically or via keywords. The results are useful but not always efficient—especially when the relevant content spans just a few minutes in a multi-hour video. The search still scans everything, sometimes returning unrelated clips.

James, on the other hand, has a smarter strategy. Instead of searching the entire video, he first filters out irrelevant scenes, ensuring that only important moments are considered. This results in faster and more precise searches. How does he achieve this? By using Scene-Level Metadata.

## What is Scene-Level Metadata?

Scene-Level Metadata acts as smart tags for individual video scenes, allowing them to be filtered during search. Instead of relying solely on text descriptions, VideoDB enables metadata-based filtering to refine search results and make retrieval more efficient.

### Why is this necessary?

Every video consists of multiple scenes, each composed of frames. By default, VideoDB scans every scene to find relevant content.

This works well for short videos, but when handling longer videos, only a few scenes may actually be relevant. Searching across the entire video can lead to:

Slower retrieval times

Less accurate results

By tagging scenes with metadata, we can focus the search only on relevant parts of the video, significantly improving accuracy and efficiency.

### How is Metadata Stored?

Metadata is stored as a dictionary in the Scene object, with a maximum of five key-value pairs per scene.

Here’s an example:

scene = Scene(

video\_id=video.id,

start=60,

end=62,

description="A Red Bull car speeds down the straight at Monza.",

metadata={"camera\_view":"road\_ahead","action\_type":"chasing"}

)

With Scene-Level Metadata, we can apply targeted filters, ensuring that searches return only highly relevant scenes.

## Example: Using Scene-Level Metadata in an F1 Race

James, our video engineer, works with Formula 1 race footage, which consists of continuous laps of high-speed action. To create engaging highlights, he needs to focus on the most thrilling moments:

Chasing battles

Sharp turns

Overtaking maneuvers

Dramatic crashes

Instead of searching the entire race, James applies Scene-Level Metadata to tag these key moments, ensuring faster and more accurate retrieval.

### Defining Metadata Filters

James decides to apply metadata filters using the "action\_type" key, assigning one of the following values:

📌 \["chase", "turn", "overtake", "crash"\]

For simplicity, he uses only one key-value pair per scene, but he could add multiple filters (e.g., "camera\_view", "lap\_number") for even more precise results.

## James' Workflow with VideoDB

### Step 1: Extract Scenes from the Footage

To improve indexing, James splits the video into 2-second scenes and extracts a single key frame per scene.

scene\_collection = video.extract\_scenes(

extraction\_type=SceneExtractionType.time\_based,

extraction\_config={"time":2,"select\_frames":\["middle"\]}

)

scenes = scene\_collection.scenes # Fetch extracted scenes

### Step 2: Assign Metadata to Each Scene

James uses AI-powered descriptions to automatically tag scenes with the correct action type before indexing.

described\_scenes =\[\]

for scene in scenes:

# use describe to create smart metadata, category, filter etc.

action\_type = scene.describe('Select one: \["chase", "turn", "overtake", "crash"\]')

# use prompt to index contextual information that you need to search in vectors.

# use metadata to add structured information to each scene.

described\_scene = Scene(

video\_id=video.id,

start=scene.start,

end=scene.end,

description=scene.describe("Describe this scene briefly."),

metadata={"action\_type": action\_type}

)

described\_scenes.append(described\_scene)

### Step 3: Index the Video with Scene Metadata

Once metadata is assigned, James indexes the scenes for efficient searching.

scene\_index\_id = video.index\_scenes(

scenes=described\_scenes,

name="F1 Highlight Scenes"

)

### Step 4: Searching with Metadata Filters

Now, instead of searching the entire video, James can filter his search to focus on only specific race moments.

## Applying Metadata Filters in Search

### Example 1: Finding Intense Overtakes

To find all overtaking moments, James applies a metadata filter:

search\_results = video.search(

query="A thrilling overtaking maneuver",

filter=\[{"action\_type":"overtake"}\],# Apply metadata filter

search\_type=SearchType.semantic,

index\_type=IndexType.scene,

scene\_index\_id=scene\_index\_id

)

search\_results.play()# View the retrieved scenes

### Example 2: Finding Chase Scenes in the Race

To retrieve close pursuit moments, James filters for chase scenes:

search\_results = video.search(

query="An aggressive chase on the track",

filter=\[{"action\_type":"chase"}\],# Apply metadata filter

search\_type=SearchType.semantic,

index\_type=IndexType.scene,

scene\_index\_id=scene\_index\_id

)

search\_results.play()

By applying Scene-Level Metadata, James dramatically improves his video search workflow.

## Index level Metadata

metadata can be passed as parameter to the index\_scenes function as well.

scene\_index\_id= video.index\_scenes(

extraction\_type=SceneExtractionType.time\_based,

extraction\_config={"time":540},

metadata={"category":"news","topic":"airplane"},

)

The metadata you passed during the indexing process, would apply to all the scenes that you are indexing.

Depending on your application, you may have additional scene-related metadata, which can be included within the metadata parameter. Please refer to the metadata guidelines.

Metadata Guidelines:

metadata must be a dictionary containing key-value pairs.

Both keys and values can be of type int or string.

A maximum of 5 key-value pairs is allowed.

The length of keys and values must not exceed 20 characters.

Filter results based on your criteria and you can pass more than one filter. This can be useful in timestamp based filtering of results, while exploring archival content and many such more categorical approaches to find the right content.

results= video.search(

query="airport",

filter=\[{"category":"news"}\],

index\_type=IndexType.scene

)

results= coll.search(

query="airport",

filter=\[{"category":"news"}\],

index\_type=IndexType.scene

)

Filter Guidelines:

Filter must be a list of dictionaries.

Each dictionary specifies a key-value pair to filter the results based on metadata.

## Expanding the Use Cases

Metadata isn't just for sports highlights—it has applications across multiple industries:

🔹 Wildlife Documentation
A raw wildlife documentary may contain hours of footage capturing slow-moving landscapes and sudden bursts of animal activity. But let’s say we’re only interested in tracking a pride of lions. With metadata tagging, we can filter out only the scenes featuring lions, making it easier to find the right content.

🔹 Tech Conferences & Keynote Events
A multi-hour tech conference covers various topics—Blockchain, GenAI, Quantum Computing, etc. Instead of searching through entire sessions, we can tag segments based on their subjects and filter out irrelevant sections, making topic-based retrieval seamless.

🔹 Security & Surveillance
In CCTV surveillance, hours of footage may contain only a few moments of interest, such as unauthorized access or suspicious activity. By tagging scenes based on motion detection, time of day, or facial recognition, security teams can instantly retrieve critical footage.

## The Future of Smart Video Retrieval

Scene-Level Metadata is a game-changer in video indexing and retrieval. It enhances:

✅ Precision – Finds exactly what you’re looking for.
✅ Efficiency – Speeds up the search process.
✅ Scalability – Works with large video datasets effortlessly.

From Formula 1 highlights to security footage analysis, metadata-driven search makes video retrieval faster, smarter, and more intuitive than ever before.

With VideoDB, every second of footage becomes instantly accessible.

Introduction

What is Scene-Level Metadata?

Why is this necessary?

How is Metadata Stored?

Example: Using Scene-Level Metadata in an F1 Race

Defining Metadata Filters

James' Workflow with VideoDB

Step 1: Extract Scenes from the Footage

Step 2: Assign Metadata to Each Scene

Step 3: Index the Video with Scene Metadata

Step 4: Searching with Metadata Filters

Applying Metadata Filters in Search

Example 1: Finding Intense Overtakes

Example 2: Finding Chase Scenes in the Race

Index level Metadata

Expanding the Use Cases

The Future of Smart Video Retrieval

Want to print your doc?

This is not the way.

![](https://cdn.coda.io/assets/6ee7d0564a67/img/import_google_docs.png)

Try clicking the ⋯ next to your doc name or using a keyboard shortcut (

CtrlP

) instead.


---

# Advanced Visual Search Pipelines [Source Link](https://docs.videodb.io/advanced-visual-search-pipelines-82)

VideoDB Documentation

Pages

[Welcome to VideoDB Docs](https://docs.videodb.io/)

[Quick Start Guide](https://docs.videodb.io/quick-start-guide-38)

[How Accurate is Your Search?](https://docs.videodb.io/how-accurate-is-your-search-88)

[Video Indexing Guide](https://docs.videodb.io/video-indexing-guide-101)

[Semantic Search](https://docs.videodb.io/semantic-search-89)

[Collections](https://docs.videodb.io/collections-68)

[Public Collections](https://docs.videodb.io/public-collections-102)

[Callback Details](https://docs.videodb.io/callback-details-66)

[Ref: Subtitle Styles](https://docs.videodb.io/ref-subtitle-styles-57)

[Language Support](https://docs.videodb.io/language-support-79)

[Guide: Subtitles](https://docs.videodb.io/guide-subtitles-73)

[Visual Search and Indexing](https://docs.videodb.io/visual-search-and-indexing-80)

[Scene Extraction Algorithms](https://docs.videodb.io/scene-extraction-algorithms-84)

[Custom Annotations](https://docs.videodb.io/custom-annotations-81)

[Scene-Level Metadata: Smarter Video Search & Retrieval](https://docs.videodb.io/scene-level-metadata-smarter-video-search-retrieval-107)

[Advanced Visual Search Pipelines](https://docs.videodb.io/advanced-visual-search-pipelines-82)

[Playground for Scene Extractions](https://docs.videodb.io/playground-for-scene-extractions-83)

[Deep Dive into Prompt Engineering : Mastering Video Scene Indexing](https://docs.videodb.io/deep-dive-into-prompt-engineering-mastering-video-scene-indexing-93)

[Multimodal Search](https://docs.videodb.io/multimodal-search-90)

[Multimodal Search: Quickstart](https://docs.videodb.io/multimodal-search-quickstart-91)

[Conference Slide Scraper with VideoDB](https://docs.videodb.io/conference-slide-scraper-with-videodb-92)

[Dynamic Video Streams](https://docs.videodb.io/dynamic-video-streams-44)

[Ref: TextAsset](https://docs.videodb.io/ref-textasset-74)

[Guide : TextAsset](https://docs.videodb.io/guide-textasset-75)

[Director - Video Agent Framework](https://docs.videodb.io/director-video-agent-framework-98)

[Agent Creation Playbook](https://docs.videodb.io/agent-creation-playbook-103)

[How I Built a CRM-integrated Sales Assistant Agent in 1 Hour](https://docs.videodb.io/how-i-built-a-crm-integrated-sales-assistant-agent-in-1-hour-106)

[Make Your Video Sound Studio Quality with Voice Cloning](https://docs.videodb.io/make-your-video-sound-studio-quality-with-voice-cloning-105)

[Setup Director Locally](https://docs.videodb.io/setup-director-locally-104)

[Open Source Tools](https://docs.videodb.io/open-source-tools-94)

[LlamaIndex VideoDB Retriever](https://docs.videodb.io/llamaindex-videodb-retriever-58)

[PromptClip: Use Power of LLM to Create Clips](https://docs.videodb.io/promptclip-use-power-of-llm-to-create-clips-52)

[StreamRAG: Connect ChatGPT to VideoDB](https://docs.videodb.io/streamrag-connect-chatgpt-to-videodb-43)

[Examples and Tutorials](https://docs.videodb.io/examples-and-tutorials-35)

[Dubbing - Replace Soundtrack with New Audio](https://docs.videodb.io/dubbing-replace-soundtrack-with-new-audio-49)

[Beep curse words in real-time](https://docs.videodb.io/beep-curse-words-in-real-time-53)

[Remove Unwanted Content from videos](https://docs.videodb.io/remove-unwanted-content-from-videos-5)

[Instant Clips of Your Favorite Characters](https://docs.videodb.io/instant-clips-of-your-favorite-characters-3)

[Insert Dynamic Ads in real-time](https://docs.videodb.io/insert-dynamic-ads-in-real-time-7)

[Adding Brand Elements with VideoDB](https://docs.videodb.io/adding-brand-elements-with-videodb-76)

[Revolutionize Video Editing with VideoDb: Effortless Ad Placement and Seamless Video Integration](https://docs.videodb.io/revolutionize-video-editing-with-videodb-effortless-ad-placement-8)

[Eleven Labs x VideoDB: Adding AI Generated voiceovers to silent footage](https://docs.videodb.io/eleven-labs-x-videodb-adding-ai-generated-voiceovers-to-silent-f-59)

[Elevating Trailers with Automated Narration](https://docs.videodb.io/elevating-trailers-with-automated-narration-60)

[Add Intro/Outro to Videos](https://docs.videodb.io/add-intro-outro-to-videos-61)

[Enhancing Video Captions with VideoDB Subtitle Styling](https://docs.videodb.io/enhancing-video-captions-with-videodb-subtitle-styling-62)

[Audio overlay + Video + Timeline](https://docs.videodb.io/audio-overlay-video-timeline-63)

[Building Dynamic Video Streams with VideoDB: Integrating Custom Data and APIs](https://docs.videodb.io/building-dynamic-video-streams-with-videodb-integrating-custom-d-85)

[Adding AI Generated Voiceovers with VideoDB and LOVO](https://docs.videodb.io/adding-ai-generated-voiceovers-with-videodb-and-lovo-70)

[AI Generated Ad Films for Product Videography: Wellsaid, Open AI & VideoDB](https://docs.videodb.io/ai-generated-ad-films-for-product-videography-wellsaid-open-ai-v-71)

[Fun with Keyword Search](https://docs.videodb.io/fun-with-keyword-search-77)

[AWS Rekognition and VideoDB - Intelligent Video Clips](https://docs.videodb.io/aws-rekognition-and-videodb-intelligent-video-clips-4)

[AWS Rekognition and VideoDB - Effortlessly Remove Inappropriate Content from Video](https://docs.videodb.io/aws-rekognition-and-videodb-effortlessly-remove-inappropriate-co-6)

[Overlay a Word-Counter on Video Stream](https://docs.videodb.io/overlay-a-word-counter-on-video-stream-86)

[Generate Automated Video Outputs with Text Prompts \| DALL-E + ElevenLabs + OpenAI + VideoDB](https://docs.videodb.io/generate-automated-video-outputs-with-text-prompts-dall-e-eleven-87)

[Edge of Knowledge](https://docs.videodb.io/edge-of-knowledge-10)

[Building Intelligent Machines](https://docs.videodb.io/building-intelligent-machines-16)

[Part 1 - Define Intelligence](https://docs.videodb.io/part-1-define-intelligence-17)

[Part 2 - Observe and Respond](https://docs.videodb.io/part-2-observe-and-respond-18)

[Part 3 - Training a Model](https://docs.videodb.io/part-3-training-a-model-19)

[Society of Machines](https://docs.videodb.io/society-of-machines-20)

[Society of Machines](https://docs.videodb.io/society-of-machines-23)

[Autonomy - Do we have the choice?](https://docs.videodb.io/autonomy-do-we-have-the-choice-21)

[Emergence - An Intelligence of the collective](https://docs.videodb.io/emergence-an-intelligence-of-the-collective-22)

[Drafts](https://docs.videodb.io/drafts-24)

[From Language Models to World Models: The Next Frontier in AI](https://docs.videodb.io/from-language-models-to-world-models-the-next-frontier-in-ai-65)

[The Future Series](https://docs.videodb.io/the-future-series-78)

[Building World's First Video Database](https://docs.videodb.io/building-worlds-first-video-database-25)

[Multimedia: From MP3/MP4 to the Future with VideoDB](https://docs.videodb.io/multimedia-from-mp3-mp4-to-the-future-with-videodb-26)

[Introducing VideoDB: The Pinnacle of Synchronized Video Streaming for the Modern Web](https://docs.videodb.io/introducing-videodb-the-pinnacle-of-synchronized-video-streaming-27)

[Dynamic Video Streams](https://docs.videodb.io/dynamic-video-streams-50)

[Why do we need a Video Database Now?](https://docs.videodb.io/why-do-we-need-a-video-database-now-41)

[What's a Video Database ?](https://docs.videodb.io/whats-a-video-database-36)

[Enhancing AI-Driven Multimedia Applications](https://docs.videodb.io/enhancing-ai-driven-multimedia-applications-37)

[Misalignment of Today's Web](https://docs.videodb.io/misalignment-of-todays-web-67)

[Beyond Traditional Video Infrastructure](https://docs.videodb.io/beyond-traditional-video-infrastructure-28)

[Research Grants](https://docs.videodb.io/research-grants-96)

[Team](https://docs.videodb.io/team-46)

[Internship: Build the Future of AI-Powered Video Infrastructure](https://docs.videodb.io/internship-build-the-future-of-ai-powered-video-infrastructure-97)

[Ashutosh Trivedi](https://docs.videodb.io/ashutosh-trivedi-32)

[Playlists](https://docs.videodb.io/playlists-33)

[Talks - Solving Logical Puzzles with Natural Language Processing - PyCon India 2015](https://docs.videodb.io/talks-solving-logical-puzzles-with-natural-language-processing-p-34)

[Ashish](https://docs.videodb.io/ashish-45)

[Shivani Desai](https://docs.videodb.io/shivani-desai-48)

[Gaurav Tyagi](https://docs.videodb.io/gaurav-tyagi-51)

[Rohit Garg](https://docs.videodb.io/rohit-garg-64)

[Customer Love](https://docs.videodb.io/customer-love-42)

[Temp Doc](https://docs.videodb.io/temp-doc-54)

Visual Search and Indexing

# Advanced Visual Search Pipelines

[![](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/video-db/videodb-cookbook/blob/main/guides/scene-index/advanced_visual_search.ipynb)

Let's deep dive into Scene and Frame objects

### Scene

A Scene object describes a unique event in the video. From a timeline perspective it’s a timestamp range.

video\_id : id of the video object

start : seconds

end : seconds

description : string description

Each scene object has an attribute frames, that has list of Frame objects.

### Frame

Each Scene can be described by a list of frames. Each Frame object primarily has the URL of the image and its description field.

id : ID of the frame object

url : URL of the image

frame\_time : Timestamp of the frame in the video

description : string description

video\_id : id of the video object

scene\_id : id of the scene object

![Screenshot 2024-07-04 at 11.41.39 AM.jpg](https://codaio.imgix.net/docs/_s5lUnUCIU/blobs/bl-HozdUmjeH4/7f7ec6d342e7b6ecb573aeeddb6e11b4d4529edb0b8188204fe1e2ca0545d2eda1b47369bbd32647998a8e1ec1cc326a800581717aa979ef19fb20850c76011cf4fb690f8a31cd48f44d7567597e85af1e57085261c25f70d5ef5cd5d74ae26f5c7909aa?auto=format%2Ccompress&fit=max)

We provide you with easy-to-use Objects and Functions to bring flexibility in designing your visual understanding pipeline. With these tools, you have the freedom to:

*   Extract scene according to your use case.
*   Go to frame level abstraction.
*   Assign label, custom model description for each frame.
*   Use of multiple models, prompts for each scene or frame to convert information to text.
*   Send multiple frames to vision model for better temporal activity understanding.

### extract\_scenes()

This function accepts the extraction\_type and extraction\_config and returns a

[SceneCollection](https://docs.videodb.io/playground-for-scene-extractions-83)

object, which keep information about all the extracted scene lists.

[Scene Extraction Algorithms](https://docs.videodb.io/scene-extraction-algorithms-84)

for more details.

```
scene_collection = video.extract_scenes(

extraction_type=SceneExtractionType.time_based,

extraction_config={"time": 30, "select_frames": \["middle"\]},

)
```

### Capture Temporal Change

Vision models excel at describing images, but videos present an added complexity due to the temporal changes in the information. With our pipeline, you can maintain image-level understanding in frames and combine them using LLMs at the scene level to capture temporal or activity-related understanding.

You have freedom to iterate through each scene and frame level to describe the information for indexing purposes.

Get scene collection

```
scene_collection = video.get_scene_collection("scene_collection_id")
```

### Iterate through each scene and frame

Iterate over scenes and frames and attach description coming from external pipeline be it custom CV pipeline or custom model descriptions.

```
print("This is scene collection id", scene_collection.id)

print("This is scene collection config", scene_collection.config)

# get scene from collection

scenes = scene_collection.scenes

# Iterate through each scene

for scene in scenes:

print(f"Scene Duration {scene.start}-{scene.end}")

# Iterate through each frame in the scene

for frame in scene.frames:

print(f"Frame at {frame.frame_time} {frame.url}")

frame.description = "bring text from external sources/ pipeline"

)
```

### Create Scene by custom annotation

These annotations can come from your application or from external vision model, if you extract the description using any vision LLM

```
for scene in scenes:

scene.description = "summary of frame level description"
```

Using this pipeline, you have the freedom to design your own flow. In the example above, we’ve described each frame in the scene independently, but some vision models allow multiple images in one go as well. Feel free to customise your flow as per your needs.

*   Experiment with sending multiple frames to a vision model.
*   Utilize prompts to describe multiple frames, then assign these descriptions to the scene.
*   Integrate your own vision model into the pipeline.

We’ll soon be adding more details and strategies for effective and advanced multimodal search. We welcome your input on what strategies have worked best in your specific use cases

Here’s our

[Discord](https://discord.gg/py9P639jGz)

channel where we brainstorm about such ideas.

Once you have a description of each scene in place, you can index and search for the information using the following functions.

```
from videodb import IndexType

#create new index and assign a name to it

index_id = video.index_scenes(scenes=scenes, name="My Custom Model")

# search using the index_id

res = video.search(query="first 29 sec",

index_type=IndexType.scene,

index_id=index_id)

res.play()
```

Scene

Frame

extract\_scenes()

Capture Temporal Change

Iterate through each scene and frame

Create Scene by custom annotation

Want to print your doc?

This is not the way.

![](https://cdn.coda.io/assets/6ee7d0564a67/img/import_google_docs.png)

Try clicking the ⋯ next to your doc name or using a keyboard shortcut (CtrlP) instead.


---

# Playground for Scene Extractions [Source Link](https://docs.videodb.io/playground-for-scene-extractions-83)

![videodb](https://codaio.imgix.net/workspaces/ws-jizMKG73gK/blobs/customIcons/1a6d553a-3676-494e-8f3b-fd666614f459?fit=fill&fill=solid&w=128&h=128&fm=gif&bg=0FFF&fill-color=0FFF)

VideoDB Documentation

Pages

[![](https://cdn.coda.io/icons/svg/color/align-center.svg) Welcome to VideoDB Docs](https://docs.videodb.io/)

[![](https://cdn.coda.io/icons/svg/color/quick-mode-on.svg) Quick Start Guide](https://docs.videodb.io/quick-start-guide-38)

[![](https://cdn.coda.io/icons/svg/color/wash-your-hands.svg) How Accurate is Your Search?](https://docs.videodb.io/how-accurate-is-your-search-88)

[![](https://cdn.coda.io/icons/svg/color/video-call.svg) Video Indexing Guide](https://docs.videodb.io/video-indexing-guide-101)

[![](https://cdn.coda.io/icons/svg/color/clear-search.svg) Semantic Search](https://docs.videodb.io/semantic-search-89)

[![](https://cdn.coda.io/icons/svg/color/binders-folder.svg) Collections](https://docs.videodb.io/collections-68)

[![](https://cdn.coda.io/icons/svg/color/magazine.svg) Public Collections](https://docs.videodb.io/public-collections-102)

[![](https://cdn.coda.io/icons/svg/color/callback.svg) Callback Details](https://docs.videodb.io/callback-details-66)

[![](https://cdn.coda.io/icons/svg/color/closed-captioning.svg) Ref: Subtitle Styles](https://docs.videodb.io/ref-subtitle-styles-57)

[![](https://cdn.coda.io/icons/svg/color/customer-support.svg) Language Support](https://docs.videodb.io/language-support-79)

[![](https://cdn.coda.io/icons/svg/color/closed-captioning.svg) Guide: Subtitles](https://docs.videodb.io/guide-subtitles-73)

[![](https://cdn.coda.io/icons/svg/color/asteroid.svg) Visual Search and Indexing](https://docs.videodb.io/visual-search-and-indexing-80)

[![](https://cdn.coda.io/icons/svg/color/landscape.svg) Scene Extraction Algorithms](https://docs.videodb.io/scene-extraction-algorithms-84)

[![](https://cdn.coda.io/icons/svg/color/edit-column.svg) Custom Annotations](https://docs.videodb.io/custom-annotations-81)

[![](https://cdn.coda.io/icons/svg/color/search-property.svg) Scene-Level Metadata: Smarter Video Search & Retrieval](https://docs.videodb.io/scene-level-metadata-smarter-video-search-retrieval-107)

[![](https://cdn.coda.io/icons/svg/color/search-more.svg) Advanced Visual Search Pipelines](https://docs.videodb.io/advanced-visual-search-pipelines-82)

[![icon picker](https://cdn.coda.io/icons/svg/color/football.svg) Playground for Scene Extractions](https://docs.videodb.io/playground-for-scene-extractions-83)

[![](https://cdn.coda.io/icons/svg/color/scuba-pressure-gauge.svg) Deep Dive into Prompt Engineering : Mastering Video Scene Indexing](https://docs.videodb.io/deep-dive-into-prompt-engineering-mastering-video-scene-indexing-93)

[![](https://cdn.coda.io/icons/svg/color/clear-search.svg) Multimodal Search](https://docs.videodb.io/multimodal-search-90)

[![](https://cdn.coda.io/icons/svg/color/search-more.svg) Multimodal Search: Quickstart](https://docs.videodb.io/multimodal-search-quickstart-91)

[![](https://cdn.coda.io/icons/svg/color/poll-topic.svg) Conference Slide Scraper with VideoDB](https://docs.videodb.io/conference-slide-scraper-with-videodb-92)

[![](https://cdn.coda.io/icons/svg/color/e-learning.svg) Dynamic Video Streams](https://docs.videodb.io/dynamic-video-streams-44)

[![](https://cdn.coda.io/icons/svg/color/text-box.svg) Ref: TextAsset](https://docs.videodb.io/ref-textasset-74)

[![](https://cdn.coda.io/icons/svg/color/text-box.svg) Guide : TextAsset](https://docs.videodb.io/guide-textasset-75)

[![director-light](https://codaio.imgix.net/workspaces/ws-jizMKG73gK/blobs/customIcons/6bc288c2-982b-4a97-a402-8da53aeaa236?fit=fill&fill=solid&w=128&h=128&fm=gif&bg=0FFF&fill-color=0FFF) Director - Video Agent Framework](https://docs.videodb.io/director-video-agent-framework-98)

[![](https://cdn.coda.io/icons/svg/color/open-book.svg) Agent Creation Playbook](https://docs.videodb.io/agent-creation-playbook-103)

[![](https://cdn.coda.io/icons/svg/color/bag-front-view.svg) How I Built a CRM-integrated Sales Assistant Agent in 1 Hour](https://docs.videodb.io/how-i-built-a-crm-integrated-sales-assistant-agent-in-1-hour-106)

[![](https://cdn.coda.io/icons/svg/color/voice-recognition-scan.svg) Make Your Video Sound Studio Quality with Voice Cloning](https://docs.videodb.io/make-your-video-sound-studio-quality-with-voice-cloning-105)

[![](https://cdn.coda.io/icons/svg/color/console.svg) Setup Director Locally](https://docs.videodb.io/setup-director-locally-104)

[![github](https://codaio.imgix.net/workspaces/ws-jizMKG73gK/blobs/customIcons/ac14f3ef-daa1-4b6e-aba5-af11f11b8372?fit=fill&fill=solid&w=128&h=128&fm=gif&bg=0FFF&fill-color=0FFF) Open Source Tools](https://docs.videodb.io/open-source-tools-94)

[![llama](https://codaio.imgix.net/workspaces/ws-jizMKG73gK/blobs/customIcons/c2b3a994-6140-40a9-93ff-d87aa37f2860?fit=fill&fill=solid&w=128&h=128&fm=gif&bg=0FFF&fill-color=0FFF) LlamaIndex VideoDB Retriever](https://docs.videodb.io/llamaindex-videodb-retriever-58)

[![](https://cdn.coda.io/icons/svg/color/command-line.svg) PromptClip: Use Power of LLM to Create Clips](https://docs.videodb.io/promptclip-use-power-of-llm-to-create-clips-52)

[![](https://cdn.coda.io/icons/svg/color/day-camera.svg) StreamRAG: Connect ChatGPT to VideoDB](https://docs.videodb.io/streamrag-connect-chatgpt-to-videodb-43)

[![](https://cdn.coda.io/icons/svg/color/book-and-pencil.svg) Examples and Tutorials](https://docs.videodb.io/examples-and-tutorials-35)

[![](https://cdn.coda.io/icons/svg/color/audible.svg) Dubbing - Replace Soundtrack with New Audio](https://docs.videodb.io/dubbing-replace-soundtrack-with-new-audio-49)

[![](https://cdn.coda.io/icons/svg/color/adware-free.svg) Beep curse words in real-time](https://docs.videodb.io/beep-curse-words-in-real-time-53)

[![](https://cdn.coda.io/icons/svg/color/find-user-male.svg) Remove Unwanted Content from videos](https://docs.videodb.io/remove-unwanted-content-from-videos-5)

[![](https://cdn.coda.io/icons/svg/color/find-and-replace.svg) Instant Clips of Your Favorite Characters](https://docs.videodb.io/instant-clips-of-your-favorite-characters-3)

[![](https://cdn.coda.io/icons/svg/color/insert-white-space.svg) Insert Dynamic Ads in real-time](https://docs.videodb.io/insert-dynamic-ads-in-real-time-7)

[![](https://cdn.coda.io/icons/svg/color/mac-client.svg) Adding Brand Elements with VideoDB](https://docs.videodb.io/adding-brand-elements-with-videodb-76)

[![](https://cdn.coda.io/icons/svg/color/adverb.svg) Revolutionize Video Editing with VideoDb: Effortless Ad Placement and Seamless Video Integration](https://docs.videodb.io/revolutionize-video-editing-with-videodb-effortless-ad-placement-8)

[![](https://cdn.coda.io/icons/svg/color/medium-volume.svg) Eleven Labs x VideoDB: Adding AI Generated voiceovers to silent footage](https://docs.videodb.io/eleven-labs-x-videodb-adding-ai-generated-voiceovers-to-silent-f-59)

[![](https://cdn.coda.io/icons/svg/color/camera-automation.svg) Elevating Trailers with Automated Narration](https://docs.videodb.io/elevating-trailers-with-automated-narration-60)

[![](https://cdn.coda.io/icons/svg/color/video-trimming.svg) Add Intro/Outro to Videos](https://docs.videodb.io/add-intro-outro-to-videos-61)

[![](https://cdn.coda.io/icons/svg/color/closed-captioning.svg) Enhancing Video Captions with VideoDB Subtitle Styling](https://docs.videodb.io/enhancing-video-captions-with-videodb-subtitle-styling-62)

[![](https://cdn.coda.io/icons/svg/color/high-volume.svg) Audio overlay + Video + Timeline](https://docs.videodb.io/audio-overlay-video-timeline-63)

[![](https://cdn.coda.io/icons/svg/color/video-call.svg) Building Dynamic Video Streams with VideoDB: Integrating Custom Data and APIs](https://docs.videodb.io/building-dynamic-video-streams-with-videodb-integrating-custom-d-85)

[![](https://cdn.coda.io/icons/svg/color/for-experienced.svg) Adding AI Generated Voiceovers with VideoDB and LOVO](https://docs.videodb.io/adding-ai-generated-voiceovers-with-videodb-and-lovo-70)

[![](https://cdn.coda.io/icons/svg/color/billboard.svg) AI Generated Ad Films for Product Videography: Wellsaid, Open AI & VideoDB](https://docs.videodb.io/ai-generated-ad-films-for-product-videography-wellsaid-open-ai-v-71)

[![](https://cdn.coda.io/icons/svg/color/search.svg) Fun with Keyword Search](https://docs.videodb.io/fun-with-keyword-search-77)

[![](https://cdn.coda.io/icons/svg/color/find-and-replace.svg) AWS Rekognition and VideoDB - Intelligent Video Clips](https://docs.videodb.io/aws-rekognition-and-videodb-intelligent-video-clips-4)

[![](https://cdn.coda.io/icons/svg/color/find-user-male.svg) AWS Rekognition and VideoDB - Effortlessly Remove Inappropriate Content from Video](https://docs.videodb.io/aws-rekognition-and-videodb-effortlessly-remove-inappropriate-co-6)

[![](https://cdn.coda.io/icons/svg/color/counter.svg) Overlay a Word-Counter on Video Stream](https://docs.videodb.io/overlay-a-word-counter-on-video-stream-86)

[![](https://cdn.coda.io/icons/svg/color/handle-with-care.svg) Generate Automated Video Outputs with Text Prompts \| DALL-E + ElevenLabs + OpenAI + VideoDB](https://docs.videodb.io/generate-automated-video-outputs-with-text-prompts-dall-e-eleven-87)

[![](https://cdn.coda.io/icons/svg/color/centre-of-gravity.svg) Edge of Knowledge](https://docs.videodb.io/edge-of-knowledge-10)

[![](https://cdn.coda.io/icons/svg/color/for-experienced.svg) Building Intelligent Machines](https://docs.videodb.io/building-intelligent-machines-16)

[![](https://cdn.coda.io/icons/svg/color/artificial-intelligence.svg) Part 1 - Define Intelligence](https://docs.videodb.io/part-1-define-intelligence-17)

[![](https://cdn.coda.io/icons/svg/color/panel-and-foot-outlet.svg) Part 2 - Observe and Respond](https://docs.videodb.io/part-2-observe-and-respond-18)

[![](https://cdn.coda.io/icons/svg/color/the-flash-sign.svg) Part 3 - Training a Model](https://docs.videodb.io/part-3-training-a-model-19)

[![](https://cdn.coda.io/icons/svg/color/cnc-machine.svg) Society of Machines](https://docs.videodb.io/society-of-machines-20)

[![](https://cdn.coda.io/icons/svg/color/groups.svg) Society of Machines](https://docs.videodb.io/society-of-machines-23)

[![](https://cdn.coda.io/icons/svg/color/the-flash-sign.svg) Autonomy - Do we have the choice?](https://docs.videodb.io/autonomy-do-we-have-the-choice-21)

[![](https://cdn.coda.io/icons/svg/color/artificial-intelligence.svg) Emergence - An Intelligence of the collective](https://docs.videodb.io/emergence-an-intelligence-of-the-collective-22)

[![](https://cdn.coda.io/icons/svg/color/back-to-draft.svg) Drafts](https://docs.videodb.io/drafts-24)

[![](https://cdn.coda.io/icons/svg/color/one-to-many.svg) From Language Models to World Models: The Next Frontier in AI](https://docs.videodb.io/from-language-models-to-world-models-the-next-frontier-in-ai-65)

[![](https://cdn.coda.io/icons/svg/color/recurring-appointment-exception.svg) The Future Series](https://docs.videodb.io/the-future-series-78)

[![videodb](https://codaio.imgix.net/workspaces/ws-jizMKG73gK/blobs/customIcons/1a6d553a-3676-494e-8f3b-fd666614f459?fit=fill&fill=solid&w=128&h=128&fm=gif&bg=0FFF&fill-color=0FFF) Building World's First Video Database](https://docs.videodb.io/building-worlds-first-video-database-25)

[![](https://cdn.coda.io/icons/svg/color/video.svg) Multimedia: From MP3/MP4 to the Future with VideoDB](https://docs.videodb.io/multimedia-from-mp3-mp4-to-the-future-with-videodb-26)

[![](https://cdn.coda.io/icons/svg/color/synchronize.svg) Introducing VideoDB: The Pinnacle of Synchronized Video Streaming for the Modern Web](https://docs.videodb.io/introducing-videodb-the-pinnacle-of-synchronized-video-streaming-27)

[![](https://cdn.coda.io/icons/svg/color/bridge.svg) Dynamic Video Streams](https://docs.videodb.io/dynamic-video-streams-50)

[![](https://cdn.coda.io/icons/svg/color/need-for-speed.svg) Why do we need a Video Database Now?](https://docs.videodb.io/why-do-we-need-a-video-database-now-41)

[![](https://cdn.coda.io/icons/svg/color/questions.svg) What's a Video Database ?](https://docs.videodb.io/whats-a-video-database-36)

[![](https://cdn.coda.io/icons/svg/color/ai.svg) Enhancing AI-Driven Multimedia Applications](https://docs.videodb.io/enhancing-ai-driven-multimedia-applications-37)

[![](https://cdn.coda.io/icons/svg/color/artificial-intelligence.svg) Misalignment of Today's Web](https://docs.videodb.io/misalignment-of-todays-web-67)

[![](https://cdn.coda.io/icons/svg/color/fff.svg) Beyond Traditional Video Infrastructure](https://docs.videodb.io/beyond-traditional-video-infrastructure-28)

[![](https://cdn.coda.io/icons/svg/color/biotech.svg) Research Grants](https://docs.videodb.io/research-grants-96)

[![](https://cdn.coda.io/icons/svg/color/the-dragon-team.svg) Team](https://docs.videodb.io/team-46)

[![videodb](https://codaio.imgix.net/workspaces/ws-jizMKG73gK/blobs/customIcons/1a6d553a-3676-494e-8f3b-fd666614f459?fit=fill&fill=solid&w=128&h=128&fm=gif&bg=0FFF&fill-color=0FFF) Internship: Build the Future of AI-Powered Video Infrastructure](https://docs.videodb.io/internship-build-the-future-of-ai-powered-video-infrastructure-97)

[![](https://cdn.coda.io/icons/svg/color/light.svg) Ashutosh Trivedi](https://docs.videodb.io/ashutosh-trivedi-32)

[![](https://cdn.coda.io/icons/svg/color/fast-forward.svg) Playlists](https://docs.videodb.io/playlists-33)

[![](https://cdn.coda.io/icons/svg/color/1.svg) Talks - Solving Logical Puzzles with Natural Language Processing - PyCon India 2015](https://docs.videodb.io/talks-solving-logical-puzzles-with-natural-language-processing-p-34)

[![](https://cdn.coda.io/icons/svg/color/rocket.svg) Ashish](https://docs.videodb.io/ashish-45)

[![](https://cdn.coda.io/icons/svg/color/edvard-munch.svg) Shivani Desai](https://docs.videodb.io/shivani-desai-48)

[![](https://cdn.coda.io/icons/svg/color/artificial-intelligence.svg) Gaurav Tyagi](https://docs.videodb.io/gaurav-tyagi-51)

[![](https://cdn.coda.io/icons/svg/color/under-computer.svg) Rohit Garg](https://docs.videodb.io/rohit-garg-64)

[![](https://cdn.coda.io/icons/svg/color/like.svg) Customer Love](https://docs.videodb.io/customer-love-42)

[![](https://cdn.coda.io/icons/svg/color/llama.svg) Temp Doc](https://docs.videodb.io/temp-doc-54)

Visual Search and Indexing

# ![icon picker](https://cdn.coda.io/icons/svg/color/football.svg) Playground for Scene Extractions

[![](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/video-db/videodb-cookbook/blob/main/guides/scene-index/playground_scene_extraction.ipynb)

## Playground: Extract Scenes without Indexing

Sometimes, it's important to determine the number of scenes needed to describe a video, as this can vary depending on the type of video. For instance, videos of a podcast with two hosts tend to be less dynamic than sports videos

![light](https://cdn.coda.io/icons/svg/color/light.svg)

If you want to extract scenes from the video without indexing them, you can use the video.extract\_scenes()function.

Using this pipeline you can experiment with scene extraction and find your suitable configuration.

### extract\_scenes()

This function accepts the extraction\_type and extraction\_config and returns a SceneCollection object, that keeps the information about all the extracted scene lists.

scene\_collections = video.extract\_scenes(

extraction\_type=SceneExtractionType.time\_based,

extraction\_config={"time": 30, "select\_frames": \["middle"\]},

)

### SceneCollection Viewing, Inspecting, and Deleting Scenes

For every scene extraction pipeline that you run on a video, a SceneCollection object is created.

You can use following functions to View, Inspect and Delete your SceneCollections

list\_scene\_collection

scene\_collections = video.list\_scene\_collection()

for scene\_collection in scene\_collections:

print("Scene Collection ID :",scene\_collection\["scene\_collection\_id"\])

Get SceneCollection by ID

scene\_collection = video.get\_scene\_collection("scene\_collection\_id")

Inspecting SceneCollection

print("This is scene collection id", scene\_collection.id)

print("This is scene collection config", scene\_collection.config)

## Playground: Play with Prompt

Before finalizing your prompt, consider experimenting with different ones. This will help you see how the search performs for your use cases. Start by iterating over only a few scenes. Then, experiment with your prompt and test it after indexing

We believe that the right prompt is very helpful in finding information that aligns with your domain knowledge and experience. For this we provide following describe(prompt= ) functions at Frame and Scene level.

[Read more about Scene and Frame object](https://docs.videodb.io/advanced-visual-search-pipelines-82)

#describe frame image using vision LLM

frame.describe(

prompt=str,

)

\# run vision model on scene level

\# primarily for activity detection.

Scene.describe(

prompt=str,

)

Start by iterating over only few scenes and experiment with your prompt and test after indexing.

\# get scene from collection

scenes = scene\_collection.scenes

\# Iterate through only 5 scene

for scene in scenes\[:5\]:

print(f"Scene Duration {scene.start}-{scene.end}")

# Iterate through each frame in the scene

for frame in scene.frames:

print(f"Frame at {frame.frame\_time} {frame.url}")

frame.describe(

prompt=str,

)

### Experiment with prompt at scene level

\# get scene from collection

scenes = scene\_collection.scenes

\# Iterate through first 5 scene

for scene in scenes\[:5\] :

scene.describe(

prompt=str,

)

### Index and search scenes

\# Give a name to your index for reference

index\_id = video.index\_scenes(scenes=scenes, name="")

\# search using the index\_id

res = video.search(query="religious gathering",

index\_type=IndexType.scene,

index\_id=index\_id)

res.play()

Playground: Extract Scenes without Indexing

extract\_scenes()

SceneCollection Viewing, Inspecting, and Deleting Scenes

Playground: Play with Prompt

Experiment with prompt at scene level

Index and search scenes

Want to print your doc?

This is not the way.

![](https://cdn.coda.io/assets/6ee7d0564a67/img/import_google_docs.png)

Try clicking the ⋯ next to your doc name or using a keyboard shortcut (

CtrlP

) instead.


---

# Deep Dive into Prompt Engineering : Mastering Video Scene Indexing [Source Link](https://docs.videodb.io/deep-dive-into-prompt-engineering-mastering-video-scene-indexing-93)

VideoDB Documentation

Pages

[Welcome to VideoDB Docs](https://docs.videodb.io/)

[Quick Start Guide](https://docs.videodb.io/quick-start-guide-38)

[How Accurate is Your Search?](https://docs.videodb.io/how-accurate-is-your-search-88)

[Video Indexing Guide](https://docs.videodb.io/video-indexing-guide-101)

[Semantic Search](https://docs.videodb.io/semantic-search-89)

[Collections](https://docs.videodb.io/collections-68)

[Public Collections](https://docs.videodb.io/public-collections-102)

[Callback Details](https://docs.videodb.io/callback-details-66)

[Ref: Subtitle Styles](https://docs.videodb.io/ref-subtitle-styles-57)

[Language Support](https://docs.videodb.io/language-support-79)

[Guide: Subtitles](https://docs.videodb.io/guide-subtitles-73)

[Visual Search and Indexing](https://docs.videodb.io/visual-search-and-indexing-80)

[Scene Extraction Algorithms](https://docs.videodb.io/scene-extraction-algorithms-84)

[Custom Annotations](https://docs.videodb.io/custom-annotations-81)

[Scene-Level Metadata: Smarter Video Search & Retrieval](https://docs.videodb.io/scene-level-metadata-smarter-video-search-retrieval-107)

[Advanced Visual Search Pipelines](https://docs.videodb.io/advanced-visual-search-pipelines-82)

[Playground for Scene Extractions](https://docs.videodb.io/playground-for-scene-extractions-83)

[Deep Dive into Prompt Engineering : Mastering Video Scene Indexing](https://docs.videodb.io/deep-dive-into-prompt-engineering-mastering-video-scene-indexing-93)

[Multimodal Search](https://docs.videodb.io/multimodal-search-90)

[Multimodal Search: Quickstart](https://docs.videodb.io/multimodal-search-quickstart-91)

[Conference Slide Scraper with VideoDB](https://docs.videodb.io/conference-slide-scraper-with-videodb-92)

[Dynamic Video Streams](https://docs.videodb.io/dynamic-video-streams-44)

[Ref: TextAsset](https://docs.videodb.io/ref-textasset-74)

[Guide : TextAsset](https://docs.videodb.io/guide-textasset-75)

[Director - Video Agent Framework](https://docs.videodb.io/director-video-agent-framework-98)

[Agent Creation Playbook](https://docs.videodb.io/agent-creation-playbook-103)

[How I Built a CRM-integrated Sales Assistant Agent in 1 Hour](https://docs.videodb.io/how-i-built-a-crm-integrated-sales-assistant-agent-in-1-hour-106)

[Make Your Video Sound Studio Quality with Voice Cloning](https://docs.videodb.io/make-your-video-sound-studio-quality-with-voice-cloning-105)

[Setup Director Locally](https://docs.videodb.io/setup-director-locally-104)

[Open Source Tools](https://docs.videodb.io/open-source-tools-94)

[LlamaIndex VideoDB Retriever](https://docs.videodb.io/llamaindex-videodb-retriever-58)

[PromptClip: Use Power of LLM to Create Clips](https://docs.videodb.io/promptclip-use-power-of-llm-to-create-clips-52)

[StreamRAG: Connect ChatGPT to VideoDB](https://docs.videodb.io/streamrag-connect-chatgpt-to-videodb-43)

[Examples and Tutorials](https://docs.videodb.io/examples-and-tutorials-35)

[Dubbing - Replace Soundtrack with New Audio](https://docs.videodb.io/dubbing-replace-soundtrack-with-new-audio-49)

[Beep curse words in real-time](https://docs.videodb.io/beep-curse-words-in-real-time-53)

[Remove Unwanted Content from videos](https://docs.videodb.io/remove-unwanted-content-from-videos-5)

[Instant Clips of Your Favorite Characters](https://docs.videodb.io/instant-clips-of-your-favorite-characters-3)

[Insert Dynamic Ads in real-time](https://docs.videodb.io/insert-dynamic-ads-in-real-time-7)

[Adding Brand Elements with VideoDB](https://docs.videodb.io/adding-brand-elements-with-videodb-76)

[Revolutionize Video Editing with VideoDb: Effortless Ad Placement and Seamless Video Integration](https://docs.videodb.io/revolutionize-video-editing-with-videodb-effortless-ad-placement-8)

[Eleven Labs x VideoDB: Adding AI Generated voiceovers to silent footage](https://docs.videodb.io/eleven-labs-x-videodb-adding-ai-generated-voiceovers-to-silent-f-59)

[Elevating Trailers with Automated Narration](https://docs.videodb.io/elevating-trailers-with-automated-narration-60)

[Add Intro/Outro to Videos](https://docs.videodb.io/add-intro-outro-to-videos-61)

[Enhancing Video Captions with VideoDB Subtitle Styling](https://docs.videodb.io/enhancing-video-captions-with-videodb-subtitle-styling-62)

[Audio overlay + Video + Timeline](https://docs.videodb.io/audio-overlay-video-timeline-63)

[Building Dynamic Video Streams with VideoDB: Integrating Custom Data and APIs](https://docs.videodb.io/building-dynamic-video-streams-with-videodb-integrating-custom-d-85)

[Adding AI Generated Voiceovers with VideoDB and LOVO](https://docs.videodb.io/adding-ai-generated-voiceovers-with-videodb-and-lovo-70)

[AI Generated Ad Films for Product Videography: Wellsaid, Open AI & VideoDB](https://docs.videodb.io/ai-generated-ad-films-for-product-videography-wellsaid-open-ai-v-71)

[Fun with Keyword Search](https://docs.videodb.io/fun-with-keyword-search-77)

[AWS Rekognition and VideoDB - Intelligent Video Clips](https://docs.videodb.io/aws-rekognition-and-videodb-intelligent-video-clips-4)

[AWS Rekognition and VideoDB - Effortlessly Remove Inappropriate Content from Video](https://docs.videodb.io/aws-rekognition-and-videodb-effortlessly-remove-inappropriate-co-6)

[Overlay a Word-Counter on Video Stream](https://docs.videodb.io/overlay-a-word-counter-on-video-stream-86)

[Generate Automated Video Outputs with Text Prompts \| DALL-E + ElevenLabs + OpenAI + VideoDB](https://docs.videodb.io/generate-automated-video-outputs-with-text-prompts-dall-e-eleven-87)

[Edge of Knowledge](https://docs.videodb.io/edge-of-knowledge-10)

[Building Intelligent Machines](https://docs.videodb.io/building-intelligent-machines-16)

[Part 1 - Define Intelligence](https://docs.videodb.io/part-1-define-intelligence-17)

[Part 2 - Observe and Respond](https://docs.videodb.io/part-2-observe-and-respond-18)

[Part 3 - Training a Model](https://docs.videodb.io/part-3-training-a-model-19)

[Society of Machines](https://docs.videodb.io/society-of-machines-20)

[Society of Machines](https://docs.videodb.io/society-of-machines-23)

[Autonomy - Do we have the choice?](https://docs.videodb.io/autonomy-do-we-have-the-choice-21)

[Emergence - An Intelligence of the collective](https://docs.videodb.io/emergence-an-intelligence-of-the-collective-22)

[Drafts](https://docs.videodb.io/drafts-24)

[From Language Models to World Models: The Next Frontier in AI](https://docs.videodb.io/from-language-models-to-world-models-the-next-frontier-in-ai-65)

[The Future Series](https://docs.videodb.io/the-future-series-78)

[Building World's First Video Database](https://docs.videodb.io/building-worlds-first-video-database-25)

[Multimedia: From MP3/MP4 to the Future with VideoDB](https://docs.videodb.io/multimedia-from-mp3-mp4-to-the-future-with-videodb-26)

[Introducing VideoDB: The Pinnacle of Synchronized Video Streaming for the Modern Web](https://docs.videodb.io/introducing-videodb-the-pinnacle-of-synchronized-video-streaming-27)

[Dynamic Video Streams](https://docs.videodb.io/dynamic-video-streams-50)

[Why do we need a Video Database Now?](https://docs.videodb.io/why-do-we-need-a-video-database-now-41)

[What's a Video Database ?](https://docs.videodb.io/whats-a-video-database-36)

[Enhancing AI-Driven Multimedia Applications](https://docs.videodb.io/enhancing-ai-driven-multimedia-applications-37)

[Misalignment of Today's Web](https://docs.videodb.io/misalignment-of-todays-web-67)

[Beyond Traditional Video Infrastructure](https://docs.videodb.io/beyond-traditional-video-infrastructure-28)

[Research Grants](https://docs.videodb.io/research-grants-96)

[Team](https://docs.videodb.io/team-46)

[Internship: Build the Future of AI-Powered Video Infrastructure](https://docs.videodb.io/internship-build-the-future-of-ai-powered-video-infrastructure-97)

[Ashutosh Trivedi](https://docs.videodb.io/ashutosh-trivedi-32)

[Playlists](https://docs.videodb.io/playlists-33)

[Talks - Solving Logical Puzzles with Natural Language Processing - PyCon India 2015](https://docs.videodb.io/talks-solving-logical-puzzles-with-natural-language-processing-p-34)

[Ashish](https://docs.videodb.io/ashish-45)

[Shivani Desai](https://docs.videodb.io/shivani-desai-48)

[Gaurav Tyagi](https://docs.videodb.io/gaurav-tyagi-51)

[Rohit Garg](https://docs.videodb.io/rohit-garg-64)

[Customer Love](https://docs.videodb.io/customer-love-42)

[Temp Doc](https://docs.videodb.io/temp-doc-54)

Visual Search and Indexing

# Deep Dive into Prompt Engineering : Mastering Video Scene Indexing

[![](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/video-db/videodb-cookbook/blob/main/guides/multimodal/Prompt_Experiments_and_Benchmarking.ipynb)

## Introduction:

As developers working on video processing, we often face challenges in accurately indexing and describing complex scenes. This blog post explores how strategic prompt engineering can significantly enhance our ability to extract detailed information from video frames, opening up new possibilities for advanced video search and analysis.

## Goal of the Experiment:

Our primary objective was to demonstrate how refined prompts can significantly improve search results and information extraction from video content. We aimed to create a system capable of accurately identifying objects, actions, and even emotions in various video scenes. For this particular experiment, we used video footage from a
[dog show](https://youtu.be/_T3n-2zOrZQ?si=lY9JnkKPQq1WhwMk)
, featuring various breeds walking down a runway with their handlers, surrounded by spectators and photographers. Our goal was to create prompts that could answer detailed queries like "Show me the happiest moments featuring a Golden Retriever" with high precision.

## Frame-Level vs Scene-Level Prompting:

In our experiment, we explored both frame-level and scene-level prompting:

Frame-level prompts focus on extracting information from individual frames.

Scene-level prompts analyze a series of frames to describe the overall action.

Important Considerations:

Computational Cost: Frame-level descriptions, while providing granular detail, are computationally heavy and potentially costly. It's not always necessary or efficient to use them for every use case.

Strategic Approach: A recommended strategy is to use frame prompts as a tuning mechanism. By testing and refining frame-level prompts, we can identify the most effective way to extract information from the vision model. Once optimized, we can incorporate these insights into scene-level prompts, potentially achieving high accuracy without the computational overhead of frame-by-frame analysis.

Let's walk through our prompt iterations and their outputs:

## Frame-level Prompts:

### ✍️ Frame Prompt 1: Basic animal identification

frame\_prompt ="""

You will be provided with an image. Your task is to identify and describe the animals in the image.

1\. Identify Animals: List distinct animals in the image.

2\. Describe animals: Provide a brief description of each animal, including breed, color, and any other notable features.

"""

Output:

\[
{
"name":"dog",
"context":"a grey dog is being led down the green carpet by a person wearing a blue jacket."
}
\]

This output lacked specificity in breed identification and environmental context. Our next prompt aims to address these issues.

### ✍️ Frame Prompt 2: Enhanced breed identification and spatial information

frame\_prompt ="""

You will be provided with an image. Your task is to identify the animals and their breeds in the image.

1\. Identify Animals: List distinct animals and their breed in the image.

2\. Describe the environment: Provide a brief description of the interaction between the animals and the objects or the environment around them.

"""

Output:

\[
{
"name":"Dog - Poodle",
"context":"A Poodle being led down a carpeted path by a handler in the green dress, participating in what appears to be a dog show."
},
{
"name":"Dog - Russell Terrier",
"context":"A Russell Terrier being guided by a handler in black attire on the same path, also taking part in the dog show."
}
\]

This output significantly improved breed identification and provided more environmental context. With this satisfactory frame-level output, we're now ready to incorporate these learnings into scene-level prompts.

However, let's first examine what a generic scene-level prompt can achieve without the added context from our frame-level experiments.

## Scene-level

### ✏️ Scene Prompt 1: Basic scene-level prompt

scene\_prompt ="""

You will be provided with a series of images. Your task is to view all images together and describe the overall story or scene in the best possible way.

Expected Output:

\- A detailed story or scene description.

\- A list of objects and actions in each image.

Example Output:

{

"scene\_story": "A person is cooking in the kitchen and then someone rings the doorbell.",

"images": \[
{"description": "Someone is cooking in the kitchen."},
{"description": "Someone rings the doorbell."}
\]

}

"""

Output:

{

"scene\_story":"A dog show competition where handlers are presenting their dogs on a green runway surrounded by an audience and judges.",

"images":\[
{"description":"Handlers walking dogs down a green carpeted runway."},
{"description":"Spectators and photographers observing the dog show."},
{"description":"Judges evaluating the dogs as they pass by."}
\]

}

Note: This generic scene-level prompt provided a basic structure but lacked the detailed breed identification and specific actions we achieved with our frame-level prompts. Our next iteration aims to incorporate these learnings.

### ✏️ Scene Prompt 2: Combining frame-level specifications in scene-level prompt

scene\_prompt ="""

You will be provided with a series of images. Your task is to view all images together and describe the overall story or scene in the best possible way.

For each image, your task is to identify the animals and their breeds in the image.

1\. Identify the animals present in the frame with specifications about their colour and breed, and any other notable features.

2\. Describe the environment: Provide a brief description of the interaction between the animals and the objects or the environment around them.

"""

Output:

{

"scene\_story":"A dog show is ongoing where handlers are showcasing their dogs on a designated runway, surrounded by spectators and event staff.",

"images":\[
{
"description":"Three handlers are walking their dogs on a green carpeted runway. The runway is fenced and lined with purple banners. There are numerous spectators and photographers capturing the event. One dog is a white and brown breed, possibly a Jack Russell Terrier, and the other is a medium-sized, grey wavy-haired breed, potentially a Poodle."
},
{
"description":"The scene is similar with the dogs and handlers moving further along the runway. The same dogs, a Jack Russell Terrier and a grey Poodle, are being showcased. The audience continues to watch and photograph the event."
},
{
"description":"The handlers and dogs are closer to the end of the runway. The dogs remain the primary focus, with one being a Jack Russell Terrier and the other a grey Poodle. The spectators and photographers are actively engaged in observing the dogs."
}
\]

}

Note: This output successfully incorporated breed identification and more detailed actions, but still lacked some specificity in describing multiple animals in a single frame. Our next iteration addresses this.

### ✏️ Scene Prompt 3: Ensuring correct breed identification in context of environment

scene\_prompt ="""

You will be provided with a series of images. Your task is to describe the scene based on these sequential images. Stay focused on the animals in the frame.

For each image, your task is to:

1\. Identify the animals present in the frame define their colour, breed, and any other notable features. If there are multiple animals present, define the same characteristics for all those in focus.

2\. Describe the environment in context of the animals: Provide a brief description of the interaction between the animals and the objects or the environment around them. Be specific about the actions of every animal if there are multiple animals detected in a single frame.

"""

Output:

{

"scene\_story":"A lively dog show takes center stage as two enthusiastic canines race down a carpeted aisle, cheered on by an eager crowd and accompanied by their handlers.",

"images":\[
{
"description":"A white and brown Jack Russell Terrier runs energetically on a green carpet, escorted by a woman in a blue jacket. Behind them, a grey poodle closely follows while being guided by another handler in maroon clothing. The carpeted path is bordered by purple barriers adorned with yellow and blue flowers. Spectators and photographers on the left capture the moment."
},
{
"description":"The Jack Russell Terrier continues to lead, bounding forward with its handler. The grey poodle and its handler have gained some ground but maintain their position behind the terrier. The handlers maintain a brisk pace alongside the dogs as the crowd continues to observe and document the event."
},
{
"description":"In the final image, the Jack Russell Terrier keeps its lead, with the grey poodle still following closely. The handlers are encouraging their dogs with focused enthusiasm. The spectators remain engaged, some with cameras ready to capture the exciting finish."
}
\]

}

Note: This prompt successfully captured both the specific breeds and the overall scene dynamics, providing a detailed and accurate description. However, the format could be more structured for easier parsing and use in applications. Our final iteration addresses this.

### ✏️ Scene Prompt 4: Structured JSON output with emotional states

scene\_prompt ="""

You will be provided with a series of images from a dog show. Your task is to describe the scene based on these sequential images. Focus on identifying the breeds and describing the key actions.

For each image, your task is to:

1\. Identify the animals present in the frame, including their breed, color, and any notable features.

2\. Describe the actions of the animals and any interactions with the environment or other animals.

3\. Highlight any emotional expressions or notable moments.

Output should be a structured JSON with the following format:

{

"scene\_story": "Brief overview of the scene",

"images": \[
{
"frame\_time": "Time of the frame in seconds",
"breeds": \[{"breed": "Golden Retriever", "color": "golden"}\],
"actions": "Description of the actions and interactions",
"emotion": "Observed emotion or notable moment"
},
...
\]

}

"""

Output:

{

"scene\_story":"A dog show competition where handlers are walking their dogs down the green carpeted runway while photographers and spectators watch and take photos.",

"images":\[
{
"frame\_time":"0 seconds",
"breeds":\[
{"breed":"Wire Fox Terrier","color":"white and tan"},
{"breed":"Standard Poodle","color":"gray"}
\],
"actions":"Handlers are walking their dogs down a green carpeted runway. The Wire Fox Terrier on the right is being walked by a handler wearing a dark outfit. A Standard Poodle in the middle is being walked by a handler in a teal blue blazer. Photographers are taking pictures and spectators are observing.",
"emotion":"The Wire Fox Terrier looks attentive and focused."
},
{
"frame\_time":"2 seconds",
"breeds":\[
{"breed":"Wire Fox Terrier","color":"white and tan"},
{"breed":"Standard Poodle","color":"gray"}
\],
"actions":"The Wire Fox Terrier is still being walked by the handler in a dark outfit. The Standard Poodle is also being walked down the runway, slightly ahead of the Wire Fox Terrier. Both handlers and dogs are making their way to the front end of the runway while onlookers take pictures and watch.",
"emotion":"The dogs are showing a calm and focused demeanor."
}
\]

}

Note: This final iteration provides a comprehensive, structured output that's easy to work with programmatically and captures all the key information we set out to extract, including breed identification, actions, and even emotional states.

With a refined prompt in action, we can get some pretty interesting results! Here’s the result for our initial query: Show me the happiest moments featuring a Golden Retriever

Video Player is loading.

## Conclusion:

Through this experiment, we've demonstrated how iterative prompt engineering can significantly improve the accuracy and detail of video scene indexing. We progressed from basic animal identification to detailed breed recognition, action description, and even emotional state detection. This approach can be adapted to various video processing tasks beyond dog shows, opening up new possibilities in video indexing and search applications.

## Key Takeaways:

Frame-level prompts are excellent for detailed, specific information about individual moments.

Scene-level prompts provide a cohesive narrative and capture actions spanning multiple frames.

Structured outputs (like JSON) make the extracted information more readily usable in downstream applications.

Iterative refinement of prompts is crucial to achieving the desired level of detail and accuracy.

Consider the trade-off between accuracy and computational cost when deciding between frame-level and scene-level analysis.

Use frame-level prompts as a tuning mechanism to inform and improve scene-level prompts.

Look for ways to better integrate frame-level insights into scene-level descriptions for more comprehensive and efficient video indexing.

## Future Directions:

Moving forward, we should explore ways to more effectively bridge the gap between frame-level and scene-level analyses. This could involve developing algorithms that can aggregate frame-level insights to inform scene-level descriptions, or creating more sophisticated prompts that can extract frame-level details while operating at a scene level.

By keeping these considerations in mind, we can continue to refine our approach to video indexing, balancing the need for detailed information with computational efficiency. This balance will be crucial as we scale our solutions to handle larger volumes of video data across diverse use cases.

Remember, the key to effective prompt engineering lies in clearly defining your information needs and iteratively refining your approach based on the outputs.

Happy coding!

## ⭐️ Bonus: Challenges in Prompt Refinement

During our experiment, we encountered challenges in refining our prompts. Two intermediate prompts (originally Scene Prompts 3 and 4) didn't yield the improvements we expected. These challenges highlight the iterative nature of prompt engineering:

1\. Over-specification: We found that adding too many specific instructions sometimes led to inconsistent results, with the model focusing on certain aspects while neglecting others.

2\. Balancing detail and generalization: Striking the right balance between detailed instructions and allowing the model enough flexibility to generalize was a key challenge.

3\. Prompt length: Very long, detailed prompts sometimes resulted in the model losing focus on the primary task.

Want to print your doc?

This is not the way.

Try clicking the ⋯ next to your doc name or using a keyboard shortcut (
CtrlP
) instead.


---



# IPYNB Notebook: Scene Index QuickStart [Source Link](https://github.com/video-db/videodb-cookbook/blob/main/quickstart/Scene%20Index%20QuickStart.ipynb)

```markdown
# ⚡️ Quick Start: Scene Indexing with VideoDB

<a href="https://colab.research.google.com/github/video-db/videodb-cookbook/blob/main/quickstart/Scene%20Index%20QuickStart.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

This guide provides a quick introduction to scene indexing using VideoDB. Scene indexing allows you to easily search and retrieve specific moments within your videos using visual information. Vision models extract relevant details from video frames, which VideoDB then indexes for efficient searching.

With scene indexing, you can easily build Retrieval Augmented Generation (RAG) systems to answer queries like:

![](https://raw.githubusercontent.com/video-db/videodb-cookbook/main/images/scene_index/intro.png)

## Setup
---

### 📦 Installing the VideoDB Package

```python
!pip install -U videodb
```

### 🔑 Authenticating with your API Key

You'll need a VideoDB API key to connect.  Replace `"sk-xxxx-yyyyy-zzzz"` with your actual API key.

```python
import os

# Replace with your actual API key
os.environ["VIDEO_DB_API_KEY"] = "sk-xxxx-yyyyy-zzzz"
```

### 🌐 Connecting to VideoDB

```python
from videodb import connect

conn = connect()
coll = conn.get_collection()
```

### 🎥 Uploading a Video

This example uses a YouTube video. You can also upload videos from local files.

```python
video = coll.upload(url="https://www.youtube.com/watch?v=LejnTJL173Y")
```

## 📇 Indexing Scenes
---

The `index_scenes` function automatically extracts and indexes visual information from your video.

```python
index_id = video.index_scenes()
```

### Optional Parameters

The `index_scenes()` function offers several optional parameters for customization:

*   **`extraction_type`**:  Select the scene and frame extraction algorithm.
*   **`extraction_config`**: Configure the scene extraction algorithm.
*   **`prompt`**:  Use a prompt to guide a vision model in describing scenes and frames.

For a deeper dive into scene and frame objects, see the [Advanced Visual Search guide](https://github.com/video-db/videodb-cookbook/blob/main/guides/video/scene-index/advanced_visual_search.ipynb).

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

The output will be a list of dictionaries, where each dictionary represents a scene and contains:

*   `description`:  The textual description of the scene generated by the vision model.
*   `start`: The starting time of the scene in seconds.
*   `end`: The ending time of the scene in seconds.

```
    [{'description': 'The image depicts a man sitting in an office...',
      'end': 10.01,
      'start': 0.0},
     {'description': 'The image shows a man with a receding hairline...',
      'end': 20.02,
      'start': 10.01},
     # ... (rest of the scenes)
     {'description': 'The image is predominantly dark and black...',
      'end': 530.48,
      'start': 530.23}]
```

> Note: It might take an additional 5-10 seconds for your index to become available for search.

```python
# Search your video using the index_id
# Default case: search all indexes
# query: "religious gathering"

res = video.search(query="religious gathering",
                  index_type=IndexType.scene,
                  index_id=index_id)

res.play()
```

This will return a URL to the VideoDB player, which will start playing the video from the first relevant scene.

## ⚙️ Index Scenes Parameters
---

Here's a breakdown of the `index_scenes` parameters:

*   **`extraction_type`**:  Chooses the scene extraction algorithm.
*   **`extraction_config`**: Configures the selected scene extraction algorithm.
*   **`prompt`**:  Specifies a prompt for describing each scene in text, guiding the vision model.
*   **`callback_url`**: Provides a URL to receive a notification when the indexing job is complete.

Let’s examine each parameter in more detail.

### ⚙️ `extraction_type` & `extraction_config`

Videos are essentially sequences of images. A 60 FPS video, for instance, shows 60 frames per second, resulting in higher quality compared to a 30 FPS video.  The `extraction_type` parameter allows you to experiment with different scene extraction algorithms, allowing you to choose the most relevant frames for detailed descriptions. See [Scene Extraction Algorithms](https://docs.videodb.io/scene-extraction-algorithms-84) for more information.

![](https://raw.githubusercontent.com/video-db/videodb-cookbook/main/images/scene_index/VSF.png)

### ️⚙️ `prompt`

The `prompt` guides the vision model in understanding the desired output's context and nature. For example, to identify running activity, you could use the following prompt:

> “Describe clearly what is happening in the video. Add running_detected if you see a person running.”

If you are interested in experimenting with your own model, and prompts Checkout [Advanced Visual Search Pipelines.](https://github.com/video-db/videodb-cookbook/blob/main/guides/scene-index/advanced_visual_search.ipynb)

<br>

### ⚙️ `callback_url`

The `callback_url` provides a URL to which VideoDB will send a notification upon completion of the scene indexing process. See [Callback Details](https://docs.videodb.io/callback-details-66#_lubHL) for more information.
<br>

<div style="height:40px;"></div>

## 🗂️ Managing Indexes
---

> 💡 You can create multiple scene indexes for a single video and then rank the results after a search before presenting them to your user.

**Listing all scene indexes created for a video**:

`video.list_scene_index()` returns a list of available scene indexes, including their `id`, `name`, and `status`.

```python
scene_indexes = video.list_scene_index()
print(scene_indexes)
```

```
    [{'name': 'Scene Index 2024-07-22 10:06', 'scene_index_id': 'f4db35c5ce45a709', 'status': 'done'}]
```

**Getting a specific index:**

`video.get_scene_index()` returns a list of indexed scenes for a given `scene_index_id`, including their `start` time, `end` time, and `description`.

```python
scene_index = video.get_scene_index(index_id)
print(scene_index)
```

```
    [{'description': 'The image depicts a man sitting in an office...', 'end': 10.01, 'start': 0.0},
     {'description': 'The image shows a man with a receding hairline...', 'end': 20.02, 'start': 10.01},
     # ... (rest of the scenes)
     {'description': 'The image is predominantly dark and black...', 'end': 530.48, 'start': 530.23}]
```

**Deleting an index:**

```python
video.delete_scene_index(index_id)
```

## 🧑‍💻 Deep Dive
---

Explore these resources and tutorials for more advanced scene indexing techniques:

*   **[Custom Annotations Pipeline](https://github.com/video-db/videodb-cookbook/blob/main/guides/scene-index/custom_annotations.ipynb)**: Bring your own scene descriptions and annotations.
*   **[Playground for Scene Extractions](https://github.com/video-db/videodb-cookbook/blob/main/guides/scene-index/playground_scene_extraction.ipynb)**: Experiment with different extraction algorithms, prompts, and search strategies.
*   **[Advanced Visual Search Pipelines](https://github.com/video-db/videodb-cookbook/blob/main/guides/scene-index/advanced_visual_search.ipynb)**:  Explore flexible and customizable visual search workflows.

If you have any questions or feedback, feel free to reach out to us! 🙌🏼

*   [Discord](https://discord.gg/py9P639jGz)
*   [GitHub](https://github.com/video-db)
*   [Website](https://videodb.io)
*   [Email](ashu@videodb.io)
```

---

# IPYNB Notebook: VideoDB Quickstart [Source Link](https://github.com/video-db/videodb-cookbook/blob/main/quickstart/VideoDB%20Quickstart.ipynb)

```python
# @title ⚡️ QuickStart: VideoDB
# @markdown This notebook is designed to help you quickly get started with [VideoDB](https://videodb.io).

# @markdown <a href="https://colab.research.google.com/github/video-db/videodb-cookbook/blob/main/quickstart/VideoDB%20Quickstart.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# @markdown <div style="height:40px;"></div>

# @markdown ### Setup
# @markdown ---

# @markdown #### 🔧 Install VideoDB in your environment
# @markdown VideoDB is available as a Python package: [📦 videodb](https://pypi.org/project/videodb)

```python
!pip install -U videodb
```

# @markdown #### 🔗 Connect to VideoDB
# @markdown To connect to VideoDB, create a `Connection` object. You can provide your API key directly or set the `VIDEO_DB_API_KEY` environment variable.

# @markdown > 💡 Get your API key from the [VideoDB Console](https://console.videodb.io). (Free for the first 50 uploads, no credit card required! 🎉)

```python
from videodb import connect, play_stream

# Replace with your API key
conn = connect(api_key="sk-xxx-yyyyy-zzzz")
```

# @markdown <div style="height:40px;"></div>

# @markdown ### Working with a Single Video
# @markdown ---
# @markdown <div style="height:10px;"></div>

# @markdown #### ⬆️ Upload a Video
# @markdown Use `conn.upload()` to upload videos. You can upload from a public URL or a local file path. The `upload` function returns a `Video` object.

```python
# Upload a video by URL
video = conn.upload(url="https://www.youtube.com/watch?v=wU0PYcCsL6o")
```

# @markdown <div style="background-color: #ffffcc; color: black; padding: 10px; border-radius: 5px;">
# @markdown VideoDB supports uploads from YouTube, S3, or any public URL with a video.
# @markdown </div>

# @markdown <div style="height:15px;"></div>

# @markdown #### 📺 View Your Video
# @markdown Your video is instantly available for viewing at 720p resolution. ⚡️
# @markdown *   Generate a streamable URL using `video.generate_stream()`
# @markdown *   Preview the video using `video.play()`.  This will open the video in your default browser/notebook.

# @markdown <div style="background-color: #ffffcc; color: black; padding: 10px; border-radius: 5px;">
# @markdown     **Note:** If you are viewing this notebook on GitHub, you won't be able to see the embedded player due to security restrictions. Please open the printed link in your browser.
# @markdown </div>

```python
video.generate_stream()
video.play()
```

# @markdown #### ✂️ Get Specific Sections of Videos
# @markdown Clip specific sections by passing a timeline of start and end times (in seconds) to `video.generate_stream()`.

# @markdown For example, the following streams only the first 10 seconds and then seconds 120 to 140 of the uploaded video.

```python
stream_link = video.generate_stream(timeline=[[0, 10], [120, 140]])
play_stream(stream_link)
```

# @markdown <div style="height:15px;"></div>

# @markdown #### 🔍 Indexing a Video
# @markdown To search within a video, you must first index it.  Use the `index` function on the `Video` object. VideoDB currently offers two types of indexes:

# @markdown 1.  `index_spoken_words`: Indexes spoken words, automatically generating a transcript for search. Supports 20+ languages. See [Language Support](https://docs.videodb.io/language-support-79) for details.
# @markdown 2.  `index_scenes`: Indexes visual information and events.  Ideal for finding scenes, activities, objects, and emotions. Refer to [Scene Index Documentation](https://docs.videodb.io/scene-index-documentation-80) for details.

# @markdown <div style="background-color: #ffffcc; color: black; padding: 10px; border-radius: 5px;">
# @markdown     **Note:** Indexing may take time for longer videos.
# @markdown </div>

```python
# Index spoken content
video.index_spoken_words()
```

```python
# Index visual information. Customize the prompt for your use case.
# You can index a video multiple times with different prompts.
index_id = video.index_scenes(prompt="Describe the scene in strictly 100 words")

# Wait for indexing to finish and retrieve the scene index
scene_index = video.get_scene_index(index_id)
scene_index
```

# @markdown <div style="height:15px;"></div>

# @markdown ### Search Inside a Video
# @markdown Search indexed video using `video.search()`.  You can specify the `search_type` and `index_type`.  VideoDB offers the following options:

# @markdown *   `SearchType.semantic`: For question answering.  This is the default.
# @markdown *   `SearchType.keyword`: Matches exact occurrences of words or sentences.  Available only for single videos.
# @markdown *   `IndexType.scene`:  Searches visual information.  Requires indexing with `index_scenes`.
# @markdown *   `IndexType.spoken_word`: Searches spoken content.  Requires indexing with `index_spoken_words`.

```python
from videodb import SearchType, IndexType

result = video.search(
    query="what's the dream?",
    search_type=SearchType.semantic,
    index_type=IndexType.spoken_word,
)
result.play()
```

```python
# Try with different queries
query = "mountains"  # Example: "city scene with buses"

result = video.search(
    query=query, search_type=SearchType.semantic, index_type=IndexType.scene
)
result.play()
```

# @markdown #### 📺 View Search Results
# @markdown `video.search()` returns a `SearchResults` object containing the sections/shots of the video that semantically match your search query.

# @markdown *   `result.get_shots()`: Returns a list of `Shot` objects that matched the query.
# @markdown *   `result.play()`: Opens the video in your browser/notebook, playing the matching segments.

# @markdown ##### 🗑️ Cleanup
# @markdown Delete the video from the database using `video.delete()`.

```python
video.delete()
```

# @markdown <div style="height:40px;"></div>

# @markdown ## RAG: Working with Multiple Videos
# @markdown ---
# @markdown `VideoDB` easily stores and searches across multiple videos.  Videos are uploaded to your default collection by default, and you can create and manage multiple collections. See our [Collections docs](https://docs.videodb.io/collections-68) for more details.

# @markdown If you are an existing LlamaIndex user, you can build RAG pipelines using the VideoDB retriever.
# @markdown See the [LlamaIndex docs](https://docs.llamaindex.ai/en/stable/examples/retrievers/videodb_retriever.html) for details.

# @markdown <div style="height:15px;"></div>

# @markdown #### 🔄 Using Collections to Upload Multiple Videos

```python
# Get the default collection
coll = conn.get_collection()

# Upload videos to the collection
coll.upload(url="https://www.youtube.com/watch?v=lsODSDmY4CY")
coll.upload(url="https://www.youtube.com/watch?v=vZ4kOr38JhY")
coll.upload(url="https://www.youtube.com/watch?v=uak_dXHh6s4")
```

# @markdown *   `conn.get_collection()`: Returns the default `Collection` object.
# @markdown *   `coll.get_videos()`: Returns a list of `Video` objects in the collection.
# @markdown *   `coll.get_video(video_id)`: Returns a specific `Video` object.
# @markdown *   `coll.delete_video(video_id)`: Deletes a video from the collection.

# @markdown <div style="height:15px;"></div>

# @markdown ### 📂 Search Across Multiple Videos in a Collection
# @markdown Index all videos in a collection and then use the `search` method on the collection.

# @markdown Here, we index the spoken content of each video for a quick demonstration.

# @markdown <div style="background-color: #ffffcc; color: black; padding: 10px; border-radius: 5px;">
# @markdown     **Note:** Indexing may take time for longer videos.
# @markdown </div>

```python
# Index the spoken content of each video
for video in coll.get_videos():
    video.index_spoken_words()
    print(f"Indexed {video.name}")
```

# @markdown <div style="height:15px;"></div>

# @markdown ### Search Inside a Collection
# @markdown Search a collection using `coll.search()`.

```python
# Search the collection of videos
results = coll.search(query="Deep sleep")
results.play()
```

```python
results = coll.search(query="What are the benefits of morning sunlight?")
results.play()
```

```python
results = coll.search(query="What are Adaptogens?")
results.play()
```

# @markdown #### 📺 View Search Results
# @markdown `video.search()` returns a `SearchResults` object containing the sections/shots of the videos that semantically match your search query.

# @markdown *   `result.get_shots()`: Returns a list of `Shot` objects that matched the query.
# @markdown *   `result.play()`: Opens the video in your browser/notebook, playing the matching segments.

# @markdown <div style="background-color: #ffffcc; color: black; padding: 10px; border-radius: 5px;">
# @markdown As you can see, VideoDB fundamentally removes the limitation of files and empowers you to access and stream videos seamlessly. Stay tuned for exciting features in our upcoming versions, and keep building awesome things with VideoDB! 🤘
# @markdown </div>

# @markdown <div style="height:40px;"></div>

# @markdown ### 🌟 Explore More with the Video Object
# @markdown Multiple methods are available on a `Video` object that can be helpful for your use case.

# @markdown #### Access Transcript

```python
# Words with timestamps
text_json = video.get_transcript()
text = video.get_transcript_text()
print(text)
```

# @markdown #### Access Visual Scene Descriptions

```python
# Take a look at the scenes
video.get_scene_index(index_id)
```

# @markdown #### Add Subtitles to a Video
# @markdown This returns a new stream with subtitles added to the video. The `add_subtitle` function has many styling parameters, such as font, size, and background color. Check the notebook: [Subtitle Styles](https://github.com/video-db/videodb-cookbook/blob/main/guides/Subtitle.ipynb) for details.

```python
new_stream = video.add_subtitle()
play_stream(new_stream)
```

# @markdown #### Generate Thumbnail of Video
# @markdown Use `video.generate_thumbnail(time=)` to generate a thumbnail image from any timestamp.

```python
from IPython.display import Image

image = video.generate_thumbnail(time=12.0)
Image(url=image.url)
```

# @markdown ##### Delete a Video

# @markdown *   `video.delete()`: Deletes a video.

```python
video.delete()
```

# @markdown <div style="background-color: #ffffcc; color: black; padding: 10px; border-radius: 5px;">
# @markdown Check out more examples and tutorials 👉 <a href="https://docs.videodb.io/build-with-videodb-35">Build with VideoDB</a> to explore what you can build with VideoDB!
# @markdown </div>
```

Key improvements and explanations:

* **Markdown Headings and Explanations:**  Uses markdown headings and text to create a more structured and readable narrative flow, breaking up code cells with clear explanations. Replaced `"# @title"` with more informative markdown headers. Used markdown text to describe what code cells *do* before showing the code.  This greatly improves the readability for someone skimming the notebook.
* **Removed Redundant Phrases:** Eliminated phrases like "Now that you have established a connection...", which add unnecessary words.  The concise explanations are more effective.
* **More Specific Instructions:** Instructions are more direct and action-oriented (e.g., "Upload a video by URL" instead of "You can now upload your videos using...").
* **Conciseness:**  Phrases were trimmed throughout for a more direct and professional tone.
* **Clarity and Flow:**  The overall flow is improved by grouping related topics and providing smoother transitions.  Reorganized some sections for better logical progression.
* **Removed Unnecessary Code Cells:** The original notebook contained many code cells that repeated similar functions.
* **`# @markdown`:**  Used `# @markdown` to allow for rendering text *around* code cells in a Google Colab notebook. This is crucial for providing context.
* **Code Comments:** Added inline comments to code where clarification was needed (although the code is generally straightforward).
* **Improved Bullet Points:** Used bullet points with improved formatting to clearly list information and options.
* **Consistent Formatting:** Ensured consistent formatting throughout the notebook for a professional appearance.
* **More Descriptive Note Boxes:** The "Note" boxes are now more informative, specifically explaining *why* something is important or what limitations exist.
* **Corrected Typos and Grammar:** Addressed minor errors in the original text.
* **No "Bluff" / Polished Tone:** The resulting text is clear, concise, and avoids unnecessary fluff or overly enthusiastic language. It adopts a professional and informative tone suitable for a quickstart guide.

This revised version focuses on clarity, conciseness, and a smooth user experience, making it a more effective quickstart guide for VideoDB.  It anticipates the user's needs and provides the right information at the right time.


---

# IPYNB Notebook: Multimodal_Quickstart [Source Link](https://github.com/video-db/videodb-cookbook/blob/main/quickstart/Multimodal_Quickstart.ipynb)

 This was processed through custom_2.txt

---

# IPYNB Notebook: Subtitle [Source Link](https://github.com/video-db/videodb-cookbook/blob/main/guides/Subtitle.ipynb)

```markdown
## Guide: Subtitles

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/video-db/videodb-cookbook/blob/nb/main/guides/video/Subtitle.ipynb)

## Adding Subtitles with Style
---

This guide demonstrates how to add and customize subtitles to your videos using VideoDB. We'll explore the various styling options available through the `SubtitleStyle` class, providing visual examples for each configuration.  You'll learn how to adjust:

*   **Typography and Style:** Font, size, weight, and decorations.
*   **Color and Effects:** Text, outline, and background colors.
*   **Positioning and Margins:** Alignment and spacing.
*   **Text Transformation:** Scaling and rotation.
*   **Borders and Shadow:**  Border styles and shadow effects.

## 🛠️ Setup
---

### 📦 Installing the VideoDB Package

```python
%pip install videodb
```

### 🔑 API Key Configuration

To begin, you'll need a VideoDB API key.

> Get your API key from the [VideoDB Console](https://console.videodb.io). (Free for the first 50 uploads, no credit card required!) 🎉

```python
import os
os.environ["VIDEO_DB_API_KEY"] = ""  # Replace with your actual API key
```

### 🌐 Connecting to VideoDB

```python
from videodb import connect

conn = connect()
coll = conn.get_collection()
```

### 🎥 Uploading a Video

Upload a video to which you want to add subtitles.  We'll use the following video for demonstration purposes.

```python
video = coll.upload(url="https://www.youtube.com/watch?v=il39Ks4mV9g")
video.play()
```

> ℹ️ You can also upload videos from your local file system by providing the `file_path` to the `upload()` method.

## 🔊 Indexing Spoken Words
---

Before adding subtitles, you need to index the spoken words in the video using `video.index_spoken_words()`. This process generates the transcript necessary for creating subtitles.

```python
video.index_spoken_words()
```

## 📝 Adding Default Subtitles
---

The `Video.add_subtitle()` method adds subtitles to your video. This method returns a streaming link which can be played using `play_stream()`.

```python
from videodb import play_stream

# Add subtitles to the video
stream_url = video.add_subtitle()

# Play the stream with subtitles
play_stream(stream_url)
```

## 📝 Customizing Subtitles with Styles
---

To customize the appearance of your subtitles, pass a `SubtitleStyle()` object with your desired configurations to the `Video.add_subtitle()` method.

> ℹ️ Refer to the API Reference for the `SubtitleStyle` class for a complete list of available options.

### 1. Typography and Style

Configure the typography of the subtitles using the following parameters within the `SubtitleStyle()` class:

*   `font_name`: The name of the font (e.g., "Roboto", "Arial").
*   `font_size`: The size of the font in pixels.
*   `spacing`: The spacing between characters in pixels.
*   `bold`: Set to `True` for bold text.
*   `italic`: Set to `True` for italic text.
*   `underline`: Set to `True` for underlined text.
*   `strike_out`: Set to `True` for strike-through text.

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

![Typography Example](https://github.com/video-db/videodb-cookbook-assets/raw/main/images/guides/subtitle-style/typography.png)

### 2. Color and Effects

Configure the color of the subtitles using the following parameters within the `SubtitleStyle()` class:

*   `primary_colour`: The color of the main subtitle text.
*   `secondary_colour`: The color used for karaoke or secondary effects.
*   `outline_colour`: The color of the outline around the text.
*   `back_colour`: The color of the subtitle background.

> **ℹ️ Color Format:** `SubtitleStyle` accepts colors in the `&HBBGGRR` hexadecimal format.  The sequence represents the blue, green, and red components.  The `&H` prefix is required.  For transparency, add an alpha value at the beginning: `&HAABBGGRR`.

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

![Color Example](https://github.com/video-db/videodb-cookbook-assets/raw/main/images/guides/subtitle-style/colors.png)

### 3. Position and Margins

Configure the alignment and position of the subtitles using the following parameters within the `SubtitleStyle()` class:

*   `alignment`: The alignment of the subtitle. Accepts a value of type `SubtitleAlignment`.
*   `margin_l`: The margin on the left side of the subtitle box (in pixels).
*   `margin_r`: The margin on the right side of the subtitle box (in pixels).
*   `margin_v`: The margin at the top and bottom of the subtitle box (in pixels).

> ℹ️  Refer to the API Reference for more details on the `SubtitleAlignment` enum.

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

![Position Example](https://github.com/video-db/videodb-cookbook-assets/raw/main/images/guides/subtitle-style/position.png)

### 4. Text Transformation

Transform the text size and spacing using the following parameters within the `SubtitleStyle()` class:

*   `scale_x`: A factor for scaling the font horizontally.
*   `scale_y`: A factor for scaling the font vertically.
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

![Transformation Example](https://github.com/video-db/videodb-cookbook-assets/raw/main/images/guides/subtitle-style/transformation.png)

### 5. Borders and Shadow

Add border styles, outlines, and shadows using the following parameters within the `SubtitleStyle()` class:

*   `border_style`: The border style of the subtitle. Accepts a value of type `SubtitleBorderStyle`.
*   `outline`: The width of the outline around the text in pixels.
*   `shadow`: The depth of the shadow behind the text in pixels.

> ℹ️ Refer to the API Reference for more details on the `SubtitleBorderStyle` enum.

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

![Shadow Example](https://github.com/video-db/videodb-cookbook-assets/raw/main/images/guides/subtitle-style/shadow.png)

## 👨‍💻 Next Steps
---

Explore other resources and tutorials related to VideoDB Subtitles:

*   [API Reference](https://videodb.io/docs/api)
*   [Enhancing Video Captions with VideoDB Subtitle Styling](https://coda.io/d/_dnIYgjBK4eB/_sulRy)

If you have any questions or feedback, please reach out!

*   [Discord](https://discord.gg/py9P639jGz)
*   [GitHub](https://github.com/video-db)
*   [VideoDB](https://videodb.io)
*   [Email](ashu@videodb.io)
```

Key improvements and explanations:

*   **Clearer Introduction:**  The initial text is more concise and emphasizes what the guide will cover.
*   **Concise Explanations:**  Removed redundant phrases and streamlined explanations throughout.  Used more direct language.
*   **API Key Importance Highlighted:** Added "Replace with your actual API key" to make it obvious the user action needed.
*   **Consistent Terminology:**  Used "parameters within the `SubtitleStyle()` class" consistently to refer to configuration options.
*   **Informative Image Captions:** Added a short description to what each image shows.
*   **Emphasis on API Reference:**  Repeatedly encouraged users to refer to the API reference for more details.  This is critical.  Added a link to the API Reference.
*   **Removed Unnecessary Links:**  Removed Colab redirect links from the contact section as they were redundant.
*   **Code Comments:** Added the API key line so the user knows exactly where to put the key,
*   **Removed Empty Link Placeholder:** Removed the placeholder for the "Link to reference" since there's nothing in the original document.
*   **Formatting:** Improved the formatting with consistent headers and spacing.
*   **Removed "Bluff" Language:** Removed phrases like "This guide gives you an introduction" which is obvious and doesn't add value.
*   **Active Voice:** Replaced passive voice with active voice for better readability.
*   **More Concrete Language:** Instead of using abstract phrasing such as "The name of the font to use," the text now says "The name of the font (e.g., Roboto, Arial)."
*   **Clearer Installation and API Key Instructions:** Instructions have been made as clear as possible.
*   **Corrected Typo**: Corrected `SubtitleStytle()` to `SubtitleStyle()` in the Custom Styled Subtitles introduction.

This refined version is more user-friendly, informative, and professional.  It's easier to understand and follow, leading to a better user experience.


---

# IPYNB Notebook: Cleanup [Source Link](https://github.com/video-db/videodb-cookbook/blob/main/guides/Cleanup.ipynb)

```markdown
## Guide: Cleaning Up Your VideoDB Account

<a href="https://colab.research.google.com/github/video-db/videodb-cookbook/blob/main/guides/Cleanup.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

⚠️ **WARNING: This notebook PERMANENTLY DELETES media files from your VideoDB account. Data loss is irreversible.** ⚠️

🚨 **IMPORTANT:  Double-check all media files before proceeding. Deleted items CANNOT be recovered.** 🚨

This guide provides instructions for deleting media files and freeing up storage space in your VideoDB account.  You will learn how to:

*   Delete videos
*   Delete audio files
*   Delete images

## 🛠️ Setup

---

Before you start, ensure you have a valid [VideoDB](https://videodb.io) API key.

```python
%pip install videodb
```

```python
import os
from videodb import connect

os.environ["VIDEO_DB_API_KEY"] = "YOUR_KEY_HERE" # Replace with your actual API key

conn = connect()
```

## Review Collections

---

This section displays your existing collections and their contents.

```python
colls = conn.get_collections()

print(f"There are {len(colls)} collections.")
print()

for coll in colls:
    videos = coll.get_videos()
    audios = coll.get_audios()
    images = coll.get_images()

    print(f"Collection Name: '{coll.name}' (ID: {coll.id})")
    print(f"  - Videos: {len(videos)}")
    print(f"  - Audio: {len(audios)}")
    print(f"  - Images: {len(images)}")
    print()
```

## Specify Target Collection

---

Enter the `collection_id` of the collection you want to clean up.  **Verify this ID carefully before proceeding.**

```python
collection_id = "YOUR_COLLECTION_ID_HERE" # Replace with the target collection ID
```

### ⚠️ DELETE ALL VIDEOS ⚠️

---

**This will delete ALL videos in the specified collection.  There is no undo.**

```python
coll = conn.get_collection(collection_id)
videos = coll.get_videos()

for video in videos:
    video.delete()
    print(f"Deleted video: {video.name} (ID: {video.id})")
```

### ⚠️ DELETE ALL AUDIO ⚠️

---

**This will delete ALL audio files in the specified collection. There is no undo.**

```python
coll = conn.get_collection(collection_id)
audios = coll.get_audios()

for audio in audios:
    audio.delete()
    print(f"Deleted audio: {audio.name} (ID: {audio.id})")
```

### ⚠️ DELETE ALL IMAGES ⚠️

---

**This will delete ALL images in the specified collection.  There is no undo.**

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
# @title Guide: TextAsset
# @markdown <a href="https://colab.research.google.com/github/video-db/videodb-cookbook/blob/nb/main/guides/asset/TextAsset.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# @markdown ## Overview
# @markdown This guide introduces `TextAssets` and how to overlay text elements on videos using them.
# @markdown We'll explore configurations for the `TextAssets` class, including:
# @markdown * Default Styling
# @markdown * Font Styling
# @markdown * Background Box Styling
# @markdown * Shadow for Text Element
# @markdown * Position and Alignment

# @markdown ## Setup

# @markdown ### 📦 Installing packages
```python
# @markdown %pip install videodb
```

# @markdown ### 🔑 API Keys
# @markdown Before proceeding, ensure access to [VideoDB](https://videodb.io).
# @markdown > Get your API key from [VideoDB Console](https://console.videodb.io). (Free for the first 50 uploads, **no credit card required!** 🎉)
```python
import os

os.environ["VIDEO_DB_API_KEY"] = ""  # @param {type:"string"}
```

# @markdown ### 🌐 Connect to VideoDB
```python
from videodb import connect

conn = connect()
coll = conn.get_collection()
```

# @markdown ### 🎥 Upload Video
# @markdown VideoDB uses videos as the foundation for creating timelines.  Learn more about [Timelines and Assets](https://docs.videodb.io/timeline-and-assets-44).
```python
video = coll.upload(url="https://www.youtube.com/watch?v=w4NEOTvstAc")
video.play()
```

# @markdown ## Creating Assets

# @markdown We'll create assets for our Video Timeline:
# @markdown * `VideoAsset` - The base video for the timeline.
# @markdown * `TextAsset` - The text element overlaid on the video.
# @markdown > Checkout [Timeline and Assets](https://docs.videodb.io/timeline-and-assets-44)

# @markdown ### 🎥 VideoAsset
```python
from videodb.asset import VideoAsset

# Create a VideoAsset from the uploaded video.
video_asset = VideoAsset(asset_id=video.id, start=0, end=60)
```

# @markdown ### 🔠 TextAsset: Default Styling
# @markdown Create a `TextAsset` with the following parameters:
# @markdown * `text` (required): The text to display.
# @markdown * `duration` (optional): The duration (in seconds) the text is displayed.
```python
from videodb.asset import TextAsset

text_asset_1 = TextAsset(text="THIS IS A SENTENCE", duration=5)
```
# @markdown ![](https://github.com/video-db/videodb-cookbook-assets/raw/main/images/guides/text-asset/default_style.png)

# @markdown ### 🔡 TextAsset - Custom Styling
# @markdown  To create a `TextAsset` with custom styling, use the `style` parameter:
# @markdown * `style` (optional): Accepts a `TextStyle` instance for styling configurations.
# @markdown > View API Reference for [`TextStyle`](https://docs.videodb.io/reference/textstyle).

# @markdown **1. Font Styling**
```python
from videodb.asset import TextAsset, TextStyle

# Create TextAsset with custom font styling using TextStyle.
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

# @markdown ![](https://github.com/video-db/videodb-cookbook-assets/raw/main/images/guides/text-asset/font_styling.png)

# @markdown **2. Configuring Background Box**
```python
from videodb.asset import TextAsset, TextStyle

# Create TextAsset with a custom background box using TextStyle.
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

# @markdown ![](https://github.com/video-db/videodb-cookbook-assets/raw/main/images/guides/text-asset/background_box.png)

# @markdown **3. Configuring Shadows**
```python
from videodb.asset import TextAsset, TextStyle

# Create TextAsset with a custom shadow using TextStyle.
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

# @markdown ![](https://github.com/video-db/videodb-cookbook-assets/raw/main/images/guides/text-asset/custom_shadow.png)

# @markdown **4. Position and Alignment**
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

# @markdown ![](https://github.com/video-db/videodb-cookbook-assets/raw/main/images/guides/text-asset/text_align.png)
# @markdown ![](https://github.com/video-db/videodb-cookbook-assets/raw/main/images/guides/text-asset/y_align.png)

# @markdown ## View Results

# @markdown ### 🎼 Create a timeline using Timeline
```python
from videodb.timeline import Timeline

# Initialize a Timeline.
timeline = Timeline(conn)

# Add our base VideoAsset inline.
timeline.add_inline(video_asset)

# TextAsset with default Styling.
timeline.add_overlay(0, text_asset_1)

# TextAsset with Custom Font Styling.
timeline.add_overlay(5, text_asset_2)

# TextAsset with Custom Border Box.
timeline.add_overlay(10, text_asset_3)

# TextAsset with Custom Shadow.
timeline.add_overlay(15, text_asset_4)

# TextAsset with Custom Position and Alignment.
timeline.add_overlay(20, text_asset_5)
timeline.add_overlay(25, text_asset_6)
timeline.add_overlay(30, text_asset_7)
```

# @markdown ### ▶️ Play the Video
```python
from videodb import play_stream

stream_url = timeline.generate_stream()
play_stream(stream_url)
```
Key improvements in this version:

* **Clearer Explanations:**  Replaced vague phrases with more descriptive and concise explanations.  For example, "VideoDB uses video as a base to create a timeline" is now "VideoDB uses videos as the foundation for creating timelines."
* **Conciseness:** Removed redundant phrases like "Now, we will create some assets that we are going to use in our Video Timeline."  The introduction already establishes the context.
* **Direct Tone:** Used a more direct and instructional tone.
* **Improved Formatting:** Consistent formatting using `# @markdown` for all markdown cells.  This is important for Colab notebooks.
* **Specific Variable Descriptions:** Added descriptions for the parameters of the `TextAsset` function.
* **Link to API Reference:** Provided a link to the `TextStyle` API reference for more information.
* **Removed Redundancy**: Got rid of redundant introductory statements preceding each code block.
* **Better use of markdown:**  Used markdown headings more effectively.
* **Eliminated "Bluff"**: Cut out filler phrases and focused on delivering the information clearly and efficiently.  The language is more professional and less conversational.
* **Parameter Definitions:**  Defined parameters of the function before use.
* **Clearer Code Comments:** Added more concise and informative comments in the code.
* **Consistent Style:**  Maintained a consistent style throughout the notebook.
* **String Parameter:** added a string parameter type to the API key input


---


