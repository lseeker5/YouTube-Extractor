import functions_framework
from flask import Request, Response, jsonify
from pytube import YouTube
import os
from google.cloud import storage
from urllib.parse import quote

@functions_framework.http
def download_audio(request: Request) -> Response:
    """HTTP Cloud Function to download audio from a YouTube video URL."""
    request_json = request.get_json(silent=True)
    video_url = request_json.get('video_url')

    if not video_url:
        return {'error': 'No video URL provided'}, 400

    try:
        yt = YouTube(video_url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_file_path = audio_stream.download()  # Downloads to the current directory
        
        # Get video title and use it as the filename
        video_title = yt.title
        file_extension = os.path.splitext(audio_file_path)[1]  # Get the file extension
        audio_filename = f"{video_title}{file_extension}"

        # Upload audio file to Google Cloud Storage
        client = storage.Client()
        bucket = client.bucket('audio_extracted_5')
        blob = bucket.blob(audio_filename)
        with open(audio_file_path, "rb") as file:
            blob.upload_from_file(file)


        # Generate permanent download link
        download_link = f"https://storage.googleapis.com/audio_extracted_5/{quote(audio_filename)}"


        return {'download_link': download_link, 'error': "NA"}, 200
    except Exception as e:
        return {'download_link': "NA", 'error': str(e)}, 500




