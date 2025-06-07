import os
from datetime import datetime
from typing import Dict

from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

# MongoDB 환경변수
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB", "llm_chat")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION", "chat_contents")

# Mongo 클라이언트 생성
client = MongoClient(MONGO_URI)
db = client[MONGO_DB]
collection = db[MONGO_COLLECTION]


def save_chat_content(conversation_id: str, content: Dict):
    """
    MongoDB에 conversation_id 기준으로 대화 내용 저장
    기존에 있으면 덮어씀
    """
    content["updated_at"] = datetime.utcnow()
    collection.replace_one(
        {"conversation_id": conversation_id},
        {"conversation_id": conversation_id, **content},
        upsert=True
    )


def get_chat_content(conversation_id: str) -> Dict | None:
    """
    conversation_id로 대화 내용 조회
    """
    return collection.find_one({"conversation_id": conversation_id})
