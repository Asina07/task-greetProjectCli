"""
Flask application for greeting service.
"""

from flask import Flask
from greet import greet

app = Flask(__name__)

@app.route("/")
def home():
    """Return greeting message."""
    return greet("Asina")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
