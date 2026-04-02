from newProject.database.database import SessionLocal
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from newProject.auth.auth import decode_access_token
from newProject.models.models import User

oAuth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(
        token: str = Depends(oAuth2_scheme),
        db: Session = Depends(get_db)):
    
    payload = decode_access_token(token)

    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    user_id = payload.get("user_id")

    user = db.query(User).filter(User.id == user_id).first()
     
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    
    return user

def require_admin(
        user = Depends(get_current_user)):
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin privileges required")
    return user

@router.get("/me")
def get_me( 
    user = Depends(get_current_user)
):
    return {
        "id": user.id,
        "username": user.username,
        "role": user.role
    }


