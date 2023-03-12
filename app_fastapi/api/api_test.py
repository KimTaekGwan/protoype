from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=['TEST'])
async def root():
    return {"msg": "Hello World"}
