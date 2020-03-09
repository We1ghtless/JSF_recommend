from flask import Flask, jsonify, request
from flask_cors import CORS
import json

# configuration
DEBUG = True

with open ('data.json') as read_file:
    data = json.load(read_file)

answers = []
results = ['Vue', 'React', 'Angular']
v = 0
r = 0
a = 0


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/answers', methods=['GET', 'POST'])
def addAnswer():
    i = 0
    if request.method == 'POST' and i < 4:
        req_data = request.get_json()
        answers.insert(i, req_data)
        message = 'SUCCESS'
        i = i + 1
        print answers
    if i == 4:
        i = i - 4

    return message

@app.route('/0', methods=['GET'])
def question1():
    return jsonify(data['item1'])

@app.route('/1', methods=['GET'])
def question2():
    return jsonify(data['item2'])

@app.route('/2', methods=['GET'])
def question3():
    return jsonify(data['item3'])

@app.route('/3', methods=['GET'])
def question4():
    return jsonify(data['item4'])

@app.route('/result', methods=['Get'])
def result():
    if answers[0] == 'Large scale/ enterprise level project':
        a = a + 2
        r = r + 1
    elif answers[0] == 'Medium scale/business website':
        r = r + 1
    elif answers[0] == 'Small scale/personal project':
        r = r + 1
        v = v + 1
    else:
        msg = 'Error! An answer is missing!'

    return jsonify(results)



if __name__ == '__main__':
    app.run()
