import pytest
from starlette.testclient import TestClient

from app.src.main import app


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client
