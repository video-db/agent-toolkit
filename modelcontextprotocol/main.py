import os
import requests
import videodb
from constants import LLM_FULL_TXT_URL
from mcp.server.fastmcp import FastMCP
from utils import handle_videodb_tools_error
from videodb import SubtitleStyle
from videodb.timeline import Timeline
from videodb.asset import VideoAsset, ImageAsset

mcp = FastMCP("videodb")


@mcp.resource(
    "videodb://code_helper",
    name="videodb_code_helper",
    description="Will give you data related to VideoDB SDK which allows developers to use videodb in python. IMPORTANT: Whenever user wants to write code related to videos, yotube videos or VideoDB specifically, always call this tool.",
)
def code_helper() -> str:
    try:
        response = requests.get(LLM_FULL_TXT_URL)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error: Unable to fetch data from URL. Details: {str(e)}"


@mcp.tool(
    name="videodb_code_helper",
    description="Will give you data related to VideoDB SDK which allows developers to use videodb in python. IMPORTANT: Whenever user wants to write code related to videos, yotube videos or VideoDB specifically, always call this tool.",
)
def code_helper() -> str:
    try:
        response = requests.get(LLM_FULL_TXT_URL)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error: Unable to fetch data from URL. Details: {str(e)}"


@mcp.tool(
    name="upload_asset",
    description="Uploads video, audio or image inside VideoDB Storage. Valid media type are 'video', 'audio' and 'image'. 'file_type' will be 'local_file' if user gives the local path of the video. 'file_type' will be 'url' if the user gives a link to an asset",
)
@handle_videodb_tools_error
async def upload_asset(
    path: str,
    media_type: str = "video",
    file_type: str = "local_file",
    collection_id: str = "default",
):
    conn = videodb.connect(os.getenv("VIDEODB_API_KEY"))
    coll = conn.get_collection(collection_id)

    if file_type == "local_file":
        asset = coll.upload(file_path=path, media_type=media_type)
    else:
        asset = coll.upload(url=path, media_type=media_type)
    return {"id": asset.id, "collection_id": asset.collection_id, "type": media_type}


@mcp.tool(
    name="get_videos_information",
    description="Retrieves information about all video collections and their videos from VideoDB. Use this to get video details such as video_id and collection_id by name.",
)
@handle_videodb_tools_error
async def get_context():
    conn = videodb.connect(os.getenv("VIDEODB_API_KEY"))
    collections = conn.get_collections()
    video_information = ""
    for coll in collections:
        videos = coll.get_videos()

        video_information += f"collection_id:{coll.id}\n"

        for video in videos:
            video_information += f"name:{video.name} | video_id:{video.id}\n"
        video_information += "\n"
    return video_information


@mcp.tool(
    name="get_transcript",
    description="Takes in a Video ID 'video_id' and the 'collection_id' and generates a transcript of it",
)
@handle_videodb_tools_error
async def get_transcript(video_id: str, collection_id: str = "default"):

    conn = videodb.connect(os.getenv("VIDEODB_API_KEY"))
    coll = conn.get_collection(collection_id=collection_id)
    video = coll.get_video(video_id)

    try:
        transcript = video.get_transcript_text()
    except:
        video.index_spoken_words()
        transcript = video.get_transcript_text()
    return {"video_id": video.id, "transcript": transcript}


@mcp.tool(name="get_collection", description="Gets a VideoDB collection's information")
@handle_videodb_tools_error
async def get_collection(collection_id: str = "default"):
    conn = videodb.connect(os.getenv("VIDEODB_API_KEY"))
    coll = conn.get_collection(collection_id=collection_id)

    return {"id": coll.id, "name": coll.name, "description": coll.description}


@mcp.tool(
    name="get_collections", description="Gets information of all collections in VideoDB"
)
@handle_videodb_tools_error
async def get_collections():
    conn = videodb.connect(os.getenv("VIDEODB_API_KEY"))
    colls = conn.get_collections()

    return [
        {"id": coll.id, "name": coll.name, "description": coll.description}
        for coll in colls
    ]


