from pydantic import BaseModel, Field
from typing import List
from .tag import Tag
from typing import  Optional
class Note(BaseModel):
    id: Optional[str] = Field(None, example="64b8f0c2e1d3f5a6b7c8d9e0")
    title: str = Field(..., example="Make a project")
    notes: str = Field(..., example="You must make a project using FastAPI and MongoDB, it's important")
    token_user: str = Field(..., example="user_token_12345")
    tags: List[Tag] = Field(default_factory=list)
