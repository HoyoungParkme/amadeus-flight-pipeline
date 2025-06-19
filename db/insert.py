# db/insert.py

from sqlalchemy import Table, Column, String, Float, MetaData, DateTime
from db.database import engine

metadata = MetaData()

flights = Table(
    "flights", metadata,
    Column("origin", String),
    Column("destination", String),
    Column("departure_at", DateTime),
    Column("arrival_at", DateTime),
    Column("price", Float),
)

metadata.create_all(engine)


def insert_flights(data):
    with engine.begin() as conn:
        conn.execute(flights.insert(), data)
