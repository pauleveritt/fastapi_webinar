def test_read_heroes(client):
    response = client.get("/heroes/")
    heroes = response.json()
    assert response.status_code == 200
    assert len(heroes) == 3
    assert heroes[0]["name"] == "Deadpond"


def test_read_heroes_direct():
    from main import read_heroes
    from models import Hero
    heroes: list[Hero] = read_heroes()
    assert len(heroes) == 3
    assert heroes[0].name == "Deadpond"


def test_read_hero(client):
    response = client.get("/heroes/0")
    assert response.status_code == 200
    assert response.json()["name"] == "Deadpond"


def test_delete_heroes(client):
    response = client.delete("/heroes/1")
    assert response.status_code == 200
    assert response.json()["ok"] == True
