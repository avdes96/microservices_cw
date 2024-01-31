from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/books", methods = ['GET'])
def books():

    min_year = request.args.get('min_year', default = None)
    if min_year == "":
        min_year = None
    max_year = request.args.get('max_year', default = None)
    if max_year == "":
        max_year = None
    author = request.args.get('author', default = None)
    if author == "":
        author = None
    genre = request.args.get('genre', default=None)
    if genre == "":
        genre = None

    all_data = [ {
        'id': 1,
        'title': 'To Kill a Mockingbird',
        'author': 'Harper Lee',
        'publication_year': 1960,
        'genre': 'Southern Gothic'
    },
    {
        'id': 2,
        'title': '1984',
        'author': 'George Orwell',
        'publication_year': 1949,
        'genre': 'Dystopian Fiction'
    },
    {
        'id': 3,
        'title': 'Pride and Prejudice',
        'author': 'Jane Austen',
        'publication_year': 1813,
        'genre': 'Romantic Novel'
    },
    {
        'id': 4,
        'title': 'The Great Gatsby',
        'author': 'F. Scott Fitzgerald',
        'publication_year': 1925,
        'genre': 'American Literature'
    },
    {
        'id': 5,
        'title': 'The Hunger Games',
        'author': 'Suzanne Collins',
        'publication_year': 2008,
        'genre': 'Young Adult Dystopian'
    },
    {
        'id': 6,
        'title': 'The Seven Husbands of Evelyn Hugo',
        'author': 'Taylor Jenkins Reid',
        'publication_year': 2017,
        'genre': 'Historical Fiction'
    },
    {
        'id': 7,
        'title': 'The Da Vinci Code',
        'author': 'Dan Brown',
        'publication_year': 2003,
        'genre': 'Mystery'
    },
    {
        'id': 8,
        'title': 'Lord of the Flies',
        'author': 'William Golding',
        'publication_year': 1954,
        'genre': 'Classic'   
    },
    {
        'id': 9,
        'title': 'Life of Pi',
        'author': 'Yann Martel',
        'publication_year': 2001,
        'genre': 'Fiction' 
    },
    {
        'id': 10,
        'title': 'The Hobbit',
        'author': 'J.R.R Tolkien',
        'publication_year': 1937,
        'genre': 'Fantasy' 
    }]

    if genre != None:
        final_data = [book for book in all_data if book['genre'] == genre]
    else:
        final_data = all_data

    if author != None:
        final_data = [book for book in final_data if book['author'] == author]
    
    if max_year != None:
        max_year = int(max_year)
        final_data = [book for book in final_data if book['publication_year'] <= max_year]
    
    if min_year != None:
        min_year = int(min_year)
        final_data = [book for book in final_data if book['publication_year'] >= min_year]

    return jsonify(final_data)