# Start Heroes

Let's start implementing the Heroes tutorial from SQLModel, but first, just as Pydantic models.

- Tests first
  - `read_heroes`, `read_hero`, and `delete_hero`
  - Fail faster on typing and testing
    ```python
    def test_read_heroes(client):
        response = client.get("/heroes/")
        assert response.status_code == 200
    
    
    def test_read_hero(client):
        response = client.get("/heroes/1")
        assert response.status_code == 200
    
    
    def test_delete_heroes(client):
        response = client.delete("/heroes/1")
        assert response.status_code == 200
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
        Hero(id=0, name="Deadpond"),
        Hero(id=1, name="Rusty-Man"),
        Hero(id=2, name="Spider-Girl")
    ]
  
  
    @app.get("/heroes/")
    def read_heroes():
        return heroes
  
  
    @app.get("/heroes/{hero_id}")
    def read_hero(hero_id: int):
        return heroes[hero_id]
  
  
    @app.delete("/heroes/{hero_id}")
    def delete_hero(hero_id: int):
        del heroes[hero_id]
        return dict(ok=True)
  ```
- (SK) Explain the role of `BaseModel`
- Now return to the first test and run just that one...it passes
  - (*) Our tests are a "Smarter" consumer of our code, just like JS
- **USE `fat` Live Template** to add a test for the JSON and another test for direct method: 
  ```python
  def test_read_heroes(client):
      response = client.get("/heroes/")
      heroes = response.json()
      assert response.status_code == 200
      assert len(heroes) == 3
      assert heroes[0]["name"] == "Deadpond"


  def test_read_heroes_direct():
      from main import read_heroes
      from main import Hero
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
    ```
- Use debugger first to simulate confused about dict vs. instance
- But OpenAPI doesn't know what is our response type
- Add to first two endpoints
- Show in `/docs/`
  - (SK) Explain the role of `BaseModel` and `response_model`
- Navigation and usages thanks to type hint on function args
- Add other endpoints and tests
- Refactor Rename Heroes -> Heros
- Undo
- Quick documentation inlay and Endpoints tab for docs
  - (AK) Does this render Google Style Docstrings? 
- Finally, extract model stuff to `models.py`
- How are we doing on `mypy`
  - (*) (SR) Anything special done for FastAPI/SQLModel/mypy?

## Discussion

- (Both) Show how I wish typing and response model worked in test-first
- (SR) Do endpoint-writers care about tests?

## `main.py`

```{literalinclude} main.py
```

## `models.py`

```{literalinclude} models.py
```

## `test_main.http`

```{literalinclude} test_main.http
```

## `tests/test_main.py`

```{literalinclude} test_main.py
```

## `tests/conftest.py`

```{literalinclude} conftest.py
```

