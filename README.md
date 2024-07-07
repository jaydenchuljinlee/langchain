![js](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

# 📚 Lang Chain 기반의 LLM 학습 저장소

## 💡 예제 목록

### 1. 기본 대화형 체인 예제
- **파일명**: `basic_conversation_chain.py`
- **설명**: OpenAI를 사용하여 기본적인 대화형 체인을 구현한 예제입니다.
- **사용된 기술**: `langchain`, `OpenAI`

### 2. Pinecone 벡터 저장소를 사용한 문서 업로드 예제 <span style="color: orange;">(예제 작성중)</span>
- **파일명**: `document_upload.py`
- **설명**: Pinecone을 사용하여 문서를 임베딩하고 벡터 저장소에 업로드하는 예제입니다.
- **사용된 기술**: `pinecone-client`, `OpenAIEmbeddings`, `langchain`

### 3. Redis와 Pinecone을 사용한 대화형 체인 예제 <span style="color: orange;">(예제 작성중)</span>
- **파일명**: `app.py`
- **설명**: Redis를 메모리 저장소로, Pinecone을 벡터 저장소로 사용하여 대화형 체인을 구현한 예제입니다.
- **사용된 기술**: `Flask`, `pinecone-client`, `redis`, `langchain`, `OpenAI`

### 4. PostgreSQL과 Redis를 사용한 대화 기록 관리 예제 <span style="color: orange;">(예제 작성중)</span>
- **파일명**: `app_with_postgresql.py`
- **설명**: PostgreSQL을 사용하여 대화 기록을 영구 저장하고, Redis를 사용하여 실시간 컨텍스트를 유지하는 하이브리드 접근 방식의 예제입니다.
- **사용된 기술**: `Flask`, `pinecone-client`, `redis`, `psycopg2`, `langchain`, `OpenAI`

## 사용된 주요 기술

- **OpenAI**: 자연어 처리 및 생성 모델을 제공하는 API.
- **Pinecone**: 대규모 벡터 검색을 지원하는 클라우드 기반 벡터 데이터베이스.
- **Redis**: 빠른 읽기/쓰기를 제공하는 인메모리 데이터 구조 저장소.
- **PostgreSQL**: 관계형 데이터베이스로, 복잡한 쿼리와 트랜잭션을 지원.
- **Flask**: 파이썬 기반의 마이크로 웹 프레임워크로, 간단한 API 서버를 구축하는 데 사용.
- **LangChain**: 대화형 체인을 구축하는 데 사용되는 라이브러리.
- **psycopg2**: PostgreSQL 데이터베이스와 파이썬을 연결해주는 드라이버.

## 설정 및 실행 방법

### 필수 설치 패키지

다음 패키지들을 설치해야 합니다:

```sh
pip install flask langchain openai pinecone-client redis psycopg2
