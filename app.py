from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Welcome to My Watchlist!'


@app.route('/hello')
def hell0_totoro():
    return '<h1>Hello Totoro!</h1><img src="https://helloflask.com/totoro.gif">'


if __name__ == '__main__':
    app.run(debug=True)