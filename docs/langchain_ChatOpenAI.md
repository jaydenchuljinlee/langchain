# 🧠 LangChain `BaseChatModel` 학습 정리

## 📌 개요

`BaseChatModel`은 LangChain에서 모든 **Chat 기반 LLM 모델**을 추상화하기 위한 **기본 추상 클래스**입니다. `ChatOpenAI`, `ChatAnthropic`, `ChatMistral` 등 모든 LLM은 이 클래스를 기반으로 구현됩니다.

```python
class BaseChatModel(BaseLanguageModel[BaseMessage], ABC):
```

- Runnable을 간접 상속하여 실행 가능한 객체로 동작함
- 핵심 메서드: _generate(), _call(), invoke()

---

## 📚 상속 구조

```text
ChatOpenAI
 └── BaseChatOpenAI
      └── BaseChatModel
           └── BaseLanguageModel
                └── RunnableSerializable
                     └── Runnable
```

- invoke, __call__, batch, stream 등의 메서드는 Runnable에서 제공됨

---

## 🔧 핵심 구현 메서드

| 메서드                    | 설명                                             | 필수 여부 |
| ---------------------- | ---------------------------------------------- | ----- |
| `_generate(messages)`  | 실제 LLM 호출 및 결과 생성                              | ✅ 필수  |
| `_llm_type` (property) | 모델 타입 명시 (`"openai-chat"`, `"anthropic"`, ...) | ✅ 필수  |
| `_identifying_params`  | 트레이싱/로깅용 파라미터 반환                               | ⭕ 선택  |
| `_stream(messages)`    | 스트리밍 응답 처리                                     | ⭕ 선택  |
| `_agenerate()`         | 비동기 LLM 응답 생성                                  | ⭕ 선택  |
| `_astream()`           | 비동기 스트리밍 처리                                    | ⭕ 선택  |


---

## 🚀 실행 흐름 (호출 스택)

```python
llm = ChatOpenAI(...)
llm.invoke(input)
```

### 내부 흐름

```text
invoke(input)
 → Runnable.invoke()
   → _call_with_config(func=self._call, input)
     → context.run(call_func_with_variable_args, self._call, ...)
       → self._call(input)
         → self._generate(messages)
           → openai.ChatCompletion.create(...)
```

- invoke()와 __call__()은 동일한 동작을 함
- self._call은 BaseChatModel에서 구현됨

---

## ⚙️ Imperative Methods (즉시 실행 메서드)

| 메서드                     | 입력                                    | 출력                           | 설명        |
| ----------------------- | ------------------------------------- | ---------------------------- | --------- |
| `invoke()`              | `str`, `BaseMessage`, `PromptValue` 등 | `BaseMessage`                | 단일 실행     |
| `ainvoke()`             | 위와 동일                                 | `BaseMessage`                | 비동기 실행    |
| `stream()`              | 입력                                    | `Iterator[BaseMessageChunk]` | 스트리밍 실행   |
| `astream()`             | 입력                                    | `AsyncIterator[...]`         | 비동기 스트리밍  |
| `batch()`               | 여러 입력                                 | `List[BaseMessage]`          | 병렬 실행     |
| `abatch()`              | 여러 입력                                 | `List[BaseMessage]`          | 비동기 병렬 실행 |
| `batch_as_completed()`  | 여러 입력                                 | 완료 순서대로 반환                   | 병렬 처리 결과  |
| `abatch_as_completed()` | 여러 입력                                 | 완료 순서대로 비동기 반환               | 비동기 병렬 처리 |


---

## 🧱 Declarative Methods (구성 및 래퍼 메서드)

| 메서드                              | 설명                  |
| -------------------------------- | ------------------- |
| `with_retry()`                   | 실패 시 자동 재시도 기능 추가   |
| `with_fallbacks([모델])`           | 모델 실패 시 대체 모델 사용    |
| `with_structured_output(schema)` | 모델 출력을 구조화된 형식으로 파싱 |
| `bind_tools(tools)`              | 도구 호출이 가능한 모델로 구성   |
| `configurable_fields()`          | 런타임에 구성 가능한 필드 지정   |
| `configurable_alternatives()`    | 교체 가능한 모델 정의        |


---

## 📚 클래스 계층 구조

```plaintext
ChatOpenAI
 └── BaseChatOpenAI
      └── BaseChatModel
           └── BaseLanguageModel
                └── RunnableSerializable
                     └── Runnable
```

## 🧱 1. BaseChatModel

```python
class BaseChatModel(BaseLanguageModel[BaseMessage], ABC):
    @abstractmethod
    def _generate(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> ChatResult:
        ...
```

- LangChain의 chat 기반 모델 추상 클래스
- _generate() 메서드를 통해 실제 모델 호출 구현을 요구
- invoke, __call__, stream, batch 등은 Runnable을 통해 자동 제공됨

## 🧱 2. BaseChatOpenAI

```python
class BaseChatOpenAI(BaseChatModel, ABC):
    model_name: str
    temperature: float = 0.7
    max_tokens: Optional[int] = None
    ...
```

- OpenAI Chat 모델의 공통 속성을 정의한 중간 추상 클래스
- BaseChatModel을 상속하여 구조 통합
- _generate()는 여전히 구현되지 않음 → ChatOpenAI에서 구현

## 🧱 3. ChatOpenAI 구현 예

```python
class ChatOpenAI(BaseChatOpenAI):
    def _generate(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> ChatResult:
        response = openai.ChatCompletion.create(
            model=self.model_name,
            messages=[m.to_dict() for m in messages],
            temperature=self.temperature,
            ...
        )
        content = response.choices[0].message["content"]
        message = AIMessage(content=content)
        return ChatResult(generations=[ChatGeneration(message=message)])
    
    @property
    def _llm_type(self) -> str:
        return "openai-chat"
```

- _generate() 내부에서 실제 OpenAI API (openai.ChatCompletion.create)를 호출
- 응답은 LangChain의 ChatResult, ChatGeneration, AIMessage로 래핑됨

---

## 🧭 실행 흐름 요약

```python
llm = ChatOpenAI(...)
result = llm.invoke([HumanMessage(content="Hello")])
```


### 내부 호출 스택

```text
invoke() → Runnable.invoke()
  → _call_with_config(self._call)
    → self._call(input)
      → self._generate(messages)
        → openai.ChatCompletion.create(...)
```

## 📝 참고 링크

- [📄 LangChain 공식 가이드: Custom Chat Model](https://python.langchain.com/docs/how_to/custom_chat_model/)

--- 