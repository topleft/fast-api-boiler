import json
import uuid

from app.src.repositories.items_repository import ItemsRepository


def override_get_db():
    pass


def test_get_items(test_app, monkeypatch):
    test_data = [{"id": str(uuid.uuid4()), "name": "something", "created_at": "2020-11-02", "updated_at": "2020-11-02"}]

    def mock_get_all(self):
        return test_data

    monkeypatch.setattr(ItemsRepository, "get_all", mock_get_all)

    response = test_app.get("/items")
    assert response.status_code == 200
    assert response.json() == test_data


def test_get_single_item(test_app, monkeypatch):
    id = str(uuid.uuid4())
    test_data = {"id": id, "name": "something", "created_at": "2020-11-02", "updated_at": "2020-11-02"}

    def mock_get_one(self, id):
        return test_data

    monkeypatch.setattr(ItemsRepository, "get_one", mock_get_one)

    response = test_app.get(f"/items/{id}")
    assert response.status_code == 200
    assert response.json() == test_data


def test_post_item_invalid_json(test_app):
    response = test_app.post("/items", data=json.dumps({"wrong": "something"}))
    assert response.status_code == 422


def test_post_item(test_app, monkeypatch):
    test_data = {"id": str(uuid.uuid4()), "name": "something", "created_at": "2020-11-02", "updated_at": "2020-11-02"}

    def mock_add(self, data):
        return test_data

    monkeypatch.setattr(ItemsRepository, "add", mock_add)

    response = test_app.post("/items", data=json.dumps({"name": "something"}))
    assert response.status_code == 200
    assert response.json() == test_data
