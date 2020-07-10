from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

for i in range(2,28):
    actions[str(i)] = {'state':'0'}
