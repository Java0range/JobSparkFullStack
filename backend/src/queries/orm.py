from src.database.database import async_engine, BaseModel
from src.auth.orm import UsersORM
from src.resumes.orm import ResumeORM
from src.employers.orm import EmployersORM



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
            description="A Python Backend Developer",
            education="Высшее",
            educational_institution="МГУ",
            faculty="ФКН",
            experience=2,
            expected_salary=200_000,
            city="Москва",
            phone_number="89003015099",
            email="",
            telegram_username="@username"
        )
        await ResumeORM.insert_resume(
            name="Root",
            surname="Toor",
            job_name="FastApi Backend Developer",
            description="A FastAPI Python Backend Developer",
            education="Высшее",
            educational_institution="ВГУ",
            faculty="ПММ",
            experience=2,
            expected_salary=80_000,
            city="London",
            phone_number="89004033340",
            email="obmanaNet@main.ru",
            telegram_username=""
        )

    @staticmethod
    async def insert_employers():
        await EmployersORM.insert_employer(
            name="Python Backend Developer",
            user_id=1,
            salary=350_000,
            work_experience=3,
            remotely=True,
            description="Нам нужен fastapi backend developer",
            phone_number="89777777777",
            email="obmanaNet@mail.ru",
            telegram_username="",
            city="Москва"
        )
        await EmployersORM.insert_employer(
            name="Backend Developer",
            user_id=1,
            salary=80_000,
            work_experience=3,
            remotely=True,
            description="Нам нужен python backend developer",
            phone_number="89777777777",
            email="razwodka@mail.ru",
            telegram_username="@razwodka",
            city="Воронеж"
        )