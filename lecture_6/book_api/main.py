from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from database import engine, Base, get_db
from models import Book
from schemas import BookCreate, BookOut, BookUpdate

app = FastAPI()

# Create DB tables
Base.metadata.create_all(bind=engine)


@app.get("/healthcheck")
async def healthcheck() -> dict:
    return {"status": "ok"}


@app.post("/books/", response_model=BookOut)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    """Create a new book"""
    db_book = Book(title=book.title, author=book.author, year=book.year)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


@app.get("/books/", response_model=list[BookOut])
def get_books(limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    """Get all books"""
    return db.query(Book).offset(offset).limit(limit).all()


@app.delete("/books/{book_id}", response_model=BookOut)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """Delete a book by ID"""
    db_book = db.query(Book).get(book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(db_book)
    db.commit()
    return db_book


@app.put("/books/{book_id}", response_model=BookOut)
def update_book(book_id: int, book_data: BookUpdate, db: Session = Depends(get_db)):
    """Update a book's details"""
    db_book = db.query(Book).get(book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")

    # Update fields only if provided
    if book_data.title is not None:
        db_book.title = book_data.title
    if book_data.author is not None:
        db_book.author = book_data.author
    if book_data.year is not None:
        db_book.year = book_data.year

    db.commit()
    db.refresh(db_book)
    return db_book


@app.get("/books/search/", response_model=list[BookOut])
def search_books(
    title: str | None = None,
    author: str | None = None,
    year: int | None = None,
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    """Search books by title, author or year"""

    if title is None and author is None and year is None:
        return []

    query = db.query(Book)

    if title:
        query = query.filter(Book.title.contains(title))
    if author:
        query = query.filter(Book.author.contains(author))
    if year:
        query = query.filter(Book.year == year)

    return query.offset(offset).limit(limit).all()
