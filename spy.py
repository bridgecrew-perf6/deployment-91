from flask import Flask, render_template, request
import pickle
import numpy as np
spy = Flask(__name__)
model = pickle.load(open('C:\spydeploy\RFR.pkl', 'rb'))
@spy.route('/',methods=['GET'])
def Home():
    return render_template('index.html')
@spy.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        year=int(request.form["year"])
        manufacturer=request.form["manufacturer"] 
        condition=request.form["condition"] 
        cylinders=int(request.form["cylinders"])
        fuel=request.form["fuel"] 
        odometer=int(request.form["odometer"])
        transmission=request.form["transmission"]
        drive=request.form["drive"] 
        size=request.form["size"]
        paint_color=request.form["paint_color"]
        type=request.form["type"]
        prediction=model.predict([[year,manufacturer,condition,cylinders,fuel,odometer,transmission,drive,size,paint_color,type]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="You Can Sell The Car at {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    spy.run(debug=True)