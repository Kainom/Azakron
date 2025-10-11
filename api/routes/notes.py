from fastapi import APIRouter, HTTPException
from api.models import Note
from api.schemas.dao_notes import create_note,get_note,get_notes
router = APIRouter()

@router.post("/notes", response_model=str)
async def create_note_route(note: Note):
    return await create_note(note.model_dump())

@router.get("/notes/{note_id}", response_model=Note)
async def get_note_route(note_id: str):
    note = await get_note(note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.get("/notes", response_model=list[Note])
async def get_notes_route():
    return await get_notes()