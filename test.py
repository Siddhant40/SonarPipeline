from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask app!"})

@app.route('/external-data')
def external_data():
    response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
