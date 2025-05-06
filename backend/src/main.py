from flask import Flask
from flask_cors import CORS
from asyncio import run
from src.auth.router import blueprint as auth_blueprint
from src.resumes.router import blueprint as resumes_blueprint
from src.queries.orm import AsyncORM


async def main():
    await AsyncORM.create_tables()
    await AsyncORM.insert_root()
    await AsyncORM.insert_resume()


app = Flask(__name__)
# CORS(app, supports_credentials=True, origins=["http://localhost:5173"])
app.register_blueprint(auth_blueprint)
app.register_blueprint(resumes_blueprint)


if __name__ == '__main__':
    run(main())
    app.run(debug=True, port=5000)