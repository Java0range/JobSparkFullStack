from sqlalchemy.orm import Mapped, mapped_column
from src.database.database import BaseModel


class UserModel(BaseModel):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    password: Mapped[str]
    # resumes
    # vacancy