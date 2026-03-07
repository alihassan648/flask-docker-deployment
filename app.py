from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head><meta charset="UTF-8"><title>Sohail Ali - DevOps Engineer</title></head>
    <body>
        <h1>Sohail Ali - DevOps Engineer</h1>
        <p>Python Flask app running inside Docker on DigitalOcean.</p>
        <p>Stack: Python | Flask | Docker | Nginx | Linux</p>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
