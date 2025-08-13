import io
import time
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import edge_tts
import asyncio

app = FastAPI(title="Edge-TTS Service")

class TTSRequest(BaseModel):
    text: str
    language_code: str = "en-US"  # example: en-US, ta-IN, fr-FR
    voice: str = "en-US-AriaNeural"  # default voice

async def synthesize_tts(text: str, voice: str):
    # Create a stream in memory
    stream = io.BytesIO()
    communicate = edge_tts.Communicate(text, voice)
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            stream.write(chunk["data"])
    stream.seek(0)
    return stream

@app.post("/synthesize")
async def synthesize(req: TTSRequest):
    if not req.text.strip():
        raise HTTPException(status_code=400, detail="Text is required")

    try:
        audio_bytes = await synthesize_tts(req.text, req.voice)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"TTS synthesis error: {e}")

    filename = f"tts_{int(time.time())}.mp3"
    return StreamingResponse(audio_bytes, media_type="audio/mpeg",
                             headers={"Content-Disposition": f"attachment; filename={filename}"})
