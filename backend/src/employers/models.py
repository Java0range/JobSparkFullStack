from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.auth.models import UserModel
from src.database.database import BaseModel


class EmployerModel(BaseModel):
    __tablename__ = 'employer'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))
    name: Mapped[str]
    salary: Mapped[int]
    work_experience: Mapped[int]
    remotely: Mapped[bool]
    description: Mapped[str]
    phone_number: Mapped[str]
    email: Mapped[str]
    telegram_username: Mapped[str]
    city: Mapped[str]
    user: Mapped["UserModel"] = relationship()