from fastapi import APIRouter
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/")
async def root():
    return "Hello World from CrudAPI"

@router.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="Custom Swagger",
        swagger_favicon_url="/static/FastAPI.png",
        swagger_ui_parameters={"defaultModelExpandDepth": -1},
        init_oauth=None
    )
