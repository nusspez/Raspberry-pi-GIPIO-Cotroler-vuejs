from app import app
from flask import jsonify
from app.resources.control import Pin
from app.views.HelloView import Hello
actions = {}

for i in range(2,28):
    actions[str(i)] = {'state':'0'}


app.add_url_rule('/api/v1.0/mensaje', view_func=Hello.as_view('Hello'))



if __name__ == '__main__':
    app.run(debug=False, port=5000, host='0.0.0.0')
