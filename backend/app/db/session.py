from collections.abc import Generator

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker

from backend.app.core.config import get_settings


def build_engine(database_url: str | None = None) -> Engine:
    return create_engine(
        database_url or get_settings().database_url,
        pool_pre_ping=True,
    )


def build_session_factory(database_url: str | None = None) -> sessionmaker[Session]:
    return sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=build_engine(database_url),
        expire_on_commit=False,
    )


engine = build_engine()
SessionLocal = build_session_factory()


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
