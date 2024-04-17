from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.actions import crud_user
from crud.db.database import SessionLocal
from crud.schema.user import UserSchema

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/users/", response_model=UserSchema)
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    return crud_user.create_user(db=db, user=user)


@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    return crud_user.get_users(db=db)
