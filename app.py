from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import config

# These imports will work after we create them
from services import DealerService
from models import DealerResponse

# --------------------------------------------------------
# FastAPI App
# --------------------------------------------------------

app = FastAPI(
    title=config.APP_NAME,
    description=config.DESCRIPTION,
    version=config.VERSION
)

# --------------------------------------------------------
# Static Files
# --------------------------------------------------------

app.mount(
    "/static",
    StaticFiles(directory=config.STATIC_DIR),
    name="static"
)

# HTML Templates

templates = Jinja2Templates(
    directory=config.TEMPLATE_DIR
)

# --------------------------------------------------------
# Dealer Service
# --------------------------------------------------------

dealer_service = DealerService()

# --------------------------------------------------------
# Home Page
# --------------------------------------------------------


@app.get("/")
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


# --------------------------------------------------------
# Search Dealer
# --------------------------------------------------------

@app.get(
    "/api/search",
    response_model=list[DealerResponse]
)
async def search(query: str):

    """
    Search dealers

    query can be

    422101

    OR

    Green Agro

    OR

    Nashik
    """

    result = dealer_service.search(query)

    return result


# --------------------------------------------------------
# Nearest Dealers
# --------------------------------------------------------

@app.get(
    "/api/nearest",
    response_model=list[DealerResponse]
)
async def nearest(
    lat: float,
    lon: float
):

    """
    Find nearest dealers

    Example

    /api/nearest?lat=19.99&lon=73.78
    """

    result = dealer_service.nearest(
        latitude=lat,
        longitude=lon
    )

    return result


# --------------------------------------------------------
# Health Check
# --------------------------------------------------------

@app.get("/health")
async def health():

    """
    Used by Render
    or monitoring tools
    """

    return {
        "status": "healthy",
        "application": config.APP_NAME,
        "version": config.VERSION
    }


# --------------------------------------------------------
# Exception Handler
# --------------------------------------------------------

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):

    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "Something went wrong.",
            "error": str(exc)
        }
    )