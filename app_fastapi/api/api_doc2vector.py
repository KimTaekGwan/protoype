from fastapi import APIRouter

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from ai.module.doc2vector import Util, Doc2Vector

router = APIRouter()


@router.post("/{file_name}", tags=['Document'])
async def document2vector(file_name: str):
    util = Util()
    util.input_files_update()

    process = Doc2Vector()
    resDict = process.run(file_name)
    resJson = jsonable_encoder(resDict)
    return JSONResponse(content=resJson)
