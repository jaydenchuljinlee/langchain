# 대화 기록 및 응답 처리

# document_upload.py에서 저장한 문서 기반의 응답 예제

import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from langchain_openai import OpenAI, OpenAIEmbeddings
from langchain.chains import ConversationalRetrievalChain
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from langchain.vectorstores import Pinecone
from langchain.memory import RedisChatMessageHistory
from langchain.chains import LLMChain
import pinecone
import redis

app = Flask(__name__)

# .env 파일에서 환경변수 로드
load_dotenv()

# 환경변수에서 API 키 가져오기
open_api_key = os.getenv("CHAT_GPT_API_KEY")

# OpenAI 모델 초기화
llm = OpenAI(temperature=0.9, openai_api_key=open_api_key)

# Pinecone 초기화
pinecone.init(api_key='YOUR_PINECONE_API_KEY', environment='us-west1-gcp')
pinecone_index = pinecone.Index('langchain-demo')

# Redis 초기화
# redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# 임베딩 생성
embeddings = OpenAIEmbeddings(openai_api_key=open_api_key)

# 벡터 저장소 생성
vector_store = Pinecone(index=pinecone_index, embedding=embeddings)

# QA 체인 로드
qa_chain = load_qa_chain(llm, chain_type="map_reduce")

# 질문 생성기 프롬프트 템플릿 정의
question_generator_template = PromptTemplate(
    input_variables=["context"],
    template="Generate a question based on the following context:\n\n{context}"
)

# 질문 생성기 체인 생성
question_generator_chain = LLMChain(
    llm=llm,
    prompt=question_generator_template
)

# RedisChatMessageHistory 초기화
redis_url = 'redis://localhost:6379/0'
memory = RedisChatMessageHistory(redis_url)

# 대화형 체인 생성
conversation_chain = ConversationalRetrievalChain(
    retriever=vector_store.as_retriever(),
    question_generator=question_generator_chain,
    combine_docs_chain=qa_chain,
    memory=memory
)


@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("question")
    response = conversation_chain({"question": user_input})
    return jsonify(response)


if __name__ == '__main__':
    app.run(port=5000)
