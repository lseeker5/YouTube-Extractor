
import requests
from pytube import YouTube

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        req_body = req.get_json()
        video_url = req_body['video_url']
        
        yt = YouTube(video_url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_stream.download('/Internal storage/Download') 
        
        return func.HttpResponse("Download complete", status_code=200)
    except Exception as e:
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
    

    
