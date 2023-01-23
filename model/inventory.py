from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///activities.db'
db = SQLAlchemy(app)

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20))
    action = db.Column(db.String(20))
    user = db.Column(db.String(20))
    item = db.Column(db.String(20))
    quantity = db.Column(db.String(20))

    def __init__(self, date, action, user, item, quantity):
        self.date = date
        self.action = action
        self.user = user
        self.item = item
        self.quantity = quantity

@app.route('/activity', methods=['POST'])
def add_activity():
    data = request.get_json()
    date = data['date']
    action = data['action']
    user = data['user']
    item = data['item']
    quantity = data['quantity']

    new_activity = Activity(date, action, user, item, quantity)

    db.session.add(new_activity)
    db.session.commit()

    return jsonify({'message': 'Activity added successfully'})
