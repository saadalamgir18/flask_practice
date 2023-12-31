from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')

def welcome():
    return "welcome to HomePage"

@app.route('/success/<int:score>')

def success(score):
    return "Person has passed and the marks are "+ str(score)

@app.route('/fail/<int:score>')

def fail(score):
    return "Person has failed and the marks are "+ str(score)



@app.route('/result/<int:marks>')

def result(marks):
    result = ''
    if marks>50:
        result = 'success'
    else:
        result = 'fail'
    return redirect(url_for(result, score = marks))



if __name__ == '__main__':
    app.run()