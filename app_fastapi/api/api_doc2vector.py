from fastapi import APIRouter

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

# from ai.module.doc2vector

router = APIRouter()


@router.get("/", tags=["Document"])
async def gpu_check():
    resDict = {'result': 'test'}
    resJson = jsonable_encoder(resDict)
    return JSONResponse(content=resJson)
