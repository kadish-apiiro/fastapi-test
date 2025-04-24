import logging

from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from starlette import status
from starlette.responses import Response

logger = logging.getLogger(‘blabla’)


def init(service) -> APIRouter:
    router = APIRouter()

    @router.get("/test/list", status_code=status.HTTP_200_OK)
    async def foo():
        pass

    @router.get("/test/historical/{id}", status_code=status.HTTP_200_OK)
    async def foo(id: str):
        pass

    @router.post("/test/create", status_code=status.HTTP_200_OK)
    async def foo(param):
        pass

    @router.post("/test/launch", status_code=status.HTTP_200_OK)
    async def foo(param):
        pass


    return router
