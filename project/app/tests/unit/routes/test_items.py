from app.src.repositories.items_repository import ItemsRepository
import uuid


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
