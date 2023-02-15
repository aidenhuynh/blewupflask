from flask_cors import CORS
from api import app, db

from api.inventory import inventory_bp

from model.inventory import init_inventory

app.register_blueprint(inventory_bp)



@app.before_first_request
def init_db():
    with app.app_context():
        db.create_all()
        init_inventory


if __name__ == "__main__":
    cors = CORS(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./volumes/sqlite.db"
    app.run(debug=True, host="0.0.0.0", port="8135")
