import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib
import json
from feature_eng import engineer_features

# Force RandomForest for better generalization with small dataset
USE_RANDOMFOREST = True
print("Using RandomForest for better generalization")

# Load and prepare data
with open('public_cases.json', 'r') as f:
    data = json.load(f)

# Extract input features and target
input_data = pd.DataFrame([d['input'] for d in data])
target_data = [d['expected_output'] for d in data]

print(f"Loaded {len(input_data)} training cases")
print(f"Features: {list(input_data.columns)}")

# Engineer features
input_data = engineer_features(input_data)
print(f"After feature engineering: {list(input_data.columns)}")

# Split data
X_train, X_val, y_train, y_val = train_test_split(input_data, target_data, test_size=0.2, random_state=42)

# Train RandomForest with conservative settings to prevent overfitting
primary_model = RandomForestRegressor(
    n_estimators=50,        # Reduced from 100
    max_depth=8,           # Limit depth to prevent overfitting
    min_samples_split=10,   # Require more samples to split
    min_samples_leaf=5,     # Require more samples in leaf
    random_state=42
)

primary_model.fit(X_train, y_train)

# Train Linear Regression
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

# Evaluate models
primary_val_score = primary_model.score(X_val, y_val)
lr_val_score = lr_model.score(X_val, y_val)

print(f"RandomForest R² Score: {primary_val_score:.4f}")
print(f"Linear Regression R² Score: {lr_val_score:.4f}")

# Save models
joblib.dump(primary_model, 'primary_model.pkl')
joblib.dump(lr_model, 'lr_model.pkl')
print("Models saved successfully!")