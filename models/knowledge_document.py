from sqlalchemy import String, DateTime, ForeignKey, Text,Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from decimal import Decimal

from database.db import Base
from datetime import datetime
from enums import SourceType, EmbeddingStatus

class KnowledgeDocument(Base):
    __tablename__ = "knowledge_documents"

    id: Mapped[int] = mapped_column(primary_key=True)

    blog_post_id: Mapped[int | None] = mapped_column(
        ForeignKey("blog_posts.id"),
        nullable=True,
        index=True
    )

    title: Mapped[str] = mapped_column(
        String(300),
        nullable=False
    )

    content: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    source_type: Mapped[SourceType] = mapped_column(
        SQLEnum(SourceType),
        nullable=False
    )

    embedding_status: Mapped[EmbeddingStatus] = mapped_column(
        SQLEnum(EmbeddingStatus),
        default=EmbeddingStatus.PENDING,
        nullable=False
    )

    indexed_at: Mapped[datetime | None] = mapped_column(
        DateTime
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    blog_post: Mapped["BlogPost"] = relationship(
        back_populates="knowledge_documents"
    )