from flask import Blueprint, request
from flask_restful import Api, Resource 
import requests

mainData = Blueprint('marketfake', __name__, url_prefix='/api/marketfake')

api = Api(mainData)

data = [
    {
        "uid":"aidenhuynh",
        "userData":[
            {
                "id":1,
                "date":"01-05-2023",
                "product":"Shipped",
                "user":"aidenhuynh",
                "cost":"Pencils",
                "stock":"1500",
            },
            {
                "id":2,
                "date":"02-07-2023",
                "product":"Delivered",
                "user":"TheGerbil21",
                "cost":"Pens",
                "stock":"1000",
            },
            {
                "id":3,
                "date":"02-02-2023",
                "product":"Packaged",
                "user":"aidenhuynh",
                "cost":"Markers",
                "stock":"300",
            },
            {
                "id":4,
                "date":"01-15-2023",
                "product":"In Transit",
                "user":"aidenhuynh",
                "cost":"Highlighters",
                "stock":"100",
            },
            {
                "id":5,
                "date":"01-05-2023",
                "product":"Shipped",
                "user":"aidenhuynh",
                "cost":"Pencils",
                "stock":"1500",
            },
            {
                "id":6,
                "date":"02-07-2023",
                "action":"Delivered",
                "user":"TheGerbil21",
                "item":"Pens",
                "quantity":"1000",
            },
            {
                "id":7,
                "date":"02-02-2023",
                "action":"Packaged",
                "user":"aidenhuynh",
                "item":"Markers",
                "quantity":"300",
            },
            {
                "id":8,
                "date":"01-15-2023",
                "action":"In Transit",
                "user":"aidenhuynh",
                "item":"Highlighters",
                "quantity":"100",
            },
            {
                "id":9,
                "date":"01-05-2023",
                "action":"Shipped",
                "user":"aidenhuynh",
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
                "user":"aidenhuynh",
                "item":"Pencils",
                "quantity":"1500",
            },
            {
                "id":2,
                "date":"02-07-2023",
                "action":"Delivered",
                "user":"TheGerbil21",
                "item":"Pens",
                "quantity":"1000",
            },
            {
                "id":3,
                "date":"02-02-2023",
                "action":"Packaged",
                "user":"aidenhuynh",
                "item":"Markers",
                "quantity":"300",
            },
            {
                "id":4,
                "date":"01-15-2023",
                "action":"In Transit",
                "user":"aidenhuynh",
                "item":"Highlighters",
                "quantity":"100",
            },
            {
                "id":5,
                "date":"01-05-2023",
                "action":"Shipped",
                "user":"aidenhuynh",
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

    class _append(Resource):
        def post(self):
            global data
            body = request.get_data(..., True)
            print(body)
            data.append(body)
            return data 
    
    class _remove(Resource):
        def post(self):
            global data
            body = request.get_data(..., True)
            data.remove(body)
            return data

    api.add_resource(_get, '/')
    api.add_resource(_append, '/PUT')
    api.add_resource(_remove, '/DELETE')
