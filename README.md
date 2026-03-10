Sales Prediction System

This is a simple MLOps project designed to predict product sales based on various product features such as price, rating, and reviews.

Project Overview

In this project, we create a sales prediction model using Python and deploy it as a FastAPI API service. We simulate the entire ML pipeline from data preprocessing to model training, versioning, and API deployment.

Project Structure

sales-mlops-project/
│
├── data/
│   └── sales.csv        # Example dataset with product data
│
├── models/
│   └── sales_model_v1.pkl  # Trained model
│
├── src/
│   ├── preprocess.py    # Data preprocessing script
│   └── train.py         # Model training script
│
├── api/
│   └── app.py           # FastAPI application
│
└── requirements.txt     # List of dependencies

Requirements

- Python 3.7+
- pip (for package management)

Install the required dependencies by running:

pip install -r requirements.txt

Setup

1. Data Preprocessing
The data preprocessing script loads the dataset, cleans the data, and splits it into training and testing sets.

Run the following command to process the data:

python src/preprocess.py

This will generate the preprocessed datasets and save them in the data/ folder.

2. Model Training
Once the data is processed, you can train a Linear Regression model by running:

python src/train.py

This will train the model and save it as sales_model_v1.pkl in the models/ folder.

3. API Deployment
To start the FastAPI server and expose the prediction API, run the following command:

uvicorn api.app:app --reload

This will start the API at http://127.0.0.1:8000.

API Usage

The API exposes a POST endpoint /predict for predicting sales based on product data.

Example Request

POST /predict
Content-Type: application/json

{
  "price": 120,
  "rating": 4.5,
  "reviews": 100
}

Example Response

{
  "predicted_sales": 820.5
}

Logging

The API also logs each prediction to a file (logs.txt) for basic monitoring.

Next Steps

1. Model Versioning: You can extend the project by saving models with different versions (e.g., sales_model_v2.pkl).
2. Monitoring: Implement more sophisticated logging and data drift detection.
3. Experiment Tracking: Use tools like MLflow for experiment tracking and model registry.

License

This project is licensed under the MIT License.