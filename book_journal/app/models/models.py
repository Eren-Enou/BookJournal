#Database Models (add separation later)

from .. import db

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=True)
    pub_date = db.Column(db.String(10), nullable=True)

     # Relationship with JournalEntry
    journal_entries = db.relationship('JournalEntry', backref='book', cascade='all, delete-orphan')


class JournalEntry(db.Model):
    __tablename__ = 'journal_entries'

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    content = db.Column(db.Text, nullable=False)

    # Relationship with Book
    # book = db.relationship('Book', backref='journal_entries')
