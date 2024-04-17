from sqlalchemy.orm import Session
from ..db import models


def create_user(db: Session, user: models.User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_users(db: Session):
    return db.query(models.User).all()
