#run "python print.py" to see the data!

from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/print.py')
def index():
    # Connect to the database file
    conn = sqlite3.connect('sqlites.db')

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Execute a SELECT statement to retrieve data from the "data" table
    cursor.execute("SELECT * FROM data")

    # Fetch all the rows of data
    rows = cursor.fetchall()

    # Close the cursor and connection to the database
    cursor.close()
    conn.close()

    return render_template('datas.html', rows=rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8135)