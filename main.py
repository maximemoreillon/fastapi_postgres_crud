from fastapi import FastAPI
from psql import SessionLocal, engine
from routers import directors, movies


# from . import crud, models, schemas
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.include_router(directors.router)
app.include_router(movies.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)