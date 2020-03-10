# Import dependancies
from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import time
from decimal import *

# configuration
DEBUG = True

# Retrieve question data from json file
with open ('data.json') as read_file:
    data = json.load(read_file)

# Array of user input answers
user_response = []

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# Response route to add user data to array
@app.route('/answers', methods=['GET', 'POST'])
def addAnswer():
    i = 0

# Retrieve data in json format
    if request.method == 'POST' and i < 5:
        req_data = request.get_json()
        data = json.dumps(req_data)

        user_response.insert(i, data)
        message = 'SUCCESS'
        i = i + 1

        print user_response

    if i == 4:
        i = i - 4

    return message

# Routes which deliver the question data to front end
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

# Result response route which supplies the scores for each framework
@app.route('/result', methods=['Get'])
def result():
    time.sleep(0.5)

    v = 0
    r = 0
    a = 0

    pig = json.loads(user_response[0])

# Algorithm to score the frameworks based on user data
    if pig["answer"] == 'Frequently updated with dynamic content':
        r = r + 2

    elif pig["answer"] == 'Updated occassionally':
        r = r + 1
        v = v + 1

    elif pig["answer"] == 'Rarely updated':
        a = a + 1
        v = v + 1

    horse = json.loads(user_response[1])

    if horse["answer"] == 'Yes':
        v = v + 2

    cow = json.loads(user_response[2])

    if cow["answer"] == 'Expert':
        a = a + 1
        r = r + 1

    elif cow["answer"] == 'Intermediate':
        r = r + 2

    elif cow["answer"] == 'Beginner':
        r = r + 1
        v = v + 2

    duck = json.loads(user_response[3])

    if duck["answer"] == 'Large scale/enterprise level project':
        a = a + 2
        r = r + 1

    elif duck["answer"] == 'Medium scale/business website':
        r = r + 1

    elif duck["answer"] == 'Small scale/personal project':
        r = r + 1
        v = v + 1

    total = a + v + r

    (a_percent) = (float(a) / float(total))*float(100)
    (v_percent) = (float(v) / float(total))*float(100)
    (r_percent) = (float(r) / float(total))*float(100)

    if a_percent >= v_percent and a_percent >= r_percent:
        result = "Angular"
        percent = round(a_percent)
    elif v_percent >= a_percent and v_percent >= r_percent:
        result = "Vue"
        percent = round(v_percent)
    elif r_percent >= a_percent and r_percent >= v_percent:
        result = "React"
        percent = round(r_percent)


    return jsonify(result, str(percent)+'%')


if __name__ == '__main__':
    app.run()
