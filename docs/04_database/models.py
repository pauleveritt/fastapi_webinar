from pathlib import Path
from typing import Optional

from sqlmodel import SQLModel, create_engine, Field, Session

engine = create_engine(
    "sqlite:///database.db", echo=True,
    connect_args=dict(check_same_thread=False)
)


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


def create_db_and_tables():
    exists = Path("database.db").exists()
    SQLModel.metadata.create_all(engine)
    if exists:
        return
    with Session(engine) as session:
        for hero in heroes:
            session.add(hero)
        session.commit()


def get_session():
    with Session(engine) as session:
        yield session


heroes = [
    Hero(id=0, name="Deadpond"),
    Hero(id=1, name="Rusty-Man"),
    Hero(id=2, name="Spider-Girl")
]
