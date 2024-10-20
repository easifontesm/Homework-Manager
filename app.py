from flask import Flask, request
import json
import os.path


DATA_FILE = 'data.json'
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hi!'


@app.route('/getData')
def get_data():

    verify_file()

    with open(DATA_FILE, 'r') as file:
        return file.read()


@app.route('/setData', methods=["POST"])
def set_data():
    new_data = request.form.get("data")
    if not new_data:
        return 'invalid request'

    data = {}

    verify_file()

    with open(DATA_FILE, 'r') as file:
        data = json.loads(file.read())

    data['data'] = new_data

    with open(DATA_FILE, 'w') as file:
        file.write(data)

    return json.dumps(data)

def verify_file():
    if not os.path.isfile(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            pass