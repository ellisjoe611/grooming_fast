from sqlalchemy import create_engine, Engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv
import os

# .env 파일에서 환경변수 불러오기
load_dotenv()
SQLALCHEMY_DATABASE_URL: str = os.getenv("DATABASE_URL")

# DB 엔진 2개 생성 (일반 버전, 비동기 버전)
engine: Engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_size=10, max_overflow=10
)

async_engine: Engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_size=10, max_overflow=10, future=True, echo=True
)


# 세션 생성기 2개 생성 (일반 버전, 비동기 버전)
SessionLocal: sessionmaker[Session] = sessionmaker(
    bind=engine, autoflush=False, autocommit=False, expire_on_commit=False
)

AsyncSessionLocal: sessionmaker[AsyncSession] = sessionmaker(
    bind=async_engine, class_=AsyncSession, autoflush=False, autocommit=False, expire_on_commit=False
)


# SQL Alchemy 상의 Base 클래스
Base = declarative_base()


# DI용 세션 함수 2개 생성 (일반 버전, 비동기 버전)
def get_db_session():
    session: Session = SessionLocal()
    try:
        yield session
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


async def get_async_db_session():
    async with AsyncSessionLocal() as async_session:
        # 비동기 세션 클래스(AsyncSession)의 __aexit__ 함수에 이미 self.close() 함수가 포함됨
        # 따라서 async with 절을 쓰는 동안에는 따로 .close() 함수를 쓸 필요가 없음!
        async with async_session.begin():
            try:
                yield async_session
            except Exception as e:
                await async_session.rollback()
                raise e
