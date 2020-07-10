from flask.views import View, MethodView
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
            return jsonify(actions[gpio_number])

    def post(self):
        # create a new user
        gpio_number = int(max(actions.keys())) + 1
        gpio_number = '%i' % gpio_number
        actions[gpio_number] = {'state': args['state']}
        return jsonify(actions[gpio_number])

    def delete(self, gpio_number):
        # delete a single user
        pass

    def put(self, gpio_number):
        # update a single user
        pass
