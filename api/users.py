from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from datetime import datetime
from model.users import User
from .. import db
from model.inventory import Inventory

app = Flask(__name__)
api = Api(app)

class UserAPI(Resource):
    def post(self):
        ''' Read data for json body '''
        body = request.get_json()
            
        ''' Avoid garbage in, error checking '''
        # validate name
        name = body.get('name')
        if name is None or len(name) < 2:
            return {'message': f'Name is missing, or is less than 2 characters'}, 210
        # validate uid
        uid = body.get('uid')
        if uid is None or len(uid) < 2:
            return {'message': f'User ID is missing, or is less than 2 characters'}, 210
        # look for password and dob
        password = body.get('password')
        dob = body.get('dob')

        ''' #1: Key code block, setup USER OBJECT '''
        uo = User(name=name, 
                  uid=uid)
            
        ''' Additional garbage error checking '''
        # set password if provided
        if password is not None:
            uo.set_password(password)
        # convert to date type
        if dob is not None:
            try:
                uo.dob = datetime.strptime(dob, '%m-%d-%Y').date()
            except:
                return {'message': f'Date of birth format error {dob}, must be mm-dd-yyyy'}, 210
            
        ''' #2: Key Code block to add user to database '''
        # create user in database
        user = uo.create()
        # success returns json of user
        if user:
            return jsonify(user.read())
        # failure returns error
        return {'message': f'Processed {name}, either a format error or User ID {uid} is duplicate'}, 210

class InventoryAPI(Resource):
    def post(self):
        body = request.get_json()

        date = body.get('date')
        action = body.get('action')
        user = body.get('user')
        item = body.get('item')
        quantity = body.get('quantity')

class InventoryAPI(Resource):
    def post(self):
        body = request.get_json()

        date = body.get('date')
        action = body.get('action')
        user = body.get('user')
        item = body.get('item')
        quantity = body.get('quantity')

        if date is None or action is None or user is None or item is None or quantity is None:
            return {'message': 'Missing one or more required fields'}, 210

        new_inventory = Inventory(date=date, action=action, user=user, item=item, quantity=quantity)
        db.session.add(new_inventory)
        db.session.commit()

        return {'message': 'Inventory added successfully'}, 200

# Adding some sample data to the Inventory table
inventory1 = Inventory(date='2022-01-01', action='purchase', user='John Doe', item='item1', quantity=10)
inventory2 = Inventory(date='2022-01-02', action='purchase', user='Jane Doe', item='item2', quantity=5)
inventory3 = Inventory(date='2022-01-03', action='sale', user='John Smith', item='item1', quantity=2)
inventory4 = Inventory(date='2022-01-04', action='purchase', user='Jane Smith', item='item3', quantity=7)
inventory5 = Inventory(date='2022-01-05', action='sale', user='Bob', item='item2', quantity=3)

db.session.add(inventory1)
db.session.add(inventory2)
db.session.add(inventory3)
db.session.add(inventory4)
db.session.add(inventory5)
db.session.commit()

api.add_resource(InventoryAPI, '/inventory')