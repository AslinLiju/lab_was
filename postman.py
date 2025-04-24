from flask import Flask, jsonify, request

app = Flask(_name_)

# Sample data (in-memory "database")
books = [
    {"id": 1, "title": "Harry Potter", "author": "J.K. Rowling"},
    {"id": 2, "title": "The Hobbit", "author": "J.R.R. Tolkien"}
]

# GET - Retrieve all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# POST - Add a new book
@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(new_book), 201

# PUT - Update a book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    for book in books:
        if book['id'] == book_id:
            data = request.get_json()
            book.update(data)
            return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

# DELETE - Delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return jsonify({"message": "Book deleted"})
    return jsonify({"error": "Book not found"}), 404

# Run the app
if _name_ == '_main_':
    app.run(debug=True)