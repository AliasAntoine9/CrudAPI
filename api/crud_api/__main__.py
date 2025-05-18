from fastapi import FastAPI

from crud_api import settings
from crud_api.controller.car import router as car_router
from crud_api.controller.database import router as database_router
from crud_api.controller.utils import router as utils_router
from crud_api.utils.constant import swagger_tags

def create_api() -> FastAPI:
    """This function is creating a new fastapi instance"""
    api = FastAPI(
        docs_url=None,
        openapi_tags=swagger_tags,
        openapi_url="/openapi.json",
        title=settings.api_name,
        version=settings.api_version,
    )

    api.include_router(car_router)
    api.include_router(database_router)
    api.include_router(utils_router)

    return api
