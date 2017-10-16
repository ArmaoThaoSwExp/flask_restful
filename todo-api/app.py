#!flask/bin/python
from flask import Flask, jsonify

# Create a Flask app using the name of the file
app = Flask(__name__)


tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    """
    If the user requested to get tasks, return the list of tasks.
    :return:
    """
    return jsonify({'tasks': tasks})


if __name__ == '__main__':
    app.run(debug=True)
