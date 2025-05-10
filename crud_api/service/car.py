from typing import List

from sqlalchemy import text
from sqlalchemy.orm import Session

from crud_api.response.car import CarSpecification


def retrieve_car_specification(db: Session) -> List[CarSpecification]:
    response = db.execute(text("SELECT * FROM cars.cars")).fetchall()
    return [CarSpecification(**spec._asdict()) for spec in response]
