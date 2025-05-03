from src.database.database import async_engine, BaseModel, async_session_factory
from src.auth.orm import UsersORM
from src.auth.models import UserModel


class AsyncORM:
    @staticmethod
    async def create_tables():
        async with async_engine.begin() as conn:
            await conn.run_sync(BaseModel.metadata.drop_all)
            await conn.run_sync(BaseModel.metadata.create_all)

    @staticmethod
    async def insert_root():
        await UsersORM.insert_user(username='root', password='toor')