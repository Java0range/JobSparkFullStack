from flask import Flask
from asyncio import run
from src.auth.router import blueprint as auth_blueprint
from src.queries.orm import AsyncORM


async def main():
    await AsyncORM.create_tables()
    await AsyncORM.insert_root()



app = Flask(__name__)
app.register_blueprint(auth_blueprint)


if __name__ == '__main__':
    run(main())
    app.run(debug=True)