from flask.views import View
from flask import jsonify

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
            return jsonify(actions(gpio_number))

    def post(self):
        # create a new user
        pass

    def delete(self, gpio_number):
        # delete a single user
        pass

    def put(self, gpio_number):
        # update a single user
        pass
