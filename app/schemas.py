from pydantic import BaseModel
from datetime import datetime

class Flight(BaseModel):
    flight_id: int
    flight_no: str
    scheduled_departure: datetime
    scheduled_arrival: datetime
    departure_airport: str
    arrival_airport: str
    status: str
    aircraft_code: str
    airlines_name: str  # New field

    class Config:
        orm_mode = True
