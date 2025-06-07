from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from src.config.database import Base

class ChatLog(Base):
    __tablename__ = "chat_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(64), nullable=False)
    conversation_id = Column(String(128), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    title = Column(String(255))
    model_version = Column(String(64))

    user_query = Column(Text, nullable=False)
    ai_response = Column(Text, nullable=False)
    category = Column(String(50))
    keywords = Column(Text)
    tags = Column(Text)
