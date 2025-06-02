# 📘 LLM (Large Language Model) 기본 학습 문서

## 1. LLM이란?

**LLM (Large Language Model)**은 수십억 개 이상의 파라미터를 가진 대규모 딥러닝 모델로, 자연어 처리(NLP) 작업을 위한 **사전 학습 기반 언어 모델**입니다. GPT(Generative Pretrained Transformer), LLaMA, Claude, PaLM 등 다양한 LLM이 존재합니다.

### 🔍 주요 특징
- 대규모 텍스트 코퍼스로 사전 학습됨
- 문맥 이해와 생성 능력이 뛰어남
- 다양한 자연어 작업에 범용적으로 활용 가능

---

## 2. LLM의 주요 구성

| 구성 요소 | 설명 |
|-----------|------|
| **Tokenization** | 텍스트를 모델이 이해할 수 있는 단위(token)로 분할 |
| **Embedding** | 토큰을 고차원 벡터로 변환 |
| **Transformer** | Attention 메커니즘 기반의 모델 구조 |
| **Decoder** | 토큰 시퀀스를 입력 받아 다음 토큰을 생성 |

---

## 3. 동작 원리

1. 사용자가 입력한 자연어 문장을 **Tokenize**
2. 각 토큰을 **Embedding 벡터**로 변환
3. **Transformer block**을 통해 문맥 정보를 처리
4. 다음 토큰을 예측하여 결과를 생성
5. 생성된 토큰을 다시 문자열로 디코딩

---

## 4. 대표 활용 사례

| 분야 | 예시 |
|------|------|
| 💬 챗봇 | 고객센터 자동응답, AI 비서 |
| 📝 문서 요약 | 뉴스, 논문 요약 |
| 🔍 질의응답 | FAQ 시스템, 내부 문서 검색 |
| 💡 코드 생성 | Copilot, 코드 자동 보완 |
| 📊 데이터 추출 | 로그 분석, JSON 구조 추출 |

---

## 5. LLM + LangChain 구조 이해

LangChain은 LLM을 **실제 비즈니스 로직이나 외부 시스템**과 연결하기 위한 파이프라인 프레임워크입니다.


```text
사용자 입력
   ↓
PromptTemplate (프롬프트 구성)
   ↓
LLM (예: OpenAI GPT)
   ↓
Output Parser (예: JSON 파싱)
   ↓
Chain or Agent로 연결
```

---

## 📌 주요 개념 요약

| 개념              | 설명 |
|-------------------|------|
| **Prompt**        | LLM에게 작업을 지시하는 명령어 또는 질문 문장. 명확하고 구체적으로 작성해야 원하는 결과를 얻을 수 있음 |
| **PromptTemplate**| 프롬프트에 변수를 삽입할 수 있도록 템플릿화한 구조. 입력값에 따라 다양한 프롬프트를 자동 생성 가능 |
| **Few-shot Prompt** | 예제를 포함해 LLM이 작업 방식이나 형식을 학습하도록 유도하는 프롬프트 전략 |
| **Chain**         | 여러 단계의 처리 로직(예: 프롬프트 → LLM → 후처리)을 연결해 하나의 파이프라인처럼 작동하게 함 |
| **RunnableSequence** | LangChain 최신 방식에서 사용하는 체이닝 객체. 여러 구성요소를 파이프처럼 연결할 수 있음 (`prompt | llm`) |
| **Branching**     | LLM의 응답 결과(예: JSON 상태값 등)에 따라 다른 체인을 선택적으로 실행하는 흐름 제어 방식 |
| **Agent**         | 도구(tool), 메모리(memory), 체인 등을 사용해 스스로 의사결정을 내리고 적절한 작업을 선택해 수행하는 구조 |
| **Retriever**     | 벡터 DB나 문서 저장소에서 관련 정보를 검색하여 LLM에 전달하는 구성요소 (RAG에 활용됨) |
| **RAG (Retrieval-Augmented Generation)** | LLM이 외부 지식을 검색(Retrieve)하고 그 문맥을 기반으로 응답을 생성(Generate)하는 방식 |
| **Memory**        | 이전 대화나 입력 이력을 저장해 LLM이 문맥을 유지하도록 돕는 기능 |
| **Output Parser** | LLM의 출력 텍스트를 JSON, 숫자 등 원하는 형태로 파싱하기 위한 처리 단계 |

