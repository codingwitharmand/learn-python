from fastapi import FastAPI, Response, status
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int
    email: str


app = FastAPI()


@app.post("/users", status_code=status.HTTP_201_CREATED)
def save_user(user: User, response: Response):
    response.set_cookie(key="age", value=user.age)
    response.headers["X-Example"] = "New Header"
    return {"message": f"User with name: {user.name} saved."}

@app.get("/notfound", status_code=status.HTTP_404_NOT_FOUND)
def not_found():
    return {"message": "Item not found..."}


