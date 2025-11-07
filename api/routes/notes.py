from fastapi import APIRouter, HTTPException
from api.models import Note
from api.schemas.dao_notes import create_note,get_note,get_notes,get_notes_paginated
from api.schemas.dao_notes import update_note,delete_note

router = APIRouter()

@router.post("/notes", response_model=str)
async def create_note_route(note: Note):
    return await create_note(note.model_dump())

@router.get("/note/{note_id}/{user_id}", response_model=Note)
async def get_note_route(note_id: str,user_id: str):
    note = await get_note(note_id,user_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@router.get("/notes/{user_id}", response_model=list[Note])
async def get_notes_route(user_id: str):
    return await get_notes(user_id=user_id)

@router.get("/notes/paginated", response_model=list[Note])
async def get_notes_paginated_route(skip: int = 0, limit: int = 10,user_id: str = None):
    return await get_notes_paginated(skip, limit,user_id)

@router.get("/notes/search/{user_id}", response_model=list[Note])
async def search_notes_route(user_id: str, query: str):
    notes = await get_notes(user_id=user_id)
    return [
        note
        for note in notes
        if query.lower() in note['title'].lower()
        or query.lower() in note['description'].lower()
    ]

@router.put("/notes/{note_id}/{user_id}", response_model=bool)
async def update_note_route(note_id: str, user_id: str, note: Note):
    return await update_note(note_id, user_id, note.model_dump())

@router.delete("/notes/{note_id}/{user_id}", response_model=bool)
async def delete_note_route(note_id: str, user_id: str):
    return await delete_note(note_id, user_id=user_id)  