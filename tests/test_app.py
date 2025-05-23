import pytest

from app import *


@pytest.fixture()
def app():
    app = create_app()

    app.config.update({
        "TESTING": True,
    })
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_request_example(client):
    response = client.get("/hello")

    assert "Hello World!" in response.text
