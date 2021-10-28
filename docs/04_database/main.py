from fastapi import FastAPI, Depends
from sqlmodel import Session, select

from models import Hero, create_db_and_tables, get_session

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/heroes/", response_model=list[Hero])
def read_heroes(session: Session = Depends(get_session)):
    heroes = session.exec(select(Hero)).all()
    return heroes


@app.get("/heroes/{hero_id}", response_model=Hero)
def read_hero(*, session: Session = Depends(get_session), hero_id: int):
    hero = session.get(Hero, hero_id)
    return hero


@app.delete("/heroes/{hero_id}")
def delete_hero(*, session: Session = Depends(get_session), hero_id: int):
    hero = session.get(Hero, hero_id)
    session.delete(hero)
    session.commit()
    return {"ok": True}
