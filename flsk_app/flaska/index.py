from app import app
from app.resources.control import Pin
from app.views.AppViews import Hello
actions = {}

for i in range(2,28):
    actions[str(i)] = {'state':'0'}

app.add_url_rule('/api/v1.0/mensaje', view_func=HelloMesage.as_view('Hello'))


if __name__ == '__main__':
    app.run(debug=False, port=5000, host='0.0.0.0')
