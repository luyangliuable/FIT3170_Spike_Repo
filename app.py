from flask import Flask, jsonify, request, Response
import json
import pymongo
from bson.objectid import ObjectId


app = Flask(__name__)

interview_questions = {
    'question1': 'Why should we hire you?',
}

try:
    mongo = pymongo.MongoClient(
        host='localhost',
        port=27017,
    )
    db = mongo.flashcards
    mongo.server_info() # Triger exception if connection fails to the database
except Exception as ex:
    print('failed to connect', ex)

# @app.route('/')
# def home():
#     msg = '<h1>Interview Questions</h1>'
#     return msg


# @app.route('/questions', methods = ['GET'])
# def get_interview_questions(name=""):
#     # return interview_questions
#     return jsonify(interview_questions)

@app.route('/members')
def get_questions():
    # res = []
    # for key in interview_questions.keys():
    #     res.append(interview_questions[key])
    data = list(db.questions.find())
    for question in data:
        question["_id"] = str(question["_id"])
    print(data)

    return json.dumps(data)


@app.route('/add', methods = ['POST'])
def add_interview_questions():
    question = request.json['question']
    print(question)
    try:
        item = {"question": str( question )}
        dbResponse = db.questions.insert_one(item)
        print("inserted id", dbResponse.inserted_id)
    except Exception as error:
        print(error)

    return Response(
        response = json.dumps({'message': 'question added!', "id": f"{dbResponse.inserted_id}"}),
        status=200,
        mimetype="application/json",
    )


if __name__ == "__main__":
    print("name is", __name__)
    app.run(host="localhost", port=3001, debug=True)
