from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud_api.database.dependencies import get_db
from crud_api.service.database import initialization

router = APIRouter()


@router.post("initialize-database")
def initialize_database(db: Session = Depends(get_db)) -> None:
    return initialization(db)
