from flask import Flask
app = Flask(__name__)

@app.route('/projects/') # acts as a directory
def projects():
    return 'The project page'

@app.route('/about')     # acts as a file
def about():
    return 'The about page'

if __name__ == '__main__':
    app.run()