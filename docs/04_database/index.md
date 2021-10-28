# SQLModel for Databases


## Demo

- Install SQLModel by typing in `models.py` `from sqlmodel import SQLModel`
- Make the engine
  ```python
  engine = create_engine(
    "sqlite:///database.db", echo=True,
    connect_args=dict(check_same_thread=False)
  )
  ```
- Add to `models.py`: 
  ```python
  class Hero(SQLModel, table=True):
     id: Optional[int] = Field(default=None, primary_key=True)
  ```
  
- Add to `models.py`:
  ```python
  def create_db_and_tables():
      SQLModel.metadata.create_all(engine)
  ```

- Add to `main.py`:
  ```python
  @app.on_event("startup")
  def on_startup():
      create_db_and_tables()
  ```
- Look, our server generated some output
- DataGrip by double clicking on the .db file
  - It's currently empty
- Mention you might have to download drivers first
- Let's add the sample data to the database
  ```python
  def create_db_and_tables():
      exists = Path("database.db").exists()
      SQLModel.metadata.create_all(engine)
      if exists:
          return
      with Session(engine) as session:
          for hero in heroes:
              session.add(hero)
          session.commit()
  ```
- Convert the endpoints to be driven by the database
- In models.py
  ```python
  def get_session():
    with Session(engine) as session:
        yield session
  ```
- In main.py, remove the import of `heroes`
- Test it in `test_main.http`
- Add a `heroes.js` with:
  ```javascript
  fetch('/heroes/')
  .then(response => response.json())
  .then(data => console.log(data));
  ```
- Review the rest of the code below
- Teleport to other project

## Discussion

## `main.py`

```{literalinclude} main.py
```

## `models.py`

```{literalinclude} models.py
```

## `tests/conftest.py`

```{literalinclude} conftest.py
```

## `tests/test_main.py`

```{literalinclude} test_main.py
```

## `heroes.js`

```{literalinclude} heroes.js
```

