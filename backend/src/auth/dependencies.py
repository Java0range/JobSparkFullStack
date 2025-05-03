from src.auth.AuthJWT import security
from flask import abort, Response, Request


async def get_access_token(request: Request):
    access_token = request.cookies.get('access_token')
    if not access_token:
        abort(Response("Invalid access token", 401))
    return access_token


async def get_refresh_token(request: Request):
    refresh_token = request.cookies.get('refresh_token')
    if not refresh_token:
        abort(Response("Invalid refresh token", 401))
    return refresh_token


async def get_user_id(request: Request) -> int:
    access_token = request.cookies.get('access_token')
    if not access_token:
        abort(Response("Invalid access token", 401))
    user_id = security.check_access_token(access_token)
    if "Error" in user_id:
        abort(Response(user_id, 401))
    return int(user_id)