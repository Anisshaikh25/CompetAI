# 🚀 CompetAI – AI-Powered Competitive Intelligence Platform

CompetAI is an AI-powered competitive intelligence platform that automatically monitors competitor websites, tracks daily product and price changes, summarizes competitor blogs using Large Language Models (LLMs), and enables intelligent question answering using Retrieval-Augmented Generation (RAG).

The platform helps businesses stay informed about competitor pricing, product launches, and content strategy through automated data collection and AI-powered insights.

---

## 📌 Features

- 🔍 Automated competitor website monitoring
- 💻 Dynamic web scraping using Selenium
- 💰 Daily product price tracking
- 📈 Historical price comparison and trend analysis
- 📰 Competitor blog scraping
- 🤖 AI-powered blog summarization using Google Gemini
- 🧠 RAG-based intelligent chatbot for querying competitor data
- 📊 PostgreSQL database for structured data storage
- ⏰ Automated scheduling for periodic scraping
- 📉 Dashboard for competitive analytics and insights

---

# 🏗️ System Architecture

```text
                    Competitor Websites
                            │
                            ▼
                  Selenium Web Scraper
                            │
            ┌───────────────┴───────────────┐
            ▼                               ▼
      Product Data                    Blog Data
            │                               │
            ▼                               ▼
     PostgreSQL Database          Gemini AI Summarizer
            │                               │
            └───────────────┬───────────────┘
                            ▼
                     RAG Knowledge Base
                            │
                            ▼
                   AI Chat & Dashboard
```

---

# 🗄️ Database Design

```text
Competitor
     │
     ├──────────────┐
     │              │
     ▼              ▼
 Product       BlogPost
     │              │
     ▼              ▼
ProductSnapshot  BlogSummary
     │
     ▼
PriceChange

SchedulerRun

RAGDocument

ChatHistory

ScrapingTarget
```

---

# 🛠️ Tech Stack

## Backend
- Python
- FastAPI

## Web Scraping
- Selenium
- BeautifulSoup

## Database
- PostgreSQL
- SQLAlchemy ORM

## Artificial Intelligence
- Google Gemini API
- Retrieval-Augmented Generation (RAG)
- FAISS Vector Store

## Scheduling
- APScheduler

## Data Processing
- Pandas

## Version Control
- Git
- GitHub

---

# 📂 Project Structure

```text
CompetAI/
│
├── config/
├── data/
├── database/
│   ├── create_db.py
│   ├── crud.py
│   ├── db.py
│   ├── models.py
│   └── __init__.py
│
├── detector/
├── docs/
├── logs/
├── scraper/
├── scheduler/
├── rag/
├── api/
├── dashboard/
│
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

---

# ⚙️ Installation

## Clone the repository

```bash
git clone https://github.com/your-username/CompetAI.git
```

```bash
cd CompetAI
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file.

```env
DATABASE_URL=postgresql+psycopg://username:password@localhost:5432/competiai_db

GEMINI_API_KEY=your_api_key

EMAIL_USER=your_email@gmail.com

EMAIL_PASSWORD=your_app_password
```

---

## Run Database Setup

```bash
python -m database.create_db
```

---

# 📊 Current Development Progress

| Module | Status |
|----------|--------|
| Project Setup | ✅ Completed |
| PostgreSQL Integration | ✅ Completed |
| SQLAlchemy ORM | ✅ Completed |
| Competitor Model | ✅ Completed |
| Product Model | ✅ Completed |
| Product Snapshot Module | 🚧 In Progress |
| Price Change Detection | ⏳ Planned |
| Selenium Scraper | ⏳ Planned |
| Scheduler | ⏳ Planned |
| Blog Scraper | ⏳ Planned |
| Gemini Integration | ⏳ Planned |
| RAG Chatbot | ⏳ Planned |
| Dashboard | ⏳ Planned |
| Deployment | ⏳ Planned |

---

# 🎯 Learning Outcomes

This project demonstrates practical experience with:

- Relational Database Design
- SQLAlchemy ORM
- PostgreSQL
- FastAPI Backend Development
- Selenium Web Automation
- AI Integration with Gemini
- Retrieval-Augmented Generation (RAG)
- Vector Databases
- Background Task Scheduling
- Scalable Backend Architecture

---

# 🚀 Future Enhancements

- Multi-competitor support
- Product availability tracking
- Email alerts for price changes
- Dashboard analytics
- Authentication & Authorization
- REST API
- Docker Support
- Cloud Deployment (AWS/GCP/Azure)
- Redis Caching
- CI/CD Pipeline

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

# 📄 License

This project is intended for educational and portfolio purposes.

---

# 👨‍💻 Author

**Anis Shaikh**

Aspiring AI Engineer | Data Analyst | Backend Developer
