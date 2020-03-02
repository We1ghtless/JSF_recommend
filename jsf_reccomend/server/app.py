from flask import Flask, jsonify
from flask_cors import CORS
import json

# configuration
DEBUG = True

with open ('data.json') as read_file:
    data = json.load(read_file)




# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/0', methods=['GET'])
def question1():
    return jsonify(data['item1'])

@app.route('/1', methods=['GET'])
def question2():
    return jsonify(data['item2'])

@app.route('/2', methods=['GET'])
def question3():
    return jsonify(data['item3'])



if __name__ == '__main__':
    app.run()
