from fastapi import APIRouter, Depends
from ..schemas.user import User, ShowUser, UpdateUser
from app.db.database import get_db
from sqlalchemy.orm import Session
from typing import List
from app.repository import user

router = APIRouter(prefix="/user", tags=["Users"])


@router.get("/{user_id}", response_model=ShowUser)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    myUser = user.get_user_by_id(user_id, db)
    return myUser


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return user.delete_user(user_id, db)


@router.patch("/{user_id}")
def update_user(user_id: int, updateUser: UpdateUser, db: Session = Depends(get_db)):
    user.update_user(user_id, db, updateUser)
    return {"response": "User updated successfully"}


@router.get("", response_model=List[ShowUser])
def get_users(db: Session = Depends(get_db)):
    return user.get_users(db)


@router.post("")
def create_user(thisUser: User, db: Session = Depends(get_db)):
    user.create_user(thisUser, db)
    return {"response": "User created successfully"}
