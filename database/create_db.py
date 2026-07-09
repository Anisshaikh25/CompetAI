from database.db import Base, engine

# Import all models
from database import models

Base.metadata.create_all(bind=engine)

print("Database tables created successfully!")