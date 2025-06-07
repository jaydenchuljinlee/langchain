![js](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

# 📚 Lang Chain 기반의 LLM 학습 저장소

## 💡 예제 목록

### 1. 기본 대화형 예제
- **파일명**: `conversation_prompt.py`
- **설명**: OpenAI를 사용하여 기본적인 대화형 체인을 구현한 예제입니다.
- **사용된 기술**: `langchain`, `OpenAI`

### 2. 구조화된 프롬프트 예제
- **파일명**: `/template/structured_output_prompt.py`
- **설명**: 구조화된 체인을 통해 프롬프트에 대한 응답을 정형화한 예제입니다.
- **사용된 기술**: `langchain`, `OpenAI`

### 3. 체이닝 프롬프트 예제
- **파일명**: `/template/chaining_prompt.py`
- **설명**: 구조화 + 블레이싱을 통해 프롬프트를 단계별로 제어하는 예제입니다.
- **사용된 기술**: `langchain`, `OpenAI`

### 4. FAISS 벡터 저장소를 사용한 문서 업로드 예제
- **파일명**: `document_upload.py`
- **설명**: FAISS를 사용하여 문서를 벡터 저장소에 업로드하는 예제입니다.
- **사용된 기술**: `OpenAIEmbeddings`, `langchain`

### 5. FAISS 벡터 저장소를 사용한 임베딩 예제
- **파일명**: `/template/embbeded_document_prompt.py`
- **설명**: FAISS를 사용하여 문서를 임베딩하고 이를 기반으로 질의하는 예제입니다.
- **사용된 기술**: `OpenAIEmbeddings`, `langchain`

### 6. FAISS & 구조화 & 체이닝 프롬프트를 연계한 예제
- **파일명**: `/template/chaining_embbeded_prompt.py`
- **설명**: 이전에 학습한 구조화 + 체이닝 예제와 임베딩 문서를 연계한 예제입니다. 
- **사용된 기술**: `OpenAIEmbeddings`, `langchain`

### 6. Redis와 FAISS를 사용한 대화형 체인 예제
- **파일명**: `/template/caching_embbeded_prompt.py`
- **설명**: Redis를 메모리 저장소로, FAISS를 벡터 저장소로 사용하여 대화형 체인을 구현한 예제입니다.
- **사용된 기술**: `Flask`, `redis`, `langchain`, `OpenAI`

### 4. PostgreSQL과 MongoDB를 사용한 대화 기록 관리 예제
- **파일명**: `/template/caching_with_db_and_document_embbeded_prompt.py`
- **설명**: PostgreSQL을 사용하여 대화 메타 데이터를 저장하고 영구 저장하고, MongoDB를 사용하여 메타 데이터의 ID를 기반으로 대화 내용을 보관하는 에제입니다.
- **사용된 기술**: `Flask`, `pinecone-client`, `redis`, `psycopg2`, `langchain`, `OpenAI`

## 사용된 주요 기술

- **OpenAI**: 자연어 처리 및 생성 모델을 제공하는 API.
- **FAISS**: 대규모 벡터 검색을 지원하는 클라우드 기반 벡터 데이터베이스.
- **Redis**: 빠른 읽기/쓰기를 제공하는 인메모리 데이터 구조 저장소.
- **PostgreSQL**: 관계형 데이터베이스로, 복잡한 쿼리와 트랜잭션을 지원.
- **MongoDB**: 문서형 데이터베이스로, 비정형 데이터 기록을 지원
- **Flask**: 파이썬 기반의 마이크로 웹 프레임워크로, 간단한 API 서버를 구축하는 데 사용.
- **LangChain**: 대화형 체인을 구축하는 데 사용되는 라이브러리.
- **psycopg2**: PostgreSQL 데이터베이스와 파이썬을 연결해주는 드라이버.

### 필수 설치 패키지

다음 패키지들을 설치해야 합니다:

```sh
pip install -r requirements.txt
```

## 설정 파일 작성

```sh
# .env 파일 생성 (env 파일은 root 디렉토리 하위에 위치해야 합니다.)

CHAT_GPT_API_KEY=OPEN_AI_KEY_작성

# Redis
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0

# PostgreSQL
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=mydatabase
POSTGRES_USER=myuser
POSTGRES_PASSWORD=mypassword

# mongodb
MONGO_URI=mongodb://myuser:mypassword@localhost:27017
MONGO_DB=llm_chat
MONGO_COLLECTION=chat_contents
```

## 실행 파일 위치
- `/src/template` 디렉토리 아래 존재
- 해당 파일 단독으로 실행 가능



