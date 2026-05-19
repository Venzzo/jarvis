import requests
import playsound
import os
import time

from config.settings import API_KEY, VOICE_ID

def falar_eleven(texto):

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    data = {
        "text": texto,
        "model_id": "eleven_multilingual_v2"
    }

    response = requests.post(url, json=data, headers=headers)

    audio_file = "response.mp3"

    # remove antigo
    if os.path.exists(audio_file):
        try:
            os.remove(audio_file)
        except:
            pass

    with open(audio_file, "wb") as f:
        f.write(response.content)

    playsound.playsound(audio_file)

    time.sleep(0.2)