from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Function to connect to MySQL
def get_db_connection():
    return mysql.connector.connect(
        host="wrc353.encs.concordia.ca",
        port="3306",
        user="wrc353_4",
        password="DBCOMP53",
        database="wrc353_4"
    )

# Function to fetch table names
def get_table_names():
    try:
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("SHOW TABLES;")
        tables = [table[0] for table in cursor.fetchall()]
        db.close()
        return tables
    except Exception as e:
        return []

@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    columns = []
    error = None
    tables = get_table_names()  # Fetch table names

    if request.method == 'POST':
        query = request.form.get('sql_query')

        try:
            db = get_db_connection()
            cursor = db.cursor(dictionary=True)
            cursor.execute(query)
            results = cursor.fetchall()
            columns = cursor.column_names
            db.close()
        except Exception as e:
            error = str(e)

    return render_template('index.html', tables=tables, results=results, columns=columns, error=error)

if __name__ == '__main__':
    app.run(debug=True)
