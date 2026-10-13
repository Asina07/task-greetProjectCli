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

# @app.route("/case/normal")
# def case_normal():
#     """Test: normal name."""
#     return greet("Zara")

# @app.route("/case/empty")
# def case_empty():
#     """Test: empty string."""
#     return greet("")

# @app.route("/case/whitespace")
# def case_whitespace():
#     """Test: whitespace."""
#     return greet(" ")

# @app.route("/case/multiple")
# def case_multiple():
#     """Test: multiple words."""
#     return greet("Alice and Bob")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
