from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserRead
from app.db.session import get_db
from app.services.user_service import create_user
from app.schemas.user import UserLogin
from app.services.user_service import authenticate_user
from app.core.security import create_access_token, create_refresh_token
from app.schemas.user import TokenResponse
from jose import JWTError
from app.schemas.user import RefreshTokenRequest


router = APIRouter(prefix="/auth", tags=["Auth"])
@router.post(
    "/register",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED
)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    try:
        user = create_user(db, user_in)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    return user

@router.post("/login", response_model=TokenResponse)
def login(user_in: UserLogin, db: Session = Depends(get_db)):
    user = authenticate_user(db, user_in.email, user_in.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    access_token = create_access_token({"sub": str(user.id)})
    refresh_token = create_refresh_token({"sub": str(user.id)})

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "user": user
    }
@router.post("/refresh")
def refresh_token(
    data: RefreshTokenRequest,
    db: Session = Depends(get_db)
):
    try:
        payload = decode_token(data.refresh_token)
        user_id: str | None = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid refresh token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    new_access_token = create_access_token({"sub": str(user.id)})

    return {
        "access_token": new_access_token,
        "token_type": "bearer"
    }
