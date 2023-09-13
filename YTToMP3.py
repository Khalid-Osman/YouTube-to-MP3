from pytube import YouTube 
import os

url = 'https://www.youtube.com/watch?v=MjEYCUJuh-g'
video = YouTube(url)

print('title', video.title)
print('Downloading right now...')

# Get it into audio format and download it
audio_stream = video.streams.filter(only_audio=True).first()
out_path = audio_stream.download()

# Rename it and adding dot MP3 extension
root, extension = os.path.splitext(out_path)
new_path = root + '.mp3'
os.rename(out_path, new_path)

# heeky print out 
print('Its done...')
