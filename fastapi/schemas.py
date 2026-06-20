
from pydantic import BaseModel, Field, field_validator
from typing import Literal

class AgentRequest(BaseModel):
    request_id: str = Field(min_length=1)
    user_id: str = Field(min_length=1)
    prompt: str = Field(min_length=1, max_length=1000)
    tool_name: Literal['search', 'calculator', 'weather' ]
    top_k: int = Field(default=5, ge=1, le=20)
    user_preference: str | None = None

    @field_validator("prompt")
    @classmethod
    def validate_prompt(cls, value: str):
        if not value.strip():
            raise ValueError("prompt cannot be empty")
        
        return value.strip()