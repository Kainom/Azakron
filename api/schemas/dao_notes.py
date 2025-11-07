from api.config import collection_notes
from bson.objectid import ObjectId

async def create_note(note_data: dict) -> str:
  result = await collection_notes.insert_one(note_data)
  return str(result.inserted_id)

async def get_note(note_id: str,user_id: str) -> dict:
  note = await collection_notes.find_one({"_id": ObjectId(note_id),"user_id":user_id})
  if note:
    note["id"] = str(note["_id"])
    del note["_id"]
  return note

async def get_notes(user_id: str = None) -> list:
  query = {}
  if user_id:
      query["user_id"] = user_id
  notes = await collection_notes.find(query).to_list(100)
  for note in notes:
      note["id"] = str(note["_id"])
  return notes


async def update_note(note_id: str, note_data: dict) -> bool:
    result = await collection_notes.update_one(
        {"_id": ObjectId(note_id)},
        {"$set": note_data}
    )
    return result.modified_count > 0


async def get_notes_paginated(skip: int = 0, limit: int = 10,user_id: str = None) -> list:
    query = {}
    if user_id:
        query["user_id"] = user_id
    notes = await collection_notes.find(query).skip(skip).limit(limit).to_list(limit)
    for note in notes:
        note["id"] = str(note["_id"])
    return notes

async def delete_note(note_id: str,user_id: str) -> bool:
    result = await collection_notes.delete_one({"_id": ObjectId(note_id),"user_id":user_id})
    return result.deleted_count > 0

async def update_note(note_id: str, user_id: str, note_data: dict) -> bool:
    result = await collection_notes.update_one(
        {"_id": ObjectId(note_id), "user_id": user_id},
        {"$set": note_data}
    )
    return result.modified_count > 0