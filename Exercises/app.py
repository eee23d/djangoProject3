from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Home page'


@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'Guest')
    msg = f'Hello {name}'
    return msg, 200, {'Content-Type': 'text/plain; charset=utf-8'}
