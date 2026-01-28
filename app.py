from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import pickle

app = Flask(__name__)
CORS(app)

model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# Correct feature order (must match training)
feature_order = [
 'age','bp','sg','al','su','rbc','pc','pcc','ba',
 'bgr','bu','sc','sod','pot','hemo','pcv','wc','rc',
 'htn','dm','cad','appet','pe','ane'
]

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "CKD Flask API Running"})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    input_features = data["features"]

    # Arrange input in correct order
    arr = [float(input_features[col]) for col in feature_order]
    arr = np.array(arr).reshape(1, -1)

    arr = scaler.transform(arr)
    prediction = model.predict(arr)

    result = "CKD Detected ❗" if prediction[0] == 1 else "No CKD ✅"

    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)
