from flask import Blueprint, request
from flask_restful import Api, Resource, reqparse
from __init__ import db
from model.market import MarketEntry

market_bp = Blueprint("market", __name__)
market_api = Api(market_bp)


class MarketAPI(Resource):
    def get(self):
        date = request.args.get("date")
        entry = db.session.query(MarketEntry).filter_by(_date=date).all()
        print("abc" + str(date))
        if len(entry) != 0:
            return [e.to_dict() for e in entry]
        return {"error": "date not found"}, 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("date", required=True, type=str)
        parser.add_argument("product", required=True, type=str)
        parser.add_argument("cost", required=True, type=int)
        parser.add_argument("stock", required=True, type=int)
        parser.add_argument("market_name", required=True, type=str)
        args = parser.parse_args()

        entry = MarketEntry(
            args["date"],
            args["product"],
            args["cost"],
            args["stock"],
        )
        try:
            db.session.add(entry)
            db.session.commit()
            return entry.to_dict(), 201
        except Exception as e:
            db.session.rollback()
            return {"error": f"server error: {e}"}, 500

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", required=True, type=int)
        parser.add_argument("product", required=False, type=str)
        parser.add_argument("cost", required=False, type=int)
        parser.add_argument("stock", required=False, type=int)
        parser.add_argument("market_name", required=True, type=str)
        args = parser.parse_args()

        try:
            entry = db.session.query(MarketEntry).get(args["id"])
            if entry:
                if args["product"]:
                    entry.calories = args["product"]
                if args["cost"]:
                    entry.protein = args["cost"]
                if args["stock"]:
                    entry.extra_notes = args["stock"]
                if args["market_name"]:
                    entry.extra_notes = args["market_name"]
                db.session.commit()
                return entry.to_dict()
            else:
                return {"error": "entry not found"}, 404
        except Exception as e:
            db.session.rollback()
            return {"error": f"server error: {e}"}, 500

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", required=True, type=int)
        args = parser.parse_args()

        try:
            entry = db.session.query(MarketEntry).get(args["id"])
            if entry:
                db.session.delete(entry)
                db.session.commit()
                return entry.to_dict()
            else:
                return {"error": "entry not found"}, 404
        except Exception as e:
            db.session.rollback()
            return {"error": f"server error: {e}"}, 500


market_api.add_resource(MarketAPI, "/market")