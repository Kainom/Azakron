from api.config import collection_tags
from bson.objectid import ObjectId

async def create_tag(tag_data: dict) -> str:
    result = await collection_tags.insert_one(tag_data)
    return str(result.inserted_id)

async def get_tag(tag_id: str) -> dict:
    tag = await collection_tags.find_one({"_id": ObjectId(tag_id)})
    if tag:
        tag["id"] = str(tag["_id"])
        del tag["_id"]
    return tag

async def get_tags() -> list:
    tags = await collection_tags.find().to_list(100)
    for tag in tags:
        tag["id"] = str(tag["_id"])
    return tags

async def update_tag(tag_id: str, tag_data: dict) -> bool:
    result = await collection_tags.update_one(
        {"_id": ObjectId(tag_id)},
        {"$set": tag_data}
    )
    return result.modified_count > 0
