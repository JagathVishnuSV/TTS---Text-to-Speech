# voices.py
from google.cloud import texttospeech
from fastapi import APIRouter

router = APIRouter()
client = texttospeech.TextToSpeechClient()

@router.get("/voices")
def list_voices():
    resp = client.list_voices()
    # build a condensed mapping: language_code -> [voice names ...]
    mapping = {}
    for v in resp.voices:
        for lang in v.language_codes:
            mapping.setdefault(lang, []).append({
                "name": v.name,
                "ssml_gender": texttospeech.SsmlVoiceGender(v.ssml_gender).name,
                "natural_sample_rate_hertz": v.natural_sample_rate_hertz
            })
    return mapping
