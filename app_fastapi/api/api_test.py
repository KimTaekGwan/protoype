from fastapi import APIRouter
from conn.db import db

router = APIRouter()


@router.get("/", tags=['TEST'])
async def root():
    return {"msg": "Hello World"}


@router.get("/db", tags=['TEST'])
async def root():
    return {"msg": "Hello World"}