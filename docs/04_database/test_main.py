from models import Hero


def test_read_heroes(session, client):
    hero_1 = Hero(name="Deadpond")
    hero_2 = Hero(name="Rusty-Man")
    session.add(hero_1)
    session.add(hero_2)
    session.commit()

    response = client.get("/heroes/")
    data = response.json()

    assert response.status_code == 200

    assert len(data) == 2
    assert data[0]["name"] == hero_1.name
    assert data[0]["id"] == hero_1.id
    assert data[1]["name"] == hero_2.name
    assert data[1]["id"] == hero_2.id


def test_read_hero(session, client):
    hero_1 = Hero(name="Deadpond")
    session.add(hero_1)
    session.commit()

    response = client.get(f"/heroes/{hero_1.id}")
    data = response.json()

    assert response.status_code == 200
    assert data["id"] == hero_1.id
    assert data["name"] == hero_1.name


def test_delete_hero(session, client):
    hero_1 = Hero(name="Deadpond")
    session.add(hero_1)
    session.commit()

    response = client.delete(f"/heroes/{hero_1.id}")

    hero_in_db = session.get(Hero, hero_1.id)

    assert response.status_code == 200

    assert hero_in_db is None
