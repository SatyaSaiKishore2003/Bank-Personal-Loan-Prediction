from fastapi import FastAPI
from pydantic import BaseModel, Field, computed_field
from fastapi.responses import JSONResponse
from typing import Literal, Optional, Annotated
import pickle
import pandas as pd


## import ML Model
with open('model.pkl','rb') as f:
    model = pickle.load(f)

app = FastAPI()

MODEL_VERSION = '5.2.31'
## Pydantic model to validate the model
class LoanDefaultPrediction(BaseModel):
    customer_id: Annotated[
        int,
        Field(description="Unique customer identifier")
    ]

    #serious_delinquency: Annotated[
        #int,
       # Field(description="1 means delinquent, 0 means not delinquent")
    #]

    revolving_utilization: Annotated[
        float,
        Field(description="Utilization ratio of unsecured credit lines")
    ]

    age: Annotated[
        int,
        Field(description="Customer age")
    ]

    past_due_30_59_days: Annotated[
        int,
        Field(description="Number of times payment was 30-59 days late")
    ]

    debt_ratio: Annotated[
        float,
        Field(description="Debt ratio of the customer")
    ]

    monthly_income: Optional[
        Annotated[
            float,
            Field(description="Monthly income of the customer")
        ]
    ] = None

    open_credit_lines_and_loans: Annotated[
        int,
        Field(description="Total open credit lines and loans")
    ]

    times_90_days_late: Annotated[
        int,
        Field(description="Number of times customer was 90 days late")
    ]

    real_estate_loans_or_lines: Annotated[
        int,
        Field(description="Number of real estate loans or credit lines")
    ]

    past_due_60_89_days: Annotated[
        int,
        Field(description="Number of times payment was 60-89 days late")
    ]

    dependents: Optional[
        Annotated[
            float,
            Field(description="Number of dependents")
        ]
    ] = None

@app.get('/')
def home():
    return { 'message' : 'Credict Risk Predection API'}

@app.get('/health')
def health_check():
    return{'Status' : 'Ok',
           'version' : MODEL_VERSION
           }

@app.post("/predict")
def predict(data: LoanDefaultPrediction):

    features = [[
        data.customer_id,
        #data.serious_delinquency,
        data.revolving_utilization,
        data.age,
        data.past_due_30_59_days,
        data.debt_ratio,
        data.monthly_income,
        data.open_credit_lines_and_loans,
        data.times_90_days_late,
        data.real_estate_loans_or_lines,
        data.past_due_60_89_days,
        data.dependents
    ]]

    prediction = model.predict(features)

    return {
        "prediction": int(prediction[0])
    }
   