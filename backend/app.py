from src.features.extract_features import obtain_features
from src.utils.process_url import process_url
import numpy as np
from flask import Flask,request,jsonify
from flask_cors import CORS
import joblib

model = joblib.load("models/RF-Classifier-v1")

app = Flask(__name__)
CORS(app)

@app.route("/submit",methods=['POST'])
def obtain_url():
    url = request.json.get("url")
    URL,DOMAIN,DIRECTORY,FILES,PARAMETER = process_url(url)
    features = obtain_features(URL,DOMAIN,DIRECTORY,FILES,PARAMETER)
    print(features)
    prediction = model.predict(np.array(features).reshape(1,-1))
    print(prediction)
    if prediction[0]  <= 0.5:
        return jsonify({"domain":"It is not a Phishing Domain"})
    else:
        return jsonify({"domain":"It is a Phishing Domain"})

if __name__ == "__main__":
    app.run(debug=True)
