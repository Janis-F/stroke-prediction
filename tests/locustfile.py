from locust import HttpUser, between, task
from app import Observation
import random


class MyUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def predict(self):
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

        self.client.post("/predict", json=observation.dict())


users = 300
spawn_rate = 5
