# IPYNB Notebook: scene_level_metadata_indexing [Source Link](https://github.com/video-db/videodb-cookbook/blob/main/quickstart/scene_level_metadata_indexing.ipynb)

```python
# 📌 VideoDB F1 Race Search Pipeline: Turn Detection & Metadata Filtering

# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/video-db/videodb-cookbook/blob/main/quickstart/scene_level_metadata_indexing.ipynb)

# 🎯 Objective

# This notebook demonstrates how to use VideoDB for **scene-level metadata filtering** to enable precise search and retrieval within an F1 race video.

# 🔍 What We’re Doing:

# ✔ Upload an **F1 race video**
# ✔ **Extract scenes** at 2-second intervals (1 frame per scene)
# ✔ **Describe scenes** using AI to generate metadata
# ✔ **Index scenes** with structured metadata (`camera_view` & `action_type`)
# ✔ **Search scenes** using **semantic search combined with metadata filtering**

# 📦 Install VideoDB SDK

# Installs the VideoDB SDK, required for connecting and processing video data.

```python
!pip install videodb
```

```
    Collecting videodb
      Downloading videodb-0.2.10.tar.gz (25 kB)
      Preparing metadata (setup.py) ... ?25l?25hdone
    Requirement already satisfied: requests>=2.25.1 in /usr/local/lib/python3.11/dist-packages (from videodb) (2.32.3)
    Collecting backoff>=2.2.1 (from videodb)
      Downloading backoff-2.2.1-py3-none-any.whl.metadata (14 kB)
    Requirement already satisfied: tqdm>=4.66.1 in /usr/local/lib/python3.11/dist-packages (from videodb) (4.67.1)
    Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests>=2.25.1->videodb) (3.4.1)
    Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests>=2.25.1->videodb) (3.10)
    Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests>=2.25.1->videodb) (2.3.0)
    Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests>=2.25.1->videodb) (2025.1.31)
    Downloading backoff-2.2.1-py3-none-any.whl (15 kB)
    Building wheels for collected packages: videodb
      Building wheel for videodb (setup.py) ... ?25l?25hdone
      Created wheel for videodb: filename=videodb-0.2.10-py3-none-any.whl size=27143 sha256=17790c3062d5620ef1448b2c684de7485815f6d4e401e0aeb980f4ae41081e68
      Stored in directory: /root/.cache/pip/wheels/ac/43/46/922da11f9ba349968e03820b5e92a4949c78e423f6c8ec37a3
    Successfully built videodb
    Installing collected packages: backoff, videodb
    Successfully installed backoff-2.2.1 videodb-0.2.10
```

```python
# 🔑 Set Up API Key

# Authenticate with VideoDB to access indexing and search functionalities.
import videodb
import os
from getpass import getpass

api_key = getpass("Please enter your VideoDB API Key: ")

os.environ["VIDEO_DB_API_KEY"] = api_key
```

```python
# 🌐 Connect to VideoDB

# Establishes a connection to manage video storage, indexing, and search.
from videodb import connect

conn = connect()
coll = conn.get_collection()

print(coll.id)
```

```
    c-81fc6459-fe30-44ac-8c5b-ea0898c2e152
```

```python
# 🎥 Upload F1 Race Video

# Adds the video to VideoDB for further processing.
video = coll.upload(url="https://www.youtube.com/watch?v=2-oslsgSaTI")
print(video.id)
```

```
    m-z-01954d91-651d-7ef0-a022-18aad60eabdb
```

```python
# ✂️ Extracting Scenes (Every 2 Seconds)

# Splits the video into **2-second scenes**, extracting a **single frame per scene** for indexing.

# **Why?**
# - **Granular indexing** allows for more **precise scene-level filtering**.
# - **Key frame extraction** enables accurate **AI-generated metadata assignment** for each scene.
from videodb import SceneExtractionType

scene_collection = video.extract_scenes(
    extraction_type=SceneExtractionType.time_based,
    extraction_config={"time": 2, "select_frames": ["middle"]},
)

print(f"Scene Collection ID: {scene_collection.id}")

scenes = scene_collection.scenes

print(f"Total Scenes Extracted: {len(scenes)}")
```

```
    Scene Collection ID: tt2smf1
    Total Scenes Extracted: 148
```

```python
# 🔍 Generating Scene Metadata

# To **make scenes searchable**, AI is used to **describe & categorize** each scene with structured metadata:

# **📌 Scene-Level Metadata Fields:**
# 1️⃣ `camera_view` → **Where is the camera placed?**
#    - `"road_ahead"` → Driver’s **POV looking forward**
#    - `"helmet_selfie"` → Close-up of **driver’s helmet**

# 2️⃣ `action_type` → **What is the driver doing?**
#    - `"clear_road"` → No cars ahead (clean lap)
#    - `"chasing"` → Following another car (intense racing moment)

# **🚀 Why This Matters**
# - **Metadata filtering** allows us to **search for specific race scenarios.**
# - **Combining metadata & semantic search** makes retrieval **highly precise**.
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

