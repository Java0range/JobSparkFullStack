from flask import Flask
from asyncio import run as asyncio_run
from uvicorn import run as uvicorn_run
from src.auth.router import blueprint as auth_blueprint
from asgiref.wsgi import WsgiToAsgi
from src.resumes.router import blueprint as resumes_blueprint
from src.queries.orm import AsyncORM
from flask_cors import CORS


async def main():
    await AsyncORM.create_tables()
    await AsyncORM.insert_root()
    await AsyncORM.insert_resumes()


app = Flask(__name__)

CORS(app, supports_credentials=True, origins=["http://localhost:5173"])

asgi_app = WsgiToAsgi(app)
app.register_blueprint(auth_blueprint)
app.register_blueprint(resumes_blueprint)


if __name__ == '__main__':
    # asyncio_run(main())
    uvicorn_run(asgi_app, host='0.0.0.0', port=5000)
