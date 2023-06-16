from flask import Flask, request, jsonify, render_template, session, redirect, url_for, session
import requests
import pandas as pd
import numpy as np
import joblib
import feature_engine

app = Flask(__name__, template_folder='template')
@app.route('/',  methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        pclass = request.form["pclass"]
        age  = request.form['age']
        sex  = request.form['sex']
        fare = request.form['fare']        
        return redirect(url_for('result',pclass=pclass,age=age,sex=sex,fare=fare))
    return render_template('index.html')

@app.route('/result/<int:pclass>/<int:age>/<int:sex>/<int:fare>', methods = ['GET','POST'])
def result(pclass,sex, age, fare):
    # Put inputs to dataframe
    model_rf = joblib.load("model.pkl")
    data = pd.DataFrame([[pclass, sex, age, fare]], columns = ["pclass", "sex", "age", "fare"])
    # Get prediction
    prediction = model_rf.predict(data)[0]

    result = "Survived" if prediction == 1 else "Not Survived"

    return render_template('result.html', result=result)

if __name__ =='__main__':
    app.run(debug=True,host="0.0.0.0", port=int("5000"))