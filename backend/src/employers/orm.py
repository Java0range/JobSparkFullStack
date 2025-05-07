from sqlalchemy import select, func
from src.employers.models import EmployerModel
from src.database.database import async_session_factory
from src.employers.schemas import EmployersRespSchema



class EmployersORM:
    @staticmethod
    async def get_employers_for_filter(
            words_list: list,
            remotely: bool = False,
            experience_from: int = 0,
            expected_salary_from: int = 0,
            expected_salary_to: int = 1_000_000_000,
            city: str = ""
    ):
        async with async_session_factory() as session:
            query = (select(EmployerModel)
                     .filter(EmployerModel.work_experience >= experience_from)
                     .filter(EmployerModel.salary >= expected_salary_from)
                     .filter(EmployerModel.salary <= expected_salary_to)
                     .filter(EmployerModel.city.like(f"%{city}%"))
                     )
            if words_list:
                vector = func.to_tsvector("russian", EmployerModel.name + " " + EmployerModel.description)
                vector_query = func.plainto_tsquery("russian", " ".join(words_list))
                query = query.filter(vector.op('@@')(vector_query))
            if remotely:
                query = query.filter(EmployerModel.remotely == remotely)
            employers = await session.execute(query)
            employers = employers.scalars().all()
            result_dto = [EmployersRespSchema.model_validate(row, from_attributes=True).model_dump() for row in employers]
            return result_dto

    @staticmethod
    async def insert_employer(
            name: str,
            salary: int,
            work_experience: int,
            remotely: bool,
            description: str,
            phone_number: str,
            email: str,
            telegram_username: str,
            city: str
    ):
        async with async_session_factory() as session:
            employer = EmployerModel(
                name=name,
                salary=salary,
                work_experience=work_experience,
                remotely=remotely,
                description=description,
                phone_number=phone_number,
                email=email,
                telegram_username=telegram_username,
                city=city
            )
            session.add(employer)
            await session.commit()