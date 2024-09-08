from flask import Flask, render_template, request, jsonify
import pickle
import requests

app = Flask(__name__)




if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=4000)
