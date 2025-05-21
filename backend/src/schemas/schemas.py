from pydantic import BaseModel
from typing import Optional


class UserEmployerSchema(BaseModel):
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


class UserResumeSchema(BaseModel):
    id: int
    name: str
    surname: str
    job_name: str
    description: str
    education: str
    educational_institution: str
    faculty: str
    experience: int
    expected_salary: int
    city: str
    phone_number: str
    email: str
    telegram_username: str


class UserResponseSchema(BaseModel):
    id: int
    username: str
    resume: Optional[UserResumeSchema] = None
    employer: Optional[UserEmployerSchema] = None


class UserLiteResponseSchema(BaseModel):
    id: int
    username: str


class ResumesRespSchema(BaseModel):
    id: int
    name: str
    surname: str
    job_name: str
    description: str
    education: str
    educational_institution: str
    faculty: str
    experience: int
    expected_salary: int
    city: str
    phone_number: str
    email: str
    telegram_username: str
    user: UserLiteResponseSchema


class CreateResumeSchema(BaseModel):
    city: str
    description: str
    edu_institution: str
    education: str
    email: str
    expected_salary: int
    experience: int
    faculty: str
    job_name: str
    name: str
    phone_number: str
    surname: str
    telegram_username: str


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
    user: UserLiteResponseSchema


class CreateEmployerSchema(BaseModel):
    name: str
    salary: int
    work_experience: int
    remotely: bool | None
    description: str
    city: str
    phone_number: str
    email: str
    telegram_username: str