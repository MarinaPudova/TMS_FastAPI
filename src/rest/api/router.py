from fastapi import APIRouter

from src.rest.api.university import router as uni_router
router = APIRouter()

router.include_router(uni_router)
