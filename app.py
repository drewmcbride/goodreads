"""The App."""

from flask import Flask, request, jsonify, render_template
from joblib import load

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html") 
    #'<a href = "./predict?text=exampletext"> ./predict?text=exampletext</a>'

@app.route("/predict", methods = ['POST'])
def predict():
    """Takes a POST request with a key of \"text\" and the text to be classified."""
    text = request.form.get("text")
    # data_dict = request.get_json()
    # get data in correct ofrmat and then do your predict and stuff
    clf = load("clf.joblib")
    prediction = clf.predict([text])[0]
    #if prediction == 1:
    return render_template("index.html", prediction=prediction)
    #else:
        #return render_template("index.html", prediction="bad")
    # text = [data_dict["text"]]
    #print(text)

    #return jsonify({"result": clf.predict([text])[0]})

if __name__ == "__main__":
    app.run(debug=True)