```
    Scene from 0.0s to 2.0s
    Camera View: road_ahead | Action Type: chasing
    Scene Description: The scene is a tense overtaking maneuver at the Circuit de Monaco, featuring Max Verstappen in the Red Bull and Charles Leclerc in the Ferrari. Verstappen, having closed the gap significantly, is seen approaching Leclerc on the entry to the iconic Tunnel section, a narrow, winding portion of the track. With the tight confines and limited visibility, Verstappen must navigate the challenging turn with precision to make a successful overtake. The significance of the moment lies in the potential for a dramatic change in race leadership, as Verstappen seeks to regain the top position he lost earlier in the race.
    Scene from 2.0s to 4.0s
    Camera View: road_ahead | Action Type: chasing
    Scene Description: The scene depicts a close-up, in-car perspective of a Formula 1 race. The driver, sporting a Walmart-branded livery, is navigating a tight corner on the track. The camera captures the driver's view as they follow a Red Bull Racing car, likely Max Verstappen, in the lead. This particular moment is crucial as it signifies a potential overtake attempt by the Walmart-branded driver, highlighting a critical juncture in the race where the driver is seeking to gain an advantage. The scene is a testament to the intense competition and strategic maneuvers that define Formula 1 racing.
    Scene from 4.0s to 6.0s
    Camera View: road_ahead | Action Type: chasing
    Scene Description: The scene is a close-up, on-board perspective from the cockpit of the Red Bull car, driven by Max Verstappen. The car is navigating the treacherous, high-speed, and winding section of the Nürburgring, specifically the "Flugplatz" (airport) corner.  The camera angle captures the rear-view mirror reflecting a preceding car, likely a Ferrari, battling for the lead. The intense focus on the mirror suggests a dramatic battle for position, with Verstappen attempting to close the gap and potentially overtake his rival. The scene highlights the driver's intense concentration and the critical nature of this particular corner, known for its tight radius and potential for overtaking maneuvers.
    Scene from 6.0s to 8.0s
    Camera View: road_ahead | Action Type: chasing
    Scene Description: The scene unfolds at the Hockenheimring, Germany, as the driver of the Red Bull Racing car closes in on a competitor, likely a Ferrari, on the fast and flowing approach to the hairpin. The camera angle provides a cockpit view, capturing the driver's perspective as they meticulously navigate the complex series of curves. The driver is in a tense battle, pushing their car to the limit to attempt an overtaking maneuver. This is a crucial moment in the race, as overtaking opportunities at Hockenheim are limited, and the driver's success here could significantly alter the race outcome.
    Scene from 8.0s to 10.0s
    Camera View: road_ahead | Action Type: chasing
    Scene Description: The scene captures the moment a Red Bull driver, likely Max Verstappen, closes in on a rival car on the Nürburgring circuit. The iconic German track's fast and flowing nature is evident as the driver navigates a long, sweeping corner. The driver's helmet and the "Red Bull" branding are the only visible elements in the image, emphasizing the driver's intense focus. This scene is likely a critical moment in the race, with the Red Bull driver pushing for a pass and potentially taking the lead.
    Scene from 10.0s to 12.0s
    Camera View: road_ahead | Action Type: chasing
    Scene Description: This is an in-car perspective shot from a Red Bull car, likely driven by Max Verstappen. The scene takes place on a fast, flowing section of a track, potentially the Hockenheimring.  The car is trailing another car, likely a Mercedes, as they approach a slight bend. This is a pivotal moment as Verstappen is attempting to close the gap and potentially overtake Hamilton, showcasing the intense competition between the two drivers and their teams. The focus is on the aggressive driving style of Verstappen, pushing the limits of his car to gain an advantage.
    Scene from 12.0s to 14.0s
    Camera View: road_ahead | Action Type: chasing
    Scene Description: The scene captures a tense moment during a Formula 1 race, showcasing the driver's perspective from the cockpit. The driver, seemingly in a Red Bull, is approaching a corner, likely the famous Eau Rouge at Spa-Francorchamps. The driver's helmet is visible, highlighting their focus as they navigate the challenging bend. The scene is significant as it portrays the intensity of the race and the driver's skill in managing the car's speed and trajectory. The backdrop features lush greenery and a guardrail, further emphasizing the iconic location of the track.
    Scene from 14.0s to 16.0s
    Camera View: road_ahead | Action Type: clear_road
    Scene Description: The scene captures the thrilling moment as Max Verstappen in his Red Bull,  trailing a competitor,  approaches the challenging Turn 1 of the Hockenheimring. The camera angle, mounted on the Red Bull, provides a driver's perspective as the car navigates the left-hand corner at high speed. This close-up showcases the intense focus and agility required to master this iconic circuit. The scene underscores the raw power and precision of Formula 1 racing.
    Scene from 16.0s to 18.0s
    Camera View: helmet_selfie | Action Type: chasing
    Scene Description: This scene captures a driver, presumably Max Verstappen, in his Red Bull Racing car, navigating the challenging Eau Rouge and Raidillon corners at Spa-Francorchamps. The shot is taken from the driver's perspective, emphasizing the sheer speed and force the car endures as it crests the iconic hill.  The blurred background showcases the challenging nature of the corner, while the driver's helmet, bearing the slogan "There is still a race to win", highlights the relentless determination required for success in Formula 1.
    Scene from 18.0s to 20.0s
    Camera View: helmet_selfie | Action Type: chasing
    Scene Description: The scene captures a driver's perspective from the cockpit of a Red Bull Racing car. The driver, likely Max Verstappen, is in the midst of a tight battle for position, battling a rival car alongside him.  The action unfolds on a high-speed section of the track, likely the fast, flowing corners of the Hockenheimring. The driver's helmet, emblazoned with the message "Race Without Trace, There Is Still A Race To Win," conveys the intense determination and competitive spirit driving the moment.  The tension is palpable, as the driver focuses intently on his opponent, poised to make a decisive move for the lead. This scene represents a critical juncture in the race, where a single strategic maneuver could determine the outcome.
    Scene from 20.0s to 22.0s
    Camera View: helmet_selfie | Action Type: chasing
    Scene Description: The scene is a first-person cockpit view, capturing the intense focus of a driver navigating the challenging corners of a Formula 1 circuit. We see the driver, wearing a helmet emblazoned with the message "Race Without Trace, There is Still a Race to Win," which suggests a message of sustainability within the sport. The car, a Red Bull, is in the midst of the race, with the driver's hands gripping the steering wheel as they skillfully maneuver the car through a tight bend. This moment reflects the driver's unwavering determination to push their limits and secure victory despite the challenges ahead.
    Scene from 22.0s to 24.0s
    Camera View: helmet_selfie | Action Type: chasing
    Scene Description: The scene depicts a driver, presumably Sebastian Vettel, in his Red Bull Racing car during a race. The camera captures the driver's perspective, showcasing the cockpit view from the driver's seat. The car is navigating a high-speed corner, the trees lining the track blurring by as Vettel maintains focus. The key element is the "Race Without Trace" helmet design featuring the message "There is still a race to win." This signifies Vettel's determination and unwavering spirit in the face of adversity, pushing the limits to secure a victory.
    Scene from 24.0s to 26.0s
    Camera View: road_ahead | Action Type: clear_road
    Scene Description: The scene unfolds at the Nürburgring, a historic and challenging circuit known for its demanding layout. The driver, Sebastian Vettel, is behind the wheel of his Red Bull Racing car, navigating the iconic  "Schwedenkreuz," a high-speed, multi-apex corner. The action is captured from Vettel's perspective, conveying the immense speed and the intricate steering movements required to tame this corner. The significance of the moment lies in the sheer thrill and precision demanded, a testament to the driver's expertise and the demanding nature of the track.
    Scene from 26.0s to 28.0s
    Camera View: road_ahead | Action Type: clear_road
    Scene Description: The scene depicts a driver, likely Max Verstappen in his Red Bull Racing car, navigating the challenging Hockenheimring circuit in Germany. The perspective is from the driver's cockpit, showcasing the exhilarating experience of piloting an F1 car at high speed. This is a crucial moment, possibly during qualifying, as the driver pushes the car to its limits, seeking the perfect lap time. The driver's focus is evident, hands gripping the steering wheel, eyes fixed on the apex of the approaching corner. The blur of the forest surrounding the track adds to the dramatic effect, emphasizing the driver's incredible speed and the technical nature of Formula 1. This scene encapsulates the essence of racing: a driver's mastery, a car's capability, and a relentless pursuit of victory.
    Scene from 28.0s to 30.0s
    Camera View: road_ahead | Action Type: clear_road
    Scene Description: The scene depicts a Red Bull driver, likely Sebastian Vettel, navigating the challenging Ardennes Forest section of the Spa-Francorchamps circuit.  The car is on the approach to the fast, flowing "Eau Rouge" and "Raidillon" corners, a classic test of driver skill and car balance.  The driver is seen pushing the car to its limits, with the car leaned heavily into the corner as it tackles the uphill climb. This is a crucial moment for the driver, as a slight misstep can easily lead to a costly error in this high-speed section. The scene exemplifies the intensity and precision demanded of Formula 1 drivers on a track renowned for its demanding nature.
    Scene from 30.0s to 32.0s
    Camera View: road_ahead | Action Type: clear_road
    Scene Description: The scene depicts a driver in a Red Bull car navigating the challenging "S" curves of the Nürburgring. The driver is pushing hard, the car's tires are angled aggressively, and the blur of the surroundings signifies high speed. The driver is likely in pursuit or defending a position, showcasing the intense battle for track position typical of Formula 1 racing. The "S" curves, with their tight turns and elevation changes, demand precision and bravery, making this a defining moment in the race.
    Scene from 32.0s to 34.0s
    Camera View: road_ahead | Action Type: chasing
    Scene Description: The scene depicts a first-person perspective from the cockpit of a Red Bull Formula 1 car. It is a high-speed corner on the Hockenheimring, a German circuit known for its fast and flowing nature. The driver, likely Daniel Ricciardo, is battling for position with an unidentified opponent, as he aggressively leans into the corner, pushing the car to its limits. The significance of the moment lies in the driver's skill and commitment to achieving a strong qualifying lap time, showcasing the thrilling and demanding nature of Formula 1.
    Scene from 34.0s to 36.0s
    Camera View: road_ahead | Action Type: clear_road
    Scene Description: The scene captures a first-person perspective of a Red Bull driver navigating the challenging Hockenheimring circuit. The driver, likely Daniel Ricciardo, is approaching the iconic "Schwabacher Kurve" right-hander, a notoriously tricky corner known for its tight apex and potential for overtaking. The driver is smoothly negotiating the turn, maintaining control while pushing the limits of the car's grip, showcasing the finesse required for high-speed cornering in Formula 1. The scene provides a glimpse into the raw experience of a driver at the peak of their abilities, maneuvering a powerful machine with incredible precision.
    Scene from 36.0s to 38.0s
    Camera View: helmet_selfie | Action Type: chasing
    Scene Description: This is a close-up shot from the onboard camera of a Red Bull Racing car, likely driven by Max Verstappen. The scene is set on a fast section of the track, potentially the Monza circuit, where the driver is leading the pack under a Safety Car period.  His helmet inscription "There is still a race" emphasizes the driver's determination despite the temporary pause, hinting at his ambition for a strategic advantage during the restart.
    Scene from 38.0s to 40.0s
    Camera View: helmet_selfie | Action Type: chasing
    Scene Description: The scene captures the intense perspective of Sebastian Vettel in his Red Bull Racing car, battling for position with a rival on the fast and flowing corners of the Nurburgring Nordschleife. The German driver, with his iconic "Race Without Trace" helmet, pushes hard, seeking a decisive overtaking move. The action unfolds in the latter stages of the race, with Vettel looking to salvage a podium finish after a challenging start. The focus on his helmet emphasizes his determination to make up ground, illustrating the driver's unwavering focus and the high stakes of the race.
    Scene from 40.0s to 42.0s
    Camera View: helmet_selfie | Action Type: chasing
    Scene Description: The scene is an in-car perspective of Max Verstappen, driving the Red Bull Racing car, during a race. We are looking from the driver's seat, with his helmet in focus and the car's side panel partially visible.  The car is navigating a high-speed corner on a track with trees and barriers visible in the background. The significance of the scene lies in its capturing Verstappen's determination as he navigates a challenging corner, likely in the midst of a close battle for position. The focus on his helmet, with the "There is still a race to win" inscription, underscores the intensity and competitive spirit of the moment.
    Scene from 42.0s to 44.0s
    Camera View: road_ahead | Action Type: clear_road
    Scene Description: This is a first-person perspective shot from the cockpit of a Red Bull car, driven by Sebastian Vettel. The car is navigating the challenging Hockenheimring track, specifically the infamous "Motodrom" corner.  Vettel is aggressively pushing the car, the rear end is slightly loose, and the tire walls are visible as the car grazes the apex of the turn.  The scene highlights the driver's talent in managing a challenging corner while maintaining a high speed and pushing the car to its limits.
    Scene from 44.0s to 46.0s
    Camera View: road_ahead | Action Type: clear_road
    Scene Description: The scene captures the cockpit perspective of a Red Bull driver, presumably Daniel Ricciardo, navigating the tight and challenging corners of the Hockenheimring circuit in Germany. The car is shown with the driver's helmet and the steering wheel clearly visible. The track is lined with a guardrail and green trees on the left side, signifying a fast-paced cornering sequence. The driver's focus and concentration are palpable, highlighting the technical prowess and precision required for navigating such a demanding track. The scene likely depicts a qualifying session, with the driver pushing the car and himself to the limit for a strong grid position.
    Scene from 46.0s to 48.0s
    Camera View: road_ahead | Action Type: clear_road
    Scene Description: The scene captures the cockpit perspective of a Red Bull Racing car, presumably driven by Max Verstappen, as he navigates the challenging Nürburgring track. The iconic German circuit's green foliage and characteristic guardrails frame the action. The driver, in a moment of intense focus, expertly handles the car's powerful acceleration and intricate steering through a high-speed corner. The significance of this moment lies in showcasing the driver's mastery over the car and track, a testament to the precision and skill demanded in Formula 1 racing.
    Scene from 48.0s to 50.0s
    Camera View: road_ahead | Action Type: clear_road
    Scene Description: The scene depicts a Red Bull car, driven by Max Verstappen, navigating the treacherous  Hockenheimring's turn 1. The iconic blue and red livery of the car blends with the verdant backdrop, as Verstappen powers through the turn, leaving a trail of dust in his wake. This moment exemplifies the driver's aggressive driving style and his determination to establish a decisive lead.  The camera angle, likely from the onboard perspective, captures the thrilling experience of the driver pushing the car and himself to the limit.
    Scene from 50.0s to 52.0s
    Camera View: road_ahead | Action Type: clear_road
    Scene Description: The scene is a dramatic overtaking maneuver at the Nürburgring, a track famed for its challenging corners and unforgiving nature.  A Red Bull car, driven by Sebastian Vettel, is locked in a fierce battle with a Mercedes, piloted by Lewis Hamilton. As they approach the daunting, high-speed section known as the "Flugplatz," Vettel executes a daring move, diving down the inside of Hamilton. The camera, mounted on Vettel's car, captures the sheer audacity of the overtaking attempt, the blur of the Mercedes in the background as Vettel's car leans into the corner, tires squealing. This moment marks a turning point in the race, as Vettel's aggression sets the tone for a thrilling, action-packed finish.
    Scene from 52.0s to 54.0s
    Camera View: road_ahead | Action Type: clear_road
    Scene Description: The scene is a first-person perspective from the cockpit of a Red Bull car, likely driven by Sebastian Vettel, as he approaches a left-hand corner. The car is carrying significant speed, evident from the blur of the track ahead. The driver is executing a precise and confident line through the corner, demonstrating exceptional control of the car. The location appears to be a high-speed section of a circuit with a clear view of the surrounding landscape. The scene emphasizes the driver's expertise in navigating the track with precision and control, showcasing the exhilarating nature of Formula 1 racing.
    Scene from 54.0s to 56.0s
    Camera View: road_ahead | Action Type: clear_road
    Scene Description: This is an onboard shot of a Red Bull driver, likely Max Verstappen, exiting the Hockenheimring's Turn 1. The car, carrying the iconic red bull branding, is shown navigating the sharp right-hand corner with precision. The driver is demonstrating his mastery of the track by smoothly taking the apex, showcasing the car's agility and Verstappen's skill in controlling the vehicle's momentum and maintaining speed. This corner is often a crucial overtaking opportunity, and a driver's approach here can significantly impact their race strategy.  The image emphasizes the driver's perspective and the intense focus required for this high-speed turn, showcasing the challenge and skill required to compete in Formula 1.
    Scene from 56.0s to 58.0s
    Camera View: road_ahead | Action Type: chasing
    Scene Description: The scene is a close-up, on-board perspective from the cockpit of a Red Bull car, presumably driven by Sebastian Vettel, navigating the fast and sweeping corners of the Hockenheimring in Germany. The car is trailing another, unseen, competitor but attempting to close the gap. The image captures the intensity of the race, with the driver's helmet and the blur of the track highlighting the speed and concentration required in this high-stakes competition.
    Scene from 58.0s to 60.0s
    Camera View: helmet_selfie | Action Type: chasing
    Scene Description: The scene depicts a first-person perspective of a Red Bull driver during a race. The driver, wearing a helmet emblazoned with "Race Without Trace" and the phrase "There is still a race to go," is navigating the track's winding corners. The image captures the driver's focus and determination, highlighting the intensity of the race. The specific location is unclear, but the lush greenery and clear skies suggest a summer race at a circuit known for its challenging curves. The scene emphasizes the driver's resilience and unwavering belief in his ability to compete despite any prior setbacks.
    Scene from 60.0s to 62.0s
    Camera View: road_ahead | Action Type: clear_road
    Scene Description: This scene captures the exhilarating moment of a Red Bull driver, likely Daniel Ricciardo, pushing the limits through the fast-flowing Hockenheimring. The onboard camera perspective grants a thrilling immersion as the car navigates the iconic "Motodrom," showcasing the driver's finesse and precision. The slight spray from the damp track adds an element of drama and highlights the driver's unwavering focus. This iconic German track is known for its high-speed corners and challenging conditions, which further intensifies this adrenaline-fueled moment. The driver's unwavering pursuit of victory is palpable, making this an unforgettable glimpse into the raw energy of Formula 1.
    Scene from 62.0s to 64.0s
    Camera View: road_ahead | Action Type: clear_road
    Scene Description: The scene is a close-up, onboard shot from the cockpit of a Red Bull car, likely driven by Max Verstappen. The car is navigating the tight, high-speed turn at the Red Bull Ring in Austria, known as Turn 9. This corner is a key overtaking opportunity, and the shot highlights Verstappen's precise steering and commitment to the apex, showcasing the driver's skill and the car's grip. The scene conveys the thrill and pressure of a high-stakes battle for position, a defining moment in the race for victory.
    Scene from 64.0s to 66.0s
    Camera View: road_ahead | Action Type: clear_road
    Scene Description: The scene is a close-up, onboard shot from the Red Bull RB18 driven by Sergio Perez, negotiating the sweeping right-hand corner at the end of the long back straight, known as Turn 1 at the Red Bull Ring in Austria. The camera captures the intense perspective from the cockpit, highlighting Perez's meticulous steering and the rapid deceleration of the car as it transitions into the corner, showcasing the demanding nature of this high-speed circuit. This moment symbolizes the intense focus and precision required by drivers in Formula 1, even in a seemingly routine corner.
    Scene from 66.0s to 68.0s
    Camera View: helmet_selfie | Action Type: clear_road
    Scene Description: The scene depicts a Red Bull Racing car, driven by Max Verstappen, navigating the challenging Turn 1 at the Hungaroring circuit in Budapest, Hungary. The onboard camera captures the car's perspective as it enters the high-speed corner, showcasing Verstappen's smooth and precise driving style. The scene highlights the driver's ability to maintain control and momentum in a demanding and technical section of the track, demonstrating his mastery of the car and the circuit.
    Scene from 68.0s to 70.0s
    Camera View: road_ahead | Action Type: clear_road
    Scene Description: The scene depicts a Red Bull car, presumably driven by Max Verstappen, navigating a fast, flowing section of the track. The car is seen from the cockpit perspective, with the driver's helmet and steering wheel visible. The car is in a straight line, possibly approaching a corner, the asphalt streaked with tire rubber from previous laps. The location is likely a high-speed section of the track, characterized by a smooth asphalt surface, low-lying greenery, and distant hills.  The significance of this moment is the driver's focus and control as he navigates a demanding section of the circuit, showcasing the precision and athleticism required in Formula 1.
    Scene from 70.0s to 72.0s
    Camera View: road_ahead | Action Type: clear_road
    Scene Description: The scene depicts a Red Bull driver navigating the Nürburgring's fast and flowing section, the Fuchsröhre. The car, adorned with the iconic Red Bull livery, races through a slight right-hand bend, its rear wing flexing under the strain of high-speed cornering. The driver's focus is evident as they maintain a precise racing line, seeking to maximize speed and precision. The backdrop of lush green hills and the distant sounds of the crowd add to the thrilling atmosphere of the race. This moment showcases the raw speed and agility of Formula 1 machinery as it tackles one of the most iconic and challenging corners in motorsports.
    Scene from 72.0s to 74.0s
    Camera View: road_ahead | Action Type: clear_road
    Scene Description: The scene depicts a Red Bull car, likely driven by Max Verstappen, navigating the iconic Hockenheimring circuit in Germany. The car is approaching the infamous "Motodrom," the high-speed banked corner, a crucial overtaking spot. The camera perspective is from the driver's seat, highlighting the immense speed and g-forces experienced as the car carves through the corner.  The focus is on the driver's exceptional skill in maintaining control at such high speeds, a hallmark of Verstappen's driving style. The scene captures the adrenaline-pumping action of Formula 1, where every corner offers a potential opportunity for a daring maneuver.
    Scene from 74.0s to 76.0s
    Camera View: road_ahead | Action Type: clear_road
    Scene Description: The scene captures a Red Bull driver navigating the challenging, fast-flowing turns of the Hockenheimring circuit. The car, featuring the distinctive Red Bull livery, is pushing its limits, its front wing creating a visible downforce as it carves through the apex of the corner. The driver is exhibiting impressive control and precision, a testament to his skill and the car's handling capabilities. The scene underscores the raw power and technical finesse of Formula 1 racing, showcasing the drivers' commitment to achieving optimal performance.
    Scene from 76.0s to 78.0s
    Camera View: road_ahead | Action Type: clear_road
    Scene Description: The scene depicts a Red Bull car, driven by Daniel Ricciardo, navigating the treacherous Hockenheimring, specifically the fast and flowing section known as the "Sachskurve." The car is seen from the driver's perspective, showcasing Ricciardo's aggressive approach as he pushes the limits of the car through a high-speed corner. The shot highlights the driver's focus and control, demonstrating the immense skill required to master the intricacies of Formula 1. The scene captures the essence of high-speed racing, where every action is calculated and the margin for error is minimal.
    Scene from 78.0s to 80.0s
    Camera View: road_ahead | Action Type: chasing
    Scene Description: The scene depicts a thrilling overtaking maneuver at the Nürburgring's famed "Flugplatz" section. A Red Bull driver, likely Max Verstappen or Sergio Perez, aggressively pushes past a Williams car, utilizing the superior power of the Red Bull to slingshot out of the corner. The Williams driver, possibly George Russell or Nicholas Latifi, is seen struggling to maintain pace, highlighting the gap in performance between the two teams. The verdant forest backdrop and the iconic Nürburgring infrastructure create a visually stunning backdrop for this decisive move, which could potentially swing the outcome of the race.
    Scene from 80.0s to 82.0s
    Camera View: road_ahead | Action Type: chasing
    Scene Description

---

# IPYNB Notebook: VideoDB Quickstart [Source Link](https://github.com/video-db/videodb-cookbook/blob/main/quickstart/VideoDB%20Quickstart.ipynb)

```python
# ⚡️ QuickStart: VideoDB

# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/video-db/videodb-cookbook/blob/main/quickstart/VideoDB%20Quickstart.ipynb)

# This notebook provides a hands-on introduction to [VideoDB](https://videodb.io), enabling you to quickly upload, index, search, and stream video content.

# ### Setup
# ---

# #### 🔧 Install VideoDB

# Install the VideoDB Python package:

# ```python
# !pip install -U videodb
# ```

# #### 🔗 Connect to VideoDB

# Establish a connection to VideoDB using your API key. You can provide the key directly or set the `VIDEO_DB_API_KEY` environment variable.

# > 💡 Get your API key from the [VideoDB Console](https://console.videodb.io) (Free for the first 50 uploads, no credit card required!).

# ```python
import videodb
import os
from getpass import getpass

api_key = getpass("Please enter your VideoDB API Key: ")
os.environ["VIDEO_DB_API_KEY"] = api_key

conn = videodb.connect()
# ```

# ### Working with a Single Video
# ---

# #### ⬆️ Upload a Video

# Upload videos using `conn.upload()`. You can upload media from a public URL or a local file path. The `upload` function returns a `Video` object for accessing video methods.

# ```python
# Upload a video by URL
video = conn.upload(url="https://www.youtube.com/watch?v=wU0PYcCsL6o")
# ```

# > VideoDB simplifies uploads by supporting links from YouTube, S3, and any public URL with a video.

# #### 📺 View Your Video

# Videos are instantly available for viewing in 720p resolution.

# *   Generate a streamable URL using `video.generate_stream()`.
# *   Preview the video using `video.play()`. This opens the video in your default browser/notebook.

# ```python
video.generate_stream()
video.play()
# ```

# #### ✂️ Get Specific Sections of Videos

# Clip specific sections of a video by providing start and end times (in seconds) to the `timeline` argument.

# For example, stream the first 10 seconds and then from 120 to 140 seconds:

# ```python
stream_link = video.generate_stream(timeline=[[0, 10], [120, 140]])


def play_stream(stream_link):
    print(
        stream_link
    )  # Replace with a proper video player implementation if needed


play_stream(stream_link)
# ```

# #### 🔍 Indexing a Video

# Index a video to enable searching within its content. VideoDB currently offers two index types:

# 1.  `index_spoken_words`: Indexes spoken words in the video, automatically generating a transcript for search. Supports 20+ languages (see [Language Support](https://docs.videodb.io/language-support-79)).
# 2.  `index_scenes`: Indexes visual information and events in the video. Ideal for finding scenes, activities, objects, and emotions (see [Scene Index Documentation](https://docs.videodb.io/scene-index-documentation-80)).

# > Indexing may take time for longer videos.

# ```python
# Index spoken content of the video
video.index_spoken_words()
# ```

# ```python
# Index visual information in video frames. Adjust the prompt according to your use case.
# You can index a video multiple times with different prompts.
index_id = video.index_scenes(
    prompt="Describe the scene in strictly 100 words"
)

# Wait for indexing to finish (optional)
scene_index = video.get_scene_index(index_id)
scene_index
# ```

# #### Search inside a video

# Search indexed videos using `video.search()`. Options include search type and index type. VideoDB offers the following search types:

# *   `SearchType.semantic`: (Default) Ideal for question-answering.
# *   `SearchType.keyword`: Matches the exact occurrence of words or sentences. Only available for single videos.

# And the following Index types:

# *   `IndexType.scene`: Searches the visual information of the video. Index the video using `index_scenes` function.
# *   `IndexType.spoken_word`: Searches the spoken information of the video. Index the video using `index_spoken_words` function.

# ```python
from videodb import SearchType, IndexType

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

# #### View Search Results

# `video.search()` returns a `SearchResults` object containing the sections/shots of videos that semantically match your search query.

# *   `result.get_shots()`: Returns a list of `Shot` objects that matched the search query.
# *   `result.play()`: Opens the video in your default browser/notebook, focusing on the relevant sections.

# #### 🗑️ Cleanup

# You can delete the video from the database using `video.delete()`.

# ```python
video.delete()
# ```

# ## RAG: Working with Multiple Videos
# ---

# `VideoDB` can store and search across multiple videos easily. By default, videos are uploaded to your default collection, and you can create and manage multiple collections (see [Collections docs](https://docs.videodb.io/collections-68)).

# If you're an existing LlamaIndex user building a RAG pipeline on video data, you can use the VideoDB retriever. See [LlamaIndex docs](https://docs.llamaindex.ai/en/stable/examples/retrievers/videodb_retriever.html).

# #### 🔄 Using Collections to Upload Multiple Videos

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
# *   `coll.get_video(video_id)`: Returns the `Video` object for the given video ID.
# *   `coll.delete_video(video_id)`: Deletes the video from the collection.

# ### 📂 Search Across Multiple Videos in a Collection

# Index all videos in a collection and use the `search` method to find relevant results. Here, we index the spoken content for a quick experiment.

# > Indexing may take time for longer videos.

# ```python
# For simplicity, we're just indexing the spoken content of each video.
for video in coll.get_videos():
    video.index_spoken_words()
    print(f"Indexed {video.name}")
# ```

# ### Search Inside a Collection

# Search across videos in a collection using `coll.search()`.

# ```python
# search in the collection of videos
results = coll.search(query="Deep sleep")
results.play()
# ```

# ```python
results = coll.search(query="What are the benefits of morning sunlight?")
results.play()
# ```

# ```python
results = coll.search(query="What are Adaptogens?")
results.play()
# ```

# #### View Search Results

# `video.search()` returns a `SearchResults` object containing the sections/shots of videos that semantically match your search query.

# *   `result.get_shots()`: Returns a list of `Shot` objects that matched the search query.
# *   `result.play()`: Opens the video in your default browser/notebook, focusing on the relevant sections.

# VideoDB fundamentally removes file limitations, empowering you to seamlessly access and stream videos. Stay tuned for exciting features in upcoming versions, and keep building awesome stuff with VideoDB! 🤘

# ### Explore More with the Video Object

# The `Video` object has several methods useful for various use cases.

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

# Returns a new stream instantly with subtitles added to the video. The subtitle function has many styling parameters like font, size, and background color. See the notebook: [Subtitle Styles](https://github.com/video-db/videodb-cookbook/blob/main/guides/Subtitle.ipynb) for details.

# ```python
new_stream = video.add_subtitle()
play_stream(new_stream)
# ```

# #### Generate Thumbnail of Video

# Use `video.generate_thumbnail(time=)` to generate a thumbnail image of a video at a specific timestamp.

# ```python
from IPython.display import Image

image = video.generate_thumbnail(time=12.0)
Image(url=image.url)
# ```

# #### Delete a video

# *   `video.delete()`: Deletes a video.

# ```python
video.delete()
# ```

# See more examples and tutorials at [Build with VideoDB](https://docs.videodb.io/build-with-videodb-35) to explore the possibilities with VideoDB.
```

---

# IPYNB Notebook: Multimodal_Quickstart [Source Link](https://github.com/video-db/videodb-cookbook/blob/main/quickstart/Multimodal_Quickstart.ipynb)

 This was processed through custom_2.txt


---

# IPYNB Notebook: Scene Index QuickStart [Source Link](https://github.com/video-db/videodb-cookbook/blob/main/quickstart/Scene%20Index%20QuickStart.ipynb)

```markdown
# ⚡️ Quickstart: Scene Indexing with VideoDB

