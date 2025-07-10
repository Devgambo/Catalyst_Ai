from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from sqlalchemy import text

from .config.database import SessionLocal, engine
from .models import user, document, chat # Import your models

# Create DB tables (you'll replace this with Alembic later)
user.Base.metadata.create_all(bind=engine)
document.Base.metadata.create_all(bind=engine)
chat.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "CatalystAI backend is running 🎯"}

@app.get("/db-check")
def db_check(db: Session = Depends(get_db)):
    try:
        # Try to query the database
        db.execute(text("SELECT 1"))
        return {"message": "Database connection successful"}
    except Exception as e:
        print(e)
        return {"message": f"Database connection failed: {e}"}
