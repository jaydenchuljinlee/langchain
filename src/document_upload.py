# 문서 사전 저장 예제

# 문서 저장과 질문 기록의 차이

# 1. 문서 저장
# 목적: 사전에 준비된 지식을 제공하기 위해 사용.
# 시기: 시스템 초기 설정 시 또는 주기적으로 업데이트할 때.
# 내용: 제품 설명서, 지식 베이스, FAQ, 연구 논문 등.
# 예시: 제품 사용 설명서를 Pinecone에 저장하여 사용자가 제품 관련 질문을 하면 신속하게 관련 정보를 제공.

# 2. 질문 기록
# 목적: 대화의 맥락을 유지하고 사용자의 의도를 파악하기 위해 사용.
# 시기: 사용자가 대화할 때마다 실시간으로 기록.
# 내용: 사용자의 질문, 모델의 응답, 대화 히스토리.
# 예시: 사용자가 "내가 이전에 말했던 문제는 어떻게 해결할 수 있나요?"라고 물었을 때, 이전 대화 기록을 참고하여 정확한 답변을 제공.

import pinecone
from langchain.embeddings import OpenAIEmbeddings

# Pinecone 초기화
pinecone.init(api_key='YOUR_PINECONE_API_KEY', environment='us-west1-gcp')
pinecone_index = pinecone.Index('langchain-demo')

# 임베딩 생성
embeddings = OpenAIEmbeddings()


# 문서 업로드 함수
def upload_documents(documents):
    for doc_id, document in enumerate(documents):
        text = document['text']
        embedding = embeddings.embed_text(text)
        pinecone_index.upsert([(f"doc_{doc_id}", embedding, {"text": text})])


# 예시 문서
documents = [
    {"text": "Machine learning is a method of data analysis that automates analytical model building."},
    {"text": "Deep learning is a subset of machine learning that uses neural networks with many layers."}
]

# 문서 업로드
upload_documents(documents)
