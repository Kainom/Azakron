from api.config import get_collection_tags
from bson.objectid import ObjectId

async def create_tag(tag_data: dict) -> str:
    collection = get_collection_tags()
    result = await collection.insert_one(tag_data)
    return str(result.inserted_id)

async def get_tag(tag_id: str, user_id: str) -> dict:
    collection = get_collection_tags()
    tag = await collection.find_one({"_id": ObjectId(tag_id), "user_id": user_id})
    if tag:
        tag["id"] = str(tag["_id"])
        del tag["_id"]
    return tag

async def get_tags(user_id: str = None) -> list:
    collection = get_collection_tags()
    query = {}
    if user_id:
        query["user_id"] = user_id
    tags = await collection.find(query).to_list(100)
    for tag in tags:
        tag["id"] = str(tag["_id"])
        del tag["_id"]
    return tags

async def update_tag(tag_id: str, user_id: str, tag_data: dict) -> bool:
    collection = get_collection_tags()
    result = await collection.update_one(
        {"_id": ObjectId(tag_id), "user_id": user_id},
        {"$set": tag_data}
    )
    return result.modified_count > 0

async def delete_tag(tag_id: str, user_id: str) -> bool:
    collection = get_collection_tags()
    result = await collection.delete_one({"_id": ObjectId(tag_id), "user_id": user_id})
    return result.deleted_count > 0