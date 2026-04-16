from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI()

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def home():
    return {"message": "ML API is running"}

@app.get("/predict")
def predict(sepal_length: float, sepal_width: float, petal_length: float, petal_width: float):
    data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(data)
    return {"prediction": int(prediction[0])}
