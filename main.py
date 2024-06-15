from fastapi import FastAPI, Body, Path
from pydantic import EmailStr, BaseModel
from typing import Annotated 
from items import router as items_router
from users.views import router as users_router

app = FastAPI()
app.include_router(items_router, tags=["Items"])
app.include_router(users_router, tags=["Users"])

@app.get("/")
def index():
    return "Hello!"




if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)