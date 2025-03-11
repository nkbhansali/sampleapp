from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, Flight
from .database import SQLALCHEMY_DATABASE_URL
from datetime import datetime

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database tables
Base.metadata.create_all(bind=engine)

# Insert dummy data
def add_dummy_data():
    db = SessionLocal()
    dummy_flights = [
        Flight(
            flight_no="AA123",
            scheduled_departure=datetime.strptime("2023-10-01 08:00:00", "%Y-%m-%d %H:%M:%S"),
            scheduled_arrival=datetime.strptime("2023-10-01 12:00:00", "%Y-%m-%d %H:%M:%S"),
            departure_airport="JFK",
            arrival_airport="LAX",
            status="On Time",
            aircraft_code="A320",
            airlines_name="American Airlines"  # New field
        ),
        Flight(
            flight_no="BA456",
            scheduled_departure=datetime.strptime("2023-10-02 09:00:00", "%Y-%m-%d %H:%M:%S"),
            scheduled_arrival=datetime.strptime("2023-10-02 13:00:00", "%Y-%m-%d %H:%M:%S"),
            departure_airport="LHR",
            arrival_airport="JFK",
            status="Delayed",
            aircraft_code="B747",
            airlines_name="British Airways"  # New field
        ),
        Flight(
            flight_no="CA789",
            scheduled_departure=datetime.strptime("2023-10-03 10:00:00", "%Y-%m-%d %H:%M:%S"),
            scheduled_arrival=datetime.strptime("2023-10-03 14:00:00", "%Y-%m-%d %H:%M:%S"),
            departure_airport="PEK",
            arrival_airport="SFO",
            status="Cancelled",
            aircraft_code="B777",
            airlines_name="China Airlines"  # New field
        )
    ]
    db.add_all(dummy_flights)
    db.commit()
    db.close()

add_dummy_data()
