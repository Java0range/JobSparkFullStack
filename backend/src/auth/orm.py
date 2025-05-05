from sqlalchemy import select
from src.auth.models import UserModel
from src.auth.schemas import UserResponseSchema
from src.database.database import async_session_factory
from dataclasses import dataclass
import bcrypt
from passlib.context import CryptContext


@dataclass
class SolveBugBcryptWarning:
    __version__: str = getattr(bcrypt, "__version__")


setattr(bcrypt, "__about__", SolveBugBcryptWarning())


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


async def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


class UsersORM:
    @staticmethod
    async def verify(username, password):
        async with async_session_factory() as session:
            query = select(UserModel).filter_by(username=username)
            user = await session.execute(query)
            user = user.scalars().first()
            if user:
                if user.password:
                    if await verify_password(plain_password=password, hashed_password=user.password):
                        return user.id
            return False

    @staticmethod
    async def insert_user(username, password):
        async with async_session_factory() as session:
            query = select(UserModel).filter_by(username=username)
            users = await session.execute(query)
            users = users.scalars().all()
            if not users:
                hashed_password = await get_password_hash(password)
                user = UserModel(username=username, password=hashed_password)
                session.add(user)
                await session.commit()
                return UserResponseSchema.model_validate(user, from_attributes=True).model_dump()
            else:
                return "Ошибка: Данный username уже занят"

    @staticmethod
    async def get_all_users():
        async with async_session_factory() as session:
            query = select(UserModel).order_by(UserModel.id)
            users = await session.execute(query)
            users = users.scalars().all()
            result_dto = [UserResponseSchema.model_validate(row, from_attributes=True).model_dump() for row in users]
            return result_dto

    @staticmethod
    async def get_user_by_id(user_id: int):
        async with async_session_factory() as session:
            user = await session.get(UserModel, user_id)
            if user:
                user = UserResponseSchema.model_validate(user, from_attributes=True).model_dump()
                print(user)
                return user



    @staticmethod
    async def delete_user(user_id):
        async with async_session_factory() as session:
            user = await session.get(UserModel, user_id)
            if user:
                await session.delete(user)
                await session.commit()