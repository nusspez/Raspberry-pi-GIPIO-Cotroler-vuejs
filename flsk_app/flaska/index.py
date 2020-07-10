from app import app
from app.views.AppViews import HelloMesage,GpioAPI


app.add_url_rule('/api/v1.0/mensaje', view_func=HelloMesage.as_view('Hello'))

user_view = GpioAPI.as_view("gpio_api")

app.add_url_rule('/api/v1.0/actions',defaults={'gpio_number':None},
                view_func=user_view,methods=['GET',])

app.add_url_rule('/api/v1.0/actions', view_func=user_view, methods=['POST',])

app.add_url_rule('/api/v1.0/action/<gpio_number>', view_func=user_view,
                 methods=['GET', 'PUT', 'DELETE'])

if __name__ == '__main__':
    app.run(debug=False, port=5000, host='0.0.0.0')
