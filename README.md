Built on the Google Cloud Platform, this cloud function is designed to accept a URL as input. Utilizing the Pytube library, it extracts the audio from the provided video, uploads it to a public cloud bucket, and then returns the public URL to the user. Clicking on the URL allows the user to download the audio