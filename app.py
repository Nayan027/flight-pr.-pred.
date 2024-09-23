from flask import Flask, render_template, url_for, redirect
from form import Predictform
import pandas as pd
import joblib


app = Flask(__name__)
app.secret_key = "secretkey"


model = joblib.load("model.joblib")


@app.route("/")
@app.route("/home")
def homepage():
    return render_template("home.html", Title="HOME")


@app.route("/predict", methods=["GET","POST"])
def predictpage():
    form=Predictform()
    if form.validate_on_submit():
        X_new = pd.DataFrame(dict(
            Airline=[form.Airline.data],
            Date_of_Journey=[form.Date_of_Journey.data.strftime("%Y-%m-%d")],
            Source=[form.Source.data],
            Destination=[form.Destination.data],
            Dep_Time=[form.Dep_Time.data.strftime("%H:%M:%S")],
            Arrival_Time=[form.Arrival_Time.data.strftime("%H:%M:%S")],
            Duration=[form.Duration.data],
            Total_Stops=[form.Total_Stops.data],
            Additional_Info=[form.Additional_Info.data],
        ))

        prediction = model.predict(X_new)[0]
        message = f"The predicted price of your chosen flight is: {prediction} INR."

    else:
        message = f"Please enter valid input details to predict the flight price"
    return render_template("form.html", Title="PREDICTION", form=form, output=message)





if __name__=="__main__":
    app.run(debug=True)