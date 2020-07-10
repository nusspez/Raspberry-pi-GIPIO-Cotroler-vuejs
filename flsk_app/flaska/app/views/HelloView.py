from flask.views import View

class Hello(view):
    def dispatch_request(self):
        return  jsonify('Hola mundo desde Flask')
