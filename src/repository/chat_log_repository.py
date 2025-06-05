from src.config.database import SessionLocal
from src.model.chat_log import ChatLog

def save_chat_log(query: str, response: str, category: str = None, keywords: list[str] = None):
    db = SessionLocal()
    try:
        log = ChatLog(
            user_query=query,
            ai_response=response,
            category=category,
            keywords=", ".join(keywords) if keywords else None
        )
        db.add(log)
        db.commit()
    finally:
        db.close()
