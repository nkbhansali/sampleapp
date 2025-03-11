import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.init_db import add_dummy_data
from app.database import SessionLocal, engine
from app.models import Base

# Create a TestClient
client = TestClient(app)

# Set up the database for testing
@pytest.fixture(scope="module")
def setup_database():
    Base.metadata.drop_all(bind=engine)  # Clear the database
    Base.metadata.create_all(bind=engine)
    add_dummy_data()
    yield
    Base.metadata.drop_all(bind=engine)

def test_read_flights(setup_database):
    response = client.get("/flights/")
    assert response.status_code == 200
    assert len(response.json()) == 3
    assert response.json()[0]["flight_no"] == "AA123"
    assert response.json()[1]["flight_no"] == "BA456"
    assert response.json()[2]["flight_no"] == "CA789"
