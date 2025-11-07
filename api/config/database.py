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

def get_database():
    """Cria uma nova conexão para cada uso - ideal para serverless"""
    client = AsyncIOMotorClient(
        MONGO_DETAILS,
        maxPoolSize=1,
        minPoolSize=0,
        serverSelectionTimeoutMS=5000
    )
    return client.azakron

# Funções para obter collections com nova conexão
def get_collection_notes():
    return get_database().notes

def get_collection_tags():
    return get_database().tags

def get_collection_tasks():
    return get_database().tasks

logger.info("✅ Configuração MongoDB pronta")