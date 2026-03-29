from flask import Flask,render_template,request
import numpy as np
import joblib

import os
model_path = os.path.join(os.path.dirname(__file__), "knncropmodel.pkl")
model = joblib.load(model_path)


app=Flask(__name__)



@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        try:
            n=float(request.form['n'])
            p=float(request.form['p'])
            k=float(request.form['k'])
            temp=float(request.form['temp'])
            humidity=float(request.form['humidity'])
            ph=float(request.form['ph'])
            rainfall=float(request.form['rainfall'])

            test_data=np.array([[n,p,k,temp,humidity,ph,rainfall]])

            print(f"Test data is : {test_data}")

            pred=model.predict( test_data)

            print(f"Result of prediction is : {pred}")

            return render_template('index2.html',res=pred[0])
        except (KeyError, ValueError, Exception) as e:
            print(f"Prediction error: {e}")
            return render_template('index2.html', res="Error: Invalid input. Please check values.")
    else:
        return render_template('index2.html')
    



@app.route('/')    # '/' indicates default route
def index():

    return render_template("index2.html")

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
