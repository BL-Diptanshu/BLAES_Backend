from flask import Flask, jsonify, request


app = Flask(__name__)

books = [
    {"id": 1, "title": "book1", "author": "author1"},
    {"id": 2, "title": "book2", "author": "author2"},
    {"id": 3, "title": "book3", "author": "author3"}
]

#all books
@app.route('/books', methods = ['GET' ])
def get_books():
    return books

#book by Id
@app.route('/books/<int:book_id>',methods = ['GET'])
def get_bookById(book_id):
    for book in books:
        if book['id'] == book_id:
            return book
        
    return {'Error: Book not found!'}

#create book 
@app.route('/books', methods = ['POST'])
def create_book():
    new_book = {'id':len(books)+1, 'title':request.json['title'], 'author':request.json['author']}
    books.append(new_book)
    return new_book

#Update a book
@app.route('/books/<int:book_id>', methods = ['PUT'])
def update_book(book_id):
    for book in books:
        if book['id'] == book_id:
            book['title'] = request.json['title']
            book['author'] = request.json['author']
            return book
    
    return "Error: book not found! "

#delete a book
@app.route('/books/<int:book_id>', methods = ['DELETE'])
def deleteById(book_id):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return {"book":"book deleted Successfully"}
    
    return {'error: Book not found'}

def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()