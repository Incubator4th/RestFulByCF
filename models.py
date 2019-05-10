from exts import db
from passlib.apps import custom_app_context


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False,unique=True,index=True)
    password = db.Column(db.String(128))
    def hash_password(self, passwd):
        self.password = custom_app_context.encrypt(passwd)
    def verity_password(self, passwd):
        return custom_app_context.verify(passwd, self.password)

class Book(db.Model):
    __tablename__ = 'Book'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False,unique=True)

class Tag(db.Model):
    __tablename__ = 'Tag'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=True,unique=True,index=True)
    def __repr__(self):
        return '<Tag {}'.format(self.name)

class post_user2tag(db.Model):
    __tablename__ = 'post_user2tag'
    __table_args__ = (
        db.PrimaryKeyConstraint('user_id', 'tag_id'),
    )
    user_id = db.Column(db.Integer,db.ForeignKey('User.id'))
    tag_id = db.Column(db.Integer,db.ForeignKey('Tag.id'))
    value = db.Column(db.Float)

class post_book2tag(db.Model):
    __tablename__ = 'post_book2tag'
    __table_args__ = (
        db.PrimaryKeyConstraint('book_id', 'tag_id'),
    )
    book_id = db.Column(db.Integer,db.ForeignKey('Book.id'))
    tag_id = db.Column(db.Integer,db.ForeignKey('Tag.id'))
    value = db.Column(db.Float)

class user_like_books(db.Model):
    __tablename__ = 'user_like_books'
    __table_args__ = (
        db.PrimaryKeyConstraint('user_id', 'book_id'),
    )
    user_id = db.Column(db.Integer,db.ForeignKey('User.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('Book.id'))
    value = db.Column(db.Float)