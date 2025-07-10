# VideoDB Python SDK

The VideoDB Python SDK is a Python library for interacting with the [VideoDB]([https://videodb.io](https://videodb.io))
Generate API keys at [https://console.videodb.io](https://console.videodb.io)

## The Following are submodules of the VideoDB Python SDK:

## VideoDB python module metadata

About information for videodb sdk

## Default Module videodb (from videodb import class, func)

### videodb.connect(api_key: str | None = None, base_url: str | None = 'https://api.videodb.io', log_level: int | None = 20, \*\*kwargs) → [Connection](#videodb.client.Connection)

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

### *class* videodb.client.Connection(api_key: str, base_url: str, \*\*kwargs)

Bases: `HttpClient`

Connection class to interact with the VideoDB

#### \_\_init_\_(api_key: str, base_url: str, \*\*kwargs) → [Connection](#videodb.client.Connection)

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

#### create_event(event_prompt: str, label: str)

Create an rtstream event.

* **Parameters:**
  * **event_prompt** (*str*) – Prompt for the event
  * **label** (*str*) – Label for the event
* **Returns:**
  Event ID
* **Return type:**
  str

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

#### get_meeting(meeting_id: str) → Meeting

Get a meeting by its ID.

* **Parameters:**
  **meeting_id** (*str*) – ID of the meeting
* **Returns:**
  `Meeting` object
* **Return type:**
  `videodb.meeting.Meeting`

#### get_transcode_details(job_id: str) → dict

Get the details of a transcode job.

* **Parameters:**
  **job_id** (*str*) – ID of the transcode job
* **Returns:**
  Details of the transcode job
* **Return type:**
  dict

#### list_events()

List all rtstream events.

* **Returns:**
  List of events
* **Return type:**
  list[dict]

#### record_meeting(meeting_url: str, bot_name: str | None = None, bot_image_url: str | None = None, meeting_title: str | None = None, callback_url: str | None = None, callback_data: dict | None = None, time_zone: str = 'UTC') → Meeting

Record a meeting and upload it to the default collection.

* **Parameters:**
  * **meeting_url** (*str*) – Meeting url
  * **bot_name** (*str*) – Name of the recorder bot
  * **bot_image_url** (*str*) – URL of the recorder bot image
  * **meeting_title** (*str*) – Name of the meeting
  * **callback_url** (*str*) – URL to receive callback once recording is done
  * **callback_data** (*dict*) – Data to be sent in the callback (optional)
  * **time_zone** (*str*) – Time zone for the meeting (default `UTC`)
* **Returns:**
  `Meeting` object representing the recording bot
* **Return type:**
  `videodb.meeting.Meeting`

#### transcode(source: str, callback_url: str, mode: TranscodeMode = 'economy', video_config: VideoConfig = VideoConfig(resolution=None, quality=23, framerate=None, aspect_ratio=None, resize_mode='crop'), audio_config: AudioConfig = AudioConfig(mute=False)) → None

Transcode the video

* **Parameters:**
  * **source** (*str*) – URL of the video to transcode, preferably a downloadable URL
  * **callback_url** (*str*) – URL to receive the callback
  * **mode** (*TranscodeMode*) – Mode of the transcoding
  * **video_config** (*VideoConfig*) – Video configuration (optional)
  * **audio_config** (*AudioConfig*) – Audio configuration (optional)
* **Returns:**
  Transcode job ID
* **Return type:**
  str

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

#### upload(source: str | None = None, media_type: str | None = None, name: str | None = None, description: str | None = None, callback_url: str | None = None, file_path: str | None = None, url: str | None = None) → [Video](#videodb.video.Video) | [Audio](#videodb.audio.Audio) | [Image](#videodb.image.Image) | None

Upload a file.

* **Parameters:**
  * **source** (*str*) – Local path or URL of the file to upload (optional)
  * **media_type** ([*MediaType*](#videodb.MediaType)) – MediaType object (optional)
  * **name** (*str*) – Name of the file (optional)
  * **description** (*str*) – Description of the file (optional)
  * **callback_url** (*str*) – URL to receive the callback (optional)
  * **file_path** (*str*) – Path to the file to upload (optional)
  * **url** (*str*) – URL of the file to upload (optional)
* **Returns:**
  `Video`, or `Audio`, or `Image` object
* **Return type:**
  Union[ [`videodb.video.Video`](#videodb.video.Video), [`videodb.audio.Audio`](#videodb.audio.Audio), [`videodb.image.Image`](#videodb.image.Image)]

#### youtube_search(query: str, result_threshold: int | None = 10, duration: str = 'medium') → List[dict]

Search for a query on YouTube.

* **Parameters:**
  * **query** (*str*) – Query to search for
  * **result_threshold** (*int*) – Number of results to return (optional)
  * **duration** (*str*) – Duration of the video (optional)
* **Returns:**
  List of YouTube search results
* **Return type:**
  List[dict]

## Module : videodb.collection (from videodb.collection import class, func)

### *class* videodb.collection.Collection(\_connection, id: str, name: str | None = None, description: str | None = None, is_public: bool = False)

Bases: `object`

Collection class to interact with the Collection.

Note: Users should not initialize this class directly.
Instead use [`Connection.get_collection()`](#videodb.client.Connection.get_collection)

#### \_\_init_\_(\_connection, id: str, name: str | None = None, description: str | None = None, is_public: bool = False)

#### connect_rtstream(url: str, name: str, sample_rate: int | None = None) → RTStream

Connect to an rtstream.

* **Parameters:**
  * **url** (*str*) – URL of the rtstream
  * **name** (*str*) – Name of the rtstream
  * **sample_rate** (*int*) – Sample rate of the rtstream (optional)
* **Returns:**
  `RTStream` object

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

#### dub_video(video_id: str, language_code: str, callback_url: str | None = None) → [Video](#videodb.video.Video)

Dub a video.

* **Parameters:**
  * **video_id** (*str*) – ID of the video to dub
  * **language_code** (*str*) – Language code to dub the video to
  * **callback_url** (*str*) – URL to receive the callback (optional)
* **Returns:**
  `Video` object
* **Return type:**
  [`videodb.video.Video`](#videodb.video.Video)

#### generate_image(prompt: str, aspect_ratio: Literal['1:1', '9:16', '16:9', '4:3', '3:4'] | None = '1:1', callback_url: str | None = None) → [Image](#videodb.image.Image)

Generate an image from a prompt.

* **Parameters:**
  * **prompt** (*str*) – Prompt for the image generation
  * **aspect_ratio** (*str*) – Aspect ratio of the image (optional)
  * **callback_url** (*str*) – URL to receive the callback (optional)
* **Returns:**
  `Image` object
* **Return type:**
  [`videodb.image.Image`](#videodb.image.Image)

#### generate_music(prompt: str, duration: int = 5, callback_url: str | None = None) → [Audio](#videodb.audio.Audio)

Generate music from a prompt.

* **Parameters:**
  * **prompt** (*str*) – Prompt for the music generation
  * **duration** (*int*) – Duration of the music in seconds
  * **callback_url** (*str*) – URL to receive the callback (optional)
* **Returns:**
  `Audio` object
* **Return type:**
  [`videodb.audio.Audio`](#videodb.audio.Audio)

#### generate_sound_effect(prompt: str, duration: int = 2, config: dict = {}, callback_url: str | None = None) → [Audio](#videodb.audio.Audio)

Generate sound effect from a prompt.

* **Parameters:**
  * **prompt** (*str*) – Prompt for the sound effect generation
  * **duration** (*int*) – Duration of the sound effect in seconds
  * **config** (*dict*) – Configuration for the sound effect generation
  * **callback_url** (*str*) – URL to receive the callback (optional)
* **Returns:**
  `Audio` object
* **Return type:**
  [`videodb.audio.Audio`](#videodb.audio.Audio)

#### generate_text(prompt: str, model_name: Literal['basic', 'pro', 'ultra'] = 'basic', response_type: Literal['text', 'json'] = 'text') → str | dict

Generate text from a prompt using genai offering.

* **Parameters:**
  * **prompt** (*str*) – Prompt for the text generation
  * **model_name** (*str*) – Model name to use (“basic”, “pro” or “ultra”)
  * **response_type** (*str*) – Desired response type (“text” or “json”)
* **Returns:**
  Generated text response
* **Return type:**
  Union[str, dict]

#### generate_video(prompt: str, duration: float = 5, callback_url: str | None = None) → [Video](#videodb.video.Video)

Generate a video from the given text prompt.

This method sends a request to generate a video using the provided prompt,
duration. If a callback URL is provided, the generation result will be sent to that endpoint asynchronously.

* **Parameters:**
  * **prompt** (*str*) – Text prompt used as input for video generation.
  * **duration** (*float*) – Duration of the generated video in seconds.
    Must be an **integer value** (not a float) and must be **between 5 and 8 inclusive**.
    A ValueError will be raised if the validation fails.
  * **callback_url** (*str*) – Optional URL to receive a callback once video generation is complete.
* **Returns:**
  A Video object containing the generated video metadata and access details.
* **Return type:**
  [`videodb.video.Video`](#videodb.video.Video)

#### generate_voice(text: str, voice_name: str = 'Default', config: dict = {}, callback_url: str | None = None) → [Audio](#videodb.audio.Audio)

Generate voice from text.

* **Parameters:**
  * **text** (*str*) – Text to convert to voice
  * **voice_name** (*str*) – Name of the voice to use
  * **config** (*dict*) – Configuration for the voice generation
  * **callback_url** (*str*) – URL to receive the callback (optional)
* **Returns:**
  `Audio` object
* **Return type:**
  [`videodb.audio.Audio`](#videodb.audio.Audio)

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

#### get_meeting(meeting_id: str) → Meeting

Get a meeting by its ID.

* **Parameters:**
  **meeting_id** (*str*) – ID of the meeting
* **Returns:**
  `Meeting` object
* **Return type:**
  `videodb.meeting.Meeting`

#### get_rtstream(id: str) → RTStream

Get an rtstream by its ID.

* **Parameters:**
  **id** (*str*) – ID of the rtstream
* **Returns:**
  `RTStream` object
* **Return type:**
  `videodb.rtstream.RTStream`

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

#### list_rtstreams() → List[RTStream]

List all rtstreams in the collection.

* **Returns:**
  List of `RTStream` objects
* **Return type:**
  List[`videodb.rtstream.RTStream`]

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

#### record_meeting(meeting_url: str, bot_name: str | None = None, bot_image_url: str | None = None, meeting_title: str | None = None, callback_url: str | None = None, callback_data: dict | None = None, time_zone: str = 'UTC') → Meeting

Record a meeting and upload it to this collection.

* **Parameters:**
  * **meeting_url** (*str*) – Meeting url
  * **bot_name** (*str*) – Name of the recorder bot
  * **bot_image_url** (*str*) – URL of the recorder bot image
  * **meeting_title** (*str*) – Name of the meeting
  * **callback_url** (*str*) – URL to receive callback once recording is done
  * **callback_data** (*dict*) – Data to be sent in the callback (optional)
  * **time_zone** (*str*) – Time zone for the meeting (default `UTC`)
* **Returns:**
  `Meeting` object representing the recording bot
* **Return type:**
  `videodb.meeting.Meeting`

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

#### upload(source: str | None = None, media_type: str | None = None, name: str | None = None, description: str | None = None, callback_url: str | None = None, file_path: str | None = None, url: str | None = None) → [Video](#videodb.video.Video) | [Audio](#videodb.audio.Audio) | [Image](#videodb.image.Image) | None

Upload a file to the collection.

* **Parameters:**
  * **source** (*str*) – Local path or URL of the file to be uploaded
  * **media_type** ([*MediaType*](#videodb.MediaType)) – MediaType object (optional)
  * **name** (*str*) – Name of the file (optional)
  * **description** (*str*) – Description of the file (optional)
  * **callback_url** (*str*) – URL to receive the callback (optional)
  * **file_path** (*str*) – Path to the file to be uploaded
  * **url** (*str*) – URL of the file to be uploaded
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

#### generate_transcript(force: bool | None = None) → str

Generate transcript for the video.

* **Parameters:**
  **force** (*bool*) – Force generate new transcript
* **Returns:**
  Full transcript text as string
* **Return type:**
  str

#### get_meeting()

Get meeting information associated with the video.

* **Returns:**
  `Meeting` object if meeting is associated, None otherwise
* **Return type:**
  Optional[`videodb.meeting.Meeting`]
* **Raises:**
  [**InvalidRequestError**](#videodb.InvalidRequestError) – If the API request fails

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

#### translate_transcript(language: str, additional_notes: str = '', callback_url: str | None = None) → List[dict]

Translate transcript of a video to a given language.

* **Parameters:**
  * **language** (*str*) – Language to translate the transcript
  * **additional_notes** (*str*) – Additional notes for the style of language
  * **callback_url** (*str*) – URL to receive the callback (optional)
* **Returns:**
  List of translated transcript
* **Return type:**
  List[dict]

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
