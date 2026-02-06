# AI-Generated Voice Detection API

A REST API that detects whether a given voice sample is **AI-generated** or **Human**.  
Built for hackathon evaluation with strict compliance to the provided problem statement.

---

## Live API

**Endpoint:**  
https://ai-voice-detection-1-9ztu.onrender.com/api/voice-detection

**Swagger UI:**  
https://ai-voice-detection-1-9ztu.onrender.com/docs

---

## API Credentials

- **API ID / API Key:** sk_voice_ai_ABC123XYZ
> This API key must be passed in request headers for authentication.

---

## Features

- Detects **AI_GENERATED** vs **HUMAN** voice
- Accepts **Base64-encoded MP3 audio**
- Supports **Tamil, English, Hindi, Malayalam, Telugu**
- Secured using **API Key authentication**
- Returns classification, confidence score, and explanation
- Built using **FastAPI (Python)**

---

## Tech Stack

- **Backend:** FastAPI (Python)
- **Audio Processing:** Librosa, NumPy
- **Detection Logic:** Audio signal analysis  
(energy variation, zero-crossing rate, spectral consistency)
- **Deployment:** Render (Free Tier)

---

## API Usage

### Endpoint

### Headers
```http
Content-Type: application/json
x-api-key: sk_voice_ai_ABC123XYZ
{
  "language": "Hindi",
  "audioFormat": "mp3",
  "audioBase64": "<BASE64_ENCODED_MP3_STRING>"
}

{
  "status": "success",
  "language": "Hindi",
  "classification": "HUMAN",
  "confidenceScore": 0.87,
  "explanation": "Natural energy fluctuation and irregular spectral patterns indicate human speech"
}