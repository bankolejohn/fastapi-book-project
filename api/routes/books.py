# from typing import OrderedDict

# from fastapi import APIRouter, status, HTTPException, Path 
# from fastapi.responses import JSONResponse

# from api.db.schemas import Book, Genre, InMemoryDB

# router = APIRouter()

# db = InMemoryDB()
# db.books = {
#     1: Book(
#         id=1,
#         title="The Hobbit",
#         author="J.R.R. Tolkien",
#         publication_year=1937,
#         genre=Genre.SCI_FI,
#     ),
#     2: Book(
#         id=2,
#         title="The Lord of the Rings",
#         author="J.R.R. Tolkien",
#         publication_year=1954,
#         genre=Genre.FANTASY,
#     ),
#     3: Book(
#         id=3,
#         title="The Return of the King",
#         author="J.R.R. Tolkien",
#         publication_year=1955,
#         genre=Genre.FANTASY,
#     ),
# }


# @router.post("/", status_code=status.HTTP_201_CREATED)
# async def create_book(book: Book):
#     db.add_book(book)
#     return JSONResponse(
#         status_code=status.HTTP_201_CREATED, content=book.model_dump()
#     )


# @router.get(
#     "/", response_model=OrderedDict[int, Book], status_code=status.HTTP_200_OK
# )
# async def get_books() -> OrderedDict[int, Book]:
#     return db.get_books()


# @router.put("/{book_id}", response_model=Book, status_code=status.HTTP_200_OK)
# async def update_book(book_id: int, book: Book) -> Book:
#     return JSONResponse(
#         status_code=status.HTTP_200_OK,
#         content=db.update_book(book_id, book).model_dump(),
#     )


# @router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_book(book_id: int) -> None:
#     db.delete_book(book_id)
#     return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content=None)


# # New endpoint to retrieve a book by its ID
# @router.get("/{book_id}", response_model=Book, status_code=status.HTTP_200_OK)
# async def get_book_by_id(book_id: int = Path(..., description="The ID of the book to retrieve")) -> Book:
#     # Check if the book exists in the database
#     book = db.get_book_by_id(book_id)
#     if not book:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Book with ID {book_id} not found",
#         )
    
#     # Return the book details
#     return book

from typing import OrderedDict

from fastapi import APIRouter, status, HTTPException, Path
from fastapi.responses import JSONResponse

from api.db.schemas import Book, Genre, InMemoryDB

router = APIRouter()

db = InMemoryDB()
db.books = {
    1: Book(
        id=1,
        title="The Hobbit",
        author="J.R.R. Tolkien",
        publication_year=1937,
        genre=Genre.SCI_FI,
    ),
    2: Book(
        id=2,
        title="The Lord of the Rings",
        author="J.R.R. Tolkien",
        publication_year=1954,
        genre=Genre.FANTASY,
    ),
    3: Book(
        id=3,
        title="The Return of the King",
        author="J.R.R. Tolkien",
        publication_year=1955,
        genre=Genre.FANTASY,
    ),
}


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_book(book: Book):
    db.add_book(book)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED, content=book.model_dump()
    )


@router.get(
    "/", response_model=OrderedDict[int, Book], status_code=status.HTTP_200_OK
)
async def get_books() -> OrderedDict[int, Book]:
    return db.get_books()


@router.put("/{book_id}", response_model=Book, status_code=status.HTTP_200_OK)
async def update_book(book_id: int, book: Book) -> Book:
    updated_book = db.update_book(book_id, book)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=updated_book.model_dump(),
    )


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int) -> None:
    db.delete_book(book_id)
    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content=None)


# New endpoint to retrieve a book by its ID
@router.get("/{book_id}", response_model=Book, status_code=status.HTTP_200_OK)
async def get_book_by_id(book_id: int = Path(..., description="The ID of the book to retrieve")) -> Book:
    # Check if the book exists in the database
    book = db.get_book(book_id)  # Use the correct method name: get_book
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with ID {book_id} not found",
        )
    
    # Return the book details
    return book