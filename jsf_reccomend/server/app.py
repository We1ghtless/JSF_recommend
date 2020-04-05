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

        response = json.loads(data)

        user_response.insert(i, response)
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
    time.sleep(0.2)

    v = 0
    r = 0
    a = 0

    first = user_response[0]

# Algorithm to score the frameworks based on user data
    if first["answer"] == 'Frequently updated with dynamic content':
        r = r + 3

    elif first["answer"] == 'Updated occassionally':
        r = r + 1
        v = v + 1

    elif first["answer"] == 'Rarely updated':
        a = a + 1
        v = v + 1

    second = user_response[1]

    if second["answer"] == 'Yes':
        v = v + 3

    third = user_response[2]

    if third["answer"] == 'Expert':
        a = a + 2
        r = r + 1

    elif third["answer"] == 'Intermediate':
        r = r + 2

    elif third["answer"] == 'Beginner':
        r = r + 1
        v = v + 2

    fourth = user_response[3]

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

    # First
    if a_percent >= v_percent and a_percent >= r_percent:
        result = "Angular"
        percent = round(a_percent)
        colour = "#F0A6AD"
        image = "https://angular.io/assets/images/logos/angular/angular.svg"
        content = "Angular is an extensive enterprise scale framework excellent for building complex web sites."
        link = "https://angular.io/"
    elif v_percent >= a_percent and v_percent >= r_percent:
        result = "Vue.js"
        percent = round(v_percent)
        colour = "#C1EDD6"
        image = "https://vuejs.org/images/logo.png"
        content = "Vue is a light-weight performant JavaScript framework which is easy to learn."
        link = "https://vuejs.org/"
    elif r_percent >= a_percent and r_percent >= v_percent:
        result = "React"
        percent = round(r_percent)
        colour = "#7BA5CF"
        image = "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9Ii0xMS41IC0xMC4yMzE3NCAyMyAyMC40NjM0OCI+CiAgPHRpdGxlPlJlYWN0IExvZ288L3RpdGxlPgogIDxjaXJjbGUgY3g9IjAiIGN5PSIwIiByPSIyLjA1IiBmaWxsPSIjNjFkYWZiIi8+CiAgPGcgc3Ryb2tlPSIjNjFkYWZiIiBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPgogICAgPGVsbGlwc2Ugcng9IjExIiByeT0iNC4yIi8+CiAgICA8ZWxsaXBzZSByeD0iMTEiIHJ5PSI0LjIiIHRyYW5zZm9ybT0icm90YXRlKDYwKSIvPgogICAgPGVsbGlwc2Ugcng9IjExIiByeT0iNC4yIiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIi8+CiAgPC9nPgo8L3N2Zz4K"
        content = "React is the industry leader and most popular framework for its extensibility and ability to create interactive UIs"
        link = "https://reactjs.org"

    # Second
    if "Angular" != result:
        if (a_percent >= v_percent and a_percent <= r_percent) or (a_percent <= v_percent and a_percent >= r_percent):
            result2 = "Angular"
            percent2 = round(a_percent)
            colour2 = "#F0A6AD"
            image2 = "https://angular.io/assets/images/logos/angular/angular.svg"
            content2 = "Angular is an extensive enterprise scale framework excellent for building complex web sites."
            link2 = "https://angular.io/"

    if "Vue" != result:
        if(v_percent >= a_percent and v_percent <= r_percent) or (v_percent <= a_percent and v_percent >= r_percent):
            result2 = "Vue"
            percent2 = round(v_percent)
            colour2 = "#C1EDD6"
            image2 = "https://vuejs.org/images/logo.png"
            content2 = "Vue is a light-weight performant JavaScript framework which is easy to learn."
            link2 = "https://vuejs.org/"

    if "React" != result:
        if (r_percent >= a_percent and r_percent <= v_percent) or (r_percent <= a_percent and r_percent >= v_percent):
            result2 = "React"
            percent2 = round(r_percent)
            colour2 = "#7BA5CF"
            image2 = "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9Ii0xMS41IC0xMC4yMzE3NCAyMyAyMC40NjM0OCI+CiAgPHRpdGxlPlJlYWN0IExvZ288L3RpdGxlPgogIDxjaXJjbGUgY3g9IjAiIGN5PSIwIiByPSIyLjA1IiBmaWxsPSIjNjFkYWZiIi8+CiAgPGcgc3Ryb2tlPSIjNjFkYWZiIiBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPgogICAgPGVsbGlwc2Ugcng9IjExIiByeT0iNC4yIi8+CiAgICA8ZWxsaXBzZSByeD0iMTEiIHJ5PSI0LjIiIHRyYW5zZm9ybT0icm90YXRlKDYwKSIvPgogICAgPGVsbGlwc2Ugcng9IjExIiByeT0iNC4yIiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIi8+CiAgPC9nPgo8L3N2Zz4K"
            content2 = "React is the industry leader and most popular framework for its extensibility and ability to create interactive UIs"
            link2 = "https://reactjs.org"

        # Third
    if "Angular" != result2:
        if a_percent <= v_percent and a_percent <= r_percent and "Angular" != result:
            result3 = "Angular"
            percent3 = round(a_percent)
            colour3 = "#F0A6AD"
            image3 = "https://angular.io/assets/images/logos/angular/angular.svg"
            content3 = "Angular is an extensive enterprise scale framework excellent for building complex web sites."
            link3 = "https://angular.io/"
    if "Vue" != result2:
        if v_percent <= a_percent and v_percent <= r_percent and "Vue" != result:
            result3 = "Vue"
            percent3 = round(v_percent)
            colour3 = "#C1EDD6"
            image3 = "https://vuejs.org/images/logo.png"
            content3 = "Vue is a light-weight performant JavaScript framework which is easy to learn."
            link3 = "https://vuejs.org/"
    if "React" != result2:
        if r_percent <= a_percent and r_percent <= v_percent and "React" != result:
            result3 = "React"
            percent3 = round(r_percent)
            colour3 = "#7BA5CF"
            image3 = "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9Ii0xMS41IC0xMC4yMzE3NCAyMyAyMC40NjM0OCI+CiAgPHRpdGxlPlJlYWN0IExvZ288L3RpdGxlPgogIDxjaXJjbGUgY3g9IjAiIGN5PSIwIiByPSIyLjA1IiBmaWxsPSIjNjFkYWZiIi8+CiAgPGcgc3Ryb2tlPSIjNjFkYWZiIiBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiPgogICAgPGVsbGlwc2Ugcng9IjExIiByeT0iNC4yIi8+CiAgICA8ZWxsaXBzZSByeD0iMTEiIHJ5PSI0LjIiIHRyYW5zZm9ybT0icm90YXRlKDYwKSIvPgogICAgPGVsbGlwc2Ugcng9IjExIiByeT0iNC4yIiB0cmFuc2Zvcm09InJvdGF0ZSgxMjApIi8+CiAgPC9nPgo8L3N2Zz4K"
            content3 = "React is the industry leader and most popular framework for its extensibility and ability to create interactive UIs"
            link3 = "https://reactjs.org"

    return jsonify(result, str(percent)+'%', colour, image, content, link, result2, str(percent2)+'%', colour2, image2, content2, link2, result3, str(percent3)+'%', colour3, image3, content3, link3, user_response[0]['answer'], user_response[1]['answer'], user_response[2]['answer'], user_response[3]['answer'])

if __name__ == '__main__':
    app.run()
