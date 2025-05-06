from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column
from src.database.database import BaseModel


class EmployerModel(BaseModel):
    __tablename__ = 'employer'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    salary: Mapped[int]
    work_experience: Mapped[int]
    remotely: Mapped[bool]
    description: Mapped[str]
    phone_number: Mapped[str]
    email: Mapped[str]
    telegram_username: Mapped[str]
    city: Mapped[str]