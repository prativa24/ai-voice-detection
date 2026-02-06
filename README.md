# AI-Generated Voice Detection API

A REST API that detects whether a given voice sample is **AI-generated** or **Human**.  
Built for hackathon evaluation with strict compliance to the provided problem statement.

---

## 🔗 Live Links

- **Deployed API Endpoint**  
  https://ai-voice-detection-1-9ztu.onrender.com/api/voice-detection

- **Swagger UI (API Documentation & Testing)**  
  https://ai-voice-detection-1-9ztu.onrender.com/docs

---

## ✨ Features

- Detects **AI_GENERATED** vs **HUMAN** voice
- Accepts **Base64-encoded MP3 audio**
- Supports **Tamil, English, Hindi, Malayalam, Telugu**
- Secured using **API Key authentication**
- Returns classification, confidence score, and explanation
- Built using **FastAPI (Python)**

---

## 🛠 Tech Stack

- **Backend:** FastAPI (Python)
- **Audio Processing:** Librosa, NumPy
- **Detection Logic:** Audio signal analysis  
  (energy variation, zero-crossing rate, spectral consistency)
- **Deployment:** Render (Free Tier)

---



