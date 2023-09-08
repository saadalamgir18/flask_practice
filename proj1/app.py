from flask import Flask


###WSGI application
app = Flask(__name__)


@app.route('/')
def welcome():
    return 'Welcome to homepage, this is first attemp'

@app.route('/contact-us')
def contact():
    return 'Welcome to contact us page, this is first attemp'


if __name__ == '__main__':
    app.run(debug = True)
