from fastapi import FastAPI
from app.database import engine
# from app import schema  # Your models


# Create DB tables (you'll replace this with Alembic later)
# schema.Base.metadata.create_all(bind=engine)


app = FastAPI()


@app.get("/")
def root():
    return {"message": "CatalystAI backend is running 🎯"}
