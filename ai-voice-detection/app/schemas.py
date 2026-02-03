from pydantic import BaseModel, Field

class VoiceRequest(BaseModel):
    language: str = Field(
        ...,
        pattern="^(Tamil|English|Hindi|Malayalam|Telugu)$"
    )
    audioFormat: str = Field(
        ...,
        pattern="^mp3$"
    )
    audioBase64: str


class VoiceResponse(BaseModel):
    status: str
    language: str
    classification: str
    confidenceScore: float
    explanation: str
