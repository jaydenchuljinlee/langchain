-- chat_logs
CREATE TABLE chat_logs (
    id SERIAL PRIMARY KEY,
    user_query TEXT NOT NULL,
    ai_response TEXT NOT NULL,
    category VARCHAR(50),
    keywords TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
