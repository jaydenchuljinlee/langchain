# 🔗 LangChain 체이닝(Chaining)과 브랜칭(Branching) 정리

## ✅ 체이닝 (Chaining)

### 🧠 정의
- 여러 개의 처리 단계를 **선형(직렬)** 으로 연결하여, 앞 단계의 출력이 다음 단계의 입력이 되도록 구성하는 방식
- `RunnableSequence` 를 통해 구현됨

### 🧱 구조 예시

```text
[PromptTemplate1] → [LLM1] → [PromptTemplate2] → [LLM2] → 결과
```

또는

```python
from langchain_core.runnables import RunnableSequence

chain = prompt1 | llm1 | prompt2 | llm2
response = chain.invoke({"input": "에러 로그 발생"})
```

## 🧰 사용 예

1. 에러 로그 → 상태 판단 (JSON 반환)
2. JSON에서 에러 코드 추출 → 설명 프롬프트로 전달
3. 최종 응답 생성

---

## 🌿 브랜칭 (Branching)

### 🌟 정의
- 조건에 따라 다른 체인 또는 로직을 분기시켜 실행하는 방식
- 체이닝 결과의 상태나 속성에 따라 경로를 달리함 (예: "status": "ok" → 설명 체인, "ignored" → 아무것도 하지 않음)

### 🔧 구현 방식 (Python)

```python
if status == "ok":
    response = ok_chain.invoke({...})
elif status == "generated":
    response = generated_chain.invoke({...})
else:
    response = ignored_chain.invoke({...})
```

또는 RunnableLambda를 통한 동적 라우팅 방식도 가능

---

## 🔄 체이닝 + 브랜칭 통합 구조 예시

```text
[Input Log]
   ↓
[PromptTemplate: JSON 판단] ──→ {status: "ok", error_code: "502"}
   ↓
[Branching 처리]
   ├─ "ok"         → [PromptTemplate: 코드 설명] → [LLM]
   ├─ "generated"  → [PromptTemplate: 임시 코드 설명] → [LLM]
   └─ "ignored"    → 출력 생략 또는 고정 응답
```




