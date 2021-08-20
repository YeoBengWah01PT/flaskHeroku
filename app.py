from flask import Flask,jsonify,request,g,render_template
import re
import bcrypt

from flask_cors import CORS
from model.User import User
from model.Category import Category

from model.Furniture import Furniture

from validation.Validator import *

app = Flask(__name__)

CORS(app)
# http://localhost:5000?data=test@test.com

@app.route('/test')
def hello():
    userinput="abc123456";

    pattern=re.compile("^[a-zA-Z0-9]{8,}$")#create regex with a pattern

    if(pattern.match(userinput)):
       return ("Input is correct!")
    else:
       return ("Input does not match pattern!")

    return "hello world"


@app.route('/test/<number>', methods=['POST'])
@validateNumber
def hello2(number):
    
    return "Hello input number is fine"

@app.route('/users/<int:userid>')
def getUser(userid):
    try:
        #print(g.userid)
        jsonUsers=User.getUser(userid)
        jsonUsers={"Users":jsonUsers}
        print("jsonusers",jsonUsers)
        return jsonify(jsonUsers),200
    except Exception as err:
        print(err)
        return {},500

@app.route('/users') #define the api route
def getAllUsers():
    try:
        jsonUsers=User.getAllUsers()
        jsonUsers={"Users":jsonUsers}
        return jsonify(jsonUsers)
    except Exception as err:
        print(err)
        return {},500

@app.route('/users', methods=['POST'])
@validateRegister2
#@login_required
def insertUsers():
    print("justin","insertusers2")
    try:
        userJson=request.json
        output=User.insertUser(userJson)
        jsonOutput={"Rows Affected":output}
        return jsonify(jsonOutput),201
    except Exception as err:
        print(err)
        return {"Rows Affected":0},500

@app.route('/users/<int:userid>', methods=['PUT'])
def updateUser(userid):
    try:
        userJson=request.json
        output=User.updateUser(userid,userJson["email"],userJson["password"])
        jsonOutput={"Rows Affected":output}
        return jsonify(jsonOutput),200
    except Exception as err:
        print(err)
        return {"Rows Affected":0},500

@app.route('/users/<int:userid>', methods=['DELETE'])
def deleteUser(userid):
    try:
        userJson=request.json
        output=User.deleteUser(userid)
        jsonOutput={"Rows Affected":output}
        return jsonify(jsonOutput),200
    except Exception as err:
        print(err)
        return {"Rows Affected":0},500


@app.route('/category') #define the api route
def getAllCategory():
    try:
        jsonCat=Category.getAllCategory()
        jsonCat={"Category":jsonCat}
        return jsonify(jsonCat),200
    except Exception as err:
        print(err)
        return {},500


@app.route('/category/<int:catid>/furniture')
def getFurnitureByCatId(catid):
    try:
        jsonFurniture=Furniture.getFurnitureByCatID(catid)
        jsonFurniture={"Furniture":jsonFurniture}
        return jsonify(jsonFurniture),200
    except Exception as err:
        print(err)
        return {},500



@app.route('/users/login', methods=['POST'])
def loginUser():
    try:
        userJson=request.json
        output=User.loginUser(userJson)
        #print(output)
        return jsonify(output)
    except Exception as err:
        print(err)
        return {},500


if __name__ == '__main__':
    app.run(debug=True)
