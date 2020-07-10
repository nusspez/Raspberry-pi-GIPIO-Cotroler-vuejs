from flask.views import View
from flask import jsonify

class HelloMesage(View):
    def dispatch_request(self):
        return jsonify('Hola mundo desde Flask')
