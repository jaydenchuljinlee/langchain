CREATE TABLE chat_logs (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(64) NOT NULL,
    conversation_id VARCHAR(128) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    title VARCHAR(255),
    model_version VARCHAR(64),
    user_query TEXT NOT NULL,
    ai_response TEXT NOT NULL,
    category VARCHAR(50),
    keywords TEXT,
    tags TEXT
);

CREATE INDEX idx_chat_logs_user_id ON chat_logs(user_id);
CREATE INDEX idx_chat_logs_conversation_id ON chat_logs(conversation_id);
CREATE INDEX idx_chat_logs_created_at ON chat_logs(created_at);
