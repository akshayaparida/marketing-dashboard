from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_ads():
    return {"message": "List of ads"}
