import os
from dotenv import load_dotenv
from langchain import OpenAI, ConversationChain

# .env 파일에서 환경변수 로드
load_dotenv()

# 환경변수에서 API 키 가져오기
api_key = os.getenv("CHAT_GPT_API_KEY")
llm = OpenAI(temperature=0.9, openai_api_key=api_key)

conversation = ConversationChain(llm=llm)

response = conversation.predict(input="Hello! How can I improve my coding skills?")

print(response)
