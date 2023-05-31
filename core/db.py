from sqlalchemy import create_engine, Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

engine: Engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_size=10, max_overflow=10
)

SessionLocal: sessionmaker = sessionmaker(
    bind=engine, autoflush=False, autocommit=False
)

Base = declarative_base()


def get_db_session():
    session = SessionLocal()
    try:
        yield session
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
