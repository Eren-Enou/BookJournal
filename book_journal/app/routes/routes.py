#App Routes (separate files for organization)


from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for
from app.models.models import Book, JournalEntry
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

@main.route('/delete/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    # Find the book by ID and delete it
    """
    Deletes a book from the database by its ID.

    Args:
        book_id (int): The ID of the book to be deleted.

    Returns:
        Response: A redirect to the homepage after the book is deleted.
    """

    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('main.home'))

@main.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    # Find the book by ID
    """
    Edits a book in the database by its ID.

    Args:
        book_id (int): The ID of the book to be edited.

    Returns:
        Response: A redirect to the homepage if the book is successfully edited,
        or a rendered template for editing the book if the request method is GET.
    """
    book = Book.query.get_or_404(book_id)

    if request.method == 'POST':
        # Update the book's details from the form
        book.title = request.form['title']
        book.author = request.form['author']
        book.genre = request.form['genre']
        book.pub_date = request.form['pub_date']

        db.session.commit()
        return redirect(url_for('main.home'))

    return render_template('edit_book.html', book=book)


@main.route('/journal/<int:book_id>')
def view_journal(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template('view_journal.html', book=book)

@main.route('/journal/add/<int:book_id>', methods=['GET', 'POST'])
def add_journal_entry(book_id):
    book = Book.query.get_or_404(book_id)

    if request.method == 'POST':
        content = request.form['content']
        new_entry = JournalEntry(book_id=book_id, date=datetime.now(), content=content)
        db.session.add(new_entry)
        db.session.commit()
        return redirect(url_for('main.view_journal', book_id=book_id))

    return render_template('add_journal_entry.html', book=book)