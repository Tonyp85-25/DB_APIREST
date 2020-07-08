"""
A user registers : 0 token
Each user gets 10 tokens
The storage of a sentence in our Db : 1 token
Retrieve the sentence : 1 token
"""
from flask import Flask, jsonify, request, render_template
from flask_restful import Api, Resource
import os
from pymongo import MongoClient
import bcrypt


app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.SentencesDatabase
users = db["Users"]


class Register(Resource):
    def post(self):
        # First, get the data posted by the user
        data = request.get_json()

        username = data["username"]
        password = data["password"]
        hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt())

        users.insert({
            "Username": username,
            "Password": hashed_pw,
            "Sentence": "",
            "Tokens": 10
        })

        retJson = {
            "status": 200,
            "msg": "You successfully signed up for the API"
        }
        return jsonify(retJson)


class Store(Resource):
    def post(self):

        # 1. get the data
        data = request.get_json()
        username = data["username"]
        password = data["password"]
        sentence = data["sentence"]

        # 2. Verify username and password
        correct_pw = verify_pw(username, password)
        if not correct_pw:
            retJson = {
                "status": 302
            }
            return jsonify(retJson)

        # 3. Verify if the user has enough tokens
        num_tokens = verify_tokens(username)
        if num_tokens <= 0:
            retJson = {
                "status": 301
            }
            return jsonify(retJson)

        # 4. store the sentence,take one token and returns ok
        users.update({
            "Username": username}, {
                "$set": {
                    "Sentence": sentence,
                    "Tokens": num_tokens - 1
                }
        })

        retJson = {
            "status": 200,
            "msg": "Sentence saved successfully "
        }
        return jsonify(retJson)
        # hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt())


api.add_resource(Register, '/register')
api.add_resource(Store, '/store')


