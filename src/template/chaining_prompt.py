import os
import json
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableSequence

def get_api_key() -> str:
    load_dotenv()
    return os.getenv("CHAT_GPT_API_KEY")

def load_prompt_from_file(path: str) -> PromptTemplate:
    with open(path, "r", encoding="utf-8") as file:
        template_str = file.read()
    return PromptTemplate.from_template(template_str)


def main():
    try:
        api_key = get_api_key()
        llm = ChatOpenAI(temperature=0.3, openai_api_key=api_key)

        # 1단계 프롬프트: 에러 판단 -> 구조화된 프롬프트
        error_prompt = load_prompt_from_file("../resources/pormpt/chaining/chain_structured_prompt.txt")
        chain1: RunnableSequence = error_prompt | llm

        # 2단계 프롬프트: 대응 설명 -> few shot 프롬프트
        explanation_prompt = load_prompt_from_file("../resources/pormpt/chaining/chain_few_shot_prompt.txt")
        ok_chain: RunnableSequence = explanation_prompt | llm

        generated_prompt = load_prompt_from_file("../resources/pormpt/chaining/chain_generated_prompt.txt")
        generated_chain: RunnableSequence = generated_prompt | llm

        ignored_prompt = load_prompt_from_file("../resources/pormpt/chaining/chain_ignored_prompt.txt")
        ignored_chain: RunnableSequence = ignored_prompt | llm

        # 테스트용 로그
        logs = [
            "정상 처리됨",
            "에러 로그 발생. 에러 코드: 502",
            "에러 로그 발생"
        ]

        for log in logs:
            print(f"✅ Input Log: {log}")

            # 1단계 실행: 상태 판단
            response1 = chain1.invoke({"log": log})
            print("🧠 Status JSON:", response1.content.strip())

            # JSON 파싱
            try:
                status_json = json.loads(response1.content.strip())
            except json.JSONDecodeError:
                print("❌ Invalid JSON returned from error_prompt\n")
                continue

            status = status_json.get("status", "unknown")
            error_code = status_json.get("error_code", "-")

            # 2단계 실행: 상태별 브랜칭
            if status == "ok":
                response2 = ok_chain.invoke({"status": status, "error_code": error_code})
            elif status == "generated":
                response2 = generated_chain.invoke({"status": status, "error_code": error_code})
            else:
                response2 = ignored_chain.invoke({"status": status, "error_code": error_code})

            # 3단계 실행: 설명 생성
            print("💡 Explanation:", response2.content.strip(), "\n")


    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
