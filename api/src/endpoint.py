import flask
from flask import jsonify, request, Response, make_response
from flask_cors import CORS, cross_origin
import service
import auth

app = flask.Flask(__name__)
cors = CORS(app, resources={r"/people": {"origins": "http://localhost:4200"}})
app.config["DEBUG"] = True

@app.route('/people', methods=['GET'])
def getPeople():
    userId = auth.verifyUser(request.headers.get('token'))
    if(isInvalid(userId)):
        return invalidUserResponse()
    response = jsonify(service.getAllPeople(userId))
    return response

@app.route('/categories', methods=['GET'])
@cross_origin()
def getCategories():
    userId = auth.verifyUser(request.headers.get('token'))
    if(isInvalid(userId)):
        return invalidUserResponse()
    response = jsonify(service.getAllCategories(userId))
    return response

@app.route('/transaction', methods=['POST'])
@cross_origin()
def insertTransaction():
    userId = auth.verifyUser(request.headers.get('token'))
    if(isInvalid(userId)):
        return invalidUserResponse()
    response = jsonify(service.insertTransaction(request.json, userId))
    return response

@app.route('/transactions', methods=['GET'])
@cross_origin()
def getAllTransactions():
    userId = auth.verifyUser(request.headers.get('token'))
    if(isInvalid(userId)):
        return invalidUserResponse()
    response = jsonify(service.getAllTransactions(userId))
    return response

@app.route('/budget/elapsed', methods=['GET'])
@cross_origin()
def getElapsedBudget():
    userId = auth.verifyUser(request.headers.get('token'))
    if(isInvalid(userId)):
        return invalidUserResponse()
    response = jsonify(service.getElapsedBudget(userId))
    return response

@app.route('/transaction/months', methods=['GET'])
@cross_origin()
def getTransactionMonths():
    userId = auth.verifyUser(request.headers.get('token'))
    if(isInvalid(userId)):
        return invalidUserResponse()
    response = jsonify(service.getTransactionMonths(userId))
    return response

@app.route('/validate_session', methods=['POST'])
@cross_origin()
def validateSession():
    userId = auth.verifyUser(request.json['token'])
    if(isInvalid(userId)):
        return invalidUserResponse()
    response = service.validateSession(userId)
    return response

def isInvalid(userId):
    return userId == "invalid"

def invalidUserResponse():
    return make_response(jsonify("invalid user credentials"), 401, {})

app.run()