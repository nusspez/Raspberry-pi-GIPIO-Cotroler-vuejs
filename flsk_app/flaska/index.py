from app import app,api
from resources.control import Pin
from flask_restful import Resource,reqparse,Api
import json

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
        return query, 201

class ActionList(Resource):
    def get(self):
        return actions

    def post(self):
        args = parser. parse_args()
        action_id = int(max(actions.keys())) + 1
        action_id = '%i' % action_id
        actions[action_id] = {'state': args['state']}
        return actions[action_id], 201

api.add_resource(ActionList, '/api/v1.0/actions/')

api.add_resource(Action, '/api/v1.0/action/<action_id>/')

if __name__ == '__main__':
    app.run(debug=True)
