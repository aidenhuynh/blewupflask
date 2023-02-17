from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource, reqparse
from __init__ import db
from model.inventory import InventoryEntry

inventory_bp = Blueprint('inventory', __name__,
                   url_prefix='/api/inventory')

inventory_api = Api(inventory_bp)


class InventoryAPI():
    class _Create(Resource):
        def post(self):
            parser = reqparse.RequestParser()
            parser.add_argument("id", required=True, type=str)
            parser.add_argument("action", required=True, type=int)
            parser.add_argument("quantity", required=True, type=int)
            parser.add_argument("company", required=True, type=int)
            parser.add_argument("product", required=True, type=int)
            parser.add_argument("status", required=True, type=str)
            parser.add_argument("inventory_name", required=True, type=str)
            args = parser.parse_args()

            entry = InventoryEntry(
                args["id"],
                args["inventory_name"],
                args["action"],
                args["quantity"],
                args["company"],
                args["product"],
                args["status"],
            )
            try:
                db.session.add(entry)
                db.session.commit()
                return entry.to_dict(), 201
            except Exception as e:
                db.session.rollback()
                return {"error": f"server error: {e}"}, 500
    class _Read(Resource):
        def post(self):
            parser = reqparse.RequestParser()
            parser.add_argument('company', type=str)
            args = parser.parse_args()
            company = args['company']
            entries = db.session.query(InventoryEntry).filter_by(_company=company).all()
            if entries:
                return jsonify([e.to_dict() for e in entries])
            else:
                return {"error": "inventory not found for company"}, 404
    inventory_api.add_resource(_Read, "/")
    inventory_api.add_resource(_Create, "/create")
