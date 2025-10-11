from pydantic import BaseModel, Field


class Note(BaseModel):
    title: str = Field(..., example="Task X")
    notes: str = Field(..., example="This is task X")
    tag: str = Field(..., example="work")