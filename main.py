from ast import Try
from flask import Flask, request, app, jsonify, url_for, render_template
import pandas as pd
import numpy as np
import pickle
import os

app = Flask(__name__)

## Load the model
model = pickle.load(open('regmodel.pkl','rb'))
scaler =  pickle.load(open('scaling.pkl','rb'))
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data = scaler.transform(np.array(list(data.values())).reshape(1,-1))
    output = model.predict(new_data)
    print(output[0])
    return jsonify(output[0])

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = [float(x) for x in request.form.values()]
        new_data = scaler.transform(np.array(data).reshape(1,-1))
        print(new_data)
        output = model.predict(new_data)[0]
    except ValueError:
            return render_template('home.html',error = "Please enter valid values")
    return render_template('home.html',prediction=round(output,2))


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
