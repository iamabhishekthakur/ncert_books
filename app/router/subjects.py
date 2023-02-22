from fastapi import APIRouter, Response, status, Request, Depends
from collection_connection import SubjectsCollection
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


router = APIRouter()


@router.get("/list")
def subjects():
    subjects = SubjectsCollection.fetch()
    return subjects
