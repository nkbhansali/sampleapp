from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Flight])
def read_flights(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    flights = db.query(models.Flight).offset(skip).limit(limit).all()
    return flights
