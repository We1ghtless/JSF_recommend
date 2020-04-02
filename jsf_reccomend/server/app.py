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
@app.route('/first', methods=['Get'])
def first():
    time.sleep(0.5)

    v = 0
    r = 0
    a = 0

    first = json.loads(user_response[0])

# Algorithm to score the frameworks based on user data
    if first["answer"] == 'Frequently updated with dynamic content':
        r = r + 3

    elif first["answer"] == 'Updated occassionally':
        r = r + 1
        v = v + 1

    elif first["answer"] == 'Rarely updated':
        a = a + 1
        v = v + 1

    second = json.loads(user_response[1])

    if second["answer"] == 'Yes':
        v = v + 3

    third = json.loads(user_response[2])

    if third["answer"] == 'Expert':
        a = a + 2
        r = r + 1

    elif third["answer"] == 'Intermediate':
        r = r + 2

    elif third["answer"] == 'Beginner':
        r = r + 1
        v = v + 2

    fourth = json.loads(user_response[3])

    if fourth["answer"] == 'Large scale/enterprise level project':
        a = a + 3
        r = r + 1

    elif fourth["answer"] == 'Medium scale/business website':
        r = r + 2

    elif fourth["answer"] == 'Small scale/personal project':
        r = r + 1
        v = v + 1

    total = a + v + r

    (a_percent) = (float(a) / float(total))*float(100)
    (v_percent) = (float(v) / float(total))*float(100)
    (r_percent) = (float(r) / float(total))*float(100)



    if a_percent >= v_percent and a_percent >= r_percent:
        result = "Angular"
        percent = round(a_percent)
        colour = "#F0A6AD"
        image = "https://angular.io/assets/images/logos/angular/angular.svg"
    elif v_percent >= a_percent and v_percent >= r_percent:
        result = "Vue.js"
        percent = round(v_percent)
        colour = "#C1EDD6"
        image = "https://vuejs.org/images/logo.png"
    elif r_percent >= a_percent and r_percent >= v_percent:
        result = "React"
        percent = round(r_percent)
        colour = "#7BA5CF"
        image = "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9Ii0xMS41IC0xMC4yMzE3NCAyMyAyMC40NjM0OCI+CiAgPHRpdGxlPlJlYWN0IExvZ288L3RpdGxlPgogIDxjaXJjbGUgY3g9IjAiIGN5PSIwIiByPSIyLjA1IiBmaWxsPSIjNjFkYWZiIi8+CiAgPGcgc3Ryb2tlPSIjNjFkYWZiIiBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPgogICAgPGVsbGlwc2Ugcng9IjExIiByeT0iNC4yIi8+CiAgICA8ZWxsaXBzZSByeD0iMTEiIHJ5PSI0LjIiIHRyYW5zZm9ybT0icm90YXRlKDYwKSIvPgogICAgPGVsbGlwc2Ugcng9IjExIiByeT0iNC4yIiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIi8+CiAgPC9nPgo8L3N2Zz4K"


    return jsonify(result, str(percent)+'%', colour, image)

@app.route('/second', methods=['Get'])
def second():
    time.sleep(0.5)

    v = 0
    r = 0
    a = 0

    first = json.loads(user_response[0])

