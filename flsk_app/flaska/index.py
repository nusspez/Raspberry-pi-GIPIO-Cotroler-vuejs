from app import app,api
from resources.control import Pin
from flask_restful import Resource,reqparse,Api
from flask import jsonify
from flask_cors import CORS


# CORS(app, resources={r'/*': {'origins': '*'}})
CORS(app, resources=r'/api/*')


actions = {}

for i in range(2,28):
    actions[str(i)] = {'state':'0'}

def abort_if_action_doesnt_exist(action_id):
    if action_id not in actions:
        abort(404, message="action {} doesn't exist".format(action_id))

parser = reqparse.RequestParser()
parser.add_argument('state')

class Action(Resource):
    def get(self, action_id):
        abort_if_action_doesnt_exist(action_id)
        return actions[action_id]

    def delete(self, action_id):
        abort_if_action_doesnt_exist(action_id)
        del actions[action_id]
        return '', 204

    def put(self, action_id):
        args = parser.parse_args()
        query = {'state':args['state']}
        actions[action_id] = query
        pin_action = Pin(query['state'], action_id)
        pin_action.change_satate()
        return jsonify(query, 201)

class ActionList(Resource):
    def get(self):
        return jsonify(actions)

    def post(self):
        args = parser. parse_args()
        action_id = int(max(actions.keys())) + 1
        action_id = '%i' % action_id
        actions[action_id] = {'state': args['state']}
        return jsonify(actions[action_id]), 201

@app.route("/api/v1/users/create", methods=['POST'])
def create_user():
    """
        Since the path matches the regular expression r'/api/*', this resource
        automatically has CORS headers set.

        Browsers will first make a preflight request to verify that the resource
        allows cross-origin POSTs with a JSON Content-Type, which can be simulated
        as:
        $ curl --include -X OPTIONS http://127.0.0.1:5000/api/v1/users/create \
            --header Access-Control-Request-Method:POST \
            --header Access-Control-Request-Headers:Content-Type \
            --header Origin:www.examplesite.com
        >> HTTP/1.0 200 OK
        Content-Type: text/html; charset=utf-8
        Allow: POST, OPTIONS
        Access-Control-Allow-Origin: *
        Access-Control-Allow-Headers: Content-Type
        Access-Control-Allow-Methods: DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT
        Content-Length: 0
        Server: Werkzeug/0.9.6 Python/2.7.9
        Date: Sat, 31 Jan 2015 22:25:22 GMT


        $ curl --include -X POST http://127.0.0.1:5000/api/v1/users/create \
            --header Content-Type:application/json \
            --header Origin:www.examplesite.com


        >> HTTP/1.0 200 OK
        Content-Type: application/json
        Content-Length: 21
        Access-Control-Allow-Origin: *
        Server: Werkzeug/0.9.6 Python/2.7.9
        Date: Sat, 31 Jan 2015 22:25:04 GMT

        {
          "success": true
        }

    """
    return jsonify(success=True)


api.add_resource(ActionList, '/api/v1.0/actions/')

api.add_resource(Action, '/api/v1.0/action/<action_id>/')

@app.route('/api/v1.0/mensaje')
def create_task():
    return jsonify('Hola mundo desde Flask')

if __name__ == '__main__':
    app.run(debug=False, port=5000, host='0.0.0.0')
