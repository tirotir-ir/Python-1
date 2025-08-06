#pip install moviepy

from moviepy.editor import VideoFileClip

# Path to your MP4 file
video_path = r'E:\PYTHON\Term1\pythonWeeks1\week1\video\moon.mp4'

# Load and play the video
clip = VideoFileClip(video_path)
clip.preview()
