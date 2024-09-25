from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import joblib
from data_loader import load_data

# Load data
X_train, X_test, y_train, y_test = load_data()

# Create pipeline: scaling + regression
pipeline = Pipeline([("scaler", StandardScaler()), ("regressor", LinearRegression())])

# Fit the model
pipeline.fit(X_train, y_train)

# Save the trained pipeline
joblib.dump(pipeline, "california_housing_pipeline.pkl")

# Evaluate
y_pred = pipeline.predict(X_test)
print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred)}")
