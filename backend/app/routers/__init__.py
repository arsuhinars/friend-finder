from fastapi import APIRouter

from .auth import router as auth
from .user import router as user
from .profile import router as profile
from .messages import router as messages
from .updates import router as updates

# Create one global router for all of the API routes
router = APIRouter()

router.include_router(auth)
router.include_router(user)
router.include_router(profile)
router.include_router(messages)
router.include_router(updates)
