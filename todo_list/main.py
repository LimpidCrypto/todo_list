
"""
Example script showing how to represent todo lists and todo entries in Python
data structures and how to implement endpoint for a REST API with Flask.

Requirements:
* flask
"""

from flask import Flask
from flask_cors import CORS
from todo_list.controllers.lists import LIST_BLUEPRINT

APP = Flask(__name__)
CORS(APP)

APP.register_blueprint(LIST_BLUEPRINT)

if __name__ == '__main__':
    # start Flask server
    APP.debug = True
    APP.run(host="0.0.0.0", port=3000)
