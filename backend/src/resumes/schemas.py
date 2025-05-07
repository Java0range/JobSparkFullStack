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