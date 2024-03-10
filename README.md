# AI-Generated-Shorts

## This is gonna be epic

# Automated Story-to-YouTube Project

This project aims to automate the process of generating stories, creating videos from them, and uploading them to YouTube.

## Project Overview

The project consists of several steps, each handled by separate programs or scripts:
1. **Story Generation:** Using a Python script (`generate_story.py`), stories are generated and saved as text files in the `generated_stories` folder.
2. **Text-to-Voiceover:** Another Python script (`text_to_voiceover.py`) converts the generated stories into voiceovers, saving them as MP3 files in the `voiceovers` folder.
3. **Video Overlay:** A Python script (`overlay_text_on_video.py`) overlays text on a video, creating videos with text overlays. The videos are saved in the `videos_with_overlay` folder.
4. **Audio-Video Alignment:** Using `align_audio_video.py`, the voiceovers are aligned with the videos to ensure synchronization. The aligned videos are saved in the `aligned_videos` folder.
5. **Export Video:** Final videos are exported using `export_video.py` and saved in the `exported_videos` folder.
6. **Human Review:** The exported videos are placed in the `review_videos` folder for human review before uploading to YouTube.
7. **YouTube Upload:** Finally, a Python script (`upload_to_youtube.py`) uploads the approved videos from the `videos_to_upload` folder to YouTube.
## Folder Structure
