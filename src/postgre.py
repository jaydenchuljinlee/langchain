from repository.chat_log_repository import save_chat_log
from datetime import datetime


def main():
    # 예시 데이터 (실제 서비스에서는 동적으로 주입됨)
    user_id = "user_12345"
    conversation_id = "conv_20250604_xyz"
    title = "pinecone 설정 문제"
    model_version = "gpt-4o"
    created_at = datetime.now()

    query = "디스크 오류가 났어"
    response = "디스크 공간 부족으로 인한 오류입니다. 디스크 정리를 추천드립니다."
    keywords = ["디스크", "오류", "공간 부족"]
    category = "시스템"
    tags = ["LangChain", "프롬프트"]

    # ✅ PostgreSQL에 로그 저장
    save_chat_log(
        user_id=user_id,
        conversation_id=conversation_id,
        created_at=created_at,
        title=title,
        model_version=model_version,
        query=query,
        response=response,
        category=category,
        keywords=keywords,
        tags=tags
    )
    print("✅ 채팅 로그가 저장되었습니다.")


if __name__ == "__main__":
    main()
