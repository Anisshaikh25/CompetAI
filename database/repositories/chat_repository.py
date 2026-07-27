from sqlalchemy import select

from models.chat_messages import ChatMessage
from .base_repository import BaseRepository


class ChatMessageRepository(BaseRepository):

    # --------------------------------------------------
    # Get Message by ID
    # --------------------------------------------------

    def get_by_id(
        self,
        message_id: int
    ) -> ChatMessage | None:

        statement = select(ChatMessage).where(
            ChatMessage.id == message_id
        )

        result = self.db.execute(statement)

        return result.scalar_one_or_none()

    # --------------------------------------------------
    # Get Chat History
    # --------------------------------------------------

    def get_chat_history(
        self,
        session_id: str
    ) -> list[ChatMessage]:

        statement = (
            select(ChatMessage)
            .where(ChatMessage.session_id == session_id)
            .order_by(ChatMessage.created_at.asc())
        )

        result = self.db.execute(statement)

        return result.scalars().all()

    # --------------------------------------------------
    # Create Chat Message
    # --------------------------------------------------

    def create_message(
        self,
        session_id: str,
        user_message: str,
        assistant_message: str,
        retrieved_documents: str | None = None,
        response_time_ms: int = 0,
    ) -> ChatMessage:

        message = ChatMessage(
            session_id=session_id,
            user_message=user_message,
            assistant_message=assistant_message,
            retrieved_documents=retrieved_documents,
            response_time_ms=response_time_ms,
        )

        self.db.add(message)

        self.db.commit()

        self.db.refresh(message)

        return message

    # --------------------------------------------------
    # Update Feedback
    # --------------------------------------------------

    def update_feedback(
        self,
        message: ChatMessage,
        feedback: int
    ) -> ChatMessage:

        message.feedback = feedback

        self.db.commit()

        self.db.refresh(message)

        return message

    # --------------------------------------------------
    # Delete Chat Session
    # --------------------------------------------------

    def delete_chat_session(
        self,
        session_id: str
    ) -> None:

        messages = self.get_chat_history(session_id)

        for message in messages:
            self.db.delete(message)

        self.db.commit()

    # --------------------------------------------------
    # Delete Single Message
    # --------------------------------------------------

    def delete_message(
        self,
        message: ChatMessage
    ) -> None:

        self.db.delete(message)

        self.db.commit()