@mcp.tool(
    name="get_image",
    description="Get's image information from image_id and collection_id",
)
@handle_videodb_tools_error
async def get_image(image_id: str, collection_id: str = "default"):
    conn = videodb.connect(os.getenv("VIDEODB_API_KEY"))
    coll = conn.get_collection(collection_id=collection_id)
    image = coll.get_image(image_id=image_id)

    return {
        "image_id": image.id,
        "collection_id": image.collection_id,
        "url": image.url,
        "name": image.name,
        "description": getattr(image, "description", None),
    }


@mcp.tool(name="create_collection", description="Create a new collection")
@handle_videodb_tools_error
async def create_collection(name: str, description: str = ""):
    if not name:
        return "Name is required for the creation of collection"
    conn = videodb.connect(os.getenv("VIDEODB_API_KEY"))
    coll = conn.create_collection(name, description)
    return {
        "success": True,
        "message": f"Collection '{coll.id}' created successfully",
        "collection": {
            "id": coll.id,
            "name": coll.name,
            "description": coll.description,
        },
    }


@mcp.tool(name="delete_collection", description="Delete a collection")
@handle_videodb_tools_error
async def delete_collection(collection_id: str):
    if not collection_id:
        return "Collection ID not provided"
    conn = videodb.connect(os.getenv("VIDEODB_API_KEY"))
    coll = conn.get_collection(collection_id)
    coll.delete()
    return {
        "success": True,
        "message": f"Collection '{coll.id}' deleted successfully",
    }


@mcp.tool(name="get_video", description="Fetch a video from VideoDB")
@handle_videodb_tools_error
async def get_video(video_id: str, collection_id: str = "default"):
    if not collection_id:
        return "Collection ID not provided"
    conn = videodb.connect(os.getenv("VIDEODB_API_KEY"))
    coll = conn.get_collection(collection_id)
    video = coll.get_video(video_id=video_id)
    return {
        "id": video.id,
        "name": video.name,
        "description": video.description,
        "collection_id": video.collection_id,
        "stream_url": video.stream_url,
        "length": video.length,
        "thumbnail_url": video.thumbnail_url,
    }


@mcp.tool(name="delete_video", description="Delete a video from VideoDB")
@handle_videodb_tools_error
async def delete_video(video_id: str, collection_id: str = "default"):
    if not collection_id:
        return "Collection ID not provided"
    conn = videodb.connect(os.getenv("VIDEODB_API_KEY"))
    coll = conn.get_collection(collection_id)
    video = coll.get_video(video_id=video_id)
    video.delete()
    return {"success": True, "message": "Video deleted successfully"}


@mcp.tool(name="get_videos", description="Get all videos from VideoDB collection")
@handle_videodb_tools_error
async def get_videos(collection_id: str = "default"):
    if not collection_id:
        return "Collection ID not provided"
    conn = videodb.connect(os.getenv("VIDEODB_API_KEY"))
    coll = conn.get_collection(collection_id)
    videos = coll.get_videos()
    return [
        {
            "id": video.id,
            "name": video.name,
            "description": video.description,
            "collection_id": video.collection_id,
            "stream_url": video.stream_url,
            "length": video.length,
            "thumbnail_url": video.thumbnail_url,
        }
        for video in videos
    ]


@mcp.tool(name="get_audio", description="Get an audio file from VideoDB collection")
@handle_videodb_tools_error
async def get_audio(audio_id: str, collection_id: str = "default"):
    if not collection_id:
        return "Collection ID not provided"
    conn = videodb.connect(os.getenv("VIDEODB_API_KEY"))
    coll = conn.get_collection(collection_id)
    audio = coll.get_audio(audio_id=audio_id)
    return {
        "id": audio.id,
        "name": audio.name,
        "collection_id": audio.collection_id,
        "length": audio.length,
        "url": audio.generate_url(),
    }


