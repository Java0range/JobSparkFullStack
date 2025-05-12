from pydantic import BaseModel


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