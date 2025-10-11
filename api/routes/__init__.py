
from fastapi import APIRouter
from .notes import router as note_router

router = APIRouter()
router.include_router(note_router)




