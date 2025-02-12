#defaul index
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

#second index
@app.route('/arsen')
def index2():
    return '<h1>Hello arsen!</h1>'

#passing variable
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello %s!</h1>' % name

if __name__ == '__main__':
    app.run(debug=True)