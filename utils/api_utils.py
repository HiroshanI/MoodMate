import requests

# Base URL of the Flask API
API_BASE_URL = "http://localhost:5000"  # Update if deployed

def get_recommendation(emotion):
    payload = {'emotion': emotion}
    response = requests.post(f"{API_BASE_URL}/recommend", data=payload)
    return response.json()

def upload_audio_file(audio_file):
    files = {'audio_file': audio_file}
    response = requests.post(f"{API_BASE_URL}/audio_classification", files=files)
    return response.json()

def upload_video_file(video_file):
    files = {'file': video_file}
    response = requests.post(f"{API_BASE_URL}/upload_video", files=files)
    return response.json()

def get_image_classification():
    response = requests.get(f"{API_BASE_URL}/image_classification")
    return response.json()

def text_classification(input_text, model, lang):
    payload = {'input_text': input_text, 'model_select': f"{model}_{lang}"}
    response = requests.post(f"{API_BASE_URL}/text_classification", data=payload)
    return response.json()
