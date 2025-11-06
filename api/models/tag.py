from pydantic import BaseModel, Field
from typing import  Optional


class Tag(BaseModel):
    id: Optional[str] = Field(None, example="64b8f0c2e1d3f5a6b7c8d9e0")
    name: str = Field(..., example="College")
    token_user: str = Field(..., example="user_token_12345")