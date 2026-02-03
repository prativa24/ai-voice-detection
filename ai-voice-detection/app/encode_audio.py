import base64

# MP3 file ka path
audio_file_path = "D:\\ai-voice-detection\\app\\human model.mp3"

# MP3 ko read karo
with open(audio_file_path, "rb") as f:
    audio_bytes = f.read()


audio_base64 = base64.b64encode(audio_bytes).decode("utf-8")

# Output print karo
print(audio_base64)
