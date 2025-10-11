from api.config import collection_notes
from bson.objectid import ObjectId

async def create_note(note_data: dict) -> str:
  result = await collection_notes.insert_one(note_data)
  return str(result.inserted_id)

async def get_note(note_id: str) -> dict:
  note = await collection_notes.find_one({"_id": ObjectId(note_id)})
  if note:
    note["id"] = str(note["_id"])
    del note["_id"]
  return note

async def get_notes() -> list:
  notes = await collection_notes.find().to_list(100)
  for note in notes:
      note["id"] = str(note["_id"])
  return notes


async def update_note(note_id: str, note_data: dict) -> bool:
    result = await collection_notes.update_one(
        {"_id": ObjectId(note_id)},
        {"$set": note_data}
    )
    return result.modified_count > 0