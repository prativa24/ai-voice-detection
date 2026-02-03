import base64
import librosa
import tempfile
import os

def decode_audio(base64_audio: str):
    audio_bytes = base64.b64decode(base64_audio)

    # temporary mp3 file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tmp.write(audio_bytes)
        tmp_path = tmp.name

    try:
        audio, sr = librosa.load(tmp_path, sr=16000, mono=True)
    finally:
        os.remove(tmp_path)  # cleanup

    return audio, sr
