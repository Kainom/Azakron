from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

MONGO_DETAILS = os.getenv("MONGO_DETAILS")

if not MONGO_DETAILS:
    logger.error("❌ MONGO_DETAILS não encontrado")
    raise ValueError("MONGO_DETAILS is required")

logger.info(f"Connecting to MongoDB")

# Configuração otimizada para serverless
client = AsyncIOMotorClient(
    MONGO_DETAILS,
    maxPoolSize=1,  # Importante para serverless
    minPoolSize=0,
    serverSelectionTimeoutMS=5000,
    connectTimeoutMS=5000,
    socketTimeoutMS=5000
)

database = client.azakron
collection_notes = database.notes
collection_tags = database.tags
collection_tasks = database.tasks

logger.info("✅ Cliente MongoDB configurado")