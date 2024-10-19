from flask import Flask, request
import json


DATA_FILE = 'data.json'
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hi!'


@app.route('/getData')
def get_data():

    #try:
    with open(DATA_FILE, 'r') as file:
        return file.read()
    #except:
    #    return json.dumps({'data': 'Nothing has been set yet.'})


@app.route('/setData', methods=["POST"])
def set_data():
    new_data = request.form.get("data")
    if not new_data:
        return 'invalid request'

    data = {}



    with open(DATA_FILE, 'r') as file:
        data = json.loads(file.read())

    data['data'] = new_data

    with open(DATA_FILE, 'w') as file:
        file.write(data)

    return json.dumps(data)
