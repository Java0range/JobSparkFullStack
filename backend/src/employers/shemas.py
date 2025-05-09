from src.auth.schemas import UserResponseSchema
from pydantic import BaseModel


class EmployersRespSchema(BaseModel):
    id: int
    name: str
    salary: int
    work_experience: int
    remotely: bool
    description: str
    phone_number: str
    email: str
    telegram_username: str
    city: str
    user: UserResponseSchema