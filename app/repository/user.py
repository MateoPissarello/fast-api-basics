from sqlalchemy.orm import Session
from app.db import models


def _get_user(user_id, db: Session):
    user = db.query(models.User).filter(models.User.id == user_id)
    return user


def create_user(user, db: Session):
    user = user.dict()
    new_user = models.User(
        username=user["username"],
        password=user["password"],
        name=user["name"],
        last_name=user["last_name"],
        address=user["address"],
        phone_number=user["phone_number"],
        email=user["email"],
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)


def get_user_by_id(user_id, db: Session):
    user = _get_user(user_id, db).first()
    if not user:
        return {"response": "User not found"}
    return user


def delete_user(user_id, db: Session):
    user = _get_user(user_id, db)
    if not user.first():
        return {"response": "User not found"}
    user.delete(synchronize_session=False)
    db.commit()
    return {"response": "User deleted successfully"}


def get_users(db: Session):
    users = db.query(models.User).all()
    return users


def update_user(user_id, db: Session, updateUser):
    user = _get_user(user_id, db)
    if not user.first():
        return {"response": "User not found"}
    user.update(updateUser.dict(exclude_unset=True))
    db.commit()
