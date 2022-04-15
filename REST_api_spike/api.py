from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)

api = Api(app)

trello_board = {
    'todo1': {'task': 'make video on how to use flask', 'state': 'backlog'},
    'todo2': {'task': 'make video on how ', 'state': 'backlog'}
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in trello_board:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')


# Todo
# shows a single todo item and lets you delete a todo item
class Tasks(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return trello_board[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del trello_board[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        trello_board[todo_id] = task
        return 200

class TaskList(Resource):
    def get(self):
        return trello_board

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(trello_board.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        trello_board[todo_id] = {'task': args['task']}
        return trello_board[todo_id], 201

api.add_resource(Tasks, '/todos/<todo_id>')
api.add_resource(TaskList, '/todos')


if __name__ == '__main__':
    app.run(debug=True)
