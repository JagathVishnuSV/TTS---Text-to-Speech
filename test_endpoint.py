#!/usr/bin/env python3
"""
Test script for the FastAPI Edge-TTS endpoint
Saves all audio files in Downloads
"""
import requests
import os

def test_synthesize_endpoint():
    """Test the /synthesize endpoint with various configurations"""

    # Adjust this URL if your FastAPI runs on a different host/port
    base_url = "http://localhost:8000"
    endpoint = f"{base_url}/synthesize"

    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

    test_cases = [
        {
            "name": "Basic English",
            "payload": {
                "text": "Hello, this is a test of the TTS service.",
                "voice": "en-US-AriaNeural",
                "audio_format": "mp3"
            }
        },
        {
            "name": "Spanish",
            "payload": {
                "text": "Hola, esto es una prueba del servicio TTS.",
                "voice": "es-ES-ElviraNeural",
                "audio_format": "mp3"
            }
        },
        {
            "name": "SSML Example",
            "payload": {
                "ssml": "<speak><emphasis level='moderate'>Hello</emphasis> world!</speak>",
                "voice": "en-US-AriaNeural",
                "audio_format": "mp3"
            }
        },
        {
            "name": "Tamil",
            "payload": {
                "text": "வணக்கம், இது ஒரு சோதனை ஆகும்.",
                "voice": "ta-IN-PallaviNeural",
                "audio_format": "mp3"
            }
        }
    ]

    print("Testing TTS Synthesize Endpoint...")
    print("=" * 50)

    for test_case in test_cases:
        print(f"\nTest: {test_case['name']}")
        print("-" * 30)

        try:
            response = requests.post(endpoint, json=test_case['payload'])
            print(f"Status: {response.status_code}")

            if response.status_code == 200:
                print("✅ Success!")
                # Save the audio file in Downloads
                filename = os.path.join(
                    downloads_folder,
                    f"test_{test_case['name'].lower().replace(' ', '_')}.mp3"
                )
                with open(filename, 'wb') as f:
                    f.write(response.content)
                print(f"Audio saved as: {filename}")
            else:
                print(f"❌ Error: {response.text}")

        except requests.exceptions.ConnectionError:
            print("❌ Connection error - Is the server running?")
        except Exception as e:
            print(f"❌ Exception: {e}")

if __name__ == "__main__":
    test_synthesize_endpoint()
