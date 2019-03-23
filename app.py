from flask import Flask
from flask import request


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Collaborative Filtering Recommendation'

@app.route('/api/users',methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
