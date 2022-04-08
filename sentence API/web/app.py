from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import bcrypt
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.SentencesDatabase
users = db["Users"]

@app.route('/')
def hello_world():
    return "Welcome to sentence API service"

class Register(Resource):

    def post(self):
        # step 1: get posted data by user
        postedData = request.get_json()

        # step 2: get data
        username = postedData["username"]
        password = postedData["password"]
        # validation is skipped for simplicity

        # for passwords, lets do hashing
        hashed_pw = hashed_pw = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

        users.insert_one({
            "Username": username,
            "Password": hashed_pw,
            "Sentence": "",
            "Tokens": 6
        })

        retJson = {"status":200,
        'msg': "You succesfully signed up for the API"}

        return jsonify(retJson)

class Store(Resource):

    def post(self):
        # step 1: get posted data by user
        postedData = request.get_json()

        # step 2: read data
        username = postedData["username"]
        password = postedData["password"]
        sentence = postedData["sentence"]

        # step 3: verify the username and password match
        correct_pw = verifyPw(username, password)

        if not correct_pw:
            retJson = {
                "status": 302
            }
            return jsonify(retJson)
        
        # step 4: verify user has enough tokens
        num_tokens = countTokens(username)
        print(num_tokens)
        if num_tokens <= 0:
            retJson = {
                "status": 301
            }
            return jsonify(retJson)

        # step 5: store the sentence, return status code and minus the token
        users.update_one({
            "Username": username
            },
            {"$set":{
                "Sentence":sentence,
                "Tokens":num_tokens-1
                }
            })

        retJson = {
            "status": 200,
            "msg": "Sentence saved succesfully"
        }

        return jsonify(retJson)

class GetSentence(Resource):
    def post(self):
        # step 1: get posted data by user
        postedData = request.get_json()

        # step 2: read data
        username = postedData["username"]
        password = postedData["password"]

        # step 3: verify the username and password match
        correct_pw = verifyPw(username, password)

        if not correct_pw:
            retJson = {
                "status": 302
            }
            return jsonify(retJson)

        num_tokens = countTokens(username)

        if num_tokens <= 0:
            retJson = {
                "status": 301
            }
            return jsonify(retJson)

        # minus 1 token
        users.update_one({
            "Username": username
            },
            {"$set":{
                "Tokens":num_tokens-1
                }
            })

        sentence = users.find_one({
            "Username":username
        })["Sentence"]

        retJson = {
            "status": 200,
            "sentence": sentence
        }

        return jsonify(retJson)

api.add_resource(Register, "/register")
api.add_resource(Store, "/store")
api.add_resource(GetSentence, "/getSentence")

def verifyPw(username, password):
    hashed_pw = users.find_one({
        "Username":username
    })["Password"] # will return array of users so use 0 and return password as well

    if bcrypt.hashpw(password.encode('utf8'), hashed_pw) == hashed_pw:
        return True
    else:
        return False

def countTokens(username):
    tokens = users.find_one({
        "Username":username
    })["Tokens"]
    return tokens

if __name__=="__main__":
    app.run(host='0.0.0.0')
