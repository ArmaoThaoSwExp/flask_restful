#!flask/bin/python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!\n\n'

@app.route('/testing')
def testing():
    return 'TESTING!!!\n\n'

if __name__ == '__main__':
    app.run(debug=True)
