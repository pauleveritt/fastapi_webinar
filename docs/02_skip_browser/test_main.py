def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Hello World" == response.json()["message"]


def test_say_hello(client):
    response = client.get("/hello/User")
    assert response.status_code == 200
    assert "Hello User" == response.json()["message"]
