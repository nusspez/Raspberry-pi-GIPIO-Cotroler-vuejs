from app import app
from flask import jsonify
from flask.views import View
from app.resources.control import Pin

actions = {}

for i in range(2,28):
    actions[str(i)] = {'state':'0'}

class Hello(View):
    def dispatch_request(self):
        return  jsonify('Hola mundo desde Flask')

app.add_url_rule('/api/v1.0/mensaje', view_func=Hello.as_view('Hello'))



if __name__ == '__main__':
    app.run(debug=False, port=5000, host='0.0.0.0')
