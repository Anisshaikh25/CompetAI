from enum import Enum


class SourceType(str, Enum):
    BLOG = "BLOG"
    PRODUCT = "PRODUCT"
    FAQ = "FAQ"
    NEWS = "NEWS"


class EmbeddingStatus(str, Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class PriceChangeType(str, Enum):
    INCREASE = "INCREASE"
    DECREASE = "DECREASE"
    NO_CHANGE = "NO_CHANGE"


class JobStatus(str, Enum):
    RUNNING = "RUNNING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


class JobType(str, Enum):
    PRODUCT_SCRAPER = "PRODUCT_SCRAPER"
    BLOG_SCRAPER = "BLOG_SCRAPER"
    RAG_INDEXING = "RAG_INDEXING"
    NOTIFICATION = "NOTIFICATION"