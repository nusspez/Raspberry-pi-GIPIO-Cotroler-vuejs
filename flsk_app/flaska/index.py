from app import app
from flask import jsonify
from resources.control import Pin

actions = {}

for i in range(2,28):
    actions[str(i)] = {'state':'0'}


@app.route('/api/v1.0/mensaje')
def create_task():
    return jsonify('Hola mundo desde Flask')

if __name__ == '__main__':
    app.run(debug=False, port=5000, host='0.0.0.0')
