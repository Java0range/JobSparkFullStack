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
            user_employers = select(EmployerModel).filter_by(user_id=user_id)
            user_employer = await session.execute(user_employers)
            user_employer = user_employer.scalars().all()
            if user_employer:
                return "Error: User Can Have Only One Employer"
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

    @staticmethod
    async def update_employer(
            name: str,
            user_id: int,
            salary: int,
            work_experience: int,
            remotely: bool | None,
            description: str,
            phone_number: str,
            email: str,
            telegram_username: str,
            city: str
    ):
        async with async_session_factory() as session:
            query = select(EmployerModel).filter_by(user_id=user_id)
            employer = await session.execute(query)
            employer = employer.scalars().first()
            if name:
                employer.name = name
            if salary != -1:
                employer.salary = salary
            if work_experience != -1:
                employer.work_experience = work_experience
            if remotely is not None:
                employer.remotely = remotely
            if description:
                employer.description = description
            if city:
                employer.city = city
            if phone_number:
                employer.phone_number = phone_number
            if email:
                employer.email = email
            if telegram_username:
                employer.telegram_username = telegram_username
            await session.commit()