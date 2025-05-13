from fastapi import FastAPI

from crud_api import settings
from crud_api.controller.car import router as car_router
from crud_api.controller.database import router as database_router
from crud_api.controller.swagger import router as swagger_router
from crud_api.utils.constant import swagger_tags

def create_api() -> FastAPI:
    """This function is creating a new fastapi instance"""
    api = FastAPI(
        title=settings.api_name,
        version=settings.api_version,
        openapi_tags=swagger_tags,
        docs_url=None
    )

    api.include_router(car_router)
    api.include_router(database_router)
    api.include_router(swagger_router)

    return api
