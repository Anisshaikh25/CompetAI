from database.db import SessionLocal
from database.repositories.competitor_repository import CompetitorRepository
from services.blog_service import BlogService


db = SessionLocal()

try:

    competitor_repo = CompetitorRepository(db)

    competitor = competitor_repo.get_by_name("Dell")

    if not competitor:
        print("Competitor Dell not found.")
        exit()

    blog_service = BlogService(db)

    blog_data = {
        "title": "The Future of AI in E-Commerce",
        "url": "https://example.com/blog/ai-ecommerce-service-test",
        "author": "John Smith",
        "content": (
            "Artificial intelligence is transforming "
            "the e-commerce industry."
        ),
        "published_at": None
    }

    blog = blog_service.process_blog(
        competitor_id=competitor.id,
        blog_data=blog_data
    )

    print("Blog processed successfully!")
    print("ID:", blog.id)
    print("Title:", blog.title)
    print("URL:", blog.url)
    print("Author:", blog.author)
    print("Processed:", blog.is_processed)

finally:
    db.close()