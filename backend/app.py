from src.features.extract_features import obtain_features
from src.utils.process_url import process_url
import os
import numpy as np
from flask import Flask,request,jsonify
from flask_cors import CORS
import joblib

model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'RF-Classifier-v2')

model = joblib.load(model_path)

app = Flask(__name__, static_folder='build', static_url_path='/')
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def serve_index():
    return app.send_static_file('index.html')

@app.route("/submit",methods=['POST'])
def obtain_url():
    url = request.json.get("url")
    if not (url.startswith("http://") or url.startswith("https://")):
        url = 'https://' + url
    secure = True if url.startswith("https://") else False
    URL,DOMAIN,DIRECTORY,FILES,PARAMETER = process_url(url)
    print(URL,DOMAIN,DIRECTORY,FILES,PARAMETER)
    features = obtain_features(URL,DOMAIN,DIRECTORY,FILES,PARAMETER)
    print(features)
    prediction = model.predict(np.array(features).reshape(1,-1))
    print(prediction)
    if prediction[0]  <= 0.5:
        return jsonify({"response":True,"secure":secure})
    else:
        return jsonify({"response":False,"secure":secure})

if __name__ == "__main__":
    app.run(debug=True)
