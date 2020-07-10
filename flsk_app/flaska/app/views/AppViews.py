from flask.views import View, MethodView
from flask import jsonify
from flask import request
import json

actions = {}

for i in range(2,28):
    actions[str(i)] = {'state':'0'}

class HelloMesage(View):
    def dispatch_request(self):
        return jsonify('Hola mundo desde Flask')

class GpioAPI(MethodView):

    def get(self, gpio_number):
        if gpio_number is None:
            # return a list of users
            return jsonify(actions)
        else:
            # expose a single user
            return jsonify(actions[gpio_number])

    def post(self):
        # create a new user
        print(request.get_json())

        return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

        # return jsonify(success=True)

    def delete(self, gpio_number):
        # delete a single user
        pass

    def put(self, gpio_number):
        # update a single user
        pass
