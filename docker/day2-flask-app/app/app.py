from flask import Flask
import os

app = Flask(__name__)

@app.get("/")
def home():
    return {
        "message": "Hello from Flask in Docker!",
        "env": os.getenv("ENV", "local")
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


