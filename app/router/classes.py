
from fastapi import APIRouter, Response, status, Request, Depends
from collection_connection import ClassesCollection
from fastapi.responses import JSONResponse


router = APIRouter()


@router.get("/list")
def classes():
    classes = ClassesCollection.fetch()
    return classes.items
