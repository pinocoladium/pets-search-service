from fastapi import Depends, FastAPI

from app.api.dependencies import authorize
from app.api.router import api_router


app = FastAPI(
    title='pets-search-service',
    version='0.1.0',
    dependencies=[Depends(authorize)],
)


# Register routers
app.include_router(api_router)
