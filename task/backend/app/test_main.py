from starlette.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_read_user_usage():
    response = client.get("/user-usage")
    assert response.status_code == 200
    assert len(response.json()) == 151


def test_read_domainX():
    response = client.get("/domain-x")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_read_domainY():
    response = client.get("/domain-y")
    assert response.status_code == 200
    assert len(response.json()) == 151


def test_read_categoriesY():
    response = client.get("/categories-y")
    assert response.status_code == 200
    assert response.json() == 'Client'

