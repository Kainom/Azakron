from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


load_dotenv()

MONGO_DETAILS = os.getenv("MONGO_DETAILS")
logger.info(f"Connecting to MongoDB at {MONGO_DETAILS}")


client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.azakron


collection_notes = database.notes
collection_tags = database.tags
collection_tasks = database.tasks

