from fastapi import FastAPI, Body, Path
from pydantic import EmailStr, BaseModel
from typing import Annotated 
from items import router as items_router

app = FastAPI()
app.include_router(items_router, tags=["Items"])


# When using Pydantic models, we don't need to specify Body()
class CreateUser(BaseModel):
    email: EmailStr

@app.get("/")
def index():
    return "Hello!"





@app.post("/users/")
def create_user(user: CreateUser):
    return {
        "message": "success",
        "email": user.email
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)