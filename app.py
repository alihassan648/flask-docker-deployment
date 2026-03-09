from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db():
    return psycopg2.connect(
        host=os.environ.get("DB_HOST", "db"),
        database=os.environ.get("DB_NAME", "appdb"),
        user=os.environ.get("DB_USER", "sohail"),
        password=os.environ.get("DB_PASSWORD", "secret")
    )

@app.route("/")
def home():
    return """
    <html>
    <head><meta charset="UTF-8">
    <title>Sohail Ali - DevOps Engineer</title>
    </head>
    <body>
        <h1>Sohail Ali - DevOps Engineer</h1>
        <p>Stack: Python | Flask | PostgreSQL | Docker | Nginx</p>
    </body>
    </html>
    """

@app.route("/health")
def health():
    try:
        conn = get_db()
        conn.close()
        return jsonify({"status": "ok", "database": "connected"}), 200
    except Exception as e:
        return jsonify({"status": "error", "database": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
