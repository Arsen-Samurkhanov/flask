from flask import redirect
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
   
    return redirect('https://yandex.ru')

if __name__ == '__main__':
    app.run(debug=True)