from typing import List

from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from crud_api.database.dependencies import get_db
from crud_api.response.car import CarSpecification
from crud_api.service.car import retrieve_car_specification

router = APIRouter()


@router.get("/car-specification", response_model=List[CarSpecification])
def get_car_specification(request: Request, db: Session = Depends(get_db)) -> List[CarSpecification]:
    return retrieve_car_specification(db)
