from app import app


def test_index_returns_200():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200


def test_index_returns_two_tasks():
    response = app.test_client().get("/")

    assert response.status_code == 200
    assert response.get_json() == [
        {"id": 1, "title": "Estudar Docker"},
        {"id": 2, "title": "Criar o pipeline"},
    ]
    assert len(response.get_json()) == 2
