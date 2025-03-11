from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Flight(Base):
    __tablename__ = "flights"

    flight_id = Column(Integer, primary_key=True, index=True)
    flight_no = Column(String, nullable=False)
    scheduled_departure = Column(TIMESTAMP, nullable=False)
    scheduled_arrival = Column(TIMESTAMP, nullable=False)
    departure_airport = Column(String, nullable=False)
    arrival_airport = Column(String, nullable=False)
    status = Column(String, nullable=False)
    aircraft_code = Column(String, nullable=False)
    airlines_name = Column(String, nullable=False)  # New field
