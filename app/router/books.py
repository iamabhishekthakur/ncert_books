from fastapi import APIRouter, Response, status, Request, Depends
from collection_connection import BooksCollection
router = APIRouter()


@router.get("/list")
def books():
    books = BooksCollection.fetch()
    return books
