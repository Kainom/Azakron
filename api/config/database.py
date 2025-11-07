from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os
import logging
import asyncio


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


load_dotenv()

MONGO_DETAILS = os.getenv("MONGO_DETAILS")
logger.info(f"Connecting to MongoDB at {MONGO_DETAILS}")


try:
    client = AsyncIOMotorClient(MONGO_DETAILS)
    database = client.azakron
    collection_notes = database.notes
    collection_tags = database.tags
    collection_tasks = database.tasks

    async def test_connection():
        await client.admin.command('ping')
        logger.info("✅ Conectado com sucesso ao MongoDB")

    asyncio.get_event_loop().run_until_complete(test_connection())

except Exception as e:
    logger.exception(f"❌ Erro ao conectar no MongoDB: {e}")