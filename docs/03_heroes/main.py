from fastapi import FastAPI

from models import Hero, heroes

app = FastAPI()


@app.get("/heroes/", response_model=list[Hero])
def read_heroes():
    return heroes


@app.get("/heroes/{hero_id}", response_model=Hero)
def read_hero(hero_id: int):
    return heroes[hero_id]


@app.delete("/heroes/{hero_id}")
def delete_hero(hero_id: int):
    del heroes[hero_id]
    return dict(ok=True)
