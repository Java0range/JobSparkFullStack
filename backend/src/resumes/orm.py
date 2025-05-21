from sqlalchemy import select, func
from sqlalchemy.orm import selectinload
from src.resumes.models import ResumesModel
from src.database.database import async_session_factory
from src.schemas.schemas import ResumesRespSchema


class ResumeORM:
    @staticmethod
    async def get_resumes_for_filter(
            words_list: list,
            experience_from: int = 0,
            expected_salary_from: int = 0,
            city: str = ""
    ):
        async with async_session_factory() as session:
            query = (select(ResumesModel)
                     .filter(ResumesModel.experience >= experience_from)
                     .filter(ResumesModel.expected_salary >= expected_salary_from)
                     .filter(ResumesModel.city.like(f"%{city}%"))
                     .options(selectinload(ResumesModel.user))
                     )
            if words_list:
                vector = func.to_tsvector("russian", ResumesModel.job_name + " " + ResumesModel.description)
                vector_query = func.plainto_tsquery("russian", " ".join(words_list))
                query = query.filter(vector.op('@@')(vector_query))
            resumes = await session.execute(query)
            resumes = resumes.scalars().all()
            result_dto = [ResumesRespSchema.model_validate(row, from_attributes=True).model_dump() for row in resumes]
            return result_dto

    @staticmethod
    async def get_resumes_for_id(resume_id: int):
        async with async_session_factory() as session:
            query = (select(ResumesModel)
                     .options(selectinload(ResumesModel.user))
                     .filter(ResumesModel.id == resume_id)
            )
            resume = await session.execute(query)
            resume = resume.scalars().all()
            result_dto = ResumesRespSchema.model_validate(resume[0], from_attributes=True).model_dump()
            return result_dto

    @staticmethod
    async def insert_resume(
            user_id: int,
            name: str,
            surname: str,
            job_name: str,
            description: str,
            experience: int,
            education: str,
            educational_institution: str,
            faculty: str,
            expected_salary: int,
            city: str,
            phone_number: str,
            email: str,
            telegram_username: str
    ):
        async with async_session_factory() as session:
            user_resumes = select(ResumesModel).filter_by(user_id=user_id)
            user_resumes = await session.execute(user_resumes)
            user_resumes = user_resumes.scalars().all()
            if user_resumes:
                return "Error: User Can Have Only One Resume"
            resume = ResumesModel(
                user_id=user_id,
                name=name,
                surname=surname,
                job_name=job_name,
                description=description,
                education=education,
                educational_institution=educational_institution,
                faculty=faculty,
                experience=experience,
                expected_salary=expected_salary,
                city=city,
                phone_number=phone_number,
                email=email,
                telegram_username=telegram_username
            )
            session.add(resume)
            await session.commit()

    @staticmethod
    async def update_resume(
            user_id: int,
            name: str,
            surname: str,
            job_name: str,
            description: str,
            experience: int,
            education: str,
            educational_institution: str,
            faculty: str,
            expected_salary: int,
            city: str,
            phone_number: str,
            email: str,
            telegram_username: str
    ):
        async with async_session_factory() as session:
            query = select(ResumesModel).filter_by(user_id=user_id)
            resume = await session.execute(query)
            resume = resume.scalars().first()
            if name:
                resume.name = name
            if surname:
                resume.surname = surname
            if job_name:
                resume.job_name = job_name
            if description:
                resume.description = description
            if experience != -1:
                resume.experience = experience
            if education:
                resume.education = education
            if educational_institution:
                resume.educational_institution = educational_institution
            if faculty:
                resume.faculty = faculty
            if expected_salary != -1:
                resume.expected_salary = expected_salary
            if city:
                resume.city = city
            if phone_number:
                resume.phone_number = phone_number
            if email:
                resume.email = email
            if telegram_username:
                resume.telegram_username = telegram_username
            await session.commit()