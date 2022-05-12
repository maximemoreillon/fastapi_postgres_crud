from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
from os import environ

load_dotenv()

POSTGRES_USERNAME = environ.get('POSTGRES_USERNAME', 'postgres')
POSTGRES_PASSWORD = environ.get('POSTGRES_PASSWORD', 'postgres')
POSTGRES_HOST = environ.get('POSTGRES_HOST', 'localhost')
POSTGRES_DB = environ.get('POSTGRES_DB', 'postgres')

connection_string = f'postgresql+psycopg2://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}'

engine = create_engine(
    connection_string, 
    #connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()