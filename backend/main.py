from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "CX Analytics Platform Running"}

@app.route("/reviews")
def reviews():
    df = pd.read_csv("../data/customer_reviews.csv")
    return jsonify(df.head().to_dict())

if __name__ == "__main__":
    app.run(debug=True)