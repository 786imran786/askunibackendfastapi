from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.auth import router as auth_router
from app.core.dependencies import get_current_user
from app.models.user import User
from fastapi import Depends
from app.core.dependencies import require_role
from app.api.v1.questions import router as question_router
from app.api.v1.answers import router as answer_router
from app.api.v1.votes import router as vote_router
from app.api.v1.comments import router as comment_router
from app.api.v1.notifications import router as notification_router
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.onboarding import router as onboarding_router

app = FastAPI(title=settings.PROJECT_NAME)
API_PREFIX = "/api/v1"

app.include_router(auth_router, prefix=API_PREFIX)
app.include_router(question_router, prefix=API_PREFIX)
app.include_router(answer_router, prefix=API_PREFIX)
app.include_router(vote_router, prefix=API_PREFIX)
app.include_router(comment_router, prefix=API_PREFIX)
app.include_router(notification_router, prefix=API_PREFIX)
app.include_router(onboarding_router, prefix=API_PREFIX)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5174",  # Vite dev server
        "http://127.0.0.1:5174"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "AskLPU API running"}

@app.get("/protected")
def protected_route(current_user: User = Depends(get_current_user)):
    return {
        "message": "Access granted",
        "user_id": str(current_user.id),
        "email": current_user.email
    }

@app.get("/admin-only")
def admin_route(
    current_user = Depends(require_role("admin"))
):
    return {"message": "Welcome admin"}