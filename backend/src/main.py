from flask import Flask
from flask_cors import CORS
from asyncio import run
from src.auth.router import blueprint as auth_blueprint
from src.queries.orm import AsyncORM


async def main():
    await AsyncORM.create_tables()
    await AsyncORM.insert_root()


app = Flask(__name__)
app.register_blueprint(auth_blueprint)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})


if __name__ == '__main__':
    run(main())
    app.run(debug=True)