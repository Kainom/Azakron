from pydantic import BaseModel, Field
from typing import  Optional


class Tag(BaseModel):
    name: str = Field(..., example="College")
    description: Optional[str] = Field(None, example="Tasks related to college")