from sqlalchemy import String, DateTime, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from decimal import Decimal

from database.db import Base
from datetime import datetime

class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    session_id: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True
    )

    user_message: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    assistant_message: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    retrieved_documents: Mapped[str | None] = mapped_column(
        Text
    )

    response_time_ms: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    feedback: Mapped[int | None] = mapped_column(
        Integer
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )   