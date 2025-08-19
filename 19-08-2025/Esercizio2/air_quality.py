import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier  # Import Random Forest

# 1. Read dataset
df = pd.read_csv("AirQualityUCI.csv", sep=";", decimal=",", low_memory=False)

# Drop empty or unnecessary columns
df = df.dropna(axis=1, how="all")

# Convert date column to datetime
df["Date"] = pd.to_datetime(df["Date"], errors="coerce", dayfirst=True)

# Select one column as air quality reference (e.g. CO(GT))
target_col = "CO(GT)"
df = df.dropna(subset=[target_col])

# 2. Compute the daily average for each day
daily_mean = df.groupby("Date")[target_col].transform("mean")

# 3. Create binary label: 1 = good (<= mean), 0 = bad (> mean)
df["label"] = np.where(df[target_col] <= daily_mean, 1, 0)

# 4. Define features (exclude date, label, and target column)
X = df.drop(columns=["Date", "Time", "label"])
X = X.select_dtypes(include=[np.number])  # Keep only numeric columns
y = df["label"]

# Handle missing values by filling with column mean
X = X.fillna(X.mean())

# 5. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. XGBoost model
xgb_model = XGBClassifier(use_label_encoder=False, eval_metric="logloss")
xgb_model.fit(X_train, y_train)

# 7. Evaluation for XGBoost
y_pred_xgb = xgb_model.predict(X_test)
print("=== XGBoost Classification Report ===")
print(classification_report(y_test, y_pred_xgb))

# 8. Random Forest model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# 9. Evaluation for Random Forest
y_pred_rf = rf_model.predict(X_test)
print("=== Random Forest Classification Report ===")
print(classification_report(y_test, y_pred_rf))
