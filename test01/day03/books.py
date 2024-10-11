#!/usr/bin/env python3

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, Dict, Any

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str

class StandardResponse(BaseModel):
    data: Optional[Any] = None
    error: Optional[Dict[str, Any]] = None


books = []

@app.get("/", response_model=StandardResponse)
async def _root():
    return StandardResponse(data={"message": "Benvenuto nella libreria API"})

# endpoint create
@app.post("/books/add", response_model=StandardResponse)
async def _create_book(book: Book):
    books.append(book)
    return StandardResponse(data=book)

# endpoint clear
@app.get("/books/clear", response_model=StandardResponse)
async def _clear_book():
    books.clear()
    return StandardResponse(data={"message": "Libreria svuotata"})

# endpoint read
@app.get("/books/list", response_model=StandardResponse)
async def _read_books():
    return StandardResponse(data=books)

# endpoint get singolo libro
@app.get("/books/{book_id}", response_model=StandardResponse)
async def _read_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return StandardResponse(data=book)
    return StandardResponse(error={"message": "Libro non trovato", "code": 404})

# endpoint elimina singolo libro
@app.delete("/books/del/{book_id}", response_model=StandardResponse)
async def _delete_book(book_id: int):
    for i, book in enumerate(books):
        if book.id == book_id:
            del books[i]
            return StandardResponse(data={"deleted": True})
    return StandardResponse(data={"deleted": False})

