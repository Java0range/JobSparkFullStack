import pytest
from src.main import app as flask_app
from asyncio import run
from src.queries.orm import AsyncORM


async def main():
    await AsyncORM.create_tables()
    await AsyncORM.insert_root()


@pytest.fixture
def app():
    app = flask_app
    app.config.update({
        'TESTING': True,
    })
    run(main())
    yield app


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()
