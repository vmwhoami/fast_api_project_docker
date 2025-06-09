from fastapi import FastAPI

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
        'author': 'Tariq Hollow',
        'category': 'history'
    },
    {
        'title': 'The Last Equation',
        'author': 'Noah Wren',
        'category': 'mystery'
    },
    {
        'title': 'Mechanics of Heaven',
        'author': 'Isa Moreno',
        'category': 'physics'
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