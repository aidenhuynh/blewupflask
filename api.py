from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import random

# Blueprints allow this code to be procedurally abstracted from main.py, meaning code is not all in one place
app_api2 = Blueprint('api', __name__,
                   url_prefix='/api/tester')  # endpoint prefix avoid redundantly typing /api/jokes over and over

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(app_api2)
data = {
        "Blackjack": {"Wins": 0, "Losses": 0},
        "wtp": {"totalCorrect": 0, "totalIncorrect": 0, "gamesPlayed": 0, "gamesWon": 0},
        "bean": {"num": 0}
    }

class TestAPI:
    class _GetAll(Resource):
        def get(self):
            return jsonify(data)
    
    # Blackjack
    class _PutWin(Resource):
        def put(self):
            data["Blackjack"]["Wins"] = data["Blackjack"]["Wins"] + 1;
            return jsonify(data["Blackjack"])
    class _PutLoss(Resource):
        def put(self):
            data["Blackjack"]["Losses"] = data["Blackjack"]["Losses"] + 1;
            return jsonify(data["Blackjack"])

    # Who's that Pokémon (wtp)
    class _PutCorrect(Resource):
        def put(self):
            data["wtp"]["totalCorrect"] += 1
            return jsonify(data["wtp"])
    class _PutIncorrect(Resource):
        def put(self):
            data["wtp"]["totalIncorrect"] += 1
            return jsonify(data["wtp"])
    class _PutGamePlays(Resource):
        def put(self):
            data["wtp"]["gamesPlayed"] += 1
            return jsonify(data["wtp"])
    class _PutGameWins(Resource):
        def put(self):
            data["wtp"]["gamesWon"] += 1
            return jsonify(data["wtp"])

    class _PutBeans(Resource):
        def put(self):
            data["bean"]["num"] += 1
            return jsonify(data["bean"])

    api.add_resource(_GetAll, '/')
    
    api.add_resource(_PutWin, '/win')
    api.add_resource(_PutLoss, '/loss')
    
    api.add_resource(_PutCorrect, '/correct')
    api.add_resource(_PutIncorrect, '/incorrect')
    api.add_resource(_PutGamePlays, '/gamesPlayed')
    api.add_resource(_PutGameWins, '/gamesWon')

    api.add_resource(_PutBeans, '/bean')


if __name__ == "__main__": 
    # server = "http://127.0.0.1:5000" #local
    server = 'https://swag.nighthawkcodingteams.cf' #web
    url = server + "/api/tester"