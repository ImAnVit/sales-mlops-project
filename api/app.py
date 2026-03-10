from fastapi import FastAPI
import joblib
import numpy as np
import datetime

app = FastAPI()

# Load model
model = joblib.load("models/sales_model_v1.pkl")


@app.get("/")
def home():
    return {"message": "Sales Prediction API"}


@app.post("/predict")
def predict(price: float, rating: float, reviews: int):

    features = np.array([[price, rating, reviews]])
    prediction = model.predict(features)

    log = f"{datetime.datetime.now()} | price={price} rating={rating} reviews={reviews} -> {prediction[0]}\n"

    with open("logs.txt", "a") as f:
        f.write(log)

    return {"predicted_sales": float(prediction[0])}