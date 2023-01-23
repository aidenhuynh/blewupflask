from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from datetime import datetime
from model.users import User
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

        # validate date
        if date is None:
            return {'message': 'Date is missing'}, 400
        # validate action
        if action is None:
            return {'message': 'Action is missing'}, 400
        # validate user
        if user is None:
            return {'message': 'User is missing'}, 400
        # validate item
        if item is None:
            return {'message': 'Item is missing'}, 400
        # validate quantity
        if quantity is None:
            return {'message': 'Quantity is missing'}, 400


        inventory_item = Inventory(date=date, action=action, user=user, item=item, quantity=quantity)
        inventory_item.add()

        return {'message': 'Inventory added successfully'}, 201

api.add_resource(InventoryAPI, '/inventory')