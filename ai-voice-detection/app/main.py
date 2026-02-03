from fastapi import FastAPI, Header
from app.schemas import VoiceRequest, VoiceResponse
from app.auth import verify_api_key
from app.inference import predict_voice

app = FastAPI()

@app.post("/api/voice-detection", response_model=VoiceResponse)
def voice_detection(
    data: VoiceRequest,
    x_api_key: str = Header(None)
):
    verify_api_key(x_api_key)
    return predict_voice(data)
