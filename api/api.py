from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('sqlites.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM phone")
    rows = cursor.fetchall()
    conn.close()

    return jsonify(rows)

if __name__ == '__main__':
    app.run(debug=True)