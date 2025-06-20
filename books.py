from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {
        'title': 'The Martian Protocol',
        'author': 'Eliza Rayne',
        'category': 'science fiction'
    },
    {
        'title': 'Quantum Gardens',
        'author': 'Dr. Alton Vex',
        'category': 'science'
    },
    {
        'title': 'A History of Thought',
        'author': 'Linda C. Mayer',
        'category': 'philosophy'
    },
    {
        'title': 'Numbered Worlds',
        'author': 'Maxwell Kent',
        'category': 'math'
    },
    {
        'title': 'Empire of Clay',
        'author': 'Maxwell Kent',
        'category': 'history'
    },
    {
        'title': 'The Last Equation',
        'author': 'Noah Wren',
        'category': 'mystery'
    },
    {
        'title': 'Mechanics of Heaven',
        'author': 'Maxwell Kent',
        'category': 'history'
    },
    {
        'title': 'Biomes and Beyond',
        'author': 'Rhea Kim',
        'category': 'biology'
    },
    {
        'title': 'The Algorithmic Soul',
        'author': 'Kai Lin',
        'category': 'technology'
    },
    {
        'title': 'Geometry of Lies',
        'author': 'Fiona Delacroix',
        'category': 'thriller'
    }
]


@app.get("/books")
def books():
    return BOOKS


@app.get("/book/{book_title}")
def read_book(book_title:str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book


@app.get("/book/{dynamic_param}")
def read_all_books(dynamic_param:str):
    return {"my dynamic params": dynamic_param}

####### read category by querry

@app.get("/books/")
async def read_caregory_by_querry(category: str):
    book_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            book_to_return.append(book)
            
    return book_to_return


####### read category by querry

@app.get("/books/{book_author}/")
async def read_author_caregory_by_querry( book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
                book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
            
    return books_to_return
 
 ##### POST REQUESTS have a body
 
@app.post("/books/create_book")
async def create_new_book(new_book=Body()):
        BOOKS.append(new_book)
        
###### PUT/ UPDATE request
@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for b in range(len(BOOKS)):
        if BOOKS[b].get("title").casefold() == updated_book.get("title").casefold():
             BOOKS[b] = updated_book
             
###### DELETE request
@app.delete("/books/delete_book/{book_title}")
async def delete_book(delete_book=Body()):
    for b in range(len(BOOKS)):
        if BOOKS[b].get("title").casefold() == delete_book.get("title").casefold():
            BOOKS.pop(b)
            break