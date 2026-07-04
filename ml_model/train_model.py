import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os

np.random.seed(42)

# Synthetic dataset
data = pd.DataFrame({
    "target_amount": np.random.randint(1000000, 50000000, 200),
    "number_of_donors": np.random.randint(1, 100, 200),
    "completed_milestones": np.random.randint(0, 10, 200),
    "pending_milestones": np.random.randint(0, 10, 200),
})

data["total_funds_raised"] = (
    data["target_amount"] * np.random.uniform(0.3, 0.95, 200)
    + data["number_of_donors"] * 50000
    + data["completed_milestones"] * 200000
    - data["pending_milestones"] * 50000
)

X = data[["target_amount", "number_of_donors", "completed_milestones", "pending_milestones"]]
y = data["total_funds_raised"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Model trained successfully")
print("MSE:", mse)
print("R2 Score:", r2)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "ml_model", "donation_model.pkl")

joblib.dump(model, model_path)
metrics = {
    "mse": mse,
    "r2": r2
}

metrics_path = os.path.join(BASE_DIR, "ml_model", "model_metrics.pkl")
joblib.dump(metrics, metrics_path)

print("Metrics saved at:", metrics_path)

print("Model saved at:", model_path)
metrics = {
    "mse": mse,
    "r2": r2
}

metrics_path = os.path.join(
    BASE_DIR,
    "ml_model",
    "model_metrics.pkl"
)

joblib.dump(metrics, metrics_path)

print("Metrics saved at:", metrics_path)