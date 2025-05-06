from sqlalchemy import select
from src.resumes.models import ResumesModel
from src.database.database import async_session_factory
from src.resumes.schemas import ResumesRespSchema


class ResumeORM:
    @staticmethod
    async def get_resumes_for_filter(
            experience_from: int = 0,
            expected_salary_from: int = 0,
            expected_salary_to: int = 1_000_000_000,
            city: str = ""
    ):
        async with async_session_factory() as session:
            query = (select(ResumesModel)
                     .filter(ResumesModel.experience >= experience_from)
                     .filter(ResumesModel.expected_salary >= expected_salary_from)
                     .filter(ResumesModel.expected_salary <= expected_salary_to)
                     .filter(ResumesModel.city.like(f"%{city}%"))
                     )
            resumes = await session.execute(query)
            resumes = resumes.scalars().all()
            result_dto = [ResumesRespSchema.model_validate(row, from_attributes=True).model_dump() for row in resumes]
            return result_dto

    @staticmethod
    async def insert_resume(
            name: str,
            surname: str,
            job_name: str,
            experience: int,
            expected_salary: int,
            city: str
    ):
        async with async_session_factory() as session:
            resume = ResumesModel(
                name=name,
                surname=surname,
                job_name=job_name,
                experience=experience,
                expected_salary=expected_salary,
                city=city
            )
            session.add(resume)
            await session.commit()