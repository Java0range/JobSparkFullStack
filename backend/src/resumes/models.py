from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column
from src.database.database import BaseModel


class ResumesModel(BaseModel):
    __tablename__ = 'resumes'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    surname: Mapped[str]
    job_name: Mapped[str]
    description: Mapped[str]
    education: Mapped[str]
    educational_institution: Mapped[str]
    faculty: Mapped[str]
    experience: Mapped[int]
    expected_salary: Mapped[int]
    city: Mapped[str]
    phone_number: Mapped[str]
    email: Mapped[str]
    telegram_username: Mapped[str]