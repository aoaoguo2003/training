from pydantic import BaseModel, Field

class UserRequest(BaseModel):
    request_id: str = Field(min_length = 1)
    message: str = Field(min_length = 1, max_length = 1000)

