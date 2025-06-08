# 🧠 OpenAI Embeddings 학습 정리

## 📌 개요

`OpenAIEmbeddings`는 LangChain 또는 OpenAI SDK에서 제공하는 클래스/기능으로, 텍스트를 벡터로 변환하여 검색, 유사도 비교, 분류 등에 활용할 수 있게 합니다.

```python
from langchain_openai import OpenAIEmbeddings
```

---

## 📦 주요 파라미터

| 파라미터                | 설명                                                                |
| ------------------- | ----------------------------------------------------------------- |
| `model`             | 임베딩 모델 이름 (예: `text-embedding-3-small`, `text-embedding-ada-002`) |
| `dimensions`        | 출력 벡터의 차원 수 제한 (예: 128, 256, 512, ...)                            |
| `openai_api_key`    | OpenAI API 인증 키                                                   |
| `chunk_size`        | batch 처리할 문장 수                                                    |
| `show_progress_bar` | 처리 진행 바 표시 여부                                                     |


---

## 🔧 주요 메서드

| 메서드                                 | 설명                      |
| ----------------------------------- | ----------------------- |
| `embed_documents(texts: List[str])` | 여러 문장을 벡터로 임베딩          |
| `embed_query(text: str)`            | 단일 쿼리를 벡터로 임베딩 (검색에 사용) |


---

## 🎯 차원(dimensions)을 제한하는 이유

| 목적     | 설명                                |
| ------ | --------------------------------- |
| 성능 최적화 | 차원 수가 낮을수록 연산이 빠름, 메모리 적음         |
| 비용 절감  | 벡터 저장/비교 비용 감소                    |
| 시스템 호환 | 기존 DB 또는 모델과 호환을 맞추기 위함           |
| 품질 제어  | 필요 이상의 차원은 정보 손실보다 오히려 노이즈 증가 가능성 |


---

## 🧪 실험: 다양한 차원별 코사인 유사도 비교

### 📝 테스트 문장

- 문장 A: "The quick brown fox jumps over the lazy dog."
- 문장 B: "A fast dark-colored fox leaps over a sleepy dog."

### 📊 결과

```markdown
   DIM | COSINE SIMILARITY
------------------------------
   128 | 0.72319
   256 | 0.76737
   512 | 0.76606
  1024 | 0.75479
  1536 | 0.75665
```

### 🧠 해석
- 가장 높은 유사도는 256차원에서 나옴
- 고차원(1024, 1536)은 반드시 더 좋은 유사도를 보장하지 않음
- 너무 낮은 차원(128)은 정보 손실로 인해 유사도 저하
- 적절한 차원 수는 목적과 환경에 따라 256~512가 좋은 선택일 수 있음

---

## 📈 시각화 예시 (Matplotlib)

```python
import matplotlib.pyplot as plt

dims = [128, 256, 512, 1024, 1536]
sims = [0.72319, 0.76737, 0.76606, 0.75479, 0.75665]

plt.plot(dims, sims, marker='o')
plt.title("Cosine Similarity vs Embedding Dimensions")
plt.xlabel("Dimensions")
plt.ylabel("Cosine Similarity")
plt.grid(True)
plt.show()
```

---

## 🔗 참고 자료

- [OpenAI 공식 임베딩 문서](https://platform.openai.com/docs/guides/embeddings)
- [LangChain Embeddings 가이드](https://python.langchain.com/docs/how_to/embed_text/)