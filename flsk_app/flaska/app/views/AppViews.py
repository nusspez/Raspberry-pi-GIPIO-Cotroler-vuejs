from flask.views import View, MethodView
from flask import jsonify
from flask import request
import json
from app.resources.control import Pin


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
        args = request.get_json()
        i = int(len(actions)) + 2
        actions[i] = {'state': args['state']}
        print(actions[i])
        return jsonify(success=True),200,{'ContentType':'application/json'}

    def delete(self, gpio_number):
        # delete a single user
        del actions[gpio_number]
        return jsonify(success=True),200,{'ContentType':'application/json'}

    def put(self, gpio_number):
        # update a single user
        args = request.get_json()
        query = {'state':args['state']}
        actions[gpio_number] = query
        pin_action = Pin(query['state'], action_id)
        pin_action.change_satate()
        return jsonify(success=True),200,{'ContentType':'application/json'}
