"""The App."""

from flask import Flask, request, jsonify
from joblib import load

clf = load("clf.joblib")

app = Flask(__name__)

@app.route("/")
def index():
    return '<a href = "./predict?text=exampletext"> ./predict?text=exampletext</a>'

@app.route("/predict")
def predict():
    """Takes a POST request with a key of \"text\" and the text to be classified."""
    text = request.args.get("text")
    # data_dict = request.get_json()

    # text = [data_dict["text"]]
    print(text)

    return jsonify({"result": clf.predict([text])[0]})

if __name__ == "__main__":
    app.run(debug=True)
