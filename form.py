from flask_wtf import FlaskForm
from wtforms import SelectField, DateField, TimeField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Optional


import pandas as pd
train_data = pd.read_csv("data/train.csv")
val_data = pd.read_csv("data/val.csv")

X_data = pd.concat([train_data, val_data], axis=0).drop(columns="Price")



class Predictform(FlaskForm):
    Airline = SelectField(label="Airline", 
                          validators=[DataRequired()], 
                          choices=X_data.Airline.unique().tolist())


    Date_of_Journey = DateField(label="Date of Journey", 
                                validators=[DataRequired()])
    

    Source = SelectField(label="Source", 
                         validators=[DataRequired()], 
                         choices=X_data.Source.unique().tolist())
    

    Destination = SelectField(label="Destination", 
                              validators=[DataRequired()], 
                              choices=X_data.Destination.unique().tolist())
    

    Dep_Time = TimeField(label="Departure Time", 
                         validators=[DataRequired()])
    


    Arrival_Time = TimeField(label="Arrival Time", 
                             validators=[DataRequired()])
    

    Duration = IntegerField(label="Flight Duration", 
                            validators=[DataRequired()])
    

    Total_Stops = IntegerField(label="Total Stops", 
                               validators=[DataRequired()])
    

    Additional_Info = SelectField(label="Additional Info", 
                                  validators=[DataRequired()], 
                                  choices=X_data.Additional_Info.unique().tolist())


    submit = SubmitField(label="check price")