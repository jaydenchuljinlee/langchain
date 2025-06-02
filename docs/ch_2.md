# 📚 구조화된 프롬프트 (Structured Prompting) 정리

## ✅ 구조화된 프롬프트란?
- LLM이 **정해진 형식**에 따라 일관된 출력을 생성하도록 유도하는 프롬프트 방식
- 사람이 읽기 쉽게 하기보다 **기계가 처리하기 쉽도록** 포맷화된 응답을 받기 위해 사용됨
- 출력 형식은 JSON, XML, Markdown, TSV 등으로 지정 가능

---

## 🧩 주요 특징

| 특징             | 설명 |
|------------------|------|
| **정형화된 응답** | LLM이 자유롭게 서술하지 않고, 반드시 정해진 포맷(예: JSON 키 포함)에 따라 응답 |
| **후처리 용이성** | 응답값을 파싱하거나 다른 체인 단계에 전달할 때 오류 발생 가능성이 낮음 |
| **검증 가능성**  | LLM의 출력이 예상된 구조와 일치하는지 쉽게 검증 가능 |
| **파이프라인 연결** | 이전 체인의 출력이 다음 체인의 입력으로 명확히 이어질 수 있음 (chaining과 잘 어울림) |

---

## ✏️ 프롬프트 작성 예시 (JSON 출력 유도)

```text
다음 입력이 특정 조건을 만족하는지 판단하고, 값을 추출하거나 대체 값을 생성해줘.

조건:
1. 입력이 '에러 로그' 문맥이어야 함
2. '에러 코드'가 포함되어야 함

규칙:
- 문맥이 적절하지 않으면: {"status": "ignored"}
- 문맥이 적절하지만 코드가 없으면: {"status": "generated", "error_code": "<생성된 에러 코드>"}
- 문맥이 적절하고 코드가 있으면: {"status": "ok", "error_code": "<기존 코드>"}

입력 로그: {log}

출력 (JSON 형식):
```

---

## 🛠️ LangChain 적용 방식

```python
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence

prompt = PromptTemplate.from_template(template_str)
chain = prompt | ChatOpenAI(...)  # RunnableSequence 구성

response = chain.invoke({"log": "에러 로그 발생. 에러 코드: 502"})
print(response.content)
```

🧠 활용 예시
- 에러 로그 자동 분류
- 고객 응답 템플릿 자동 생성
- 서버 이벤트 → 조건 분기 → 조치 응답
- JSON 응답 기반의 체인 분기 처리 (Branching)
