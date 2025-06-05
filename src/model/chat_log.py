from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from src.config.database import Base  # 공유 Base

class ChatLog(Base):
    __tablename__ = "chat_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_query = Column(Text, nullable=False)
    ai_response = Column(Text, nullable=False)
    category = Column(String(50))
    keywords = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
