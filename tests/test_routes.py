import pytest
from app import create_app
from config import get_config
"""Create your tests"""

# Fixture to create an app with test context
@pytest.fixture
def app(monkeypatch):

    app = create_app(get_config())
    with app.app_context():
        yield app


# Fixture to create a Flask test client
@pytest.fixture
def client(app):
    return app.test_client()


class TestRoutes:

    def test_index(self, client):
        response = client.get('/')

        assert response.status_code == 200
        assert b'Hello World' in response.data
