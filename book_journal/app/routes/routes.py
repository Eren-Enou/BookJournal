#App Routes (separate files for organization)

from flask import Blueprint, render_template, request, redirect, url_for
from app.models.models import Book
from .. import db

# Blueprint for modular routing
main = Blueprint('main', __name__)

# Homepage: Display all books
@main.route('/')
def home():
    books = Book.query.all()
    return render_template('home.html', books=books)

# Add Book Page: Form to add a book
@main.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        pub_date = request.form['pub_date']

        # Create new book
        new_book = Book(title=title, author=author, genre=genre, pub_date=pub_date)
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('main.home'))

    return render_template('add_book.html')
