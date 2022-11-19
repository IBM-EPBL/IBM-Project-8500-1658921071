import numpy as np
from flask import Flask, request, render_template
import pickle

app=Flask(__name__,template_folder='template')
model = pickle.load(open('wqi.pkl','rb')) 

@app.route('/')
def home():
    return render_template("web.html")

@app.route('/predict',methods = ['GET','POST'])
def predict():
    temp=request.form["temp"]
    do=request.form["do"]
    ph =request.form["ph"] 
    co=request.form["co"] 
    bod = request.form["bod"] 
    na=request.form["na"]
    tc=request.form["tc"]
    total =np.array([float (temp), float (do), float (ph), float (co), float (bod), float (na), float(tc)])
    y_pred=model.predict(total)
    y_pred=y_pred[[0]]
    if(y_pred >= 95.0 and y_pred <= 100.0): 
        s='Excellent'
    elif(y_pred >= 89.0 and y_pred<=94.0):
        s='Very good'
    elif(y_pred >= 80.0 and y_pred<=88.0):
        s='Good'
    elif(y_pred >= 65.0 and y_pred<=79.0):
        s='Fair'
    elif(y_pred >= 45.0 and y_pred<=64.0):
        s='Marginal'
    else:
        s='Poor'
    return render_template("web.html",prediction_text = s)

    
    
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
