import os
import tempfile
from gtts import gTTS
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
from PIL import Image

def generate_video_with_ffmpeg(text, image_path, output_path="output.mp4"):
    # Step 1: Convert text to speech
    tts = gTTS(text=text, lang='en')
    temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_audio.name)

    # Step 2: Create video from image
    image = Image.open(image_path)
    image_clip = ImageClip(image_path).set_duration(AudioFileClip(temp_audio.name).duration)
    image_clip = image_clip.set_audio(AudioFileClip(temp_audio.name))

    # Step 3: Export final video
    image_clip.write_videofile(output_path, fps=24)

    # Cleanup
    temp_audio.close()
    os.remove(temp_audio.name)
    return output_path
