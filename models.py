from exts import db

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False,unique=True)
    password = db.Column(db.String(16), nullable=False)

class Book(db.Model):
    __tablename__ = 'Book'
    id = db.Column(db.Integer, primary_key=True)

class Tag(db.Model):
    __tablename__ = 'Tag'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String,nullable=True,unique=True,index=True)
    def __repr__(self):
        return '<Tag {}'.format(self.name)

class post_user2tag(db.Model):
    __tablename__ = 'post_user2tag'
    user_id = db.Column(db.Integer,db.ForeignKey('User.id'))
    tag_id = db.Column(db.Integer,db.ForeignKey('Tag.id'))
    value = db.Column(db.Float)

class post_book2tag(db.Model):
    __tablename__ = 'post_book2tag'
    book_id = db.Column(db.Integer,db.ForeignKey('Book.id'))
    tag_id = db.Column(db.Integer,db.ForeignKey('Tag.id'))
    value = db.Column(db.Float)
