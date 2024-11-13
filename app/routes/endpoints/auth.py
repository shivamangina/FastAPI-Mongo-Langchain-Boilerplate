from fastapi import APIRouter


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

@router.get("", tags=["auth"])
async def auth_check():
    return {"status": "ok"}