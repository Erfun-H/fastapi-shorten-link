from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
import os

db_dsn = URL.create(
    "postgresql",
    username=os.getenv("POSTGRES_USER"),
    database=os.getenv("POSTGRES_DB"),
    host=os.getenv("POSTGRES_HOST"),
    password=os.getenv("POSTGRES_PASSWORD"),
    port=os.getenv("POSTGRES_PORT"),
)

engine = create_engine(db_dsn, echo=False, pool_size=100)

SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

def get_db():
    with SessionLocal() as session:
        try:
            yield session
        finally:
            session.close()