@mcp.tool(
    name="extract_frame", description="Gets a frame from a video at a given timestamp"
)
@handle_videodb_tools_error
async def extract_frame(
    video_id: str, collection_id: str = "default", timestamp: int = 5
):
    if not collection_id:
        return "Collection ID not provided"
    conn = videodb.connect(os.getenv("VIDEODB_API_KEY"))
    coll = conn.get_collection(collection_id)
    video = coll.get_video(video_id=video_id)
    image = video.generate_thumbnail(time=float(timestamp))
    return {
        "id": image.id,
        "collection_id": image.collection_id,
        "name": image.name,
        "url": image.url,
    }


@mcp.tool(
    name="index_spoken_words", description="Generate spoken words indexing of a video"
)
@handle_videodb_tools_error
async def index_spoken_words(video_id: str, collection_id: str = "default"):
    if not collection_id:
        return "Collection ID not provided"
    conn = videodb.connect(os.getenv("VIDEODB_API_KEY"))
    coll = conn.get_collection(collection_id)
    video = coll.get_video(video_id=video_id)
    index = video.index_spoken_words()
    return index


@mcp.tool(
    name="index_scene",
    description="Creates a scene based indexing. 'exctraction_type' can be 'shot' or 'time'",
)
@handle_videodb_tools_error
async def index_scene(
    video_id: str,
    collection_id: str = "default",
    extraction_type: str = "shot",
    extraction_config={},
    model_name=None,
    prompt=None,
):
    if not collection_id:
        return "Collection ID not provided"
    conn = videodb.connect(os.getenv("VIDEODB_API_KEY"))
    coll = conn.get_collection(collection_id)
    video = coll.get_video(video_id)
    return video.index_scenes(
        extraction_type=extraction_type,
        extraction_config=extraction_config,
        prompt=prompt,
        model_name=model_name,
    )


@mcp.tool(
    name="list_scene_index", description="List all scene indexing present in a video"
)
@handle_videodb_tools_error
async def list_scene_index(video_id: str, collection_id: str = "default"):
    if not collection_id:
        return "Collection ID not provided"
    conn = videodb.connect(os.getenv("VIDEODB_API_KEY"))
    coll = conn.get_collection(collection_id)
    video = coll.get_video(video_id)
    return video.list_scene_index()


@mcp.tool(name="get_scene_index", description="Retrieve a scene index from a video")
@handle_videodb_tools_error
async def get_scene_index(
    video_id: str,
    scene_id: str,
    collection_id: str = "default",
):
    if not collection_id:
        return "Collection ID not provided"
    conn = videodb.connect(os.getenv("VIDEODB_API_KEY"))
    coll = conn.get_collection(collection_id)
    video = coll.get_video(video_id)
    return video.get_scene_index(scene_id)


@mcp.tool(
    name="download",
    description="Download a video from a given stream link. You can get a stream link from the 'get_video' tool",
)
@handle_videodb_tools_error
async def download(stream_link: str, name=None):
    conn = videodb.connect(os.getenv("VIDEODB_API_KEY"))
    return conn.download(stream_link, name)


@mcp.tool(name="semantic_search", description="Does a semantic search on the video")
@handle_videodb_tools_error
async def semantic_search(
    query: str,
    video_id=None,
    collection_id: str = "default",
    index_type="spoken_word",
    result_threshold=8,
    score_threshold=0.2,
    dynamic_score_percentage=20,
    scene_index_id=None,
):
    if not collection_id:
        return "Collection ID not provided"
    conn = videodb.connect(os.getenv("VIDEODB_API_KEY"))
    coll = conn.get_collection(collection_id)
    video = coll.get_video(video_id)

    if video_id:
        video = coll.get_video(video_id)
        search_resuls = video.search(
            query=query,
            index_type=index_type,
            result_threshold=result_threshold,
            score_threshold=score_threshold,
            dynamic_score_percentage=dynamic_score_percentage,
            scene_index_id=scene_index_id,
        )
    else:
        search_resuls = coll.search(
            query=query,
            index_type=index_type,
            result_threshold=result_threshold,
            score_threshold=score_threshold,
            dynamic_score_percentage=dynamic_score_percentage,
        )

    return search_resuls


