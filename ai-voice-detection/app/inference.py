from app.audio_utils import decode_audio
from app.features import extract_features
from app.explain import generate_explanation

def predict_voice(data):
    audio, sr = decode_audio(data.audioBase64)
    features = extract_features(audio, sr)

    pitch_std = features["pitch_std"]
    energy_std = features["energy_std"]
    mfcc_std = features["mfcc_std"]

    # ---------- AI SCORE (0 to 1) ----------
    ai_score = 0.0

    # tighter rules (IMPORTANT)
    if pitch_std < 5:
        ai_score += 0.4
    if energy_std < 0.008:
        ai_score += 0.3
    if mfcc_std < 18:
        ai_score += 0.3

    # clamp
    ai_score = max(0.0, min(ai_score, 1.0))

    # ---------- FINAL DECISION ----------
    if ai_score >= 0.6:
        classification = "AI_GENERATED"
        confidence = ai_score
    else:
        classification = "HUMAN"
        confidence = 1.0 - ai_score

    return {
        "status": "success",
        "language": data.language,
        "classification": classification,
        "confidenceScore": round(confidence, 2),
        "explanation": generate_explanation(features, classification)
    }
