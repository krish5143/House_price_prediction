# server.py
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import util

app = Flask(__name__)
CORS(app)  # Enable CORS for API calls


@app.route("/")
def index():
    # Renders templates/index.html
    return render_template("index.html")


@app.route("/get_location_names", methods=["GET"])
def get_location_names():
    return jsonify({"locations": util.get_location_names()})


@app.route("/predict_home_price", methods=["POST"])
def predict_home_price():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    location = data.get("location")
    sqft = data.get("sqft")
    bhk = data.get("bhk")
    bath = data.get("bath")

    if None in [location, sqft, bhk, bath]:
        return jsonify({"error": "Missing fields"}), 400

    estimated_price = util.get_estimated_price(
        location, float(sqft), int(bhk), int(bath)
    )
    return jsonify({"estimated_price": estimated_price})


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    # For local dev: localhost:5000
    # On Render, we won't use app.run(); Render will launch via Gunicorn
    app.run(host="0.0.0.0", port=5000, debug=True)
