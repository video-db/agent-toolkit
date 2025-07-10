CODE_ASSISTANT_TXT_URL = "https://videodb.io/llms-full.txt"

DOCS_ASSISTANT_TXT_URL = "https://video-db.github.io/agent-toolkit/context/docs/docs_context.md"

DIRECTOR_API = "https://api2.director.videodb.io"

DIRECTOR_CALL_DESCRIPTION = """
The Director tool orchestrates specialized agents within the VideoDB server, efficiently handling multimedia and video-related queries. Clients should send queries that Director can interpret clearly, specifying tasks in natural language. Director will then delegate these queries to appropriate agents for optimized results, utilizing defaults and contextual information if explicit parameters are not provided.

Director handles queries such as:

- Uploading & Downloading:
  - Upload media from URLs or local paths (supported media: video, audio, image)
  - Download the VideoDB generated video streams.

- Indexing & Search:
  - Index spoken words or scenes in videos (spoken_words, scene indexing; scene indexing supports shot or time-based type)
  - Search VideoDB collections semantically or by keyword (semantic, keyword search; indexing types: spoken_word, scene)

- Summarization & Subtitles:
  - Summarize video content based on custom prompts
  - Add subtitles in various languages

- Dubbing:
  - Dub videos into target languages

- Creating Videos:
  - Generate videos using specific models or engines (Fal, StabilityAI; job types: text_to_video, image_to_video)
  - Compare multiple video generation models (video_generation_comparison)

- Audio Generation & Editing:
  - Generate speech, sound effects, or background music (engines: ElevenLabs for speech/sound effects, Beatoven for music)
  - Clone voices from audio sources or overlay cloned voices onto videos
  - Censor the video on given prompt

- Image and Frame Generation:
  - Generate static image frames from videos at specified timestamps
  - Create or enhance images using GenAI models (job types: text_to_image, image_to_image using Fal, Replicate)

- Video Editing & Clip Generation:
  - Edit or combine multiple videos and audio files
  - Generate targeted video clips from user prompts

- Streaming & Web Search:
  - Stream videos by video ID or URL
  - Search for relevant online videos (engine: Serp)

- Transcription:
  - Generate transcripts for videos

- Pricing & Usage Information:
  - Provide detailed cost information and usage estimates

- Meeting Recording & Analysis:
  - Record meetings
  - Deploy recording bots to Zoom, Google Meet, or Microsoft Teams
  - Analyze recorded meetings for AI-driven insights
  - Intelligently index and summarize meetings

Clients should provide queries clearly aligned with Director's capabilities, allowing Director to use contextual defaults when explicit parameters like IDs or collection details are not specified.

IMPORTANT: if you have a previous response of this method with an appropriate session_id, please provide that session_id in the next request to continue the conversation.
IMPORTANT: It is MANDATORY to send the `session_id` param if any earlier response from this method exists with a `session_id` in its output
""".strip()
