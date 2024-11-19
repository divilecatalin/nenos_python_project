import uvicorn
from fastapi import FastAPI

from src.config import APi_HOST, API_PORT
from src.api.routers.status import router as status_router
from src.api.routers.users import router as users_router

app = FastAPI(
    title="Nenos Academy Shop API", 
    description="An API used in the Nenos Academy Shop App", 
    version="1.0.0",
    )

app.include_router(status_router, prefix="/api", tags=["API"])
app.include_router(users_router, prefix="/users", tags=["Users"])

if __name__ =="__main__":
    uvicorn.run("src.api.main:app", host=APi_HOST, port=API_PORT, reload=True)