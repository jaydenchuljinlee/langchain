import os
import openai
from scipy.spatial.distance import cosine
from dotenv import load_dotenv

def get_env_variable(key: str) -> str:
    load_dotenv()
    value = os.getenv(key)
    if not value:
        raise ValueError(f"Missing environment variable: {key}")
    return value

def get_embedding(text, model="text-embedding-3-small", dimensions=None):
    res = openai.embeddings.create(
        model=model,
        input=text,
        dimensions=dimensions  # OpenAI가 자동 차원 축소
    )
    return res.data[0].embedding

def cosine_similarity(a, b):
    return 1 - cosine(a, b)

def main():
    openai.api_key = get_env_variable("CHAT_GPT_API_KEY")
    # ✅ 문장 쌍
    text_1 = "The quick brown fox jumps over the lazy dog."
    text_2 = "A fast dark-colored fox leaps over a sleepy dog."

    # ✅ 다양한 차원 수
    dims = [128, 256, 512, 1024, 1536]

    # ✅ 임베딩 및 유사도 비교
    print(f"{'DIM':>6} | COSINE SIMILARITY")
    print("-" * 30)
    for dim in dims:
        vec1 = get_embedding(text_1, dimensions=dim)
        vec2 = get_embedding(text_2, dimensions=dim)
        sim = cosine_similarity(vec1, vec2)
        print(f"{dim:>6} | {sim:.5f}")


if __name__ == "__main__":
    main()
