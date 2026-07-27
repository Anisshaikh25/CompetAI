from database.db import SessionLocal

from database.repositories.chat_repository import (
    ChatMessageRepository,
)

db = SessionLocal()

try:

    chat_repo = ChatMessageRepository(db)

    message = chat_repo.create_message(
        session_id="session_001",
        user_message="What are Dell's latest AI laptops?",
        assistant_message="Dell recently launched the XPS AI series...",
        retrieved_documents="doc_1, doc_2",
        response_time_ms=245
    )

    print(message)

    history = chat_repo.get_chat_history("session_001")

    print(history)

    chat_repo.update_feedback(
        message,
        feedback=1
    )

finally:
    db.close()