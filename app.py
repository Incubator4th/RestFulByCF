from flask import *
from models import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Collaborative Filtering Recommendation'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ares:123456@106.15.186.230:3306/book_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
db.init_app(app)
#db.create_all(app=app)

@app.route('/api/users',methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400)
    if User.query.filter_by(username=username).first() is not None:
        abort(400)
    user = User(username=username)
    user.hash_password(passwd=password)
    db.session.add(user)
    db.session.commit()
    return jsonify({ 'username': user.username }), 201, {'Location': url_for('get_user', id = user.id, _external = True)}


@app.route('/api/users/<int:id>')
def get_user(id):
    user = User.query.get(id)
    if not user:
        abort(400)
    return jsonify({'username': user.username})


@app.route('/api/books/<int:id>')
def get_book(id):
    book = Book.query.get(id)
    if not book:
        abort(400)
    return jsonify({'bookname':book.name,})

@app.route('/api/users/<int:id>/books')
def get_books_by_user(id):
    user = User.query.get(id)
    if not user:
        abort(400)
    else:
        books = db.session.query(Book).join(user_like_books).\
            filter(user_like_books.user_id==id)
        _dict = {'username': user.username,
                 'books':{}}
        for book in books:
            _dict['books'][book.id] = book.name
        return jsonify(_dict)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':

    app.run()
