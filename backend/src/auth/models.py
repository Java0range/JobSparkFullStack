from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database.database import BaseModel


class UserModel(BaseModel):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    password: Mapped[str]
    resume: Mapped["ResumesModel"] = relationship()
    employer: Mapped["EmployerModel"] = relationship()