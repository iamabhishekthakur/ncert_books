from typing import Union
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi import FastAPI
from router import classes, subjects, books
import json

app = FastAPI()

app.include_router(classes.router, prefix="/classes", tags=["Classes"])
app.include_router(subjects.router, prefix="/subjects", tags=["Subjects"])
app.include_router(books.router, prefix="/books", tags=["Books"])


@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/initialize-data")
def initialize_data():
    # read file
    with open('data.json', 'r') as myfile:
        data = myfile.read()
    # parse file
    classList = json.loads(data)
    for classItem in classList:
        print('\n')
        print(classItem)
        subjectList = classItem['subjects']
        for subjectItem in subjectList:
            print(subjectItem)
            bookList = subjectItem['books']
            for bookItem in bookList:
                print(bookItem)
                chapterList = bookItem['chapters']
                for chapterItem in chapterList:
                    print(chapterItem)

    return {"status": "Data intialized successfully", }
