from src.config.database import SessionLocal
from src.model.chat_log import ChatLog
from datetime import datetime

def save_chat_log(
    user_id: str,
    conversation_id: str,
    created_at: datetime,
    title: str,
    model_version: str,
    query: str,
    response: str,
    category: str = None,
    keywords: list[str] = None,
    tags: list[str] = None
):
    db = SessionLocal()
    try:
        log = ChatLog(
            user_id=user_id,
            conversation_id=conversation_id,
            created_at=created_at,
            title=title,
            model_version=model_version,
            user_query=query,
            ai_response=response,
            category=category,
            keywords=", ".join(keywords) if keywords else None,
            tags=", ".join(tags) if tags else None
        )
        db.add(log)
        db.commit()
    finally:
        db.close()
