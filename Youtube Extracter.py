
import requests
from pytube import YouTube

def download_audio_from_youtube(video_url):
    try:
        yt = YouTube(video_url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_stream.download('/Internal storage/Download') 
        return "Download complete"
    except Exception as e:
        return f"Error: {str(e)}"
    


