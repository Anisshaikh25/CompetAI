from database.repositories.blog_repository import BlogPostRepository


class BlogService:

    def __init__(self, db):
        self.blog_repo = BlogPostRepository(db)

    def process_blog(
        self,
        competitor_id: int,
        blog_data: dict
    ):
        """
        Process scraped blog data and save it
        using BlogPostRepository.
        """

        blog = self.blog_repo.get_or_create(
            competitor_id=competitor_id,
            title=blog_data["title"],
            url=blog_data["url"],
            author=blog_data.get("author"),
            content=blog_data["content"],
            published_at=blog_data.get("published_at"),
        )

        return blog