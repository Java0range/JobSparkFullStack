from pydantic import BaseModel


class ResumesRespSchema(BaseModel):
    id: int
    name: str
    surname: str
    job_name: str
    experience: int
    expected_salary: int
    city: str