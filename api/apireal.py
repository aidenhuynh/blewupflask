from flask import Blueprint, request
from flask_restful import Api, Resource 
import requests, json

mainData = Blueprint('bruh', __name__, url_prefix='/api/mainData')

api = Api(mainData)

data = [
    {
        "uid":"aidenhuynh",
        "userData":[
            {
                "id":1,
                "date":"01-05-2023",
                "action":"Shipped",
                "item":"Pencils",
                "quantity":"1500",
            },
            {
                "id":2,
                "date":"02-07-2023",
                "action":"Delivered",
                "item":"Pens",
                "quantity":"1000",
            },
            {
                "id":3,
                "date":"02-02-2023",
                "action":"Packaged",
                "item":"Markers",
                "quantity":"300",
            },
            {
                "id":4,
                "date":"01-15-2023",
                "action":"In Transit",
                "item":"Highlighters",
                "quantity":"100",
            },
            {
                "id":5,
                "date":"01-05-2023",
                "action":"Shipped",
                "item":"Pencils",
                "quantity":"1500",
            },
            {
                "id":6,
                "date":"02-07-2023",
                "action":"Delivered",
                "item":"Pens",
                "quantity":"1000",
            },
            {
                "id":7,
                "date":"02-02-2023",
                "action":"Packaged",
                "item":"Markers",
                "quantity":"300",
            },
            {
                "id":8,
                "date":"01-15-2023",
                "action":"In Transit",
                "item":"Highlighters",
                "quantity":"100",
            },
            {
                "id":9,
                "date":"01-05-2023",
                "action":"Shipped",
                "item":"Pencils",
                "quantity":"1500",
            }   
        ]
    },
    {
        "uid":"TheGerbil21",
        "userData":[
            {
                "id":1,
                "date":"01-05-2023",
                "action":"Shipped",
                "item":"Pencils",
                "quantity":"1500",
            },
            {
                "id":2,
                "date":"02-07-2023",
                "action":"Delivered",
                "item":"Pens",
                "quantity":"1000",
            },
            {
                "id":3,
                "date":"02-02-2023",
                "action":"Packaged",
                "item":"Markers",
                "quantity":"300",
            },
            {
                "id":4,
                "date":"01-15-2023",
                "action":"In Transit",
                "item":"Highlighters",
                "quantity":"100",
            },
            {
                "id":5,
                "date":"01-05-2023",
                "action":"Shipped",
                "item":"Pencils",
                "quantity":"1500",
            },
        ]
    },
]

class mainDataApi:

    class _get(Resource):
        def get(self):
            return data

    class _put(Resource):
        def put(self):
            global data
            body = request.get_data(..., True)
            parsed = json.loads(body)
            print(parsed)
            key = parsed[0]
            newData = parsed[1]
            data[int(key)]["userData"].append(newData)
            return data
    
    class _delete(Resource):
        def remove(self):
            global data
            body = request.get_data(..., True)
            parsed = json.loads(body)
            print(parsed)
            key = parsed[0]
            id = parsed[1]
            data[int(key)]["userData"].remove(id)
            return data

    api.add_resource(_get, '/')
    api.add_resource(_put, '/PUT')
    api.add_resource(_delete, '/DELETE')
