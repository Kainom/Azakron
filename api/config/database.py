from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

MONGO_DETAILS = os.getenv("MONGO_DETAILS")

if not MONGO_DETAILS:
    logger.error("❌ MONGO_DETAILS não encontrado nas variáveis de ambiente")
    raise ValueError("MONGO_DETAILS is required")

logger.info(f"Connecting to MongoDB at {MONGO_DETAILS}")

try:
    # Remove o asyncio.get_event_loop() - deixa o FastAPI gerenciar
    client = AsyncIOMotorClient(MONGO_DETAILS)
    database = client.azakron
    collection_notes = database.notes
    collection_tags = database.tags
    collection_tasks = database.tasks
    
    logger.info("✅ Cliente MongoDB configurado")
    
except Exception as e:
    logger.exception(f"❌ Erro ao configurar MongoDB: {e}")
    raise