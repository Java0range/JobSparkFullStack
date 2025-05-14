from pydantic import BaseModel
from src.auth.schemas import UserResponseSchema


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


class CreateEmployerSchema(BaseModel):
    name: str
    salary: int
    work_experience: int
    remotely: bool
    description: str
    city: str
    phone_number: str
    email: str
    telegram_username: str