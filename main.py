from fastapi import FastAPI, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from typing import Optional
from database import get_db
from models import User
from schema import RegisterSchema, LoginSchema
from auth import hash_password, verify_password, create_access_token, decode_access_token

app = FastAPI()


def get_current_user(authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Unauthorized")
    token = authorization.split(" ")[1]
    return decode_access_token(token)


@app.post("/register")
def register(payload: RegisterSchema, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == payload.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        name=payload.user,
        email=payload.email,
        password=hash_password(payload.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "ID": new_user.id,
        "Message": "User Created Successfully"
    }


@app.post("/login")
def login(payload: LoginSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email).first()
    if not user or not verify_password(payload.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.email, "ID": user.id})
    return {"access_token": token, "token_type": "bearer"}


@app.get("/profile/{ID}")
def get_profile(user_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "User_id": user.id,
        "user": user.name,
        "email": user.email,
        "Message": "Login Succesfull"
    }


@app.put("/profile/{ID}")
def update_profile(id: int, payload: RegisterSchema, db: Session = Depends(get_db),
                   current_user=Depends(get_current_user)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.name = payload.user
    user.email = payload.email
    user.password = hash_password(payload.password)
    db.commit()
    db.refresh(user)

    return {
        "ID": user.id,
        "user": user.name,
        "email": user.email,
        "Message": "User Updated Succesfully"
    }
