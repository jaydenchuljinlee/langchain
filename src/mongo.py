from src.repository.chat_content_repository import save_chat_content

def main():
    conversation_id = "conv_20250604_xyz"
    chat_data = {
        "user_id": "user_12345",
        "messages": [
            {"role": "user", "content": "디스크 오류가 났어"},
            {"role": "assistant", "content": "디스크 공간 부족으로 인한 오류입니다."}
        ]
    }

    save_chat_content(conversation_id, chat_data)


if __name__ == "__main__":
    main()
