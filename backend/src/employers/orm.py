from sqlalchemy import select, func
from sqlalchemy.orm import selectinload
from src.employers.models import EmployerModel
from src.database.database import async_session_factory
from src.schemas.schemas import EmployersRespSchema



class EmployersORM:
    @staticmethod
    async def get_employers_for_filter(
            words_list: list,
            remotely: bool = False,
            experience_from: int = 0,
            expected_salary_from: int = 0,
            city: str = ""
    ):
        async with async_session_factory() as session:
            query = (select(EmployerModel)
                     .filter(EmployerModel.work_experience >= experience_from)
                     .filter(EmployerModel.salary >= expected_salary_from)
                     .filter(EmployerModel.city.like(f"%{city}%"))
                     .options(selectinload(EmployerModel.user))
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
    async def get_employer_for_id(employer_id: int):
        async with async_session_factory() as session:
            query = (select(EmployerModel)
                     .options(selectinload(EmployerModel.user))
                     .filter(EmployerModel.id == employer_id)
            )
            employer = await session.execute(query)
            employer = employer.scalars().all()
            result_dto = EmployersRespSchema.model_validate(employer[0], from_attributes=True).model_dump()
            return result_dto

    @staticmethod
    async def insert_employer(
            name: str,
            user_id: int,
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
                user_id=user_id,
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