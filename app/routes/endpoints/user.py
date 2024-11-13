from fastapi import APIRouter


router = APIRouter(
    prefix="/user",
    tags=["user"],
)

@router.get("", tags=["user"])
async def get_user():
    return {"first_name": "shiva",
            "last_name":"kumar",
            "email":"shiva2nani.mangina@gmail.com",
            "is_paid":False
            }