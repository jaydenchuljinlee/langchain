
import os
from dotenv import load_dotenv
from langchain_openai import OpenAI, OpenAIEmbeddings
from typing import List, Dict

from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain.retrievers import ContextualCompressionRetriever

from langchain.retrievers.document_compressors import EmbeddingsFilter


def get_api_key() -> str:
    # .env 파일에서 환경변수 로드
    load_dotenv()

    # 환경변수에서 API 키 가져오기
    open_api_key = os.getenv("CHAT_GPT_API_KEY")

    return open_api_key
    # match os.environ.get("OPENAI_API_KEY"):
    #     case str() as api_key:
    #         return api_key
    #     case _:
    #         raise ValueError("OPENAI_API_KEY not found in environment variables")


def create_llm(api_key: str) -> OpenAI:
    return OpenAI(temperature=0.9, openai_api_key=api_key)


def create_vector_store(documents: List[Dict[str, str]], api_key: str) -> FAISS:
    text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
    docs = text_splitter.create_documents([doc["text"] for doc in documents])
    embeddings = OpenAIEmbeddings(openai_api_key=api_key)
    return FAISS.from_documents(docs, embeddings)


def create_conversation_chain(llm: OpenAI, documents: List[Dict[str, str]], api_key: str):
    text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
    docs = text_splitter.create_documents([doc["text"] for doc in documents])
    embeddings = OpenAIEmbeddings(openai_api_key=api_key)
    vector_store = FAISS.from_documents(docs, embeddings)

    retriever = vector_store.as_retriever()

    embeddings_filter = EmbeddingsFilter(embeddings=embeddings, similarity_threshold=0.76)

    compression_retriever = ContextualCompressionRetriever(
        base_compressor=embeddings_filter, base_retriever=retriever)

    prompt = PromptTemplate.from_template("""Answer the following question based only on the provided context:

    Context: {context}

    Question: {input}

    Answer: """)

    document_chain = create_stuff_documents_chain(llm, prompt)

    return create_retrieval_chain(compression_retriever, document_chain)


def main():
    try:
        api_key = get_api_key()
        llm = create_llm(api_key)

        documents = [
            {"text": "Machine learning is a method of data analysis that automates analytical model building."},
            {"text": "Deep learning is a subset of machine learning that uses neural networks with many layers."}
        ]

        conversation_chain = create_conversation_chain(llm, documents, api_key)

        for question in [
            "Tell me about machine learning",
            "How does it differ from deep learning?"
        ]:
            response = conversation_chain.invoke({"input": question})
            print(f"Question: {question}")
            print(f"Answer: {response['answer']}\n")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
