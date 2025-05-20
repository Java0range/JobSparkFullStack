from flask import Blueprint, make_response, request, Request, abort, Response
from src.auth.orm import UsersORM
from src.auth.dependencies import get_access_token, get_refresh_token, get_user_id
from src.auth.AuthJWT import security
from re import search


blueprint = Blueprint("Auth & Users", __name__, url_prefix="/users")



async def username_validate(username: str):
    if not username.isalnum():
        return "Ошибка: Username должен содержать только буквы (включая кириллические) и цифры"
    if len(username) < 4:
        return "Ошибка: Username не может быть короче 4 символов"
    if len(username) > 24:
        return "Ошибка: Username не может быть длиннее 24 символов"
    return True


async def password_validate(password: str):
    if not password.isalnum():
        return "Ошибка: Пароль должен содержать только буквы (включая кириллические) и цифры"
    if search('[0-9]',password) is None:
        return "Ошибка: Пароль должен содержать хотя-бы одну цифру"
    if search('[A-Z]',password) is None:
        return "Ошибка: Пароль должен содержать хотя-бы одну заглавную букву"
    if len(password) < 8:
        return "Ошибка: Пароль не может быть короче 8 символов"
    if len(password) > 36:
        return "Ошибка: Пароль не может быть длиннее 24 символов"
    return True


async def check_user_auth(request_cookies: Request):
    access_token = await get_access_token(request_cookies)
    user_id = security.check_access_token(access_token=access_token)
    if "Error" in user_id:
        abort(401, message=user_id)
    return True


@blueprint.route("/login", methods=["POST"])
async def login_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    user_id = await UsersORM.verify(username=username, password=password)
    if user_id is False:
        abort(Response("Неверный username или пароль", 401))
    user = await UsersORM.get_user_by_id(user_id)
    res = make_response(user)
    res.set_cookie(
        key="access_token",
        value=security.create_access_token(user_id=user_id),
        httponly=True,
        max_age=1800
    )
    res.set_cookie(
        key="refresh_token",
        value=security.create_refresh_token(user_id=user_id),
        httponly=True,
        max_age=604800
    )
    return res



@blueprint.route("/registration", methods=["POST"])
async def registration():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    username_is_valid = await username_validate(username)
    if not username_is_valid is True:
        abort(Response(username_is_valid, 406))
    password_is_valid = await password_validate(password)
    if not password_is_valid is True:
        abort(Response(password_is_valid, 406))
    create_user_ans = await UsersORM.insert_user(username=username, password=password)
    if create_user_ans is str:
        if "Ошибка" in create_user_ans:
            abort(Response(create_user_ans, 406))
    res = make_response(create_user_ans)
    res.set_cookie(
        key="access_token",
        value=security.create_access_token(user_id=create_user_ans["id"]),
        httponly=True,
        max_age=1800
    )
    res.set_cookie(
        key="refresh_token",
        value=security.create_refresh_token(user_id=create_user_ans["id"]),
        httponly=True,
        max_age=604800
    )
    return res


@blueprint.route("/logout", methods=["POST"])
async def logout_user():
    res = make_response()
    res.delete_cookie(key="access_token")
    res.delete_cookie(key="refresh_token")
    return res


@blueprint.route("/refresh", methods=["POST"])
async def update_refresh_token():
    refresh_token = await get_refresh_token(request)
    res = make_response()
    res.set_cookie(
        key="access_token",
        value=security.check_refresh_token(refresh_token=refresh_token),
        httponly=True,
        max_age=1800
    )
    return res


@blueprint.route("/is-auth", methods=["POST"])
async def is_auth_user():
    user_id = await get_user_id(request)
    user = await UsersORM.get_user_by_id(user_id)
    json = {
        "auth": await check_user_auth(request),
        "user": user
    }
    return json