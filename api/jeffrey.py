from flask import Flask, request, jsonify
import phonenumbers
import sqlite3
from phonenumbers import geocoder
from phonenumbers import timezone
from datetime import datetime

app = Flask(__name__)

@app.route('/lookup', methods=['POST'])
def lookup():
    user_id = request.form['user_id']
    phone_number = request.form['phone_number']

    givenPN = phonenumbers.parse(phone_number, "CH")

    # get location
    ch_number = phonenumbers.parse(phone_number, "CH")
    location = geocoder.description_for_number(ch_number, "en")

    # get timezone
    timezoneOfPN = timezone.time_zones_for_number(givenPN)

    # get current time
    now = datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M:%S")

    # connect to database
    conn = sqlite3.connect('sqlites.db')
    cursor = conn.cursor()

    # insert data into database
    cursor.execute("INSERT INTO phone (user_id, phone_number, location, timezone, time) VALUES (?, ?, ?, ?, ?)",
                   (user_id, phone_number, location, timezoneOfPN[0], time))
    conn.commit()
    conn.close()

    return 'Data added to database'

@app.route('/api/phone')
def get_phone_data():
    conn = sqlite3.connect('sqlites.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM phone")
    data = cursor.fetchall()
    conn.close()

    results = []
    for row in data:
        result = {
            'user_id': row[0],
            'phone_number': row[1],
            'location': row[2],
            'timezone': row[3],
            'time': row[4]
        }
        results.append(result)

    return jsonify(results)

if __name__ == '__main__':
    app.run()