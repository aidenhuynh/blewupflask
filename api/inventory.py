from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class InventoryAPI(Resource):
    def post(self):
        # Get the data from the request body
        json_data = request.get_json()
        item = json_data.get('item')
        quantity = json_data.get('quantity')
        user = json_data.get('user')
        
        # Validate the data
        if item is None or len(item) == 0:
            return {'message': 'Item is required'}, 400
        if quantity is None or quantity <= 0:
            return {'message': 'Quantity is required and must be greater than 0'}, 400
        if user is None or len(user) == 0:
            return {'message': 'User is required'}, 400

        # Insert the data into the database
        # Code to insert data into the database goes here

        return {'message': 'Inventory added successfully'}, 201

# Create the endpoint
api.add_resource(InventoryAPI, '/inventory')

if __name__ == '__main__':
    app.run(debug=True)
