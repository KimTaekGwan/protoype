from fastapi import APIRouter

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


router = APIRouter()


@router.get("/check", tags=["NLP"])
async def gpu_check():
    resDict = {'result':'test'}
    resJson = jsonable_encoder(resDict)
    return JSONResponse(content=resJson)