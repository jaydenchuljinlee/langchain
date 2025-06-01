
import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain.chains import LLMChain

from langchain.prompts import PromptTemplate
from langchain.chains import create_retrieval_chain


def get_api_key() -> str:
    # .env 파일에서 환경변수 로드
    load_dotenv()

    # 환경변수에서 API 키 가져오기
    open_api_key = os.getenv("CHAT_GPT_API_KEY")

    return open_api_key

def create_llm(api_key: str) -> OpenAI:
    return OpenAI(temperature=0.9, openai_api_key=api_key)

def load_prompt_from_file(path: str) -> PromptTemplate:
    with open(path, "r", encoding="utf-8") as file:
        template_str = file.read()
    return PromptTemplate.from_template(template_str)

def main():
    try:
        api_key = get_api_key()
        llm = create_llm(api_key)

        prompt = load_prompt_from_file("../resources/pormpt/structured/structured_prompt.txt")
        chain = prompt | llm

        response = chain.invoke({"context": "서버 에러 발생, 에러 코드: 502"})
        print(response)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
