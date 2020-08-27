import flask
import service
from flask import jsonify, request
from flask_cors import CORS, cross_origin

app = flask.Flask(__name__)
cors = CORS(app, resources={r"/people": {"origins": "http://localhost:4200"}})
app.config["DEBUG"] = True

@app.route('/people', methods=['GET'])
def getPeople():
    response = jsonify(service.getAllPeople())
    return response

@app.route('/categories', methods=['GET'])
@cross_origin()
def getCategories():
    response = jsonify(service.getAllCategories())
    return response

@app.route('/transaction', methods=['POST'])
@cross_origin()
def insertTransaction():
    response = jsonify(service.insertTransaction(request.json))
    return response

@app.route('/transactions', methods=['GET'])
@cross_origin()
def getAllTransactions():
    response = jsonify(service.getAllTransactions())
    return response

app.run()