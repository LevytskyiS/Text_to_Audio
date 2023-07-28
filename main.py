import json
import time

import requests

from conf.config import settings


def text_to_speech(text="Hi"):
    headers = {"Authorization": f"Bearer {settings.API_KEY}"}
    url = "https://api.edenai.run/v2/audio/text_to_speech"
    payload = {
        "providers": "google",
        "language": "en-US",
        "option": "FEMALE",
        "text": text,
    }

    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    unx_time = time.time()

    with open(f"{unx_time}_chlor.json", "w", encoding="utf-8") as file:
        json.dump(result, file, indent=4, ensure_ascii=False)

    audio_url = result.get("google").get("audio_resource_url")
    r = requests.get(audio_url)

    with open(f"{unx_time}.wav", "wb") as file:
        file.write(r.content)

    print("Done!")


def main():
    with open("text.txt", "r") as file:
        text = file.read()
    text_to_speech(text)


if __name__ == "__main__":
    main()
