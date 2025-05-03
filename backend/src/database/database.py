from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from src.config import settings


async_engine = create_async_engine(
    url="sqlite+aiosqlite:///database.db",
    echo=True
)

async_session_factory = async_sessionmaker(async_engine, expire_on_commit=False)


class BaseModel(DeclarativeBase):
    pass