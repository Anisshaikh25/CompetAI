from datetime import datetime

from sqlalchemy import select

from models.blog_post import BlogPost
from .base_repository import BaseRepository


class BlogPostRepository(BaseRepository):

    # --------------------------------------------------
    # Get Blog by ID
    # --------------------------------------------------

    def get_by_id(self, blog_id: int) -> BlogPost | None:

        statement = select(BlogPost).where(BlogPost.id == blog_id)

        result = self.db.execute(statement)

        return result.scalar_one_or_none()

    # --------------------------------------------------
    # Get Blog by URL
    # --------------------------------------------------

    def get_by_url(self, url: str) -> BlogPost | None:

        statement = select(BlogPost).where(BlogPost.url == url)

        result = self.db.execute(statement)

        return result.scalar_one_or_none()

    # --------------------------------------------------
    # Get Blogs of a Competitor
    # --------------------------------------------------

    def get_by_competitor(
        self,
        competitor_id: int
    ) -> list[BlogPost]:

        statement = (
            select(BlogPost)
            .where(BlogPost.competitor_id == competitor_id)
            .order_by(BlogPost.published_at.desc())
        )

        result = self.db.execute(statement)

        return result.scalars().all()

    # --------------------------------------------------
    # Get Unprocessed Blogs
    # --------------------------------------------------

    def get_unprocessed_posts(self) -> list[BlogPost]:

        statement = (
            select(BlogPost)
            .where(BlogPost.is_processed.is_(False))
            .order_by(BlogPost.scraped_at.asc())
        )

        result = self.db.execute(statement)

        return result.scalars().all()

    # --------------------------------------------------
    # Create Blog
    # --------------------------------------------------

    def create_blog_post(
        self,
        competitor_id: int,
        title: str,
        url: str,
        content: str,
        author: str | None = None,
        published_at: datetime | None = None,
    ) -> BlogPost:

        blog = BlogPost(
            competitor_id=competitor_id,
            title=title,
            url=url,
            author=author,
            content=content,
            published_at=published_at,
        )

        self.db.add(blog)

        self.db.commit()

        self.db.refresh(blog)

        return blog

    # --------------------------------------------------
    # Get or Create
    # --------------------------------------------------

    def get_or_create(
        self,
        competitor_id: int,
        title: str,
        url: str,
        content: str,
        author: str | None = None,
        published_at: datetime | None = None,
    ) -> BlogPost:

        blog = self.get_by_url(url)

        if blog:
            return blog

        return self.create_blog_post(
            competitor_id=competitor_id,
            title=title,
            url=url,
            content=content,
            author=author,
            published_at=published_at,
        )

    # --------------------------------------------------
    # Mark Processed
    # --------------------------------------------------

    def mark_as_processed(
        self,
        blog: BlogPost
    ) -> BlogPost:

        blog.is_processed = True

        self.db.commit()

        self.db.refresh(blog)

        return blog

    # --------------------------------------------------
    # Delete Blog
    # --------------------------------------------------

    def delete_blog_post(
        self,
        blog: BlogPost
    ) -> None:

        self.db.delete(blog)

        self.db.commit()