from database.db import SessionLocal

from database.repositories.competitor_repository import CompetitorRepository
from database.repositories.blog_repository import BlogPostRepository

db = SessionLocal()

try:

    competitor_repo = CompetitorRepository(db)
    blog_repo = BlogPostRepository(db)

    competitor = competitor_repo.get_or_create(
        name="Dell",
        website="https://www.dell.com",
        category="Laptop"
    )

    blog = blog_repo.get_or_create(
        competitor_id=competitor.id,
        title="Dell launches new AI laptops",
        url="https://www.dell.com/blog/ai-laptops",
        author="Dell Team",
        content="Dell introduces its latest AI-powered laptops...",
    )

    print(blog)

finally:
    db.close()