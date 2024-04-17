from fastapi import FastAPI

app = FastAPI()

# Path and query params

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

@app.get("/users")
def get_user_by_name(name: str = None, lastname: str = None):
    return {"name": name, "lastname": lastname}

