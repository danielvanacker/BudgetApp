import flask
from flask import jsonify, request, Response, make_response, g
from flask_cors import CORS, cross_origin
from .service import *
from .auth import *

app = flask.Flask(__name__)
cors = CORS(app)
app.config["DEBUG"] = True

@app.route('/people', methods=['GET', 'POST'])
def endGetPeople():
    userId = verifyUser(request.headers.get('token'))
    if(isInvalid(userId)):
        return invalidUserResponse()
    if(flask.request.method == 'GET'):
        response = jsonify(getAllPeople(userId))
    else: #method == 'POST'
        response = jsonify(insertPerson(request.json, userId))
    return response

@app.route('/categories', methods=['GET', 'POST'])
def endCategories():
    userId = verifyUser(request.headers.get('token'))
    if(isInvalid(userId)):
        return invalidUserResponse()
    if(flask.request.method == 'GET'):
        response = jsonify(getAllCategories(userId))
    else: #method == 'POST'
        response = jsonify(insertCategory(request.json, userId))
    return response

@app.route('/income', methods=['GET'])
def endIncome():
    userId = verifyUser(request.headers.get('token'))
    if(isInvalid(userId)):
        return invalidUserResponse()

    response = jsonify(getMonthlyIncome(request.args.get('month'), userId))
    return response

@app.route('/expenses', methods=['GET'])
def endExpenses():
    userId = verifyUser(request.headers.get('token'))
    if(isInvalid(userId)):
        return invalidUserResponse()

    response = jsonify(getMonthlyExpenses(request.args.get('month'), userId))
    return response 

@app.route('/owed', methods=['GET'])
def endOwedMoney():
    userId = verifyUser(request.headers.get('token'))
    if(isInvalid(userId)):
        return invalidUserResponse()

    response = jsonify(getOwedMoney(userId))
    return response 

@app.route('/transactions', methods=['GET', 'POST'])
def endTransactions():
    userId = verifyUser(request.headers.get('token'))
    if(isInvalid(userId)):
        return invalidUserResponse()
    
    if(flask.request.method == 'GET'):
        response = jsonify(getAllTransactions(userId))
    else: #method == 'POST'
        response = jsonify(insertTransaction(request.json, userId))
    return response

@app.route('/budget/elapsed', methods=['GET'])
def endElapsedBudget():
    userId = verifyUser(request.headers.get('token'))
    if(isInvalid(userId)):
        return invalidUserResponse()
    response = jsonify(getElapsedBudget(userId))
    return response

@app.route('/budget/remaining', methods=['GET'])
def endBudgetRemaining():
    userId = verifyUser(request.headers.get('token'))
    if(isInvalid(userId)):
        return invalidUserResponse()
    response = jsonify(getBudgetRemaining(request.args.get('month'), request.args.get('year'), userId))
    return response

@app.route('/budget', methods=['POST'])
def endInsertBudget():
    userId = verifyUser(request.headers.get('token'))
    if(isInvalid(userId)):
        return invalidUserResponse()
    response = jsonify(insertBudget(request.json, userId))
    return response

@app.route('/transaction/months', methods=['GET'])
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