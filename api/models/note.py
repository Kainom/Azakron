from pydantic import BaseModel, Field
from typing import List
from .tag import Tag

class Note(BaseModel):
    title: str = Field(..., example="Make a project")
    notes: str = Field(..., example="You must make a project using FastAPI and MongoDB, it's important")
    tags: List[Tag] = Field(default_factory=list)