# Algorithm to score the frameworks based on user data
    if first["answer"] == 'Frequently updated with dynamic content':
        r = r + 3

    elif first["answer"] == 'Updated occassionally':
        r = r + 1
        v = v + 1

    elif first["answer"] == 'Rarely updated':
        a = a + 1
        v = v + 1

    second = json.loads(user_response[1])

    if second["answer"] == 'Yes':
        v = v + 3

    third = json.loads(user_response[2])

    if third["answer"] == 'Expert':
        a = a + 2
        r = r + 1

    elif third["answer"] == 'Intermediate':
        r = r + 2

    elif third["answer"] == 'Beginner':
        r = r + 1
        v = v + 2

    fourth = json.loads(user_response[3])

    if fourth["answer"] == 'Large scale/enterprise level project':
        a = a + 3
        r = r + 1

    elif fourth["answer"] == 'Medium scale/business website':
        r = r + 2

    elif fourth["answer"] == 'Small scale/personal project':
        r = r + 1
        v = v + 1

    total = a + v + r

    (a_percent) = (float(a) / float(total))*float(100)
    (v_percent) = (float(v) / float(total))*float(100)
    (r_percent) = (float(r) / float(total))*float(100)

    if a_percent >= v_percent and a_percent <= r_percent or a_percent <= v_percent and a_percent >= r_percent:
        result = "Angular"
        percent = round(a_percent)
        colour = "#F0A6AD"
        image = "https://angular.io/assets/images/logos/angular/angular.svg"
    elif v_percent >= a_percent and v_percent <= r_percent or v_percent <= a_percent and v_percent >= r_percent:
        result = "Vue"
        percent = round(v_percent)
        colour = "#C1EDD6"
        image = "https://vuejs.org/images/logo.png"
    elif r_percent >= a_percent and r_percent <= v_percent or r_percent <= a_percent and r_percent >= v_percent:
        result = "React"
        percent = round(r_percent)
        colour = "#7BA5CF"
        image = "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9Ii0xMS41IC0xMC4yMzE3NCAyMyAyMC40NjM0OCI+CiAgPHRpdGxlPlJlYWN0IExvZ288L3RpdGxlPgogIDxjaXJjbGUgY3g9IjAiIGN5PSIwIiByPSIyLjA1IiBmaWxsPSIjNjFkYWZiIi8+CiAgPGcgc3Ryb2tlPSIjNjFkYWZiIiBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPgogICAgPGVsbGlwc2Ugcng9IjExIiByeT0iNC4yIi8+CiAgICA8ZWxsaXBzZSByeD0iMTEiIHJ5PSI0LjIiIHRyYW5zZm9ybT0icm90YXRlKDYwKSIvPgogICAgPGVsbGlwc2Ugcng9IjExIiByeT0iNC4yIiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIi8+CiAgPC9nPgo8L3N2Zz4K"


    return jsonify(result, str(percent)+'%', colour, image)

@app.route('/third', methods=['Get'])
def third():
    time.sleep(0.5)

    v = 0
    r = 0
    a = 0

    first = json.loads(user_response[0])

# Algorithm to score the frameworks based on user data
    if first["answer"] == 'Frequently updated with dynamic content':
        r = r + 3

    elif first["answer"] == 'Updated occassionally':
        r = r + 1
        v = v + 1

    elif first["answer"] == 'Rarely updated':
        a = a + 1
        v = v + 1

    second = json.loads(user_response[1])

    if second["answer"] == 'Yes':
        v = v + 3

    third = json.loads(user_response[2])

    if third["answer"] == 'Expert':
        a = a + 2
        r = r + 1

    elif third["answer"] == 'Intermediate':
        r = r + 2

    elif third["answer"] == 'Beginner':
        r = r + 1
        v = v + 2

    fourth = json.loads(user_response[3])

    if fourth["answer"] == 'Large scale/enterprise level project':
        a = a + 3
        r = r + 1

    elif fourth["answer"] == 'Medium scale/business website':
        r = r + 2

    elif fourth["answer"] == 'Small scale/personal project':
        r = r + 1
        v = v + 1

    total = a + v + r

    (a_percent) = (float(a) / float(total))*float(100)
    (v_percent) = (float(v) / float(total))*float(100)
    (r_percent) = (float(r) / float(total))*float(100)

    if a_percent <= v_percent and a_percent <= r_percent:
        result = "Angular"
        percent = round(a_percent)
        colour = "#F0A6AD"
        image = "https://angular.io/assets/images/logos/angular/angular.svg"
    elif v_percent <= a_percent and v_percent <= r_percent:
        result = "Vue"
        percent = round(v_percent)
        colour = "#C1EDD6"
        image = "https://vuejs.org/images/logo.png"
    elif r_percent <= a_percent and r_percent <= v_percent:
        result = "React"
        percent = round(r_percent)
        colour = "#7BA5CF"
        image = "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9Ii0xMS41IC0xMC4yMzE3NCAyMyAyMC40NjM0OCI+CiAgPHRpdGxlPlJlYWN0IExvZ288L3RpdGxlPgogIDxjaXJjbGUgY3g9IjAiIGN5PSIwIiByPSIyLjA1IiBmaWxsPSIjNjFkYWZiIi8+CiAgPGcgc3Ryb2tlPSIjNjFkYWZiIiBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPgogICAgPGVsbGlwc2Ugcng9IjExIiByeT0iNC4yIi8+CiAgICA8ZWxsaXBzZSByeD0iMTEiIHJ5PSI0LjIiIHRyYW5zZm9ybT0icm90YXRlKDYwKSIvPgogICAgPGVsbGlwc2Ugcng9IjExIiByeT0iNC4yIiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIi8+CiAgPC9nPgo8L3N2Zz4K"

    return jsonify(result, str(percent)+'%', colour, image)


if __name__ == '__main__':
    app.run()
