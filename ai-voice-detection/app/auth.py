from fastapi import HTTPException

SECRET_API_KEY = "sk_voice_ai_ABC123XYZ"

def verify_api_key(key: str):
    if key != SECRET_API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid API Key"
        )
