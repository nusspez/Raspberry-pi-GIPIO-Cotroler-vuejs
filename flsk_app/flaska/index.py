from app import app
from resources.control import Pin
from flask import jsonify
from flask_cors import CORS

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

actions = {}

for i in range(2,28):
    actions[str(i)] = {'state':'0'}


@app.route('/api/v1.0/mensaje')
def create_task():
    return jsonify('Hola mundo desde Flask')

if __name__ == '__main__':
    app.run(debug=False, port=5000, host='0.0.0.0')
