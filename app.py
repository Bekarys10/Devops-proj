from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        database=os.getenv("DB_NAME", "mydb"),
        user=os.getenv("DB_USER", "user"),
        password=os.getenv("DB_PASSWORD", "pass")
    )
    return conn

@app.route("/weather")
def weather():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS weather (location TEXT, temperature TEXT, condition TEXT);")
    cur.execute("SELECT * FROM weather;")
    rows = cur.fetchall()
    if not rows:
        cur.execute("INSERT INTO weather VALUES ('Almaty', '22°C', 'Sunny');")
        conn.commit()
        cur.execute("SELECT * FROM weather;")
        rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([
        {"location": row[0], "temperature": row[1], "condition": row[2]} for row in rows
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
