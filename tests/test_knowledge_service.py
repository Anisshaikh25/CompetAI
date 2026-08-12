from database.db import SessionLocal
from database.repositories.blog_repository import BlogPostRepository
from services.knowledge_service import KnowledgeDocumentService
from enums import SourceType


db = SessionLocal()

try:

    blog_repo = BlogPostRepository(db)

    blog = blog_repo.get_by_url(
        "https://example.com/blog/ai-ecommerce-service-test"
    )

    if not blog:
        print("Blog not found.")
        exit()

    knowledge_service = KnowledgeDocumentService(db)

    document = knowledge_service.create_document(
        title=blog.title,
        content=blog.content,
        source_type=SourceType.BLOG,
        blog_post_id=blog.id
    )

    print("Knowledge document created successfully!")
    print("ID:", document.id)
    print("Title:", document.title)
    print("Source:", document.source_type)
    print("Embedding Status:", document.embedding_status)
    print("Blog Post ID:", document.blog_post_id)

finally:
    db.close()