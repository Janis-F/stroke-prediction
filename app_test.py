import random
from fastapi.testclient import TestClient
from app import app, Observation

client = TestClient(app)

observation = Observation(
    gender=random.choice(["Male", "Female"]),
    age=random.uniform(18, 100),
    hypertension=random.randint(0, 1),
    heart_disease=random.randint(0, 1),
    ever_married=random.choice(["Yes", "No"]),
    work_type=random.choice(
        ["Private", "Self-employed", "Govt_job", "Never_worked"]),
    Residence_type=random.choice(["Urban", "Rural"]),
    avg_glucose_level=random.uniform(50, 300),
    bmi=random.uniform(15, 50),
    smoking_status=random.choice(
        ["formerly smoked", "never smoked", "smokes", "Unknown"]),
    age_group="",
    glucose_group=""
)

response = client.post("/predict", json=observation.dict())

print(response.json())
