from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

#from newProject.database.database import 
from newProject.models.models import User
from newProject.schemas.schemas import UserCreate, UserLogin, UserResponse
from newProject.auth.auth import hash_password, verify_password, create_access_token
from newProject.dependencies.depencencies import get_current_user, get_db

router = APIRouter(prefix="/users", tags=["Users"])


# ---------------- DB DEP ----------------
# def get_db():
#    db = SessionLocal()
#    try:
#        yield db
#    finally:
#        db.close() 


# ---------------- REGISTER ----------------
@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):

    existing = db.query(User).filter(User.username == user.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")

    db_user = User(
        username=user.username,
        hashed_password=hash_password(user.password)
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


# ---------------- LOGIN ----------------
@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(User.username == user.username).first()

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid username")

    if not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid password")

    token = create_access_token({
        "sub": db_user.username,
        "user_id": db_user.id,
        "role": db_user.role
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }


# ---------------- CURRENT USER ----------------
@router.get("/me")
def get_me(user: User = Depends(get_current_user)):
    return {
        "id": user.id,
        "username": user.username,
        "role": user.role
    }