from fastapi import APIRouter, HTTPException
from api.models import Tag
from api.schemas.dao_tags   import create_tag,get_tag,get_tags,update_tag,delete_tag


router = APIRouter()


@router.post("/tags", response_model=str)
async def create_tag_route(tag: Tag):
    return await create_tag(tag.model_dump())

@router.get("/tags/{tag_id}", response_model=Tag)
async def get_tag_route(tag_id: str,user_id: str):
    tag = await get_tag(tag_id,user_id)
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    return tag

@router.get("/tags", response_model=list[Tag])
async def get_tags_route(user_id: str = None):
    return await get_tags(user_id=user_id)

@router.put("/tags/{tag_id}", response_model=bool)
async def update_tag_route(tag_id: str, tag: Tag):
    return await update_tag(tag_id, tag.model_dump())

@router.delete("/tags/{tag_id}", response_model=bool)
async def delete_tag_route(tag_id: str,user_id: str):
    return await delete_tag(tag_id,user_id=user_id)


