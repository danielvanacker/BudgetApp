import flask
from flask import jsonify, request, Response, make_response, g
from flask_cors import CORS, cross_origin
from .service import *
from .auth import *

app = flask.Flask(__name__)
cors = CORS(app, origins=['localhost:4200'])
app.config["DEBUG"] = True

@app.route('/people', methods=['GET'])
@cross_origin()
def endGetPeople():
    userId = verifyUser(request.headers.get('token'))
    if(isInvalid(userId)):
        return invalidUserResponse()
    response = jsonify(getAllPeople(userId))
    return response

@app.route('/categories', methods=['GET'])
@cross_origin()
def endGetCategories():
    userId = verifyUser(request.headers.get('token'))
    if(isInvalid(userId)):
        return invalidUserResponse()
    response = jsonify(getAllCategories(userId))
    return response

@app.route('/transaction', methods=['POST'])
@cross_origin()
def endInsertTransaction():
    userId = verifyUser(request.headers.get('token'))
    if(isInvalid(userId)):
        return invalidUserResponse()
    response = jsonify(insertTransaction(request.json, userId))
    return response

@app.route('/transactions', methods=['GET'])
@cross_origin()
def endGetAllTransactions():
    userId = verifyUser(request.headers.get('token'))
    if(isInvalid(userId)):
        return invalidUserResponse()
    response = jsonify(getAllTransactions(userId))
    return response

@app.route('/budget/elapsed', methods=['GET'])
@cross_origin()
def endGetElapsedBudget():
    userId = verifyUser(request.headers.get('token'))
    if(isInvalid(userId)):
        return invalidUserResponse()
    response = jsonify(getElapsedBudget(userId))
    return response

@app.route('/transaction/months', methods=['GET'])
@cross_origin()
def endGetTransactionMonths():
    userId = verifyUser(request.headers.get('token'))
    if(isInvalid(userId)):
        return invalidUserResponse()
    response = jsonify(getTransactionMonths(userId))
    return response

@app.route('/validate_session', methods=['POST'])
@cross_origin()
def endValidateSession():
    userId = verifyUser(request.json['token'])
    if(isInvalid(userId)):
        return invalidUserResponse()
    response = validateSession(userId)
    return response

def isInvalid(userId):
    return userId == "invalid"

def invalidUserResponse():
    return make_response(jsonify("invalid user credentials"), 401, {})

if __name__ == "__main__":
    app.run(use_reloader=True, debug=True)