from sqlalchemy import select, func
from src.resumes.models import EmployerModel
from src.database.database import async_session_factory
from src.resumes.schemas import EmployersRespSchema



class EmployersORM:
    @staticmethod
    async def get_all_employer(
            words_list: list,
            work_experience: int = 0,
            expected_salary_from: int = 0,
            expected_salary_to: int = 1_000_000_000,
            city: str = ""
    ):
        async with async_session_factory() as session:
            query = (select(EmployerModel)
                     .filter(EmployerModel.work_experience >= work_experience)
                     .filter(EmployerModel.expected_salary >= expected_salary_from)
                     .filter(EmployerModel.expected_salary <= expected_salary_to)
                     .filter(EmployerModel.city.like(f"%{city}%"))
                     )
            if words_list:
                vector = func.to_tsvector("russian", EmployerModel.job_name + " " + EmployerModel.description)
                vector_query = func.plainto_tsquery("russian", " ".join(words_list))
                query = query.filter(vector.op('@@')(vector_query))
            employer = await session.execute(query)
            employer = employer.scalars().all()
            result_dto = [EmployersRespSchema.model_validate(row, from_attributes=True).model_dump() for row in
                          employer]
            return result_dto

    @staticmethod
    async def insert_employer(
            name_employer: str,
            job_name: str,
            description: str,
            experience: int,
            education: str,
            salary: int,
            city: str,
            phone_number: str,
            email: str
    ):
        async with async_session_factory() as session:
            employer = EmployerModel(
                name=name_employer,
                job_name=job_name,
                description=description,
                education=education,
                experience=experience,
                salary=salary,
                city=city,
                phone_number=phone_number,
                email=email
            )
            session.add(employer)
            await session.commit()