@mcp.tool(name="keyword_search", description="Does a keyword search on the video")
@handle_videodb_tools_error
async def keyword_search(
    query: str,
    video_id=None,
    collection_id: str = "default",
    index_type="spoken_word",
    result_threshold=8,
    score_threshold=0.2,
    dynamic_score_percentage=20,
    scene_index_id=None,
):
    if not collection_id:
        return "Collection ID not provided"
    conn = videodb.connect(os.getenv("VIDEODB_API_KEY"))
    coll = conn.get_collection(collection_id)
    video = coll.get_video(video_id)

    if video_id:
        video = coll.get_video(video_id)
        search_resuls = video.search(
            search_type="keyword",
            query=query,
            index_type=index_type,
            result_threshold=result_threshold,
            score_threshold=score_threshold,
            dynamic_score_percentage=dynamic_score_percentage,
            scene_index_id=scene_index_id,
        )
    else:
        search_resuls = coll.search(
            search_type="keyword",
            query=query,
            index_type=index_type,
            result_threshold=result_threshold,
            score_threshold=score_threshold,
            dynamic_score_percentage=dynamic_score_percentage,
        )

    return search_resuls


@mcp.tool(
    name="generate_video_stream",
    description="Generate a video stream from a timeline. IMPORTANT: Generate this link everytime a video_id is an output compulsorily and give the 'video_link' in output text. timeline is a list of tuples. ex [(0, 10), (20, 30)] where each tuple value is time in seconds and each tuple's entry is start and end time respectively. The time mentioned in the timeline must be an integer and can be left empty if the entire video is expected",
)
@handle_videodb_tools_error
async def generate_video_stream(
    video_id: str,
    timeline=None,
    collection_id: str = "default",
):
    if not collection_id:
        return "Collection ID not provided"
    conn = videodb.connect(os.getenv("VIDEODB_API_KEY"))
    coll = conn.get_collection(collection_id)
    video = coll.get_video(video_id)
    stream_link = video.generate_stream(timeline)
    return {
        "link": stream_link,
        "video_link": f"https://console.videodb.io/player?url={stream_link}",
    }


@mcp.tool(
    name="add_brandkit",
    description="Add brandkit related content such as intro and outro videos and a brand image which can be overlaid",
)
@handle_videodb_tools_error
async def add_brandkit(
    video_id: str,
    intro_video_id: str,
    outro_video_id: str,
    brand_image_id: str,
    collection_id: str = "default",
):
    if not collection_id:
        return "Collection ID not provided"
    conn = videodb.connect(os.getenv("VIDEODB_API_KEY"))
    coll = conn.get_collection(collection_id)
    video = coll.get_video(video_id)
    timeline = Timeline(conn)
    if intro_video_id:
        intro_video = VideoAsset(asset_id=intro_video_id)
        timeline.add_inline(intro_video)
    video = VideoAsset(asset_id=video_id)
    timeline.add_inline(video)
    if outro_video_id:
        outro_video = VideoAsset(asset_id=outro_video_id)
        timeline.add_inline(outro_video)
    if brand_image_id:
        brand_image = ImageAsset(asset_id=brand_image_id)
        timeline.add_overlay(0, brand_image)
    stream_url = timeline.generate_stream()
    return stream_url


@mcp.tool(name="add_subtitle", description="Add subtitles to a given video")
@handle_videodb_tools_error
async def add_subtitle(
    video_id: str,
    style: SubtitleStyle = SubtitleStyle(),
    collection_id: str = "default",
):
    if not collection_id:
        return "Collection ID not provided"
    conn = videodb.connect(os.getenv("VIDEODB_API_KEY"))
    coll = conn.get_collection(collection_id)
    video = coll.get_video(video_id)
    stream_url = video.add_subtitle(style)
    return stream_url


if __name__ == "__main__":
    mcp.run(transport="stdio")
