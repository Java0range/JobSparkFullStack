from src.database.database import async_engine, BaseModel, async_session_factory
from src.auth.orm import UsersORM
from src.resumes.orm import ResumeORM
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

    @staticmethod
    async def insert_resumes():
        await ResumeORM.insert_resume(
            name="Root",
            surname="Toor",
            job_name="Python Backend Developer",
            education="Высшее",
            educational_institution="МГУ",
            faculty="ФКН",
            experience=2,
            expected_salary=200_000,
            city="Москва"
        )
        await ResumeORM.insert_resume(
            name="Root",
            surname="Toor",
            job_name="FastApi Backend Developer",
            education="Высшее",
            educational_institution="ВГУ",
            faculty="ПММ",
            experience=2,
            expected_salary=80_000,
            city="London"
        )