<a href="https://colab.research.google.com/github/video-db/videodb-cookbook/blob/main/quickstart/Scene%20Index%20QuickStart.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

This guide provides a quick introduction to scene indexing with VideoDB. Scene indexing enables you to easily extract and index visual information from your videos, unlocking powerful search capabilities. Leverage vision models and VideoDB to build sophisticated applications like Retrieval-Augmented Generation (RAG) systems.

Example use case:
![](https://raw.githubusercontent.com/video-db/videodb-cookbook/main/images/scene_index/intro.png)

## Setup
---

### 📦 Installing the VideoDB Package

```python
!pip install -U videodb
```

### 🔑 Authentication

To connect to VideoDB, you'll need your API key.

```python
import videodb
import os
from getpass import getpass

api_key = getpass("Please enter your VideoDB API Key: ")

os.environ["VIDEO_DB_API_KEY"] = api_key
```

### 🌐 Connecting to VideoDB

Establish a connection to VideoDB and retrieve a collection.

```python
from videodb import connect

conn = connect()
coll = conn.get_collection()
```

### 🎥 Uploading a Video

Upload a video to VideoDB to begin indexing.

```python
video = coll.upload(url="https://www.youtube.com/watch?v=LejnTJL173Y")
```

## 📇 Indexing Scenes
---

The `index_scenes` function automates the process of indexing visual information within your video.

```python
index_id = video.index_scenes()
```

### Optional Parameters

Customize the scene indexing process using these optional parameters:

*   **Extraction Algorithm:** Choose from different algorithms to select scenes and frames.
*   **Prompts:** Use prompts to guide a vision model in describing scenes and frames.

Refer to the [Scene and Frame Object documentation](https://github.com/video-db/videodb-cookbook/blob/main/guides/video/scene-index/advanced_visual_search.ipynb) for more details.

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

```text
[{'description': 'The image depicts a man sitting in an office or conference room, characterized by the presence of glass windows with blinds behind him. He is wearing a dark suit, a white dress shirt, and a dark striped tie. The man appears to be contemplative, with his eyes closed or looking down, and a slight smile on his face. The background shows a bright, well-lit room with natural light filtering through the windows. The atmosphere seems professional and formal, suggesting a workplace or corporate environment. The man’s bald head and expression give an impression of a moment of reflection or contentment.',
  'end': 10.01,
  'start': 0.0},
 {'description': 'The image shows a man with a receding hairline, wearing a dark suit, light blue shirt, and dark striped tie. He appears to be seated, with a neutral or slightly contemplative expression on his face. Behind him, there are large office windows with horizontal blinds partially closed, through which an indistinct office environment is visible. The lighting is soft, creating a professional atmosphere. The man’s posture suggests he could be engaged in a conversation or in thought, possibly in a workplace setting. The overall mood seems formal and reflective, indicating a business or serious context.',
  'end': 20.02,
  'start': 10.01},
 {'description': 'The image depicts a group of people gathered under a large tent in an outdoor setting. At the forefront, several individuals are seated, their faces showing a range of emotions. In the background, a few people stand, with one person holding a notebook and another with hands clasped in what appears to be a prayer or contemplative pose. The surrounding environment is sparsely wooded, with trees visible without leaves. The natural light suggests a possible early spring or late autumn setting. The overall atmosphere evokes a community gathering, perhaps a public meeting, sermon, or ceremony.',
  'end': 30.03,
  'start': 20.02},
 {'description': "The image shows two men under a tent, with one of them energetically raising both hands and looking upwards. He is wearing a light brown short-sleeved shirt, tucked into dark trousers, with black glasses and a dark belt. A black object is visible in his pocket. The other man, standing slightly behind, appears calm and is dressed in a plaid shirt holding a book or notebook. The background is blurred but appears to be an outdoor setting with trees or foliage. There's also a glimpse of string lights hanging in the background from the tent structure.",
  'end': 40.04,
  'start': 30.03},
 {'description': 'The image captures a man standing outdoors, wearing a brown tweed blazer, a blue dress shirt, and a striped tie. He sports dark sunglasses, and his sandy blonde hair is neatly combed. The setting appears to be rural, with a field and a sparse line of trees in the background, blending into an overcast sky. The man exudes a composed demeanor, possibly engaged in a serious conversation or observation. The composition and attire suggest a professional context, likely a detective or an investigator, amidst an investigation or some official duty in a quiet, open expanse.',
  'end': 50.05,
  'start': 40.04},
 {'description': "The image depicts a man standing under a shelter with a backdrop of a blurred, outdoor scene, possibly a field or open land. He is wearing a dark-colored, textured suit jacket over a dress shirt and tie, with his hair neatly combed back. The atmosphere appears to be overcast, as indicated by the muted, natural lighting. Behind him, the sky is cloudy with silhouettes of barren trees suggesting a cold or autumn season. The man's serious expression and formal attire suggest a contemplative or solemn mood, possibly indicating he is in a thoughtful or introspective moment.",
  'end': 60.06,
  'start': 50.05},
 {'description': 'The image depicts two men standing side by side, dressed in formal attire like suits and ties. The man on the left is wearing sunglasses and has a serious expression, while the man on the right looks pensive. They appear to be outdoors under a covered structure, with a field or open landscape visible in the blurred background. The setting seems calm, possibly rural with trees and greenery. The lighting suggests it might be early morning or late afternoon, as it has a warm, soft quality. The scene hints at a serious or contemplative moment shared between the two individuals.',
  'end': 70.07,
  'start': 60.06},
 {'description': 'The image depicts a man wearing sunglasses and a suit with a tie, standing under a covered area. His hair is light brown and he has a serious expression. From the background, it appears he is in an outdoor setting, perhaps a field or open space with a cloudy sky. Other people are visible in the blurred background, casually dressed and seemingly engaged in various activities. There are also cars and tents visible, suggesting an event or gathering is taking place. The man in the foreground seems to be an important figure or speaker at the event.',
  'end': 80.08,
  'start': 70.07},
 {'description': "The image depicts a diverse group of people gathered under a large canopy or tent in an outdoor setting. Several individuals are standing at the back, notable among them are two men in suits, one wearing sunglasses, suggesting formality or authority. The audience seated in the foreground appears engaged and attentive, suggesting a communal gathering, possibly a meeting or ceremony. The background reveals a sparse, late autumn forest, indicating a rural location. The overall atmosphere reflects a sense of solemnity or importance given the attendees' focused demeanor and the formal attire of some individuals.",
  'end': 90.09,
  'start': 80.08},
 {'description': 'The image depicts a man speaking passionately into a microphone under a tent, likely at a religious or community event. He is dressed in a short-sleeve, button-up shirt with a tie, and he gestures emphatically with his hand. The tent is adorned with various banners and signs, some of which contain religious messages such as "Jesus answers" and "I am the way." There are string lights hanging, adding to the ambiance. The setup includes an old-fashioned speaker, suggesting an emphasis on reaching an audience with his message. The atmosphere appears earnest and engaging.',
  'end': 100.1,
  'start': 90.09},
 {'description': 'The image shows two men walking towards a parked, older model sedan in an empty, expansive parking lot. The man on the left is wearing a suit and holding a book or folder, while the man on the right is dressed in a light-colored shirt and dark pants. The background features multiple warehouse-style buildings with a somewhat neglected or abandoned appearance. The sky is overcast, adding a muted, somewhat somber tone to the scene. The overall atmosphere suggests a moment of investigation or discussion in a desolate, industrial area.',
  'end': 110.11,
  'start': 100.1},
 {'description': "The image shows a woman sitting on a bed in a cozy, dimly-lit bedroom, which exudes a warm, yellowish ambiance created by a lamp on a nightstand. She appears thoughtful or pensive, wearing a casual outfit of shorts and a sleeveless top. The room is decorated with soft, plush toys, including a large teddy bear, suggesting a comforting and personal space. The bed is covered with a flowery patterned sheet. The background features floral wallpaper, adding to the room's vintage charm. Another person is partially visible but out-of-focus in the foreground, indicating an interaction or shared moment.",
  'end': 120.12,
  'start': 110.11},
 {'description': 'The image features a man with light brown hair, captured in a dimly lit environment. His expression appears serious and contemplative, as he looks downward. The lighting creates shadows on his face, accentuating his features. He is wearing a collared shirt, and appears to be indoors, possibly in a room with muted beige walls. The image has a subdued and introspective atmosphere, suggesting that the man might be deep in thought or reflecting on something significant. The overall tone of the image is moody and contemplative.',
  'end': 130.13,
  'start': 120.12},
 {'description': 'The image depicts two men in formal attire, possibly detectives or law enforcement officers, engaged in a conversation outdoors. One man, sitting on a bench, drinks from a bottle, while the other, leaning against a car, holds a cup. Both are wearing dress shirts and ties, with the man standing also carrying a gun in a shoulder holster, indicative of their professional roles. They appear to be in a rural or semi-rural setting, with a backdrop of trees, a railroad track, and some scattered buildings. The overall mood suggests a serious, though relaxed, discussion.',
  'end': 140.14,
  'start': 130.13},
 {'description': 'The image depicts two men in a dimly lit bar, engaged in conversation. One man, on the left, is wearing a blue shirt and appears to be speaking emphatically. The other man, on the right, is partially visible and is smoking a cigarette. A neon sign with indistinguishable writing and a yellow graphic is illuminated in the background, casting an atmospheric glow over the scene. The overall ambiance suggests an intense or serious discussion between the two individuals in a casual, perhaps somber setting.',
  'end': 150.15,
  'start': 140.14},
 {'description': 'The image depicts two men in a dimly lit setting, seemingly engaged in a serious conversation. The man on the left is wearing a dark shirt and has a stern, focused expression. The man on the right, slightly out of focus, is also engaged and leaning towards the other man, wearing a lighter colored shirt. The background features a neon sign giving the impression that they are in a bar or a similarly casual venue. The overall atmosphere is tense, suggesting a moment of deep discussion or confrontation between the two individuals.',
  'end': 160.16,
  'start': 150.15},
 {'description': 'The image depicts two men in casual clothing sitting closely together in a dimly lit environment, such as a bar or a night-time setting. The man on the left appears to be deeply focused, while the man on the right is speaking with a somewhat serious expression, suggesting an intense or important conversation. The background is blurred, showing vague hints of lights and signs, adding to the intimate ambiance. The lighting casts shadows on their faces, highlighting a moody atmosphere. The overall scene suggests a moment of significant dialogue or revelation between the two characters.',
  'end': 170.17,
  'start': 160.16},
 {'description': 'The image depicts a dimly lit workshop or garage with a figure engaged in action amidst various tools and machinery. The background is illuminated by natural light streaming in from the open entrance or window, creating a silhouette effect on the person and objects in the foreground. The environment appears cluttered, with shelves and workbenches holding an assortment of equipment and materials. The person seems to be in motion, potentially running or carrying something, adding a dynamic element to the scene. The overall atmosphere suggests an industrious or urgent activity taking place in an industrial setting.',
  'end': 180.18,
  'start': 170.17},
 {'description': 'The image depicts two men standing outdoors under a canopy of sprawling, leafless trees. Both men are dressed in business attire, with the one on the left wearing a dark blazer over a shirt and tie, while the one on the right has a grey suit and tie. The man on the left appears to be holding a folder or a book in his left hand, with his right hand on his hip. The setting is somewhat muted, suggesting it might be autumn or winter. Their expressions convey a serious or thoughtful demeanor, possibly indicating they are engaged in a significant or intense conversation.',
  'end': 190.19,
  'start': 180.18},
 {'description': 'The image depicts two men sitting in the front seats of a car. The man on the left, who has light-colored hair and is wearing a suit and tie, appears to be deep in thought, looking forward. The man on the right, who is driving, has darker hair and is dressed in darker clothing. He has his left arm resting on the steering wheel, focused on the road ahead. The setting outside the car seems rural, with a blurred view of trees and open land visible through the windows. The atmosphere suggests a serious or reflective moment between the two characters.',
  'end': 200.2,
  'start': 190.19},
 {'description': "The image depicts a scene inside a vehicle, with a man driving. He is seen smoking a cigarette, with his left hand resting on the steering wheel. The man's expression appears contemplative as he looks ahead. The car's interior is dimly lit, contrasting with the brighter background outside the windshield, where a blurry scene of trees and sky can be seen. Shadows and light play across his face, adding depth to the scene. The mood conveyed is somewhat introspective, with a focus on the man lost in his thoughts while driving through what seems to be a rural or suburban area.",
  'end': 210.21,
  'start': 200.2},
 {'description': 'The image shows two men inside a car, with the one on the left driving. The driver, wearing a dark top, is framed prominently in the foreground, facing forward with a focused expression. He rests his left arm on the steering wheel, partially wearing a watch. The passenger, seated to his right, appears thoughtful, gazing ahead or possibly slightly towards the driver. The background through the car windows shows a cloudy sky, suggesting overcast weather. The setting inside the vehicle feels tense or serious, possibly implying a contemplative or significant moment between the two men.',
  'end': 220.22,
  'start': 210.21},
 {'description': 'The image depicts two individuals walking in a parking lot, likely belonging to a police or law enforcement agency, as suggested by the multiple police vehicles with roof lights parked behind them. The individuals are in formal attire, wearing dress shirts and ties. Each carries something in their hands; one seems to hold a bag. The setting is outdoors, with trees providing some shade and a building visible in the background. The environment appears calm and organized, typical of official or professional premises. The overall mood is serious and professional.',
  'end': 230.23,
  'start': 220.22},
 {'description': 'The image depicts three law enforcement officers outside a building with large glass windows and doors, likely an office or police station. Two of the officers, seen from the back, wear light blue shirts and have equipment belts with handcuffs. They are walking towards the building, where another officer in a darker uniform stands near the entrance, facing them. The scene appears casual, with one officer in the doorway possibly greeting or speaking to the approaching officers. Inside, a vending machine is partially visible. The overall atmosphere suggests a routine moment in a police facility.',
  'end': 240.24,
  'start': 230.23},
 {'description': 'The image depicts a man with long, light brown hair and a mustache, sitting in what appears to be an office setting. He is wearing a light grey button-up shirt layered over a white t-shirt. The man has a serious or contemplative expression on his face. The background shows office equipment, including stacked files, a computer monitor, and an older-style printer. On the desk in front of him, there is an open beverage can. The overall atmosphere suggests a mundane, everyday office environment, possibly in a scene from a film or television show.',
  'end': 250.25,
  'start': 240.24},
 {'description': "The image depicts a man driving a car, focusing intently on the road ahead. The scene seems to take place during twilight or early evening, as it is quite dim outside with minimal light. The background shows a somewhat blurry view of trees and sky through the car's window. The man, dressed in a business suit, appears solemn, suggesting a serious or contemplative moment. The overall ambiance is tense and reserved, with the dark, muted colors contributing to a somber mood. The close-up angle accentuates the man's concentration and the confined space within the vehicle.",
  'end': 260.26,
  'start': 250.25},
 {'description': "The image shows a man sitting inside a car, viewed through the partially fogged-up window. He appears to be in a contemplative or serious mood, raising one hand in a slightly open gesture. The background outside the car suggests it is either evening or early morning, with dim natural light enhancing the somber atmosphere. The man's expression is focused, eyes directed slightly to the side as if engaged in deep thought or a conversation. The interior of the car is dimly lit, adding to the pensive, introspective ambiance of the scene.",
  'end': 270.27,
  'start': 260.26},
 {'description': "The image features two men sitting in the front seats of a car, appearing to engage in a serious conversation. The man in the driver's seat, on the right side of the image, is facing slightly towards the passenger, who seems deep in thought with his hand covering part of his face. The scene appears to take place during the day, with the car interior dimly lit and the window showing a blurry outdoor landscape. Both individuals have focused expressions, suggesting a tense or contemplative moment. The overall mood of the image is somber and reflective.",
  'end': 280.28,
  'start': 270.27},
 {'description': 'The image features two men seated in a car during what appears to be a somber or contemplative moment. The man on the left is in the passenger seat, looking down with a serious expression, while the man on the right is behind the wheel, focusing on the road ahead. The lighting is dim and moody, suggesting a cloudy or overcast sky outside. The background through the car windows reveals a blurred landscape, possibly rural with vegetation. The atmosphere hints at a deep or serious conversation, or perhaps a tense and introspective journey.',
  'end': 290.29,
  'start': 280.28},
 {'description': "The image depicts a man sitting in the driver's seat of a car during twilight or early evening. The interior lighting is dim, highlighting his contemplative expression. He appears to be casually dressed in a dark jacket over a shirt. His hand is resting on the vehicle's steering wheel, and he seems to be gazing out of the windshield, possibly lost in thought. The outside scenery through the car window is blurry, suggesting motion or an unfocused camera lens, with hints of trees and power lines in the background. The scene evokes a sense of introspection and quiet contemplation.",
  'end': 300.05,
  'start': 290.29},
 {'description': "The image depicts a man sitting inside a car, most likely the driver's seat. It appears to be late in the day or early evening as the natural light outside is dim. The man, dressed in a suit jacket and shirt, is gazing intently to his left with a contemplative expression. The interior of the car is dim, with shadows obscuring much of his face, enhancing the contemplative mood. The background, visible through the windows, shows an indistinct landscape, perhaps with trees or fields. The image conveys a somber, thoughtful atmosphere.",
  'end': 310.01,
  'start': 300.0},
 {'description': 'The image depicts a man seated inside a car, likely in the front passenger seat. The scene appears to be set during the day, as the window next to him shows an outside view with trees and a cloudy sky. He looks contemplative, gazing out the window with a serious expression. The interior of the car is dimly lit, and he wears a dark blazer suggesting a formal or business-like setting. The composition and mood of the image imply a moment of reflection or deep thought while possibly traveling.',
  'end': 320.02,
  'start': 310.01},
 {'description': 'The image shows a side profile of a man seated inside a car. It appears to be either dawn or dusk outside, given the low lighting. He is wearing a suit and shirt, looking contemplative with his fingers resting on his chin. The background outside the car window is blurred, but faint outlines of trees and electric lines can be seen against a dim sky. The interior of the car is dark, matching the somber and introspective mood of the scene. The man’s expression is serious, adding to the reflective atmosphere of the image.',
  'end': 330.03,
  'start': 320.02},
 {'description': 'The image depicts a man sitting behind the steering wheel of a vehicle, driving. He appears to be wearing a suit and is focused on the road ahead. The scene is somewhat dimly lit, suggesting it could be early morning or evening. The background, visible through the windows, shows a blurred, scenic outdoor setting with trees and a cloudy sky. The man’s expression is serious and concentrated, and the overall mood of the image hints at a reflective or tense moment during his drive. The interior of the car seems ordinary, without any highlighting features.',
  'end': 340.04,
  'start': 330.03},
 {'description': 'In the image, two people are sitting close together in an indoor setting. The person on the left, dressed in a blue collared shirt, appears contemplative or saddened, looking downward. His short dark hair is neatly combed. The person on the right, a woman with long brown hair, gazes at him but her face is slightly blurred, making her expression harder to discern. The subdued lighting and their serious demeanor suggest an emotional or intense conversation. The overall mood is intimate and reflective, with a focus on the emotional connection or conversation between the two individuals.',
  'end': 350.05,
  'start': 340.04},
 {'description': 'The image depicts a tense and emotional moment between two individuals. A man with short dark hair and a serious expression, dressed in a blue button-up shirt, gazes at a distraught woman beside him. The woman, with long, disheveled hair, appears to be in distress, with visible tears streaming down her face. The setting seems to be a somber, dimly lit room, possibly an interrogation room or a place where difficult conversations are held. The man’s facial expression conveys concern and intensity, suggesting he is either consoling or questioning the woman, who is visibly upset.',
  'end': 360.06,
  'start': 350.05},
 {'description': 'In the image, a man is seated on a dark-colored couch in an office setting. He appears disheveled and slightly injured, with a bruise or cut on his forehead. Dressed in a casual, checked shirt, he has a worn-out, fatigued expression. His posture is relaxed yet tense, with his arms resting on the back of the couch. The office has wooden paneling on the walls and a large window with blinds partially drawn. Papers and a pen lie on a desk in the foreground, suggesting a recent or ongoing conversation with another person who is partially visible.',
  'end': 370.07,
  'start': 360.06},
 {'description': 'The image shows an indoor scene viewed through horizontal blinds. A person is walking past, with their face looking straight ahead. The background appears to be an office or a workspace, characterized by bright overhead lighting and various office elements like desks, chairs, and shelves. This office seems somewhat busy with papers, folders, and other typical office equipment scattered around. The person in the foreground is slightly obscured by the blinds, adding to the sense of depth in the image. The overall color palette of the image is neutral and muted, emphasizing the work environment.',
  'end': 380.08,
  'start': 370.07},
 {'description': 'The image captures two men sitting in the front seats of a car. There is a subtle, dim light inside the vehicle, possibly indicating it is either dusk or dawn. The man on the left is in deep thought, with his hand clasped near his mouth as he looks out the window. The driver, to his right, is focused on the road ahead. Both men exhibit serious, contemplative expressions. The outside view is blurred, keeping the focus on the men and imparting a reflective, somber atmosphere to the scene. The dark interior enhances the mood of quiet introspection.',
  'end': 390.09,
  'start': 380.08},
 {'description': 'The image depicts two men in a professional setting, possibly a meeting or an interview. Both men are dressed in formal attire, with the man in the foreground wearing a striped shirt and a dark tie and the man in the background wearing a plain white shirt and a blue tie. The man in the foreground appears focused and engaged, while the man in the background is slightly blurred, suggesting a depth of field effect. A camera is positioned on the table between them, possibly recording the meeting. The room features shelves filled with files and binders, indicating an office environment.',
  'end': 400.1,
  'start': 390.09},
 {'description': "The image depicts a man with long, light brown hair and a mustache, seated indoors. He is wearing a light-colored, button-up shirt and facing to his left, appearing engaged or deep in thought. The background is blurred but shows what seems to be a room with some equipment or possibly a workspace, including what appears to be a computer monitor and some documents or photographs pinned to a board. The lighting is soft and seems to originate from above, casting gentle shadows on the man's face, adding to the contemplative or serious ambiance of the scene.",
  'end': 410.11,
  'start': 400.1},
 {'description': 'A man with long, light brown hair and a mustache is sitting at a table in an office-like setting. He is wearing a light grey buttoned-up shirt and leaning forward, resting his forearms on the table. Around him on the table, there is a can of Lone Star beer, a cup with "Big Hug" written on it, a pack of cigarettes, a lighter, and some documents. In the background, there are shelves with neatly stacked files and folders. The overall setting has a serious, possibly investigative ambiance.',
  'end': 420.12,
  'start': 410.11},
 {'description': "The image displays a monochrome, somewhat grainy photograph of a person's face, which appears to be printed on paper. The face, oriented slightly upwards, is partially obscured by shadows and printed artifacts, conveying a somber, almost eerie atmosphere. Superimposed on the image are blotchy spots that further obscure the subject's features. The paper seems to be lying on a flat surface, possibly a desk or table, with part of what could be a drawer or metal structure visible in the background. The dim, muted lighting intensifies the overall brooding and mysterious mood of the scene.",
  'end': 430.13,
  'start': 420.12},
 {'description': 'The image depicts a man with long hair and a mustache leaning on a wooden desk in what appears to be an office or interrogation room. He is wearing a gray shirt and has a tattoo on his forearm. On the desk are a couple of beverage cans, a pack of cigarettes, and some scattered paper items. In the background, office supplies such as file boxes, a computer monitor, and bookshelves can be seen. The lighting is slightly dim, giving the scene a serious and contemplative atmosphere.',
  'end': 440.14,
  'start': 430.13},
 {'description': 'This image depicts a lively social gathering, possibly a dance or party, inside a dimly lit venue adorned with string lights. The focus is on a man in the foreground, dressed in a light shirt and tie, mid-motion, indicating he is dancing. The background is bustling with people, some of whom are also dancing, while others are observing and mingling. The atmosphere appears warm and festive, with a mix of casual and semi-formal attire. The soft lighting and slight blur give the image a sense of movement and adds to the energetic vibe of the scene.',
  'end': 450.15,
  'start': 440.14},
 {'description': 'The image shows a close-up of a woman lying on the ground, possibly in a forest as suggested by the earthy surroundings and scattered leaves. She appears to be lifeless with her eyes partially open, staring blankly. There are visible blood stains on her face, neck, and chest area, hinting at some form of violence or injury. Her expression is vacant, and the overall scene is somber and eerie, suggesting a tragic event. The lighting is subdued, adding to the grim atmosphere of the image.',
  'end': 460.16,
  'start': 450.15},
 {'description': 'The image showcases a man with long hair and a mustache, sitting at a wooden table in what appears to be an office or interrogation room. He is gesturing with his hand, seemingly engaged in a conversation. On the table in front of him are a can of Lone Star beer, a "Big Hug Mug", and various documents. The background features a wooden cabinet with several binders and a computer monitor. The setting suggests a formal or serious discussion, possibly an interview or interrogation, with the man showing a contemplative and focused demeanor.',
  'end': 470.17,
  'start': 460.16},
 {'description': 'The image shows a man with long, light brown hair and a mustache in a room with wood-paneled walls. He appears to be mid-sentence with a focused and earnest expression. The setting suggests an office or a similar work environment, indicated by the presence of a blurred emblem or logo on the wall behind him and some filing boxes in the background. He is wearing a light-colored shirt, and the overall tone of the image conveys seriousness, as though he is engaged in an important conversation or discussion. The lighting is subdued, lending an air of gravity to the scene.',
  'end': 480.18,
  'start': 470.17},
 {'description': 'The image depicts a rural, overgrown field with scattered, dilapidated structures in the background. Tall grass and wild plants dominate the foreground, while a few visible trees provide some shade. The buildings appear weathered and abandoned, suggesting neglect and long-term disuse. The sky is clear with bright sunlight illuminating the scene, giving it a desolate and isolated feel. There are no apparent pathways or clear signs of human activity in the area. The overall atmosphere is one of abandonment, with nature reclaiming the space once occupied by humans.',
  'end': 490.19,
  'start': 480.18},
 {'description': 'The image depicts a man with long hair and a mustache, leaning forward on a wooden table in a room that seems to be an office or a meeting room. The man is wearing a light gray shirt and looks absorbed. On the table, there are two cans of Lone Star beer, a flip-top lighter, a small toy or figurine, and a few other miscellaneous items. Behind him, there are shelves and boxes indicating a work environment, possibly involving paperwork or records. The atmosphere suggests a serious conversation or contemplation.',
  'end': 500.2,
  'start': 490.19},
 {'description': 'In the image, two men are depicted walking outside at night. One man has his arm around the other, providing support. The man on the left is wearing a dark T-shirt, while the man on the right is in a disheveled white garment that appears akin to a hospital gown or robe, partially exposing his chest. The setting appears to be near a commercial building with bright lights and visible signage, suggesting an urban environment. The surrounding area includes greenery and tall street lamps illuminating the scene. Both individuals appear tired or distressed, indicative of a challenging situation.',
  'end': 510.21,
  'start': 500.2},
 {'description': 'The image features two men walking closely together at night in what appears to be the grounds of a medical facility. The man on the left is supporting the man on the right by holding him up, suggesting the latter may be injured or unwell. The man on the right looks dazed or exhausted, his shirt partially unbuttoned, exposing his chest. Both figures display expressions of fatigue and concern. In the background, the lit signage of the building and the glow from the exterior lights highlight the setting, indicative of a hospital or medical center. The mood is somber and supportive.',
  'end': 520.22,
  'start': 510.21},
 {'description': 'The image depicts a nighttime view of Lafayette General, a hospital with illuminated signage. Several lights illuminate the grounds and entrance area of the medical facility, casting a mix of shadows and bright spots. The building appears to be modern with large windows and a sleek architectural design. Flags are hoisted on poles near the entrance, suggesting a sense of formality and order. In the foreground, there are two people standing on the sidewalk, engaged in conversation or activity, with well-maintained landscaping surrounding the walkway. The overall atmosphere exudes a sense of safety and care expected from a healthcare institution.',
  'end': 530.23,
  'start': 520.22},
 {'description': 'The image is predominantly dark and black, suggesting it might have been taken at night or in a very low-light environment. There are no discernible objects, people, or features visible in the photograph, making it difficult to analyze or describe in detail. The lack of light and

---

# IPYNB Notebook: Cleanup [Source Link](https://github.com/video-db/videodb-cookbook/blob/main/guides/Cleanup.ipynb)

```markdown
## Guide: Cleaning Up Your VideoDB Account

<a href="https://colab.research.google.com/github/video-db/videodb-cookbook/blob/main/guides/Cleanup.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

⚠️ **WARNING: This notebook contains operations that will PERMANENTLY DELETE media files from your VideoDB account.  Deleted files CANNOT be recovered.** ⚠️

🚨 **IMPORTANT:  Before running any deletion cells, meticulously review the files you intend to delete.  Ensure you have backups if necessary.** 🚨

This guide provides instructions for deleting media files (videos, audio, and images) from your VideoDB account to free up storage.  It covers the following actions:

* Deleting all videos within a collection.
* Deleting all audio files within a collection.
* Deleting all images within a collection.

**Use this notebook with extreme caution.**

## 🛠️ Setup

Before you begin, you'll need your VideoDB API key.

```python
%pip install videodb
```

```python
import videodb
import os
from getpass import getpass

# Securely prompt for the API key
api_key = getpass("Please enter your VideoDB API Key: ")

# Set the API key as an environment variable (safer than hardcoding)
os.environ["VIDEO_DB_API_KEY"] = api_key

# Connect to VideoDB
conn = videodb.connect()
```

## Review Collections

It's crucial to understand the contents of your collections before deleting anything.  This cell lists your collections and the number of videos, audio files, and images in each.

```python
colls = conn.get_collections()

print(f"Found {len(colls)} collections:")
print()

for coll in colls:
    videos = coll.get_videos()
    audios = coll.get_audios()  # Corrected: Should be get_audios()
    images = coll.get_images()

    print(f"Collection '{coll.name}' (id: {coll.id})")
    print(f"  - Videos : {len(videos)}")
    print(f"  - Audio  : {len(audios)}")
    print(f"  - Images : {len(images)}")
    print()
```

## Specify the Collection

Before running any deletion code, **replace `"YOUR_COLLECTION_ID_HERE"` with the actual ID of the collection you want to clean up.**  You can find the Collection ID in the output of the "Review Collections" cell above.  Double-check that you've entered the correct ID.

```python
collection_id = "YOUR_COLLECTION_ID_HERE"  # REPLACE THIS WITH THE ACTUAL COLLECTION ID
```

### ⚠️ DELETE ALL VIDEOS

This cell will delete **all videos** in the specified collection.

**Double-check the `collection_id` variable above before running this cell.  This action is irreversible.**

```python
coll = conn.get_collection(collection_id)
videos = coll.get_videos()

for video in videos:
    video.delete()
    print(f"Deleted video {video.name} ({video.id})")
print("All videos in the collection have been deleted.")
```

### ⚠️ DELETE ALL AUDIO FILES

This cell will delete **all audio files** in the specified collection.

**Double-check the `collection_id` variable above before running this cell.  This action is irreversible.**

```python
coll = conn.get_collection(collection_id)
audios = coll.get_audios()

for audio in audios:
    audio.delete()
    print(f"Deleted audio {audio.name} ({audio.id})")
print("All audio files in the collection have been deleted.")
```

### ⚠️ DELETE ALL IMAGES

This cell will delete **all images** in the specified collection.

**Double-check the `collection_id` variable above before running this cell.  This action is irreversible.**

```python
coll = conn.get_collection(collection_id)
images = coll.get_images()

for image in images:
    image.delete()
    print(f"Deleted image {image.name} ({image.id})")
print("All images in the collection have been deleted.")
```
```

Key changes and improvements:

* **Enhanced Warnings:**  Made the warnings more prominent and emphasized the permanent nature of the deletions.
* **Clarified Scope:** Specifically state what *all* the notebook will do.
* **Simplified Language:** Replaced more complex wording with simpler, clearer alternatives.
* **Added Extra Clarity:** Further explanations are provided about each process.
* **Fixed a Bug:** Corrected `coll.get_images()` to `coll.get_audios()` in the "Review Collections" cell.
* **Explicit `collection_id` Instruction:** Emphasized the need to replace `"YOUR_COLLECTION_ID_HERE"` and reminded the user where to find the ID.
* **Added Completion Messages:** Added "All videos/audio/images in the collection have been deleted." after each deletion loop to confirm the operation's success.
* **Improved Security:**  Reinforced the use of `getpass` and storing the API key in an environment variable instead of hardcoding it.
* **Removed Redundancy:** Eliminated unnecessary phrases.
* **Consistent Formatting:** Ensured consistency in headings, code blocks, and comments.
* **Stronger emphasis on verifying `collection_id` before deletion.**  This is *the* most critical aspect of this notebook.
* **Avoided the word "Cleanup" in places where a more descriptive term could be used.** "Cleaning Up" is the title; using a more specific word elsewhere (like "Deletion") improves clarity.


---

# IPYNB Notebook: TextAsset [Source Link](https://github.com/video-db/videodb-cookbook/blob/main/guides/TextAsset.ipynb)

```python
# @title Open in Colab
# @markdown [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/video-db/videodb-cookbook/blob/nb/main/guides/asset/TextAsset.ipynb)

# @markdown # Guide: TextAsset

# @markdown ## Overview

# @markdown This guide introduces you to `TextAssets` and how to use them to overlay text elements on your videos within VideoDB.  We'll explore the various styling configurations available through the `TextStyle` class, including:

# @markdown *   Font Styling (font, size, color, border)
# @markdown *   Background Box Styling (color, border, size)
# @markdown *   Shadow Effects
# @markdown *   Position and Alignment

# @markdown ---

# @markdown ## Setup

# @markdown ### 📦 Installing Packages

# @markdown Make sure you have the `videodb` package installed.


```python
# @markdown %pip install videodb
```

```python
# @markdown ### 🔑 API Keys
# @markdown Before proceeding, ensure you have access to [VideoDB](https://videodb.io). You can get your API key from the [VideoDB Console](https://console.videodb.io) (free for the first 50 uploads, no credit card required!).
```

```python
import videodb
import os
from getpass import getpass

api_key = getpass("Please enter your VideoDB API Key: ")

os.environ["VIDEO_DB_API_KEY"] = api_key
```

```python
# @markdown ### 🌐 Connect to VideoDB
# @markdown Connect to VideoDB using your API key and get a collection to work with.
```

```python
from videodb import connect

conn = connect()
coll = conn.get_collection()
```

```python
# @markdown ### 🎥 Upload Video
# @markdown VideoDB uses video as a base to create a timeline. Click here to learn more about how [Timelines and Assets](https://docs.videodb.io/timeline-and-assets-44) function.
```

```python
video = coll.upload(url="https://www.youtube.com/watch?v=w4NEOTvstAc")
video.play()
```

```python
# @markdown ## Creating Assets
# @markdown ---
# @markdown Now, let's create the assets we'll use in our Video Timeline:

# @markdown *   `VideoAsset`:  The base video for our timeline.
# @markdown *   `TextAsset`:  The text elements that will be overlaid on the video.

# @markdown > Check out [Timelines and Assets](https://docs.videodb.io/timeline-and-assets-44) in the VideoDB documentation for more information.

# @markdown ### 🎥 VideoAsset
# @markdown ---
# @markdown We'll create a `VideoAsset` from the uploaded video, specifying a start and end time.
```

```python
from videodb.asset import VideoAsset

# Create a VideoAsset from the uploaded video
video_asset = VideoAsset(
    asset_id=video.id,
    start=0,
    end=60,
)
```

```python
# @markdown ### 🔠 TextAsset: Styling Examples
# @markdown ---
# @markdown To create a `TextAsset`, you need to specify the `text` and optionally the `duration`.  You can also customize the text appearance using the `style` parameter, which accepts a `TextStyle` instance.

# @markdown #### Default Styling
# @markdown By default, the `TextAsset` will use a default font and appearance.
```

```python
from videodb.asset import TextAsset

text_asset_1 = TextAsset(text="THIS IS A SENTENCE", duration=5)
```

# @markdown
# @markdown ![](https://github.com/video-db/videodb-cookbook-assets/raw/main/images/guides/text-asset/default_style.png)

```python
# @markdown #### Custom Styling with TextStyle
# @markdown You can customize the appearance of `TextAssets` using the `TextStyle` class.  Here are some examples:

# @markdown **1. Font Styling**
```

```python
from videodb.asset import TextAsset, TextStyle


# Create TextAsset with custom styling using TextStyle
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

# @markdown
# @markdown ![](https://github.com/video-db/videodb-cookbook-assets/raw/main/images/guides/text-asset/font_styling.png)

```python
# @markdown **2. Configuring Background Box**
```

```python
from videodb.asset import TextAsset, TextStyle


# Create TextAsset with custom styling using TextStyle
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

# @markdown
# @markdown ![](https://github.com/video-db/videodb-cookbook-assets/raw/main/images/guides/text-asset/background_box.png)

```python
# @markdown **3. Configuring Shadows**
```

```python
from videodb.asset import TextAsset, TextStyle


# Create TextAsset with custom styling using TextStyle
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

# @markdown
# @markdown ![](https://github.com/video-db/videodb-cookbook-assets/raw/main/images/guides/text-asset/custom_shadow.png)

```python
# @markdown **4. Position and Alignment**
# @markdown  You can control the `x` and `y` position of the text, as well as its alignment within a bounding box.  `text_align` uses a "T+L", "M+C", "B+R" notation for Top+Left, Middle+Center, and Bottom+Right alignment. `y_align` defines the alignment of the box itself.
```

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

# @markdown
# @markdown ![](https://github.com/video-db/videodb-cookbook-assets/raw/main/images/guides/text-asset/text_align.png)
# @markdown ![](https://github.com/video-db/videodb-cookbook-assets/raw/main/images/guides/text-asset/y_align.png)

```python
# @markdown ## View Results
# @markdown ---
# @markdown ### 🎼 Create a timeline using Timeline
# @markdown Create a timeline, add the base video, and then add the text overlays at different times.
```

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

```python
# @markdown ### ▶️ Play the Video
# @markdown Generate a stream URL and play the video with the text overlays.
```

```python
from videodb import play_stream

stream_url = timeline.generate_stream()
play_stream(stream_url)
```


---

# IPYNB Notebook: genai [Source Link](https://github.com/video-db/videodb-cookbook/blob/main/guides/genai.ipynb)

```python
# @title ✨ Generating Media with VideoDB: A Simple Guide { display-mode: "form" }
# @markdown This guide demonstrates how to generate various media assets (images, music, sound effects, voiceovers, and video clips) using the VideoDB Python SDK.

# @markdown [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/video-db/videodb-cookbook/blob/main/guides/genai.ipynb)

# @markdown ### 🎯 Objective
# @markdown Learn how to use VideoDB's generative functions to programmatically create media from text prompts or existing videos.

# @markdown #### 📦 Install VideoDB SDK
# @markdown First, install the VideoDB library:

# @markdown
# @markdown **Note:** You may need to restart the runtime after installing the library.

# @markdown #### 🔑 Connect to VideoDB
# @markdown
# @markdown Use your [API key](https://console.videodb.io) to connect to VideoDB.  The API key is stored as an environment variable for secure access.

# @markdown
# @markdown **Warning:** Never commit your API key directly in your code. Use environment variables or secure storage mechanisms instead.


!pip install videodb --upgrade

import videodb
import os
from getpass import getpass

api_key = getpass("Please enter your VideoDB API Key: ")

os.environ["VIDEO_DB_API_KEY"] = api_key

# Connect and get the default collection
conn = videodb.connect()
coll = conn.get_collection()

print(f"Connected! Using collection ID: {coll.id}")


# @markdown ## 🚀 Generating Media Assets
# @markdown
# @markdown Use the `coll` object to generate media.  Each code block includes example usage and explanations of configuration options.

# @markdown ### 🖼️ Generate Image (`generate_image`)
# @markdown
# @markdown Create images from text prompts.


from IPython.display import Image

image_prompt = "Green neon sign jellyfish photography"  #@param {type:"string"} # Your prompt here
print(f"Generating image for: '{image_prompt}'")

# Generate image (returns an Image object)
generated_image = coll.generate_image(prompt=image_prompt)

print(f"-> Image generation started! Image ID: {generated_image.id}")

# Get the URL
image_url = generated_image.generate_url()
print(f"-> Image URL: {image_url}")


Image(url=image_url)


# @markdown **⚡ Power Up `generate_image`:** Configuration Options Explained
# @markdown
# @markdown *   `prompt` (str): **Required.** The text description for image generation.
# @markdown *   `aspect_ratio` (Literal['1:1', '9:16', '16:9', '4:3', '3:4'] | None): *Optional.* The desired aspect ratio. Defaults to `'1:1'`.
# @markdown *   `callback_url` (str | None): *Optional.* URL for completion notification. Defaults to `None`.


generated_image = coll.generate_image(
    prompt=image_prompt,
    aspect_ratio="9:16",  # Custom Aspect ratio
)

Image(url=generated_image.generate_url())


# @markdown ### 🎵 Generate Music (`generate_music`)
# @markdown
# @markdown Create music from a text description.


from IPython.display import Audio

music_prompt = "Upbeat electronic background music"  #@param {type:"string"}
print(f"Generating music for: '{music_prompt}'")

# Generate music (returns an Audio object)
generated_music = coll.generate_music(prompt=music_prompt)

# Get the URL
music_url = generated_music.generate_url()
print(f"-> Music URL: {music_url}")

Audio(url=music_url, filename="audio.mp3")


# @markdown **⚡ Power Up `generate_music`:** Configuration Options Explained
# @markdown
# @markdown *   `prompt` (str): **Required.** The text description of the music.
# @markdown *   `duration` (int): *Optional.* The desired duration of the music in seconds. Defaults to `5`.
# @markdown *   `callback_url` (str | None): *Optional.* A URL endpoint that VideoDB will notify when generation is complete. Defaults to `None`.


generated_music = coll.generate_music(
    prompt=music_prompt,
    duration=10,  # Custom Duration
)

Audio(url=generated_music.generate_url(), filename="audio.mp3")


# @markdown ### 🔊 Generate Sound Effect (`generate_sound_effect`)
# @markdown
# @markdown Create short sounds.


from IPython.display import Audio

sfx_prompt = "Generate a sound of footsteps on wet gravel, for a mystery film scene. The sound should be realistic, rhythmic, and slightly echoey, around 3 seconds long"  #@param {type:"string"}  # Your prompt here
print(f"Generating sound effect for: '{sfx_prompt}'")

# Generate SFX (returns an Audio object)
generated_sfx = coll.generate_sound_effect(prompt=sfx_prompt, duration=5)

# Get the URL
sfx_url = generated_sfx.generate_url()
print(f"-> SFX URL: {sfx_url}")

Audio(url=sfx_url, filename="audio.mp3")


# @markdown ### 🗣️ Generate Voice (`generate_voice`)
# @markdown
# @markdown Convert text to speech.


from IPython.display import Audio

text_to_speak = "This is an AI voice speaking. I was created using the generate_voice method in VideoDB!"  #@param {type:"string"}  # Your text here
print(f"Generating voice for: '{text_to_speak}'")

# Generate voice (returns an Audio object)
generated_voice = coll.generate_voice(text=text_to_speak)

print(f"-> Voice generation started! Audio ID: {generated_voice.id}")

# Get the URL
voice_url = generated_voice.generate_url()
print(f"-> Voice URL : {voice_url}")

Audio(url=voice_url, filename="audio.mp3")


# @markdown **⚡ Power Up `generate_voice`:** Configuration Options Explained
# @markdown
# @markdown *   `text` (str): **Required.** The text to be converted to speech.
# @markdown *   `voice_name` (str): *Optional.* Name of the voice to use (check VideoDB docs/console for options). Defaults to `'Default'`.
# @markdown *   `config` (dict): *Optional.* Configuration dictionary for the voice generation (e.g., speed, pitch; depends on provider). Defaults to `{}`.
# @markdown *   `callback_url` (str | None): *Optional.* URL for completion notification. Defaults to `None`.

# @markdown #### Available Voice Names
# @markdown
# @markdown Consult the VideoDB documentation or console for the most up-to-date list of available voices and their characteristics. The following table provides examples:

# @markdown | Name      | Voice Style     | Accent        | Gender         |
# @markdown |-----------|------------------|---------------|----------------|
# @markdown | Aria      | Expressive       | American      | Female         |
# @markdown | Roger     | Confident        | American      | Male           |
# @markdown | Sarah     | Soft             | American      | Young Female   |
# @markdown | Laura     | Upbeat           | American      | Young Female   |
# @markdown | Charlie   | Natural          | Australian    | Male           |
# @markdown | George    | Warm             | British       | Middle-aged Male |
# @markdown | Callum    | Intense          | Transatlantic | Male           |
# @markdown | River     | Confident        | American      | Non-binary     |
# @markdown | Liam      | Articulate       | American      | Young Male     |
# @markdown | Charlotte | Seductive        | Swedish       | Young Female   |
# @markdown | Alice     | Confident        | British       | Middle-aged Female |
# @markdown | Matilda   | Friendly         | American      | Middle-aged Female |
# @markdown | Will      | Friendly         | American      | Young Male     |
# @markdown | Jessica   | Expressive       | American      | Young Female   |
# @markdown | Eric      | Friendly         | American      | Middle-aged Male |
# @markdown | Chris     | Casual           | American      | Middle-aged Male |
# @markdown | Brian     | Deep             | American      | Middle-aged Male |
# @markdown | Daniel    | Authoritative    | British       | Middle-aged Male |
# @markdown | Lily      | Warm             | British       | Middle-aged Female |
# @markdown | Bill      | Trustworthy      | American      | Old Male       |


generated_voice = coll.generate_voice(
    text=text_to_speak,
    voice_name="Charlotte",  # Custom Voice Name
    config={
        "stability": 0.0,  # Determines how stable the voice is and the randomness between each generation. Lower values introduce broader emotional range for the voice. Higher values can result in a monotonous voice with limited emotion.
        "similarity_boost": 1.0,  # Determines how closely the AI should adhere to the original voice when attempting to replicate it.
        "style": 0.0,  # Determines the style exaggeration of the voice. This setting attempts to amplify the style of the original speaker. It does consume additional computational resources and might increase latency if set to anything other than 0.
    },
)


Audio(url=generated_voice.generate_url(), filename="audio.mp3")


# @markdown ### 🎬 Generate Video (`generate_video`)
# @markdown
# @markdown Create short video clips (5-8 seconds).


video_prompt = "Cinematic close-up of a majestic lion slowly rolling its head, its golden mane catching the soft afternoon sunlight on the savanna."  #@param {type:"string"}  # Your prompt here
print(f"Generating video for: '{video_prompt}'")

# Generate video (returns a Video object)
# Duration must be 5-8 seconds if specified (e.g., duration=7)
generated_video = coll.generate_video(prompt=video_prompt)


# Play the video
generated_video.play()


# @markdown **Configuration Options (`generate_video`):**
# @markdown
# @markdown *   `prompt` (str): **Required.** Text prompt for video generation.
# @markdown *   `duration` (float): *Optional.* Duration in seconds. **Must be an integer value between 5 and 8 (inclusive).** Defaults to `5`. Raises `ValueError` if invalid.
# @markdown *   `callback_url` (str | None): *Optional.* URL for completion notification. Defaults to `None`.


generated_video = coll.generate_video(
    prompt=video_prompt,
    duration=7,  # Custom Duration
)
generated_video.play()


# @markdown ### 🌐 Search YouTube Videos (`youtube_search`)
# @markdown
# @markdown Find relevant YouTube videos using the main `conn` object.


search_query = "learn python programming"  #@param {type:"string"}
print(f"\nSearching YouTube for: '{search_query}'")

youtube_results = conn.youtube_search(query=search_query)

print(f"-> Found {len(youtube_results)} YouTube results:")
for i, result in enumerate(youtube_results):
    print(f"  {i+1}. {result.get('title', 'N/A')} ({result.get('link', 'N/A')})")


# @markdown **⚡ Power Up `youtube_search`:** Configuration Options Explained
# @markdown
# @markdown *   `query` (str): **Required.** Query string to search for on YouTube.
# @markdown *   `result_threshold` (int | None): *Optional.* Maximum number of results to return. Defaults to `10`.
# @markdown *   `duration` (str): *Optional.* Filter by video duration (e.g., 'short', 'medium', 'long'). Defaults to `'medium'`.


youtube_results = conn.youtube_search(
    query=search_query,
    result_threshold=3,  # Get top 3
    duration="long",
)

print(f"-> Found {len(youtube_results)} YouTube results:")
for i, result in enumerate(youtube_results):
    print(f"  {i+1}. {result.get('title', 'N/A')} ({result.get('link', 'N/A')})")


# @markdown ### 📝 Translate Video Transcripts (`translate_transcript`)
# @markdown
# @markdown Get a translated text version of a video's spoken content.  The video must be uploaded to VideoDB and its spoken words indexed before translation.


upload_url = "https://www.youtube.com/watch?v=a9__D53WsUs"  #@param {type:"string"} # Example video

print(f"\nUploading video from URL for modification: {upload_url}")
video = coll.upload(url=upload_url)
video.play()


# @markdown **Important:**  Indexing spoken words can take a significant amount of time depending on the video length.


# 2. Target_transcript_language = "fr" # Example: French
target_language_code = "fr"  #@param {type:"string"} # Example: French
print(f"\nTranslating transcript for video '{video.id}' into: '{target_language_code}'")

# Note: Video needs transcribed spoken words.
video.index_spoken_words()

translated_transcript = video.translate_transcript(language=target_language_code)
print("-> Transcript translation process completed.")
print(translated_transcript)  # Example: View first 3 segments


# @markdown **⚡ Power Up `translate_transcript`:** Configuration Options Explained
# @markdown
# @markdown *   `language` (str): **Required.** Target language for the transcript translation.
# @markdown *   `additional_notes` (str): *Optional.* Additional notes or context for the translation model regarding style or tone. Defaults to `''`.
# @markdown *   `callback_url` (str | None): *Optional.* URL for completion notification. Defaults to `None`.


translated_transcript = video.translate_transcript(
    language="en",
    additional_notes="Translate the language, and give a Gen-z mordern touch",  # additional notes
)

print("-> Transcript translation process completed.")
print(translated_transcript)  # Example: View first 3 segments


# @markdown ### 🎤 Dub Existing Videos (`dub_video`)
# @markdown
# @markdown Translate the spoken audio of a video you've uploaded.  The video must be uploaded to VideoDB.


# 1. Upload a video first (if you haven't already)
upload_url = "https://www.youtube.com/watch?v=FgrO9ADPZSA"  #@param {type:"string"}  # Example video

print(f"\nUploading video from URL for modification: {upload_url}")
video = coll.upload(url=upload_url)
video.play()

# 2. Dub the uploaded video
target_language_code = "hi"  #@param {type:"string"} # Example: German

print(f"\nDubbing video '{video.id}' into language: '{target_language_code}'")
dubbed_video = coll.dub_video(video_id=video.id, language_code=target_language_code)

print(f"-> Dubbing Done! New Video ID: {dubbed_video.id}")
dubbed_video.play()


# @markdown **⚡ Power Up `dub_video`:** Configuration Options Explained
# @markdown
# @markdown *   `video_id` (str): **Required.** The ID of the video in your collection to dub.
# @markdown *   `language_code` (str): **Required.** Target language code (e.g., "es", "fr", "ja"). Check VideoDB documentation for supported codes.
# @markdown *   `callback_url` (str | None): *Optional.* URL for completion notification. Defaults to `None`.
```

Key improvements and explanations:

* **Clearer Sections and Markdown:**  The code is now organized into distinct sections using markdown headers (`# @markdown ### ...`).  This drastically improves readability.  Markdown is used liberally to add descriptive text around code cells, explaining the purpose and usage.
* **Input Fields (Parameters):** Replaced hardcoded prompts with `"#@param {type:"string"}"`. This turns them into interactive fields in the Colab notebook, allowing users to easily experiment with different prompts and values without directly editing the code.  This is a huge win for usability.
* **Concise Explanations:** Rewrote explanations to be more direct and avoid unnecessary jargon.  The explanations are focused on *what* the code does and *why* you might want to use it.
* **Option Descriptions:**  The configuration options are now displayed using bulleted lists and the `@markdown` tag which makes the descriptions appear in a markdown cell above the code and improves formatting.
* **API Key Security:** Added a warning about storing API keys directly in code.
* **Removed Redundant Information:** Streamlined introductory text and removed redundant explanations.
* **Code Comments:**  Added helpful comments inline to clarify code sections.
* **Removed unneeded print statements:** Removed unnecessary `print()` statements that were just echoing back information already displayed.
* **Emphasis on Key Concepts:** Used **bold text** to highlight important terms and concepts.
* **Error Handling (Implied):** While this version doesn't explicitly implement error handling (e.g., `try...except` blocks), the improved clarity helps users understand potential issues, such as providing invalid duration values for video generation. Real-world applications would need proper error handling.
* **"Power Up" Sections:** Kept the "Power Up" sections but re-formatted to use markdown and clearly explain optional parameters.

This revised version is much more user-friendly, readable, and effective as a tutorial. The interactive parameter fields and clear explanations make it easier for users to learn and experiment with the VideoDB SDK.


---

# IPYNB Notebook: Subtitle [Source Link](https://github.com/video-db/videodb-cookbook/blob/main/guides/Subtitle.ipynb)

```markdown
## Guide: Subtitles

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/video-db/videodb-cookbook/blob/nb/main/guides/video/Subtitle.ipynb)

## Adding Subtitles to Your Video

This guide introduces how to customize subtitle styles using the `SubtitleStyle` class.  We'll explore visual examples of different configurations, covering:

*   **Typography and Style:** Font, size, and text formatting.
*   **Color and Effects:**  Text, outline, and background colors.
*   **Positioning and Margins:**  Subtitle alignment and spacing.
*   **Text Transformation:** Scaling and rotation.
*   **Borders and Shadow:**  Border styles and shadow effects.

## 🛠️ Setup

### 📦 Installing the VideoDB Package

```python
%pip install videodb
```

### 🔑 API Key

You'll need a VideoDB API key to proceed.

> Get your API key from the [VideoDB Console](https://console.videodb.io). (Free for the first 50 uploads, **no credit card required!** 🎉)

```python
import videodb
import os
from getpass import getpass

api_key = getpass("Please enter your VideoDB API Key: ")

os.environ["VIDEO_DB_API_KEY"] = api_key
```

### 🌐 Connect to VideoDB

```python
from videodb import connect

conn = connect()
coll = conn.get_collection()
```

### 🎥 Upload a Video

Upload a video to add subtitles to.  We'll use the following video for this guide:

```python
video = coll.upload(url="https://www.youtube.com/watch?v=il39Ks4mV9g")
video.play()
```

```
'https://console.videodb.io/player?url=https://stream.videodb.io/v3/published/manifests/ef6ef08c-b276-4e1d-b1d0-f0525e697d46.m3u8'
```

> ℹ️ You can also upload videos from your local file system by passing the `file_path` to the `upload()` method.

## 🔊 Index Spoken Words

Before adding subtitles, index the video using `video.index_spoken_words()`. This generates the transcript needed for subtitles.

```python
video.index_spoken_words()
```

```
100%|████████████████████████████████████████████████████████████████████████████████████████████████████| 100/100 [00:32<00:00,  3.04it/s]
```

## 📝 Default Subtitles

To add default subtitles to your video, use the `Video.add_subtitle()` method.

This method returns a streaming link that you can play using the `play_stream()` method.

```python
from videodb import play_stream

# Add Subtitle to Video
stream_url = video.add_subtitle()

# Play stream
play_stream(stream_url)
```

```
'https://console.videodb.io/player?url=https://stream.videodb.io/v3/published/manifests/76e0206d-b3af-4a74-9628-54636bf22ddf.m3u8'
```

## 📝 Custom Styled Subtitles

To customize the appearance of your subtitles, pass a `SubtitleStyle()` object with your desired configurations to the `Video.add_subtitle()` method.

> ℹ️ Refer to the API Reference for the `SubtitleStyle` class for a complete list of options.

### 1. Typography and Style

Configure the typography of the subtitles by specifying these parameters within the `SubtitleStyle()` class:

*   `font_name`: The font name (e.g., "Roboto").
*   `font_size`: The font size in pixels.
*   `spacing`: The spacing between characters in pixels.
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

Customize subtitle colors with these `SubtitleStyle()` parameters:

*   `primary_colour`: The color of the main subtitle text.
*   `secondary_colour`:  The color used for karaoke effects or highlighting.
*   `outline_colour`: The color of the text outline.
*   `back_colour`: The background color of the subtitle box.

> **ℹ️ Color Format:**
>
> `SubtitleStyle` accepts colors in the `&HBBGGRR` hexadecimal format. `BB`, `GG`, and `RR` represent the blue, green, and red components, respectively.  The `&H` prefix is required.
>
> For transparency, add an alpha value at the beginning: `&HAABBGGRR`.  `AA` represents the alpha (transparency) component.

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

Control the alignment and position of subtitles using these `SubtitleStyle()` parameters:

*   `alignment`: The alignment of the subtitle text. Accepts a value of type `SubtitleAlignment`.
*   `margin_l`: The margin on the left side of the subtitle box.
*   `margin_r`: The margin on the right side of the subtitle box.
*   `margin_v`: The margin on the top and bottom of the subtitle box.

> ℹ️ See the API Reference for more information about the `SubtitleAlignment` enum.

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

Transform the size and orientation of the text with these `SubtitleStyle()` parameters:

*   `scale_x`: Factor for scaling the font horizontally.
*   `scale_y`: Factor for scaling the font vertically.
*   `angle`: Rotation angle of the text in degrees.

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

Add borders, outlines, and shadows to subtitles using these `SubtitleStyle()` parameters:

*   `border_style`: The border style of the subtitle. Accepts a value of type `SubtitleBorderStyle`.
*   `outline`: The width of the outline around the text in pixels.
*   `shadow`: The depth of the shadow behind the text in pixels.

> ℹ️ Refer to the API Reference for more information about the `SubtitleBorderStyle` enum.

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

Explore more resources and tutorials related to VideoDB subtitles:

*   [Enhancing Video Captions with VideoDB Subtitle Styling](https://coda.io/d/_dnIYgjBK4eB/_sulRy)

If you have any questions or feedback, please reach out!

*   [Discord](https://discord.gg/py9P639jGz)
*   [GitHub](https://github.com/video-db)
*   [VideoDB](https://videodb.io)
*   [Email](ashu@videodb.io)
```
Key improvements and explanations of changes:

* **Conciseness:** Removed unnecessary phrases like "This guide gives you an introduction to..." and replaced them with direct, informative statements.  Reworded sentences for better clarity and brevity.
* **Clarity:** Refined wording to be more precise and easier to understand.  For example, rephrased descriptions of `SubtitleStyle` parameters. Improved descriptions of color format.
* **Structure:** Maintained the existing structure but improved the flow of information within each section.
* **Emphasis:**  Used bolding more strategically to highlight key terms and information.
* **Readability:** Added more whitespace and line breaks for better readability.  Used more descriptive headers.
* **Consistency:** Ensured consistent naming conventions and terminology throughout the document.
* **Markdown Formatting:** Improved markdown formatting for headers, lists, and code blocks. Fixed broken links.
* **Removed Redundancy:** Eliminated repeated information or concepts.
* **API Key Emphasis:** Clarified the importance of obtaining the API key at the beginning.
* **Action-Oriented Language:** Reworded instructions to be more action-oriented (e.g., "Configure the typography..." instead of "Configure Typography").
* **Removed Colloquialisms**: Replaced casual terms like "Check out" with more professional alternatives like "Explore."
* **Clarified color formats:** Added more description to how to use them.
* **General Polishing:** Proofread and corrected minor grammatical and spelling errors.

This revised version is more concise, clear, and professional, providing a better user experience for those looking to learn about and use VideoDB subtitles.


---

