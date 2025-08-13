````markdown
# Edge-TTS FastAPI Service

A lightweight **Text-to-Speech API** using **Microsoft Edge Neural voices** via Python. Fully local, free, and supports multiple languages including Tamil, Spanish, English, and more.

---

## Features
* Multi-language TTS (English, Spanish, Tamil, etc.)
* SSML support (emphasis, pitch, speed, etc.)
* Outputs MP3 audio
* Fully local — no billing required
* Simple FastAPI endpoint for easy integration

---

## Requirements
* Python 3.9+
* Windows/Linux/macOS
* FastAPI & Uvicorn
* Edge-TTS Python package

---

## Installation

1. Clone the repository or copy files to your project folder.
```bash
git clone <repo_url>
cd <repo_folder>
````

2. Install dependencies:

```bash
pip install fastapi uvicorn requests edge-tts
```

---

## Running the Server

```bash
uvicorn app:app --host 0.0.0.0 --port 8080
```

The TTS server will start at:

```
http://localhost:8080
```

---

## API Endpoint

### `/synthesize` (POST)

**Request JSON:**

```json
{
  "text": "Hello world",
  "ssml": "...",
  "voice": "en-US-AriaNeural",
  "audio_format": "mp3"
}
```

* `text`: Plain text to convert to speech (optional if using `ssml`).
* `ssml`: SSML formatted text for advanced control (optional).
* `voice`: Neural voice name (required).
* `audio_format`: `"mp3"` (default).

**Response:**

* Returns the audio file as a downloadable stream (`audio/mpeg`).

---

## Testing

A test script `test_endpoint.py` is included. It runs several test cases and saves audio files to the **Downloads** folder.

Run:

```bash
python test_endpoint.py
```

Expected output:

```
Audio saved as: C:\Users\<username>\Downloads\test_basic_english.mp3
Audio saved as: C:\Users\<username>\Downloads\test_spanish.mp3
Audio saved as: C:\Users\<username>\Downloads\test_ssml_example.mp3
Audio saved as: C:\Users\<username>\Downloads\test_tamil.mp3
```

---

## Supported Voices

| Language | Voice Example       |
| -------- | ------------------- |
| English  | en-US-AriaNeural    |
| Spanish  | es-ES-ElviraNeural  |
| Tamil    | ta-IN-PallaviNeural |
| Hindi    | hi-IN-SwaraNeural   |
| French   | fr-FR-DeniseNeural  |

You can find all supported voices [here](https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support#text-to-speech).

---

## Notes

* Make sure the server is running before testing.
* All MP3 files will be saved to the user's **Downloads** folder.
* Supports offline operation as long as the machine has internet to access Edge TTS (no billing).


