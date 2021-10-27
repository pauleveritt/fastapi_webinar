# Start Heroes

Let's start implementing the Heroes tutorial from SQLModel, but first, just as Pydantic models.

- Tests first
  - `read_heroes`, `read_hero`, and `delete_hero`
  - Fail faster on typing and testing
    ```python
    def test_read_heroes(client):
        response = client.get("/heroes/")
        assert response.status_code == 200
        # assert "Hello World" == response.json()["message"]
    
    
    def test_read_hero(client):
        response = client.get("/heroes/1")
        assert response.status_code == 200
        # assert "Hello World" == response.json()["message"]
    
    
    def test_delete_heroes(client):
        response = client.delete("/heroes/1")
        assert response.status_code == 200
        # assert "Hello World" == response.json()["message"] 
    ```
- As expected, tests fail
- Ditto for `.http`
- In `main.py`...
  - Delete two endpoints
  - Add some heroes and endpoints
    ```python
    class Hero(BaseModel):
      id: int
      name: str
  
  
    heroes = [
      Hero(id=1, name="Deadpond"),
      Hero(id=2, name="Rusty-Man"),
      Hero(id=1, name="Spider-Girl"),
  ]
  ```
- response_model with type hint in test
- Use debugger first to simulate confused
- Navigation and usages thanks to type hint on function args
- Heros -> Heroes
  - Refactor symbol name and type annotations
  - Including in Google Doc String
- Quick documentation inlay and Endpoints tab for docs
