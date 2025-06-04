import os
import json
from dotenv import load_dotenv
from typing import List, Dict

from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_core.messages import AIMessage
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain.retrievers import ContextualCompressionRetriever
from langchain_community.vectorstores import FAISS
from langchain.retrievers.document_compressors import EmbeddingsFilter


def get_env_variable(key: str) -> str:
    load_dotenv()
    value = os.getenv(key)
    if not value:
        raise ValueError(f"Missing environment variable: {key}")
    return value


def create_llm(api_key: str) -> ChatOpenAI:
    return ChatOpenAI(temperature=0.3, openai_api_key=api_key)


def load_prompt_from_file(path: str) -> PromptTemplate:
    with open(path, "r", encoding="utf-8") as file:
        template_str = file.read()
    return PromptTemplate.from_template(template_str)


def extract_keywords_chain(llm: ChatOpenAI):
    keyword_prompt = PromptTemplate.from_template(
        """
        다음 사용자 질문에서 핵심 키워드와 카테고리를 JSON 형식으로 추출하세요.
        질문: {query}

        출력 형식:
        {{
            "keywords": ["..."],
            "category": "..."
        }}
        """
    )

    return keyword_prompt | llm | RunnableLambda(lambda x: json.loads(x.content))


def create_conversation_chain(llm: ChatOpenAI, documents: List[Dict[str, str]], api_key: str):
    embeddings = OpenAIEmbeddings(openai_api_key=api_key)
    text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
    split_docs = text_splitter.create_documents([doc["text"] for doc in documents])

    vector_store = FAISS.from_documents(split_docs, embeddings)
    retriever = vector_store.as_retriever()

    compression_retriever = ContextualCompressionRetriever(
        base_compressor=EmbeddingsFilter(embeddings=embeddings, similarity_threshold=0.76),
        base_retriever=retriever
    )

    try:
        prompt = load_prompt_from_file("../resources/prompt/embedding/embedding_prompt.txt")
    except FileNotFoundError:
        prompt = PromptTemplate.from_template(
            "다음 컨텍스트를 바탕으로 질문에 답하세요:\n\n{context}\n\n질문: {input}\n답변:"
        )

    document_chain = create_stuff_documents_chain(llm, prompt)
    return create_retrieval_chain(compression_retriever, document_chain)


def main():
    try:
        api_key = get_env_variable("CHAT_GPT_API_KEY")
        llm = create_llm(api_key)

        documents = [
            {"text": "서버에서 502 에러가 발생하였습니다."},
            {"text": "디스크 공간 부족으로 인해 오류가 발생했습니다."},
            {"text": "시스템은 정상적으로 작동 중입니다."}
        ]

        keyword_extractor = extract_keywords_chain(llm)
        conversation_chain = create_conversation_chain(llm, documents, api_key)

        queries = [
            "게이트웨이 오류가 있었어.",
            "서버가 작동 중지 됐다고?",
            "디스크 문제는 왜 발생했지?"
        ]

        for query in queries:
            try:
                print(f"\n📝 질문: {query}")
                keyword_response = keyword_extractor.invoke({"query": query})

                print(f"🔎 키워드 추출 결과: {keyword_response}")

                response = conversation_chain.invoke({"input": query})
                print(f"📘 답변: {response['answer']}")
            except Exception as e:
                print(f"❌ 키워드 처리 실패: {e}")

    except Exception as e:
        print(f"❌ 전체 오류 발생: {e}")


if __name__ == "__main__":
    main()
