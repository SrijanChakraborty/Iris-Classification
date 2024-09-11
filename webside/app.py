from flask import Flask, render_template, request, jsonify
import pickle
import requests
from waitress import serve

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello!</h1>'


if __name__ == '__main__':
    # production
    # serve(app, host="localhost", port=4000)
    # Development
    app.run(debug=True, host='localhost', port=4000)
