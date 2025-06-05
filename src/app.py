from repository.chat_log_repository import save_chat_log

def main():
    # 예시 질문/응답 (실제는 LLM 응답 결과)
    query = "디스크 오류가 났어"
    response = "디스크 공간 부족으로 인한 오류입니다. 디스크 정리를 추천드립니다."
    keywords = ["디스크", "오류", "공간 부족"]
    category = "시스템"

    # ✅ PostgreSQL에 로그 저장
    save_chat_log(
        query=query,
        response=response,
        category=category,
        keywords=keywords
    )
    print("✅ 채팅 로그가 저장되었습니다.")

if __name__ == "__main__":
    main()
