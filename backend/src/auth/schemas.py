from pydantic import BaseModel


class UserResponseSchema(BaseModel):
    id: int
    username: str