from database.repositories.knowledge_document_repository import (
    KnowledgeDocumentRepository
)


class KnowledgeDocumentService:

    def __init__(self, db):
        self.knowledge_repo = KnowledgeDocumentRepository(db)

    def create_document(
        self,
        title: str,
        content: str,
        source_type,
        blog_post_id: int | None = None
    ):
        """
        Create a knowledge document from scraped/application data.
        """

        document = self.knowledge_repo.create_document(
            title=title,
            content=content,
            source_type=source_type,
            blog_post_id=blog_post_id
        )

        return document