from sklearn.linear_model import LogisticRegression
import pandas as pd
from pydantic import BaseModel
import joblib
from fastapi import FastAPI


def calculate_groups(age: float, avg_glucose_level: float):
    # Calculate the age group based on the age value
    age_bins = [0, 14, 24, 64, 120]
    age_labels = ['children', 'youth', 'adult', 'senior']
    age_group = pd.cut([age], bins=age_bins,
                       labels=age_labels, include_lowest=True)[0]

    # Calculate the glucose group based on the avg_glucose_level value
    glucose_bins = [0, 99, 125, 999]
    glucose_labels = ["healthy", "pre-diabetes", "diabetes"]
    glucose_group = pd.cut([avg_glucose_level], bins=glucose_bins,
                           labels=glucose_labels, include_lowest=True)[0]

    return age_group, glucose_group


class Observation(BaseModel):
    gender: str
    age: float
    hypertension: int
    heart_disease: int
    ever_married: str
    work_type: str
    Residence_type: str
    avg_glucose_level: float
    bmi: float
    smoking_status: str
    age_group: str
    glucose_group: str


class PredictionOut(BaseModel):
    default_proba: float


# Load the pre-trained pipeline
log_pipe = joblib.load("log_reg_model.pkl")
print(type(log_pipe))
# Start the app
app = FastAPI()

# Home page


@app.get("/")
def home():
    return {"message": "Stroke Prediction App", "model_version": 0.1}


@app.post("/predict")
def predict(observation: Observation):
    age_group, glucose_group = calculate_groups(
        observation.age, observation.avg_glucose_level)

    observation.age_group = age_group
    observation.glucose_group = glucose_group

    df = pd.DataFrame([observation.dict()])

    transformer = log_pipe[:-1].named_steps['preprocessor']
    X_processed = transformer.transform(df)

    # Get predicted probabilities from the logistic regression model
    predicted_proba = log_pipe.named_steps['classifier'].predict_proba(X_processed)[
        :, 1]

    return {"probability": f"{round(float(predicted_proba)*100)}%"}
