# AI-Generated Voice Detection API

A REST API that detects whether a given voice sample is **AI-generated** or **Human**.  
Built for hackathon evaluation with strict compliance to the provided problem statement.

---

## Features

- Detects **AI_GENERATED** vs **HUMAN** voice
- Accepts **Base64-encoded MP3 audio**
- Supports **Tamil, English, Hindi, Malayalam, Telugu**
- Secured using **API Key authentication**
- Returns **classification, confidence score, and explanation**
- Built using **FastAPI (Python)**

---

## Tech Stack

- Backend: FastAPI
- Audio Processing: Librosa, NumPy
- Detection Logic: Audio signal analysis (pitch, energy, spectral stability)
- Deployment: Render (Free Tier)

---

