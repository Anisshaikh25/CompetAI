from database.db import SessionLocal

from database.repositories.competitor_repository import CompetitorRepository
from database.repositories.blog_post_repository import BlogPostRepository
from database.repositories.knowledge_document_repository import (
    KnowledgeDocumentRepository,
)

from enums import SourceType

db = SessionLocal()

try:

    competitor_repo = CompetitorRepository(db)
    blog_repo = BlogPostRepository(db)
    knowledge_repo = KnowledgeDocumentRepository(db)

    competitor = competitor_repo.get_or_create(
        name="Dell",
        website="https://www.dell.com",
        category="Laptop"
    )

    blog = blog_repo.get_or_create(
        competitor_id=competitor.id,
        title="Dell AI Blog",
        url="https://www.dell.com/blog/ai",
        author="Dell Team",
        content="This is a sample blog post."
    )

    document = knowledge_repo.get_or_create(
        title=blog.title,
        content=blog.content,
        source_type=SourceType.BLOG,
        blog_post_id=blog.id
    )

    print(document)

finally:
    db.close()