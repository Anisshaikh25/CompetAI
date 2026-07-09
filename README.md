# CompetiAI

AI-Powered Competitive Intelligence Platform using Selenium, PostgreSQL, RAG, Gemini, and Streamlit.

## Features

- Competitor Monitoring
- Product Tracking
- AI Chatbot
- RAG
- Dashboard
- Change Detection

                                    +----------------------+
                                    |     Competitor       |
                                    +----------------------+
                                    | id (PK)              |
                                    | name                |
                                    | website             |
                                    | category            |
                                    | description         |
                                    | is_active           |
                                    | created_at          |
                                    +----------+----------+
                                               |
                              One Competitor has Many Products
                                               |
                                               |
                                    +----------v----------+
                                    |      Product        |
                                    +---------------------+
                                    | id (PK)             |
                                    | competitor_id (FK)  |
                                    | name                |
                                    | product_url         |
                                    | sku                |
                                    | category           |
                                    | brand              |
                                    | image_url          |
                                    | is_active          |
                                    | created_at         |
                                    +----------+----------+
                                               |
                          One Product has Many Daily Snapshots
                                               |
                                               |
                                    +----------v-----------+
                                    |  ProductSnapshot     |
                                    +----------------------+
                                    | id (PK)              |
                                    | product_id (FK)      |
                                    | price               |
                                    | rating              |
                                    | reviews_count       |
                                    | availability        |
                                    | discount            |
                                    | scraped_at          |
                                    +----------+----------+
                                               |
                                One Snapshot creates One Change Record
                                               |
                                               |
                                    +----------v----------+
                                    |    PriceChange      |
                                    +---------------------+
                                    | id (PK)             |
                                    | snapshot_id (FK)    |
                                    | previous_price      |
                                    | current_price       |
                                    | price_difference    |
                                    | percentage_change   |
                                    | change_type         |
                                    | created_at          |
                                    +---------------------+



Competitor
      |
      | One Competitor has Many Blogs
      |
      v
+----------------------+
|      BlogPost        |
+----------------------+
| id (PK)              |
| competitor_id (FK)   |
| title                |
| blog_url             |
| published_date       |
| content              |
| scraped_at           |
+----------+-----------+
           |
           | One Blog has One AI Summary
           |
           v
+----------------------+
|    BlogSummary       |
+----------------------+
| id (PK)              |
| blog_id (FK)         |
| summary              |
| keywords             |
| created_at           |
+----------------------+



+----------------------+
|    SchedulerRun      |
+----------------------+
| id (PK)              |
| start_time           |
| end_time             |
| status               |
| products_scraped     |
| blogs_scraped        |
| errors               |
+----------------------+



+----------------------+
|    RAGDocument       |
+----------------------+
| id (PK)              |
| source_type          |
| source_id            |
| chunk_text           |
| embedding_id         |
| created_at           |
+----------------------+



+----------------------+
|    ChatHistory       |
+----------------------+
| id (PK)              |
| question             |
| answer               |
| response_time        |
| created_at           |
+----------------------+