import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib
import json
from feature_eng import engineer_features

# Import LightGBM with fallback
try:
    from lightgbm import LGBMRegressor
    HAS_LIGHTGBM = True
except ImportError:
    HAS_LIGHTGBM = False

print("Training ensemble of models...")

# Load and prepare data
with open('public_cases.json', 'r') as f:
    data = json.load(f)

# Extract input features and target
input_data = pd.DataFrame([d['input'] for d in data])
target_data = [d['expected_output'] for d in data]

print(f"Loaded {len(input_data)} training cases")

# Engineer features
input_data = engineer_features(input_data)
print(f"Features: {len(input_data.columns)} total")

# Split data
X_train, X_val, y_train, y_val = train_test_split(input_data, target_data, test_size=0.2, random_state=42)

# Train LightGBM
if HAS_LIGHTGBM:
    print("Training LightGBM...")
    lgb_model = LGBMRegressor(n_estimators=100, learning_rate=0.1, random_state=42, verbose=-1)
    lgb_model.fit(X_train, y_train)
    lgb_score = lgb_model.score(X_val, y_val)
    joblib.dump(lgb_model, 'lgb_model.pkl')
    print(f"LightGBM R² Score: {lgb_score:.4f}")
else:
    print("LightGBM not available")

# Train RandomForest
print("Training RandomForest...")
rf_model = RandomForestRegressor(
    n_estimators=50,
    max_depth=8,
    min_samples_split=10,
    min_samples_leaf=5,
    random_state=42
)
rf_model.fit(X_train, y_train)
rf_score = rf_model.score(X_val, y_val)
joblib.dump(rf_model, 'rf_model.pkl')
print(f"RandomForest R² Score: {rf_score:.4f}")

# Train Linear Regression
print("Training Linear Regression...")
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
lr_score = lr_model.score(X_val, y_val)
joblib.dump(lr_model, 'lr_model.pkl')
print(f"Linear Regression R² Score: {lr_score:.4f}")

print("All models trained and saved!") 