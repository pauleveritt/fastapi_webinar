from pydantic import BaseModel


class Hero(BaseModel):
    id: int
    name: str


heroes = [
    Hero(id=0, name="Deadpond"),
    Hero(id=1, name="Rusty-Man"),
    Hero(id=2, name="Spider-Girl")
]
