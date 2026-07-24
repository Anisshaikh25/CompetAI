from datetime import datetime

from sqlalchemy import select

from models.knowledge_document import KnowledgeDocument
from enums import EmbeddingStatus, SourceType
from .base_repository import BaseRepository


class KnowledgeDocumentRepository(BaseRepository):

    # --------------------------------------------------
    # Get by ID
    # --------------------------------------------------

    def get_by_id(self, document_id: int) -> KnowledgeDocument | None:

        statement = select(KnowledgeDocument).where(
            KnowledgeDocument.id == document_id
        )

        result = self.db.execute(statement)

        return result.scalar_one_or_none()

    # --------------------------------------------------
    # Get by Blog Post
    # --------------------------------------------------

    def get_by_blog_post(
        self,
        blog_post_id: int
    ) -> list[KnowledgeDocument]:

        statement = (
            select(KnowledgeDocument)
            .where(KnowledgeDocument.blog_post_id == blog_post_id)
        )

        result = self.db.execute(statement)

        return result.scalars().all()

    # --------------------------------------------------
    # Get Pending Documents
    # --------------------------------------------------

    def get_pending_documents(self) -> list[KnowledgeDocument]:

        statement = (
            select(KnowledgeDocument)
            .where(
                KnowledgeDocument.embedding_status ==
                EmbeddingStatus.PENDING
            )
        )

        result = self.db.execute(statement)

        return result.scalars().all()

    # --------------------------------------------------
    # Create Document
    # --------------------------------------------------

    def create_document(
        self,
        title: str,
        content: str,
        source_type: SourceType,
        blog_post_id: int | None = None,
    ) -> KnowledgeDocument:

        document = KnowledgeDocument(
            blog_post_id=blog_post_id,
            title=title,
            content=content,
            source_type=source_type,
        )

        self.db.add(document)

        self.db.commit()

        self.db.refresh(document)

        return document

    # --------------------------------------------------
    # Get or Create
    # --------------------------------------------------

    def get_or_create(
        self,
        title: str,
        content: str,
        source_type: SourceType,
        blog_post_id: int | None = None,
    ) -> KnowledgeDocument:

        statement = (
            select(KnowledgeDocument)
            .where(
                KnowledgeDocument.title == title,
                KnowledgeDocument.blog_post_id == blog_post_id
            )
        )

        result = self.db.execute(statement)

        document = result.scalar_one_or_none()

        if document:
            return document

        return self.create_document(
            title=title,
            content=content,
            source_type=source_type,
            blog_post_id=blog_post_id,
        )

    # --------------------------------------------------
    # Mark as Embedded
    # --------------------------------------------------

    def mark_as_embedded(
        self,
        document: KnowledgeDocument
    ) -> KnowledgeDocument:

        document.embedding_status = EmbeddingStatus.COMPLETED
        document.indexed_at = datetime.utcnow()

        self.db.commit()

        self.db.refresh(document)

        return document

    # --------------------------------------------------
    # Delete Document
    # --------------------------------------------------

    def delete_document(
        self,
        document: KnowledgeDocument
    ) -> None:

        self.db.delete(document)

        self.db.commit()